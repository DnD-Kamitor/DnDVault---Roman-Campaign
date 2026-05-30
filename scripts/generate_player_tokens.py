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
import xml.etree.ElementTree as ET
import zipfile
import zlib
from pathlib import Path

try:
    from PIL import Image as PILImage
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

REPO_ROOT    = Path(__file__).parent.parent
SCRIPTS_DIR  = Path(__file__).parent
PLAYERS_DIR  = REPO_ROOT / "players"
OUTPUT_DIR   = REPO_ROOT / "Maptool" / "tokens" / "players"
MACROS_XML   = SCRIPTS_DIR / "standard_token_macros.xml"

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
    """Return skill proficiency FLAGS (0/1/2) matching the standard macro formula:
    1d20 + AbilityMod + (Proficiency * SkillFlag)
    0 = not proficient, 1 = proficient, 2 = expertise.
    skill_overrides supply total bonuses; we back-convert to the closest flag."""
    pb        = prof_bonus(cs["level"])
    profs     = set(cs.get("skill_proficiencies", []))
    expertise = set(cs.get("expertise", []))
    overrides = cs.get("skill_overrides", {})
    scores    = cs["ability_scores"]
    result    = {}
    for skill, ability in SKILL_ABILITY.items():
        if skill in overrides:
            amod = ability_mod(scores[ability])
            flag = (overrides[skill] - amod) // pb if pb else 0
            result[skill] = max(0, flag)
        elif skill in expertise:
            result[skill] = 2
        elif skill in profs:
            result[skill] = 1
        else:
            result[skill] = 0
    return result

def calc_saves(cs):
    """Return saving throw proficiency FLAGS (0 or 1) matching the standard macro formula:
    1d20 + AbilityMod + (Proficiency * SaveFlag)"""
    save_profs = set(cs.get("saving_throw_proficiencies", []))
    return {ab: (1 if ab in save_profs else 0) for ab in ABILITIES}


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


# ── Macro builder ─────────────────────────────────────────────────────────────

