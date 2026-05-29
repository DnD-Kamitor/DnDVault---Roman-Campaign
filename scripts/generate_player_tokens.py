#!/usr/bin/env python3
"""
Generate MapTool .rptok PC tokens from JSON character sheets in players/.
Property names match RomanCampaign vJMR-1.cmpgn (Meleks Simple 5e Basic type).

Usage:
  python scripts/generate_player_tokens.py           # all sheets in players/
  python scripts/generate_player_tokens.py players/Marcus.json

Output: Maptool/tokens/players/<CharacterName>.rptok
"""

import base64
import hashlib
import io
import json
import struct
import sys
import uuid
import zipfile
import zlib
from pathlib import Path

try:
    from PIL import Image as PILImage
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

REPO_ROOT   = Path(__file__).parent.parent
PLAYERS_DIR = REPO_ROOT / "players"
OUTPUT_DIR  = REPO_ROOT / "Maptool" / "tokens" / "players"

# ── Role armor (roles.qmd 137-154) ───────────────────────────────────────────

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

# ── Campaign property name mappings (RomanCampaign vJMR-1 Basic type) ─────────

ABILITY_FULL  = {"STR": "Strength", "DEX": "Dexterity", "CON": "Constitution",
                 "INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma"}
ABILITY_MOD   = {"STR": "StrMod", "DEX": "DexMod", "CON": "ConMod",
                 "INT": "IntMod", "WIS": "WisMod", "CHA": "ChaMod"}
ABILITY_SAVE  = {"STR": "StrSave", "DEX": "DexSave", "CON": "ConSave",
                 "INT": "IntSave", "WIS": "WisSave", "CHA": "ChaSave"}

SKILL_PROP = {
    "Acrobatics": "Acrobatics", "Animal Handling": "AnimalHandling",
    "Arcana": "Arcana", "Athletics": "Athletics", "Deception": "Deception",
    "History": "History", "Insight": "Insight", "Intimidation": "Intimidation",
    "Investigation": "Investigation", "Medicine": "Medicine", "Nature": "Nature",
    "Perception": "Perception", "Performance": "Performance", "Persuasion": "Persuasion",
    "Religion": "Religion", "Sleight of Hand": "SleightOfHand",
    "Stealth": "Stealth", "Survival": "Survival",
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

ALL_CLASSES = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter",
               "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

CLASS_HD = {
    "Artificer": 8, "Barbarian": 12, "Bard": 8, "Cleric": 8, "Druid": 8,
    "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 10, "Rogue": 8,
    "Sorcerer": 6, "Warlock": 8, "Wizard": 6,
}

SLOT_NAMES = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",
              "Seventh", "Eighth", "Ninth"]

# Spell slots by class at level 3 (full casters)
SPELL_SLOTS_L3 = {
    "Bard":      [4, 2, 0, 0, 0, 0, 0, 0, 0],
    "Cleric":    [4, 2, 0, 0, 0, 0, 0, 0, 0],
    "Druid":     [4, 2, 0, 0, 0, 0, 0, 0, 0],
    "Sorcerer":  [4, 2, 0, 0, 0, 0, 0, 0, 0],
    "Wizard":    [4, 2, 0, 0, 0, 0, 0, 0, 0],
    "Warlock":   [0, 2, 0, 0, 0, 0, 0, 0, 0],  # pact slots
    "Paladin":   [3, 0, 0, 0, 0, 0, 0, 0, 0],  # half-caster
    "Ranger":    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    "Artificer": [3, 0, 0, 0, 0, 0, 0, 0, 0],
}


# ── Stat helpers ─────────────────────────────────────────────────────────────

def ability_mod(score):
    return (score - 10) // 2

def prof_bonus(level):
    return 2 + (level - 1) // 4

def calc_ac(cs):
    override = cs.get("ac_override")
    if override is not None:
        return override
    dex   = ability_mod(cs["ability_scores"]["DEX"])
    armor = ROLE_ARMOR.get(cs.get("role", ""))
    if not armor:
        return 10 + dex
    if armor["flat"]:
        return armor["base_ac"] + (2 if armor["shield"] else 0)
    return armor["base_ac"] + min(dex, armor["dex_cap"]) + (2 if armor["shield"] else 0)

