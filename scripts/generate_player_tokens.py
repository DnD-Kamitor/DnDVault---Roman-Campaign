#!/usr/bin/env python3
"""
Generate MapTool .rptok PC tokens from JSON character sheets in players/.

Usage:
  python scripts/generate_player_tokens.py           # all sheets in players/
  python scripts/generate_player_tokens.py players/Marcus.json

Output: Maptool/tokens/players/<CharacterName>.rptok

Properties included per token:
  HP / MaxHP / TempHP / AC / Speed / Initiative / Level / Class / Race /
  Background / ProfBonus / STR-CHA scores + mods / all saving throws /
  all 18 skill bonuses / Passive Perception|Investigation|Insight /
  SpellcastingAbility / SpellSaveDC / SpellAttackBonus /
  UnitRole / CorruptionLevel / CommendationesCount / CitizenshipStatus /
  Armor / Languages / Notes
"""

import base64
import hashlib
import json
import struct
import sys
import uuid
import zipfile
import zlib
from pathlib import Path

REPO_ROOT  = Path(__file__).parent.parent
PLAYERS_DIR = REPO_ROOT / "players"
OUTPUT_DIR  = REPO_ROOT / "Maptool" / "tokens" / "players"

# ── Role armor table (from roles.qmd lines 137-154) ─────────────────────────

