#!/usr/bin/env python3
"""
Inject Devin Night token portraits into .rptok files.

Usage: python3 scripts/inject_portraits.py
"""

import hashlib
import io
import re
import zipfile
from pathlib import Path

from PIL import Image

REPO    = Path(__file__).parent.parent
DEVIN   = Path("/home/chris/.maptool-rptools/resource/Devin Night's Tokens")
TOKENS  = REPO / "Maptool/tokens"

# -------------------------------------------------------------------
# User-supplied mapping: JSON key -> Devin Night filename
# -------------------------------------------------------------------
MAPPING = {
    "Legate_Corvinus":          "castleguard_07.png",
    "Augur_Cassia":             "townsfolk_01.png",
    "Centurion_Varro":          "cityguardsHelm_07.png",
    "Tribune_Lucius":           "CharacterBG3_38.png",
    "Vercingetorix_the_Red":    "DwellerN_06.png",
    "Senator_Brutus":           "Char_41.png",
    "Mars":                     "Char_10.png",
    "Thusnelda":                "Char_67.png",
    "Paterculus":               "castleguard_11.png",
    "Valeria_the_Medicus":      "townsfolk_14.png",
    "Quartus":                  "CityGuardsFace_07.png",
    "Rufus_the_Smith":          "townsfolk_12.png",
    "Brennus":                  "townsfolk_25.png",
    "Lucilla_the_Postwoman":    "lord_13.png",
    "Aldric_the_Gaul":          "CityGuardsFace_03.png",
    "Titus_Half-Germanic":      "CityGuardsFace_05.png",
    "Sigrun_the_Trader":        "lord_02.png",
    "Arnulf_the_Firekeeper":    "townsfolk_23.png",
    "Edda_the_Spear-Mother":    "Char_51.png",
    "Skadi_the_Healer":         "Char_59.png",
    "Flavius_Martis":           "witch_07.png",
    "Aemilia_Secunda":          "cityguardsHelm_05.png",
    "Lucius_Calvus":            "CharacterBG3_39.png",
    "Marcus_Sextius":           "cityguardsHelm_15.png",
    "Publius_Arma":             "castleguard_05.png",
    "Quintus_Caelius":          "townsfolk_03.png",
    "Titus_Vindex":             "cityguardsHelm_02.png",
    "Grunwald":                 "Char_14.png",
    "Aquilifer_Vacant":         "CharacterBG3_47.png",
    "Strix":                    "DdwellerN_04.png",
    "Larvae":                   "basicundead_25.png",
    "Genius_Loci":              "basicundead_09.png",
    "Alp":                      "DMessentialsDJ2_23.png",
    "Draugar":                  "basicundead_06.png",
    "Lindworm":                 "DMessentialsDJ2_38.png",
    "Nix":                      "townsfolk_21.png",
    "Haugbui":                  "basicundead_16.png",
    "Myling":                   "townsfolk_16.png",
    "Vaettir":                  "DMessentialsDJ2_06.png",
    "Legionary_Milites":        "Char_63.png",
    "Praetorian_Guard":         "CityGuardsFace_13.png",
    "Guard":                    "cityguardsHelm_15.png",
    "Scout":                    "cityguardsHelm_16.png",
    "Tribal_Warrior":           "Char_64.png",
    "Berserker":                "Char_60.png",
    "Cultist_of_Mars":          "Char_07.png",
    "Bandit":                   "CharacterBG3_34.png",
    "Bandit_Captain":           "CharacterBG3_36.png",   # fixed user typo
    "Skeleton":                 "basicundead_08.png",
    "Ghoul":                    "basicundead_18.png",
    "Ghast":                    "basicundead_21.png",
    "Shadow":                   "DMessentialsDJ2_23.png",
    "Wight":                    "basicundead_25.png",
    "Wraith":                   "basicundead_20.png",
    "Specter":                  "basicundead_15.png",
    "Zombie":                   "basicundead_28.png",
    "Will-o-Wisp":              "DMessentialsDJ2_18.png",
    "Wolf":                     "tp9camp_26.png",
    "Dire_Wolf":                "tp9camp_26.png",
    "Brown_Bear":               "tp9camp_21.png",
    "Giant_Spider":             "DMessentialsDJ2_33.png",
    "Boar":                     "DME2Hi_26.png",
}

