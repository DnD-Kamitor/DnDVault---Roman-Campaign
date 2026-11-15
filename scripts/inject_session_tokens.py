#!/usr/bin/env python3
"""
Add the Session 6 and Session 7 tokens and maps to a COPY of a MapTool campaign.

  python3 scripts/inject_session_tokens.py Maptool/campaigns/5e/3nov.cmpgn Maptool/campaigns/5e/3nov_s6.cmpgn

The source campaign is never modified. MapTool must be closed while this runs.

What it does (all new tokens go on the GM layer, so players cannot see them until
you move them to the Token layer):
  * Fort Vindula map: 4 Skeletons at the Skull Entrance image.
  * BloodOmenss map: Core Room map image east of the dungeon, plus a staging block of
    every Session 6 dungeon creature next to it.
  * New map "S7 The Wrath of Mars": the three s5_mars_* battle maps scaled to the
    100 px grid, with every Session 7 token staged beside the map it belongs to.

XStream stores links as positional paths (tokenMap/entry[3]...), so everything is
appended after existing entries; nothing existing is reordered.
"""
import base64
import hashlib
import os
import re
import sys
import zipfile
from pathlib import Path

from PIL import Image

BASE = Path(__file__).resolve().parent.parent
TOK = BASE / "Maptool/tokens"
MAPS = BASE / "Maptool/maps"

new_assets = {}  # md5 -> (descriptor xml, ext, bytes)


def guid():
    return base64.b64encode(os.urandom(16)).decode()


def rptok_path(name):
    for sub in ("npcs/creatures", "npcs/named", "props", "npcs"):
        p = TOK / sub / f"{name}.rptok"
        if p.exists():
            return p
    raise FileNotFoundError(name)


def load_rptok(name):
    z = zipfile.ZipFile(rptok_path(name))
    xml = z.read("content.xml").decode("utf-8")
    xml = re.sub(r"^<\?xml[^>]*\?>\s*", "", xml)
    for n in z.namelist():
        m = re.match(r"assets/([0-9a-f]{32})(\.\w+)?$", n)
        if m and m.group(2):
            md5, ext = m.group(1), m.group(2)[1:]
            desc = z.read(f"assets/{md5}").decode("utf-8")
            new_assets[md5] = (desc, ext, z.read(n))
    return xml


def token_entry(name, display, x, y, layer="GM", size=None):
    xml = load_rptok(name)
    gid = guid()
    xml = re.sub(r"<id>\s*<baGUID>[^<]*</baGUID>\s*</id>",
                 '<id reference="../../net.rptools.maptool.model.GUID"/>', xml, count=1)
    xml = re.sub(r"(<exposedAreaGUID>\s*<baGUID>)[^<]*(</baGUID>)", lambda m: m.group(1) + guid() + m.group(2), xml, count=1)
    xml = re.sub(r"<x>-?\d+</x>", f"<x>{x}</x>", xml, count=1)
    xml = re.sub(r"<y>-?\d+</y>", f"<y>{y}</y>", xml, count=1)
    xml = re.sub(r"<name>[^<]*</name>", f"<name>{display}</name>", xml, count=1)
    xml = re.sub(r"<layer>[^<]*</layer>", f"<layer>{layer}</layer>", xml, count=1)
    if size:
        xml = re.sub(r"<width>\d+</width>", f"<width>{size}</width>", xml, count=1)
        xml = re.sub(r"<height>\d+</height>", f"<height>{size}</height>", xml, count=1)
    return (f"<entry><net.rptools.maptool.model.GUID><baGUID>{gid}</baGUID></net.rptools.maptool.model.GUID>"
            f"{xml}</entry>")