def _xe(s):
    """XML-escape a string for embedding in element text."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _macro_entry(idx, label, group, color, command, fontcolor="black",
                 fontsize="1.25em", minwidth="100px", sortby=""):
    return (
        f"  <entry>\n"
        f"    <int>{idx}</int>\n"
        f"    <net.rptools.maptool.model.MacroButtonProperties>\n"
        f"      <macroUUID>{uuid.uuid4()}</macroUUID>\n"
        f"      <saveLocation>Token</saveLocation>\n"
        f"      <index>{idx}</index>\n"
        f"      <colorKey>{color}</colorKey>\n"
        f"      <hotKey>None</hotKey>\n"
        f"      <command>{_xe(command)}</command>\n"
        f"      <label>{_xe(label)}</label>\n"
        f"      <group>{group}</group>\n"
        f"      <sortby>{sortby}</sortby>\n"
        f"      <autoExecute>true</autoExecute>\n"
        f"      <includeLabel>false</includeLabel>\n"
        f"      <applyToTokens>false</applyToTokens>\n"
        f"      <fontColorKey>{fontcolor}</fontColorKey>\n"
        f"      <fontSize>{fontsize}</fontSize>\n"
        f"      <minWidth>{minwidth}</minWidth>\n"
        f"      <maxWidth/>\n"
        f"      <allowPlayerEdits>true</allowPlayerEdits>\n"
        f"      <toolTip/>\n"
        f"      <displayHotKey>true</displayHotKey>\n"
        f"      <commonMacro>false</commonMacro>\n"
        f"      <compareGroup>true</compareGroup>\n"
        f"      <compareSortPrefix>true</compareSortPrefix>\n"
        f"      <compareCommand>true</compareCommand>\n"
        f"      <compareIncludeLabel>true</compareIncludeLabel>\n"
        f"      <compareAutoExecute>true</compareAutoExecute>\n"
        f"      <compareApplyToSelectedTokens>true</compareApplyToSelectedTokens>\n"
        f"    </net.rptools.maptool.model.MacroButtonProperties>\n"
        f"  </entry>"
    )

def _attack_cmd(atk, spell_mod_prop="0"):
    """Return MTScript command string for one attack entry, or None to skip."""
    atype  = atk.get("type", "melee")
    weapon = atk.get("weapon", "weapon")
    note   = atk.get("note", "")
    note_part = f"<br><i style='color:gray'>({note})</i>" if note else ""

    if atype in ("melee", "ranged"):
        # Resolve atk_props — substitute SpellAttackBonus with inline formula
        resolved = []
        for p in atk.get("atk_props", ["Proficiency"]):
            if p == "SpellAttackBonus":
                resolved.append(f"Proficiency + {spell_mod_prop}")
            else:
                resolved.append(p)
        atk_expr = " + ".join(resolved)

        dice   = atk.get("damage_dice", "1d4")
        dmgmod = atk.get("damage_mod", "")
        if dmgmod == "SpellAttackBonus":
            dmgmod = spell_mod_prop
        dmgtyp = atk.get("damage_type", "damage")
        dmg_expr = f"{dice} + {dmgmod}" if dmgmod else dice

        # [h: critRoll] captures d20 for crit check; [e:] shows full breakdown inline
        # e.g. "« critRoll+DexMod+Proficiency = 14+3+2 = 19 »"
        return (
            f"[h: critRoll = 1d20]"
            f"/me [r, if(critRoll == 20): \"<b style='color:red'>CRITICALLY HITS</b> with\"; \"attacks with\"] "
            f"{weapon}"
            f"[r, if(critRoll == 1): \" but rolled a <b style='color:red'>NATURAL 1!</b>\"; \"!\"]<br>"
            f"ATK: [e: critRoll + {atk_expr}] | DMG: [e: {dmg_expr}] {dmgtyp}"
            f"{note_part}"
        )

    elif atype == "damage":
        # Merged into the melee/ranged macro above — skip separate button
        return None

    elif atype == "save":
        dc_expr  = f"8 + Proficiency + {spell_mod_prop}"
        save_ab  = atk.get("save_ability", "WIS")
        dice     = atk.get("damage_dice", "1d4")
        dmgtyp   = atk.get("damage_type", "damage")
        on_fail  = atk.get("on_fail", "")
        fail_part = f"<br><i>On fail: {on_fail}</i>" if on_fail else ""
        return (
            f"/me uses {weapon}!<br>"
            f"DC [e: {dc_expr}] {save_ab} save or takes [e: {dice}] {dmgtyp} damage.{fail_part}{note_part}"
        )

    elif atype == "heal":
        dice   = atk.get("damage_dice", "1d4")
        dmgmod = atk.get("damage_mod", spell_mod_prop)
        if dmgmod == "SpellAttackBonus":
            dmgmod = spell_mod_prop
        heal_expr = f"{dice} + {dmgmod}" if dmgmod else dice
        return (
            f"/me uses {weapon}!<br>"
            f"Target regains [e: {heal_expr}] HP.{note_part}"
        )

    elif atype == "utility":
        dice = atk.get("damage_dice", "")
        if dice:
            return f"/me uses {weapon}!<br>Roll: [e: {dice}].{note_part}"
        return f"/me uses {weapon}!{note_part}"

    return f"/me uses {weapon}!{note_part}"

def build_macros_xml(cs):
    # Standard macros from extracted Standard Token
    if MACROS_XML.exists():
        raw = MACROS_XML.read_text()
        inner = raw.strip()
        if inner.startswith("<macroPropertiesMap>"):
            inner = inner[len("<macroPropertiesMap>"):]
        if inner.endswith("</macroPropertiesMap>"):
            inner = inner[:-len("</macroPropertiesMap>")]
        standard_entries = inner.strip()
    else:
        standard_entries = ""

    # Resolve spell modifier property name from spellcasting_ability
    spell_ab       = cs.get("spellcasting_ability", "")
    spell_mod_prop = ABILITY_MOD.get(spell_ab, "0") if spell_ab else "0"

    # Character-specific attack macros (index 100+), skipping "damage" type
    attack_entries = []
    idx = 100
    for atk in cs.get("attacks", []):
        cmd = _attack_cmd(atk, spell_mod_prop)
        if cmd is None:
            continue
        color = atk.get("color", "default")
        label = atk.get("label", f"Attack {idx}")
        attack_entries.append(
            _macro_entry(idx, label, "Combat", color, cmd, sortby="3.0")
        )
        idx += 1

    parts = [standard_entries] + attack_entries
    body  = "\n".join(p for p in parts if p)
    return f"<macroPropertiesMap>\n{body}\n</macroPropertiesMap>"


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

    # ── Passive checks (10 + ability_mod + proficiency * flag) ──────────────────
    def _passive(skill_name):
        ability = SKILL_ABILITY[skill_name]
        return 10 + ability_mod(scores[ability]) + pb * skills[skill_name]
    props["PassivePerception"]    = _passive("Perception")
    props["PassiveInsight"]       = _passive("Insight")
    props["PassiveInvestigation"] = _passive("Investigation")

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

    # CustomCounters — JSON array consumed by the Sheet macro's counter display
    counters = cs.get("counters", [])
    props["CustomCounters"] = json.dumps(counters) if counters else ""

    entries    = "\n".join(_prop(k, v) for k, v in props.items())
    macros_xml = build_macros_xml(cs)
    sight_type = "Darkvision 120" if "darkvision" in cs.get("notes", "").lower() else "Normal"

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
  <visibleOnlyToOwner>false</visibleOnlyToOwner>
  <vblColorSensitivity>-1</vblColorSensitivity>
  <alwaysVisibleTolerance>2</alwaysVisibleTolerance>
  <isAlwaysVisible>false</isAlwaysVisible>
  <name>{cs["name"]}</name>
  <ownerList/>
  <ownerType>1</ownerType>
  <tokenShape>CIRCLE</tokenShape>
  <tokenType>PC</tokenType>
  <layer>TOKEN</layer>
  <propertyType>Basic</propertyType>
  <tokenOpacity>1.0</tokenOpacity>
  <isFlippedX>false</isFlippedX>
  <isFlippedY>false</isFlippedY>
  <isFlippedIso>false</isFlippedIso>
  <uniqueLightSources class="linked-hash-map"/>
  <lightSourceList/>
  <hasSight>true</hasSight>
  <sightType>{sight_type}</sightType>
  <propertyMapCI>
    <store>
{entries}
    </store>
  </propertyMapCI>
  <state/>
  {macros_xml}
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

    asset_name = cs["name"].replace(" ", "_").lower()
    asset_xml = (
        f"<net.rptools.maptool.model.Asset>\n"
        f"  <id>\n    <id>{md5}</id>\n  </id>\n"
        f"  <name>{asset_name}</name>\n"
        f"  <extension>png</extension>\n"
        f"  <type>image</type>\n"
        f"  <image/>\n"
        f"</net.rptools.maptool.model.Asset>"
    )

    with zipfile.ZipFile(output_dir / f"{cs['name'].replace(' ','_')}.rptok",
                         "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.xml", build_content_xml(cs, md5))
        zf.writestr("properties.xml", build_properties_xml())
        zf.writestr(f"assets/{md5}", asset_xml)
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
