#!/usr/bin/env python3
"""
Generate MapTool .rptok NPC tokens from JSON files in npcs/.
Output to Maptool/tokens/npcs/named/ (named NPCs) or Maptool/tokens/npcs/creatures/.

Named NPCs are identified by the presence of an "objective" field.
Shares infrastructure with generate_player_tokens.py.

Usage:
  python scripts/generate_npc_tokens.py           # all sheets in npcs/
  python scripts/generate_npc_tokens.py npcs/shadow.json
"""

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

REPO_ROOT      = Path(__file__).parent.parent
SCRIPTS_DIR    = Path(__file__).parent
NPCS_DIR       = REPO_ROOT / "npcs"
OUTPUT_NAMED   = REPO_ROOT / "Maptool" / "tokens" / "npcs" / "named"
OUTPUT_CREATURE = REPO_ROOT / "Maptool" / "tokens" / "npcs" / "creatures"
MACROS_DIR     = REPO_ROOT / "Maptool" / "macros" / "monsters"
MACROS_XML     = SCRIPTS_DIR / "standard_token_macros.xml"

# ── Stat helpers ─────────────────────────────────────────────────────────────

def ability_mod(score):
    return (score - 10) // 2

ABILITY_FULL = {"STR": "Strength", "DEX": "Dexterity", "CON": "Constitution",
                "INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma"}
ABILITY_MOD  = {"STR": "StrMod", "DEX": "DexMod", "CON": "ConMod",
                "INT": "IntMod", "WIS": "WisMod", "CHA": "ChaMod"}
ABILITY_SAVE = {"STR": "StrSave", "DEX": "DexSave", "CON": "ConSave",
                "INT": "IntSave", "WIS": "WisSave", "CHA": "ChaSave"}

ABILITIES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

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


def calc_npc_skills(npc):
    """Return skill proficiency flags (0/1) for NPC, with override support."""
    proficiencies = set(npc.get("skill_proficiencies", []))
    overrides     = npc.get("skill_overrides", {})
    scores        = npc["ability_scores"]
    result        = {}
    for skill in SKILL_PROP:
        if skill in overrides:
            # Encode the total bonus directly; 1 = proficient (close enough for display)
            result[skill] = 1
        elif skill in proficiencies:
            result[skill] = 1
        else:
            result[skill] = 0
    return result


def calc_passive_perception(npc):
    scores    = npc["ability_scores"]
    overrides = npc.get("skill_overrides", {})
    if "Perception" in overrides:
        return 10 + overrides["Perception"]
    base = ability_mod(scores["WIS"])
    flag = 1 if "Perception" in npc.get("skill_proficiencies", []) else 0
    return 10 + base + (2 * flag)   # assume proficiency bonus 2 for display


# ── PNG helpers ───────────────────────────────────────────────────────────────

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