def background_entry(template_token_xml, img_path, display, x, y, scale):
    data = Path(img_path).read_bytes()
    md5 = hashlib.md5(data).hexdigest()
    ext = Path(img_path).suffix[1:].lower()
    w, h = Image.open(img_path).size
    desc = (f"<net.rptools.maptool.model.Asset>\n  <id>\n    <id>{md5}</id>\n  </id>\n  <name>{display}</name>\n"
            f"  <extension>{ext}</extension>\n  <type>IMAGE</type>\n</net.rptools.maptool.model.Asset>")
    new_assets[md5] = (desc, ext, data)
    xml = template_token_xml
    xml = re.sub(r"(<imageAssetMap>.*?<id>)[0-9a-f]{32}(</id>)", lambda m: m.group(1) + md5 + m.group(2), xml, count=1, flags=re.S)
    xml = re.sub(r"(<exposedAreaGUID>\s*<baGUID>)[^<]*(</baGUID>)", lambda m: m.group(1) + guid() + m.group(2), xml, count=1)
    for tag, val in (("x", x), ("y", y), ("width", int(w * scale)), ("height", int(h * scale)),
                     ("isoWidth", int(w * scale)), ("isoHeight", int(h * scale))):
        xml = re.sub(rf"<{tag}>-?\d+</{tag}>", f"<{tag}>{val}</{tag}>", xml, count=1)
    xml = re.sub(r"<name>[^<]*</name>", f"<name>{display}</name>", xml, count=1)
    return (f"<entry><net.rptools.maptool.model.GUID><baGUID>{guid()}</baGUID></net.rptools.maptool.model.GUID>"
            f"{xml}</entry>")


def zone_span(s, name):
    i = s.index(f"<name>{name}</name>")
    zs = s.rindex("<net.rptools.maptool.model.Zone>", 0, i)
    ze = s.index("</net.rptools.maptool.model.Zone>", i) + len("</net.rptools.maptool.model.Zone>")
    return zs, ze


def count_entries(token_map_xml):
    # direct children of tokenMap: count "<entry>" at depth 1
    depth, n = 0, 0
    for m in re.finditer(r"<(/?)entry\b[^>]*?(/?)>", token_map_xml):
        if m.group(2):
            continue
        if m.group(1):
            depth -= 1
        else:
            if depth == 0:
                n += 1
            depth += 1
    return n


def append_to_zone(zone_xml, entries):
    tm_end = zone_xml.index("</tokenMap>")
    tm_start = zone_xml.index("<tokenMap>") + len("<tokenMap>")
    existing = count_entries(zone_xml[tm_start:tm_end])
    zone_xml = zone_xml[:tm_end] + "".join(entries) + zone_xml[tm_end:]
    refs = "".join(
        f'<net.rptools.maptool.model.Token reference="../../tokenMap/entry[{existing + k + 1}]/net.rptools.maptool.model.Token"/>'
        for k in range(len(entries)))
    if "<tokenOrderedList class=\"linked-list\"/>" in zone_xml:
        zone_xml = zone_xml.replace("<tokenOrderedList class=\"linked-list\"/>", f'<tokenOrderedList class="linked-list">{refs}</tokenOrderedList>', 1)
    else:
        zone_xml = zone_xml.replace("</tokenOrderedList>", refs + "</tokenOrderedList>", 1)
    return zone_xml


