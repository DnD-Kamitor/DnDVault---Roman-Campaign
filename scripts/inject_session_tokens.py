#!/usr/bin/env python3
"""
Add the Session 6 and Session 7 tokens and maps to a COPY of a MapTool campaign.

  python3 scripts/inject_session_tokens.py Maptool/campaigns/5e/3nov.cmpgn Maptool/campaigns/5e/3nov_s6.cmpgn

The source campaign is never modified. MapTool must be closed while this runs.

What it does (all new tokens go on the GM layer, so players cannot see them until
you move them to the Token layer):
  * Fort Vindula map: 4 Skeletons at the Skull Entrance image.
  * BloodOmenss map (the final map for Sessions 6 and 7): every Session 6 and Session 7
    token staged east of the dungeon image, prefixed "S6" / "S7".

Image records are written in MapTool's own Asset format (some token files carry a
malformed record that makes MapTool stop loading images). XStream stores links as
positional paths (tokenMap/entry[3]...), so new tokens are appended after existing
entries; nothing existing is reordered.
"""
import base64
import os
import re
import sys
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TOK = BASE / "Maptool/tokens"

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
            data = z.read(n)
            label = name.lower()
            desc = (f"<net.rptools.maptool.model.Asset>\n  <id>\n    <id>{md5}</id>\n  </id>\n  <name>{label}</name>\n"
                    f"  <extension>{ext}</extension>\n  <type>IMAGE</type>\n</net.rptools.maptool.model.Asset>\n")
            new_assets[md5] = (desc, ext, data)
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

    zs, ze = zone_span(s, "BloodOmenss")
    blood = s[zs:ze]

    # ── Sessions 6 and 7: everything staged on the BloodOmenss map (GM layer) ──
    # The dungeon image spans x 291-4351, y 288-6308; staging sits east of it.
    staging = staged([
        ("Yochlol", "S6 Yochlol (gestating)", 1, None), ("Dretch", "S6 Dretch", 2, None),
        ("Shadow_Demon", "S6 Shadow Demon", 3, None), ("Wraith", "S6 Chieftain Wraith", 2, None),
        ("Glabrezu", "S6 Glabrezu", 1, 200), ("Skeleton", "S6 Ossuary Skeleton", 2, None),
    ], 4600, 300)
    staging += staged([
        ("Wraith", "S7 Armory Wraith", 2, None), ("Wight", "S7 Wight", 1, None), ("Specter", "S7 Specter", 2, None),
        ("Vercingetorix_Bound", "S7 Vercingetorix, Bound", 1, None), ("Skeleton", "S7 Fallen Skeleton", 4, None),
        ("Mars", "S7 Mars", 1, 200), ("Janus_(Threshold_Vision)", "S7 Janus", 1, None),
        ("Caesar_Chain_Winch", "S7 Chain Winch", 4, None), ("Shadow_Demon", "S7 Summoned Shadow Demon", 2, None),
        ("Wight_General_(Centurion_Cameo)", "S7 Wight-General (if spared S1)", 1, None),
        ("Thusnelda", "S7 Thusnelda (if with party)", 1, None),
    ], 4600, 2400)
    blood = append_to_zone(blood, staging)
    s = s[:zs] + blood + s[ze:]

    # ── Session 6: Skull Entrance skeletons on Fort Vindula ──
    zs, ze = zone_span(s, "Fort Vindula")
    fort = s[zs:ze]
    skel = [token_entry("Skeleton", f"S6 Entrance Skeleton {i + 1}", 23300 + i * 150, 9500) for i in range(4)]
    fort = append_to_zone(fort, skel)
    s = s[:zs] + fort + s[ze:]

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
    print(f"Wrote {dst}: +{len(staging)} on BloodOmenss, +4 on Fort Vindula, {added} new assets")


if __name__ == "__main__":
    main(*sys.argv[1:3])