ROLE_ARMOR = {
    "Optio":            {"armor": "Lorica Hamata",       "base_ac": 14, "dex_cap": 2, "shield": True,  "flat": False},
    "Tesserarius":      {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": True,  "flat": False},
    "Aquilifer":        {"armor": "Lorica Segmentata",   "base_ac": 17, "dex_cap": 0, "shield": False, "flat": True},
    "Signifer":         {"armor": "Lorica Hamata",       "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Cornicen":         {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Medicus":          {"armor": "Lorica Hamata",       "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Haruspex":         {"armor": "Linothorax",          "base_ac": 12, "dex_cap": 3, "shield": False, "flat": False},
    "Faber":            {"armor": "Lorica Hamata",       "base_ac": 14, "dex_cap": 2, "shield": True,  "flat": False},
    "Librarius":        {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Explorator":       {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Frumentarius":     {"armor": "Lorica Hamata",       "base_ac": 14, "dex_cap": 2, "shield": True,  "flat": False},
    "Sacerdos":         {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
    "Flamen Martialis": {"armor": "Linothorax (red)",    "base_ac": 12, "dex_cap": 3, "shield": False, "flat": False},
    "Capsarius":        {"armor": "Linothorax",          "base_ac": 12, "dex_cap": 3, "shield": False, "flat": False},
    "Custos Armorum":   {"armor": "Lorica Segmentata",   "base_ac": 17, "dex_cap": 0, "shield": True,  "flat": True},
    "Foederatus":       {"armor": "Lorica Squamata",     "base_ac": 14, "dex_cap": 2, "shield": False, "flat": False},
}

SKILL_ABILITY = {
    "Acrobatics": "DEX", "Animal Handling": "WIS", "Arcana": "INT",
    "Athletics": "STR", "Deception": "CHA", "History": "INT",
    "Insight": "WIS", "Intimidation": "CHA", "Investigation": "INT",
    "Medicine": "WIS", "Nature": "INT", "Perception": "WIS",
    "Performance": "CHA", "Persuasion": "CHA", "Religion": "INT",
    "Sleight of Hand": "DEX", "Stealth": "DEX", "Survival": "WIS",
}

ABILITIES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]


# ── Stat helpers ─────────────────────────────────────────────────────────────

def ability_mod(score):
    return (score - 10) // 2

def prof_bonus(level):
    return 2 + (level - 1) // 4

def calc_ac(cs):
    override = cs.get("ac_override")
    if override is not None:
        return override
    dex = ability_mod(cs["ability_scores"]["DEX"])
    role = cs.get("role", "")
    armor = ROLE_ARMOR.get(role)
    if not armor:
        return 10 + dex
    if armor["flat"]:
        return armor["base_ac"] + (2 if armor["shield"] else 0)
    ac = armor["base_ac"] + min(dex, armor["dex_cap"])
    return ac + (2 if armor["shield"] else 0)

def calc_skills(cs):
    pb = prof_bonus(cs["level"])
    profs = set(cs.get("skill_proficiencies", []))
    expertise = set(cs.get("expertise", []))
    scores = cs["ability_scores"]
    result = {}
    for skill, ability in SKILL_ABILITY.items():
        base = ability_mod(scores[ability])
        if skill in expertise:
            result[skill] = base + pb * 2
        elif skill in profs:
            result[skill] = base + pb
        else:
            result[skill] = base
    return result

def calc_saves(cs):
    pb = prof_bonus(cs["level"])
    save_profs = set(cs.get("saving_throw_proficiencies", []))
    scores = cs["ability_scores"]
    return {ab: ability_mod(scores[ab]) + (pb if ab in save_profs else 0) for ab in ABILITIES}


# ── Minimal PNG (stdlib only) ─────────────────────────────────────────────────

def _chunk(tag, data):
    tag_b = tag.encode() if isinstance(tag, str) else tag
    crc = struct.pack(">I", zlib.crc32(tag_b + data) & 0xFFFFFFFF)
    return struct.pack(">I", len(data)) + tag_b + data + crc

def make_png(r, g, b, size=100):
    ihdr = _chunk("IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
    raw = b"".join(b"\x00" + bytes([r, g, b] * size) for _ in range(size))
    idat = _chunk("IDAT", zlib.compress(raw))
    iend = _chunk("IEND", b"")
    return b"\x89PNG\r\n\x1a\n" + ihdr + idat + iend

def hex_to_rgb(hex_color):
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def new_baguid():
    return base64.b64encode(uuid.uuid4().bytes).decode()


# ── .rptok XML builders ───────────────────────────────────────────────────────

def _prop(key, value):
    return (
        f"      <entry>\n"
        f"        <string>{key.lower()}</string>\n"
        f"        <net.rptools.CaseInsensitiveHashMap_-KeyValue>\n"
        f"          <key>{key}</key>\n"
        f"          <value class=\"string\">{value}</value>\n"
        f"          <outer-class reference=\"../../../..\"/>\n"
        f"        </net.rptools.CaseInsensitiveHashMap_-KeyValue>\n"
        f"      </entry>"
    )

def build_content_xml(cs, image_md5):
    scores = cs["ability_scores"]
    level  = cs["level"]
    pb     = prof_bonus(level)
    skills = calc_skills(cs)
    saves  = calc_saves(cs)
    ac     = calc_ac(cs)

    props = {}
    props["HP"]         = cs["hp_max"]
    props["MaxHP"]      = cs["hp_max"]
    props["TempHP"]     = 0
    props["AC"]         = ac
    props["Speed"]      = 30
    props["Initiative"] = ability_mod(scores["DEX"])
    props["Level"]      = level
    props["Class"]      = cs.get("class", "")
    props["Subclass"]   = cs.get("subclass", "")
    props["Race"]       = cs.get("race", "")
    props["Background"] = cs.get("background", "")
    props["ProfBonus"]  = pb

    for ab in ABILITIES:
        props[ab]            = scores[ab]
        props[f"{ab}Mod"]    = ability_mod(scores[ab])
        props[f"{ab}Save"]   = saves[ab]

    for skill, val in skills.items():
        props[skill.replace(" ", "")] = val

    props["PassivePerception"]    = 10 + skills["Perception"]
    props["PassiveInvestigation"] = 10 + skills["Investigation"]
    props["PassiveInsight"]       = 10 + skills["Insight"]

    spell_ab = cs.get("spellcasting_ability", "")
    spell_mod = ability_mod(scores.get(spell_ab, 10)) if spell_ab else 0
    props["SpellcastingAbility"] = spell_ab
    props["SpellSaveDC"]         = (8 + pb + spell_mod) if spell_ab else 0
    props["SpellAttackBonus"]    = (pb + spell_mod) if spell_ab else 0

    props["UnitRole"]            = cs.get("role", "")
    props["CorruptionLevel"]     = cs.get("corruption_level", 0)
    props["CommendationesCount"] = cs.get("commendationes", 0)
    props["CitizenshipStatus"]   = cs.get("citizenship", "Peregrinus")
    props["Armor"]               = ROLE_ARMOR.get(cs.get("role", ""), {}).get("armor", "None")
    props["Languages"]           = ", ".join(cs.get("languages", []))
    props["Notes"]               = cs.get("notes", "")

    entries = "\n".join(_prop(k, v) for k, v in props.items())

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<net.rptools.maptool.model.Token>
  <id><baGUID>{new_baguid()}</baGUID></id>
  <beingImpersonated>false</beingImpersonated>
  <exposedAreaGUID><baGUID>{new_baguid()}</baGUID></exposedAreaGUID>
  <imageAssetMap>
    <entry>
      <null/>
      <net.rptools.lib.MD5Key><id>{image_md5}</id></net.rptools.lib.MD5Key>
    </entry>
  </imageAssetMap>
  <x>0</x><y>0</y><z>0</z>
  <anchorX>0</anchorX><anchorY>0</anchorY>
  <sizeScale>1.0</sizeScale>
  <lastX>0</lastX><lastY>0</lastY>
  <snapToScale>true</snapToScale>
  <width>100</width><height>100</height>
  <isoWidth>100</isoWidth><isoHeight>100</isoHeight>
  <scaleX>1.0</scaleX><scaleY>1.0</scaleY>
  <sizeMap/>
  <snapToGrid>true</snapToGrid>
  <isVisible>true</isVisible>
  <isVisibleOnlyToOwner>false</isVisibleOnlyToOwner>
  <vblAlpha>0</vblAlpha>
  <alwaysVisibleTolerance>2</alwaysVisibleTolerance>
  <isAlwaysVisible>false</isAlwaysVisible>
  <name>{cs["name"]}</name>
  <ownerType>0</ownerType>
  <tokenShape>CIRCLE</tokenShape>
  <tokenType>PC</tokenType>
  <layer>TOKEN</layer>
  <propertyType>Basic</propertyType>
  <isFlippedX>false</isFlippedX>
  <isFlippedY>false</isFlippedY>
  <isFlippedIso>false</isFlippedIso>
  <charsheetImage/><portraitImage/>
  <hasSight>true</hasSight>
  <sightType>Normal Vision</sightType>
  <hasFog>false</hasFog>
  <propertyMapCI>
    <store>
{entries}
    </store>
  </propertyMapCI>
  <state/>
  <macroPropertiesMap/>
  <speechMap/>
</net.rptools.maptool.model.Token>"""


def build_properties_xml():
    return """<map>
  <entry>
    <string>version</string>
    <string>1.18.6</string>
  </entry>
  <entry>
    <string>herolab</string>
    <boolean>false</boolean>
  </entry>
</map>"""


# ── Token packager ────────────────────────────────────────────────────────────

def generate_token(sheet_path, output_dir):
    with open(sheet_path) as f:
        cs = json.load(f)

    r, g, b = hex_to_rgb(cs.get("portrait_color", "#8B0000"))
    png      = make_png(r, g, b, 100)
    thumb    = make_png(r, g, b, 50)
    md5      = hashlib.md5(png).hexdigest()

    content_xml    = build_content_xml(cs, md5)
    properties_xml = build_properties_xml()

    safe_name = cs["name"].replace(" ", "_")
    out_path  = output_dir / f"{safe_name}.rptok"

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.xml", content_xml)
        zf.writestr("properties.xml", properties_xml)
        zf.writestr(f"assets/{md5}", png)
        zf.writestr(f"assets/{md5}.png", png)
        zf.writestr("thumbnail", thumb)
        zf.writestr("thumbnail_large", png)

    print(f"  {cs['name']} ({cs.get('role','?')}, L{cs['level']}, AC {calc_ac(cs)}) → {out_path.name}")
    return out_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1:
        sheets = [Path(p) for p in sys.argv[1:]]
    else:
        sheets = sorted(p for p in PLAYERS_DIR.glob("*.json") if p.name != "template.json")

    if not sheets:
        print(f"No character sheets found in {PLAYERS_DIR}")
        print("Copy players/template.json → players/YourName.json and fill it in.")
        return

    print(f"Generating PC tokens → {OUTPUT_DIR}")
    for sheet in sheets:
        generate_token(sheet, OUTPUT_DIR)
    print("Done.")


if __name__ == "__main__":
    main()