def staged(names_counts, x0, y0, per_row=6, step=150, layer="GM"):
    out, k = [], 0
    for name, display, count, size in names_counts:
        for i in range(count):
            label = display if count == 1 else f"{display} {i + 1}"
            out.append(token_entry(name, label, x0 + (k % per_row) * step, y0 + (k // per_row) * step, layer, size))
            k += 1
        k += (-k) % per_row  # new row per creature type
    return out


def main(src, dst):
    if os.path.abspath(src) == os.path.abspath(dst):
        raise SystemExit("Refusing to overwrite the source campaign.")
    zin = zipfile.ZipFile(src)
    s = zin.read("content.xml").decode("utf-8")
    existing_assets = {n for n in zin.namelist() if n.startswith("assets/")}

    # background template: the dungeon image token on BloodOmenss
    zs, ze = zone_span(s, "BloodOmenss")
    blood = s[zs:ze]
    m = re.search(r"(<net.rptools.maptool.model.Token>(?:(?!</net.rptools.maptool.model.Token>).)*?<name>Blood-Cult-Dungeon-Gridded-29x43-MapPublic</name>.*?</net.rptools.maptool.model.Token>)", blood, re.S)
    bg_template = m.group(1)
    if "<id reference=" not in bg_template[:200]:
        raise SystemExit("unexpected background token layout")

    # ── Session 6: BloodOmenss additions ──
    core = MAPS / "dicegrimorium/CastleCoreRoom/Castle Core Room Public/CastleCoreRoomPublic.jpg"
    s6 = [background_entry(bg_template, core, "S6 Core Room (Scene 9b)", 4700, 300, 1.0)]
    s6 += staged([
        ("Yochlol", "Yochlol (gestating)", 1, None), ("Dretch", "Dretch", 2, None),
        ("Shadow_Demon", "Shadow Demon", 3, None), ("Wraith", "Chieftain Wraith", 2, None),
        ("Glabrezu", "Glabrezu", 1, 200), ("Skeleton", "Ossuary Skeleton", 2, None),
    ], 4700, 2700)
    blood = append_to_zone(blood, s6)
    s = s[:zs] + blood + s[ze:]

    # ── Session 6: Skull Entrance skeletons on Fort Vindula ──
    zs, ze = zone_span(s, "Fort Vindula")
    fort = s[zs:ze]
    skel = [token_entry("Skeleton", f"Entrance Skeleton {i + 1}", 23300 + i * 150, 9500) for i in range(4)]
    fort = append_to_zone(fort, skel)
    s = s[:zs] + fort + s[ze:]

    # ── Session 7: new zone built from the BloodOmenss shell ──
    zs, ze = zone_span(s, "BloodOmenss")
    shell = s[zs:ze]
    shell = shell[:shell.index("<tokenMap>")] + "<tokenMap></tokenMap>" + shell[shell.index("</tokenMap>") + len("</tokenMap>"):]
    shell = re.sub(r"<exposedAreaMeta>.*?</exposedAreaMeta>", "<exposedAreaMeta/>", shell, count=1, flags=re.S)
    shell = re.sub(r"<tokenOrderedList class=\"linked-list\">.*?</tokenOrderedList>", '<tokenOrderedList class="linked-list"/>', shell, count=1, flags=re.S)
    shell = re.sub(r"<exposedArea>.*?</exposedArea>", "<exposedArea>\n<curves/>\n</exposedArea>", shell, count=1, flags=re.S)
    shell = re.sub(r"<name>BloodOmenss</name>", "<name>S7 The Wrath of Mars</name>", shell, count=1)
    shell = re.sub(r"<creationTime>\d+</creationTime>", "<creationTime>1794700000000</creationTime>", shell, count=1)

    s7 = [
        background_entry(bg_template, MAPS / "s5_mars_vault_overview.jpg", "S7 Scenes 0-1 Stair, Armory", 0, 0, 2.5),
        background_entry(bg_template, MAPS / "s5_mars_vault.jpg", "S7 Scenes 2-3 Passages, Vercingetorix", 3500, 0, 2.5),
        background_entry(bg_template, MAPS / "s5_mars_confrontation.jpg", "S7 Scenes 4-5 Antechamber of Mars", 7000, 0, 100 / 60),
    ]
    s7 += staged([("Wraith", "Armory Wraith", 2, None)], 0, 4700)
    s7 += staged([("Zombie", "Zombie", 6, None), ("Wight", "Wight", 1, None), ("Specter", "Specter", 2, None),
                  ("Vercingetorix_Bound", "Vercingetorix, Bound", 1, None), ("Skeleton", "Fallen Skeleton", 4, None)],
                 3500, 4200)
    s7 += staged([("Mars", "Mars", 1, 200), ("Janus_(Threshold_Vision)", "Janus", 1, None),
                  ("Caesar_Chain_Winch", "Chain Winch", 4, None), ("Shadow_Demon", "Summoned Shadow Demon", 2, None),
                  ("Wight_General_(Centurion_Cameo)", "Wight-General (only if spared S1)", 1, None),
                  ("Thusnelda", "Thusnelda (only if with party)", 1, None)],
                 7000, 2200)
    shell = append_to_zone(shell, s7)
    zone_entry = (f"<entry><net.rptools.maptool.model.GUID><baGUID>{guid()}</baGUID></net.rptools.maptool.model.GUID>"
                  f"{shell}</entry>")
    # insert after the last zone entry, before </m> of the zones map
    zones_end = s.index("<mutex class=\"java.util.Collections$SynchronizedMap\"")
    m_close = s.rindex("</m>", 0, zones_end)
    s = s[:m_close] + zone_entry + s[m_close:]

    # ── write the copy ──
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == "content.xml":
                zout.writestr("content.xml", s)
            else:
                zout.writestr(item, zin.read(item.filename))
        added = 0
        for md5, (desc, ext, data) in new_assets.items():
            if f"assets/{md5}" not in existing_assets:
                zout.writestr(f"assets/{md5}", desc)
                zout.writestr(f"assets/{md5}.{ext}", data)
                added += 1
    print(f"Wrote {dst}: +{len(s6)} on BloodOmenss, +4 on Fort Vindula, new map with {len(s7)} items, {added} new assets")


if __name__ == "__main__":
    main(*sys.argv[1:3])