# Explicit overrides for tokens whose filenames differ from key pattern
EXPLICIT_RPTOK = {
    "Legionary_Milites": "Legionary_(Milites).rptok",
    "Aquilifer_Vacant":  "Aquilifer_(Vacant_\u2014_Metellus_Dead).rptok",
}


def build_devin_index():
    idx = {}
    for p in DEVIN.rglob("*.png"):
        idx[p.name] = p
    return idx


def find_rptok(key):
    if key in EXPLICIT_RPTOK:
        for folder in [TOKENS / "npcs/named", TOKENS / "npcs/creatures"]:
            candidate = folder / EXPLICIT_RPTOK[key]
            if candidate.exists():
                return candidate
        return None

    for folder in [TOKENS / "npcs/named", TOKENS / "npcs/creatures"]:
        for f in sorted(folder.glob("*.rptok")):
            stem = f.stem
            if stem == key:
                return f
            # Strip parenthetical suffix: "Flavius_Martis_(Flamen)" -> "Flavius_Martis"
            bare = re.sub(r'_?\(.*\)$', '', stem)
            if bare == key:
                return f
    return None


def md5_hex(data):
    return hashlib.md5(data).hexdigest()


def make_thumbnail(data, size):
    img = Image.open(io.BytesIO(data)).convert("RGBA")
    img.thumbnail(size, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def inject_portrait(rptok_path, portrait_path):
    portrait_data = portrait_path.read_bytes()
    new_md5 = md5_hex(portrait_data)

    with zipfile.ZipFile(rptok_path, 'r') as zin:
        content_xml = zin.read("content.xml").decode("utf-8")
        props_xml   = zin.read("properties.xml")

    # Replace 32-char lowercase hex MD5 inside <id>...</id>
    new_content_xml = re.sub(
        r'(?<=<id>)[0-9a-f]{32}(?=</id>)',
        new_md5,
        content_xml,
    )

    thumb_sm = make_thumbnail(portrait_data, (50,  50))
    thumb_lg = make_thumbnail(portrait_data, (200, 200))

    tmp = rptok_path.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("content.xml",           new_content_xml.encode("utf-8"))
        zout.writestr("properties.xml",        props_xml)
        zout.writestr(f"assets/{new_md5}",     portrait_data)
        zout.writestr(f"assets/{new_md5}.png", portrait_data)
        zout.writestr("thumbnail",             thumb_sm)
        zout.writestr("thumbnail_large",       thumb_lg)

    tmp.replace(rptok_path)


def main():
    devin_idx = build_devin_index()
    print(f"Devin Night index: {len(devin_idx)} PNGs\n")

    ok, skipped, failed = 0, 0, []

    for key, filename in MAPPING.items():
        rptok = find_rptok(key)
        if rptok is None:
            print(f"  SKIP  {key:<42}  (no matching .rptok)")
            skipped += 1
            continue

        portrait = devin_idx.get(filename)
        if portrait is None:
            print(f"  MISS  {key:<42}  ({filename} not found)")
            failed.append((key, filename, "portrait not found"))
            continue

        try:
            inject_portrait(rptok, portrait)
            print(f"  OK    {key:<42}  <- {filename}")
            ok += 1
        except Exception as exc:
            print(f"  ERR   {key:<42}  {exc}")
            failed.append((key, filename, str(exc)))

    print(f"\n{ok}/{len(MAPPING)} portraits injected  ({skipped} skipped, {len(failed)} failed)")
    if failed:
        print("\nFailed:")
        for k, f, r in failed:
            print(f"  {k}: {r}  (file: {f})")


if __name__ == "__main__":
    main()