def _pil_to_png(img, size=200):
    img  = img.convert("RGBA")
    w, h = img.size
    if h > w:
        img = img.crop((0, 0, w, w))
    else:
        side = min(w, h)
        img  = img.crop(((w-side)//2, (h-side)//2, (w+side)//2, (h+side)//2))
    img  = img.resize((size, size), PILImage.LANCZOS)
    buf  = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def new_baguid():
    import base64
    return base64.b64encode(uuid.uuid4().bytes).decode()

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

def load_portrait(npc):
    if not HAS_PIL:
        return None
    pf = npc.get("portrait_file", "").strip()
    if pf:
        path = NPCS_DIR / pf
        if path.exists():
            return _pil_to_png(PILImage.open(path))
    return None


# ── XML helpers ───────────────────────────────────────────────────────────────

def _xe(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

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


# ── Macro builder ─────────────────────────────────────────────────────────────

def _macro_entry(idx, label, group, color, command):
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
        f"      <sortby></sortby>\n"
        f"      <autoExecute>true</autoExecute>\n"
        f"      <includeLabel>false</includeLabel>\n"
        f"      <applyToTokens>false</applyToTokens>\n"
        f"      <fontColorKey>white</fontColorKey>\n"
        f"      <fontSize>1.25em</fontSize>\n"
        f"      <minWidth>100px</minWidth>\n"
        f"      <maxWidth/>\n"
        f"      <allowPlayerEdits>false</allowPlayerEdits>\n"
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


def build_npc_macros_xml(npc):
    """Build macroPropertiesMap for an NPC token.

    Includes:
    - Standard token macros (Roll Initiative, End Turn, etc.) from standard_token_macros.xml
    - Attack macro from Maptool/macros/monsters/{macro_file} if present
    """
    # Load standard macros
    if MACROS_XML.exists():
        raw   = MACROS_XML.read_text()
        inner = raw.strip()
        if inner.startswith("<macroPropertiesMap>"):
            inner = inner[len("<macroPropertiesMap>"):]
        if inner.endswith("</macroPropertiesMap>"):
            inner = inner[:-len("</macroPropertiesMap>")]
        standard_entries = inner.strip()
    else:
        standard_entries = ""

    # Load attack macro file if specified
    macro_file = npc.get("macro_file", "").strip()
    attack_entry = ""
    if macro_file:
        macro_path = MACROS_DIR / macro_file
        if macro_path.exists():
            mts_content = macro_path.read_text()
            label = "Attack"
            attack_entry = _macro_entry(100, label, "Combat", "red", mts_content)
        else:
            print(f"    WARNING: macro file not found: {macro_path}")

    parts = [standard_entries, attack_entry]
    body  = "\n".join(p for p in parts if p)
    return f"<macroPropertiesMap>\n{body}\n</macroPropertiesMap>"


# ── Content XML builder ───────────────────────────────────────────────────────

def build_npc_content_xml(npc, image_md5, is_named):
    scores  = npc["ability_scores"]
    skills  = calc_npc_skills(npc)
    cr_str  = str(npc.get("cr", "0"))

    # Token dimensions
    width  = 200 if is_named else 100
    height = 200 if is_named else 100

    # Determine sight type from senses
    senses_text = npc.get("senses", "")
    has_darkvision = "darkvision" in senses_text.lower()
    sight_type = "Darkvision 120" if has_darkvision else "Normal"

    # Properties map
    props = {}

    # Core combat
    props["HP"]             = npc.get("hp", 0)
    props["MaxHP"]          = npc.get("hp", 0)
    props["TempHP"]         = 0
    props["AC"]             = npc.get("ac", 10)
    props["Speed"]          = npc.get("speed", "30 ft.")
    props["Initiative"]     = ability_mod(scores["DEX"])
    props["InitiativeBonus"] = ability_mod(scores["DEX"])
    props["CharLevel"]      = _cr_to_level(cr_str)
    props["Proficiency"]    = _cr_to_proficiency(cr_str)
    props["CR"]             = cr_str
    props["Creaturetype"]   = npc.get("creature_type", "Humanoid")

    # Ability scores
    for ab in ABILITIES:
        props[ABILITY_FULL[ab]] = scores[ab]
        props[ABILITY_MOD[ab]]  = ability_mod(scores[ab])

    # Saving throws -- flag-based (0 or 1)
    save_profs = set(npc.get("saving_throw_proficiencies", []))
    for ab in ABILITIES:
        props[ABILITY_SAVE[ab]] = 1 if ab in save_profs else 0

    # Skills
    for skill, val in skills.items():
        props[SKILL_PROP[skill]] = val

    # Skill overrides -- store actual bonus values in dedicated fields
    overrides = npc.get("skill_overrides", {})
    for skill, bonus in overrides.items():
        prop_name = SKILL_PROP.get(skill)
        if prop_name:
            props[prop_name + "Bonus"] = bonus

    # Passive perception
    props["PassivePerception"] = calc_passive_perception(npc)

    # Defensive properties
    props["Resistances"]          = npc.get("resistances", "")
    props["Immunities"]           = npc.get("immunities", "")
    props["ConditionImmunities"]  = npc.get("condition_immunities", "")
    props["Senses"]               = senses_text
    props["Languages"]            = npc.get("languages", "")

    # Notes and GM notes
    props["Notes"]       = npc.get("notes", "")
    props["Description"] = npc.get("notes", "")

    # Campaign-specific
    props["UnitRole"]           = "NPC"
    props["CorruptionLevel"]    = 0
    props["Session"]            = npc.get("session", 0)
    props["Size"]               = npc.get("size", "Medium")
    props["Alignment"]          = npc.get("alignment", "")

    # OGAS fields for named NPCs
    if is_named:
        props["Objective"] = npc.get("objective", "")
        props["Goal"]      = npc.get("goal", "")
        props["Agenda"]    = npc.get("agenda", "")

    entries    = "\n".join(_prop(k, v) for k, v in props.items())
    macros_xml = build_npc_macros_xml(npc)

    # GM Notes as separate element (DM-only, not in propertyMapCI)
    gm_notes_raw = npc.get("gm_notes", "")
    # Include OGAS secret in GM notes if present
    secret = npc.get("secret", "")
    if secret:
        gm_notes_raw = f"SECRET: {secret}\n\n{gm_notes_raw}"
    gm_notes_escaped = _xe(gm_notes_raw)

    token_type  = "NPC"
    token_shape = "TOP_DOWN"

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
  <width>{width}</width><height>{height}</height>
  <isoWidth>{width}</isoWidth><isoHeight>{height}</isoHeight>
  <scaleX>1.0</scaleX><scaleY>1.0</scaleY>
  <sizeMap/>
  <snapToGrid>true</snapToGrid>
  <isVisible>true</isVisible>
  <visibleOnlyToOwner>false</visibleOnlyToOwner>
  <vblColorSensitivity>-1</vblColorSensitivity>
  <alwaysVisibleTolerance>2</alwaysVisibleTolerance>
  <isAlwaysVisible>false</isAlwaysVisible>
  <name>{_xe(npc["name"])}</name>
  <ownerList/>
  <ownerType>1</ownerType>
  <tokenShape>{token_shape}</tokenShape>
  <tokenType>{token_type}</tokenType>
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
  <notes>{_xe(npc.get("notes", ""))}</notes>
  <gmNotes>{gm_notes_escaped}</gmNotes>
  <gmNotesType>text/plain</gmNotesType>
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


# ── CR helpers ────────────────────────────────────────────────────────────────

def _cr_to_level(cr_str):
    """Convert CR string to approximate character level for MapTool display."""
    cr_map = {
        "0": 1, "1/8": 1, "1/4": 1, "1/2": 2,
        "1": 2, "2": 3, "3": 5, "4": 6, "5": 8,
        "6": 9, "7": 10, "8": 11, "9": 13, "10": 14,
        "11": 15, "12": 16, "13": 17, "14": 18, "15": 19,
        "16": 20, "17": 20, "18": 20, "19": 20, "20": 20,
    }
    return cr_map.get(str(cr_str), 1)

def _cr_to_proficiency(cr_str):
    """Return proficiency bonus for the given CR."""
    try:
        # Handle fractions
        if "/" in str(cr_str):
            return 2
        cr_val = float(cr_str)
        if cr_val <= 4:   return 2
        if cr_val <= 8:   return 3
        if cr_val <= 12:  return 4
        if cr_val <= 16:  return 5
        return 6
    except (ValueError, TypeError):
        return 2


# ── Token packager ────────────────────────────────────────────────────────────

def generate_token(sheet_path):
    with open(sheet_path) as f:
        npc = json.load(f)

    # Determine if named NPC or creature
    is_named = bool(npc.get("objective") or npc.get("goal") or npc.get("agenda"))
    output_dir = OUTPUT_NAMED if is_named else OUTPUT_CREATURE

    # Generate portrait PNG
    png = load_portrait(npc)
    portrait_src = "file"
    if png is None:
        color_hex = npc.get("token_color", "#4a4a4a")
        r, g, b   = hex_to_rgb(color_hex)
        img_size  = 200 if is_named else 100
        png       = make_color_png(r, g, b, img_size)
        portrait_src = "color"

    thumb = _pil_to_png(PILImage.open(io.BytesIO(png)), 50) if HAS_PIL else png
    md5   = hashlib.md5(png).hexdigest()

    asset_name = npc["name"].replace(" ", "_").lower()
    asset_xml  = (
        f"<net.rptools.maptool.model.Asset>\n"
        f"  <id>\n    <id>{md5}</id>\n  </id>\n"
        f"  <name>{asset_name}</name>\n"
        f"  <extension>png</extension>\n"
        f"  <type>image</type>\n"
        f"  <image/>\n"
        f"</net.rptools.maptool.model.Asset>"
    )

    safe_name = npc["name"].replace(" ", "_").replace("/", "-")
    out_path  = output_dir / f"{safe_name}.rptok"
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.xml",    build_npc_content_xml(npc, md5, is_named))
        zf.writestr("properties.xml", build_properties_xml())
        zf.writestr(f"assets/{md5}",  asset_xml)
        zf.writestr(f"assets/{md5}.png", png)
        zf.writestr("thumbnail",      thumb)
        zf.writestr("thumbnail_large", png)

    kind    = "named" if is_named else "creature"
    cr_str  = npc.get("cr", "?")
    ac      = npc.get("ac", "?")
    hp      = npc.get("hp", "?")
    macro   = npc.get("macro_file", "") or "-"
    print(f"  [{kind}] {npc['name']:<28} CR{cr_str:<5} AC{ac:<4} HP{hp:<5} [{portrait_src}] macro={macro}")
    return kind


def main():
    OUTPUT_NAMED.mkdir(parents=True, exist_ok=True)
    OUTPUT_CREATURE.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1:
        sheets = [Path(p) for p in sys.argv[1:]]
    else:
        sheets = sorted(p for p in NPCS_DIR.glob("*.json")
                        if not p.name.startswith("_"))
    if not sheets:
        print(f"No sheets found in {NPCS_DIR}")
        return

    print(f"Generating NPC tokens")
    print(f"  Named   -> {OUTPUT_NAMED}")
    print(f"  Creature-> {OUTPUT_CREATURE}")
    print()

    named_count    = 0
    creature_count = 0
    for sheet in sheets:
        kind = generate_token(sheet)
        if kind == "named":
            named_count += 1
        else:
            creature_count += 1

    print()
    print(f"Done. Named NPCs: {named_count}  Creatures: {creature_count}  Total: {named_count + creature_count}")


if __name__ == "__main__":
    main()