def calc_skills(cs):
    pb        = prof_bonus(cs["level"])
    profs     = set(cs.get("skill_proficiencies", []))
    expertise = set(cs.get("expertise", []))
    overrides = cs.get("skill_overrides", {})
    scores    = cs["ability_scores"]
    result    = {}
    for skill, ability in SKILL_ABILITY.items():
        if skill in overrides:
            result[skill] = overrides[skill]
        elif skill in expertise:
            result[skill] = ability_mod(scores[ability]) + pb * 2
        elif skill in profs:
            result[skill] = ability_mod(scores[ability]) + pb
        else:
            result[skill] = ability_mod(scores[ability])
    return result

def calc_saves(cs):
    pb         = prof_bonus(cs["level"])
    save_profs = set(cs.get("saving_throw_proficiencies", []))
    scores     = cs["ability_scores"]
    return {ab: ability_mod(scores[ab]) + (pb if ab in save_profs else 0) for ab in ABILITIES}


# ── Portrait loading ──────────────────────────────────────────────────────────

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

def _pil_to_png(img, size=200):
    img  = img.convert("RGBA")
    w, h = img.size
    side = min(w, h)
    img  = img.crop(((w-side)//2, (h-side)//2, (w+side)//2, (h+side)//2))
    img  = img.resize((size, size), PILImage.LANCZOS)
    buf  = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def load_portrait(cs):
    if not HAS_PIL:
        return None
    pf = cs.get("portrait_file", "").strip()
    if pf:
        path = PLAYERS_DIR / pf
        if path.exists():
            return _pil_to_png(PILImage.open(path))
    first = cs["name"].split()[0].lower()
    for f in sorted(PLAYERS_DIR.iterdir()):
        if f.suffix.lower() in IMAGE_EXTS and first in f.stem.lower():
            return _pil_to_png(PILImage.open(f))
    return None


# ── Minimal PNG fallback ──────────────────────────────────────────────────────

def _chunk(tag, data):
    tag_b = tag.encode() if isinstance(tag, str) else tag
    crc   = struct.pack(">I", zlib.crc32(tag_b + data) & 0xFFFFFFFF)
    return struct.pack(">I", len(data)) + tag_b + data + crc

def make_color_png(r, g, b, size=200):
    ihdr = _chunk("IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
    raw  = b"".join(b"\x00" + bytes([r, g, b] * size) for _ in range(size))
    return b"\x89PNG\r\n\x1a\n" + ihdr + _chunk("IDAT", zlib.compress(raw)) + _chunk("IEND", b"")

def hex_to_rgb(h):
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def new_baguid():
    return base64.b64encode(uuid.uuid4().bytes).decode()


# ── XML builder ───────────────────────────────────────────────────────────────

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
    scores  = cs["ability_scores"]
    level   = cs["level"]
    pb      = prof_bonus(level)
    skills  = calc_skills(cs)
    saves   = calc_saves(cs)
    ac      = calc_ac(cs)
    cls     = cs.get("class", "")
    hd      = CLASS_HD.get(cls, 8)
    slots   = SPELL_SLOTS_L3.get(cls, [0]*9)

    spell_ab  = cs.get("spellcasting_ability", "")
    spell_mod = ability_mod(scores.get(spell_ab, 10)) if spell_ab else 0

    props = {}

    # ── Core combat ─────────────────────────────────────────────────────────
    props["HP"]            = cs["hp_max"]
    props["MaxHP"]         = cs["hp_max"]
    props["eHP"]           = cs["hp_max"]
    props["eMaxHP"]        = cs["hp_max"]
    props["DisplayHP"]     = cs["hp_max"]
    props["TempHP"]        = 0
    props["TempMaxHP"]     = 0
    props["AC"]            = ac
    props["Speed"]         = 30
    props["Initiative"]    = ability_mod(scores["DEX"])
    props["InitiativeBonus"] = ability_mod(scores["DEX"])
    props["CharLevel"]     = level
    props["Proficiency"]   = pb

    # ── Class & race ─────────────────────────────────────────────────────────
    props["Class"]         = cls
    props["TrueClass"]     = cls
    props["Race"]          = cs.get("race", "")
    props["TrueRace"]      = cs.get("race", "")
    props["Creaturetype"]  = "Humanoid"

    # ── Class levels (one field per class, 0 if not that class) ──────────────
    for c in ALL_CLASSES:
        props[c] = level if c == cls else 0

    # ── Hit dice ──────────────────────────────────────────────────────────────
    for die in [4, 6, 8, 10, 12, 20]:
        props[f"HD{die}"]     = level if die == hd else 0
        props[f"UsedHD{die}"] = 0

    # ── Ability scores ────────────────────────────────────────────────────────
    for ab in ABILITIES:
        props[ABILITY_FULL[ab]] = scores[ab]
        props[ABILITY_MOD[ab]]  = ability_mod(scores[ab])
        props[ABILITY_SAVE[ab]] = saves[ab]

    # ── Skills ───────────────────────────────────────────────────────────────
    for skill, val in skills.items():
        props[SKILL_PROP[skill]] = val

    # ── Passive checks ────────────────────────────────────────────────────────
    props["PassivePerception"]    = 10 + skills["Perception"]
    props["PassiveInsight"]       = 10 + skills["Insight"]
    props["PassiveInvestigation"] = 10 + skills["Investigation"]

    # ── Spellcasting ──────────────────────────────────────────────────────────
    props["SpellcastingAbility"]  = spell_ab
    props["SpellSaveDC"]          = (8 + pb + spell_mod) if spell_ab else 0
    props["SpellAttackBonus"]     = (pb + spell_mod) if spell_ab else 0
    for i, name in enumerate(SLOT_NAMES):
        props[name] = slots[i]

    # ── Status / tracking ─────────────────────────────────────────────────────
    props["DeathSuccesses"]  = 0
    props["DeathFails"]      = 0
    props["Exhaustion"]      = 0
    props["Concentration"]   = 0
    props["ReadyAction"]     = 0
    props["HitDieUsed"]      = 0

    # ── Campaign-specific ─────────────────────────────────────────────────────
    props["UnitRole"]            = cs.get("role", "")
    props["CorruptionLevel"]     = cs.get("corruption_level", 0)
    props["CommendationesCount"] = cs.get("commendationes", 0)
    props["CitizenshipStatus"]   = cs.get("citizenship", "Peregrinus")
    props["Armor"]               = ROLE_ARMOR.get(cs.get("role",""), {}).get("armor", "")
    props["Languages"]           = ", ".join(cs.get("languages", []))
    props["Backstory"]           = cs.get("background_story", "")
    props["Description"]         = cs.get("notes", "")
    props["Senses"]              = "Darkvision 60 ft." if "darkvision" in cs.get("notes","").lower() else ""

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

    png = load_portrait(cs)
    if png is None:
        r, g, b = hex_to_rgb(cs.get("portrait_color", "#8B0000"))
        png = make_color_png(r, g, b, 200)
        portrait_src = "color"
    else:
        portrait_src = cs.get("portrait_file") or "auto"

    thumb = _pil_to_png(PILImage.open(io.BytesIO(png)), 50) if HAS_PIL else png
    md5   = hashlib.md5(png).hexdigest()
    ac    = calc_ac(cs)
    role  = cs.get("role") or "unassigned"

    with zipfile.ZipFile(output_dir / f"{cs['name'].replace(' ','_')}.rptok",
                         "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.xml", build_content_xml(cs, md5))
        zf.writestr("properties.xml", build_properties_xml())
        zf.writestr(f"assets/{md5}", png)
        zf.writestr(f"assets/{md5}.png", png)
        zf.writestr("thumbnail", thumb)
        zf.writestr("thumbnail_large", png)

    print(f"  {cs['name']:<28} {cs.get('class','?'):<12} L{cs['level']} AC{ac:<4} {role}  [{portrait_src}]")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if len(sys.argv) > 1:
        sheets = [Path(p) for p in sys.argv[1:]]
    else:
        sheets = sorted(p for p in PLAYERS_DIR.glob("*.json")
                        if p.name not in ("template.json",) and not p.name.startswith("_"))
    if not sheets:
        print(f"No sheets found in {PLAYERS_DIR}")
        return
    print(f"Generating PC tokens → {OUTPUT_DIR}")
    for sheet in sheets:
        generate_token(sheet, OUTPUT_DIR)
    print("Done.")


if __name__ == "__main__":
    main()
