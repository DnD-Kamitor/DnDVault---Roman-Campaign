#!/usr/bin/env python3
"""
Inject creature stat data into .rptok creature tokens:
1. Fix save proficiency values (0 = not proficient, 1 = proficient)
2. Add Attack dialog macros to creatures that are missing them
3. Update token notes with the full notes text from creature_stats.json

Usage:
  python3 scripts/inject_creature_stats.py
"""

import html
import json
import os
import re
import uuid
import zipfile
from pathlib import Path

BASE = Path(__file__).parent.parent
CREATURES_DIR = BASE / "Maptool/tokens/npcs/creatures"
STATS_FILE = Path(__file__).parent / "creature_stats.json"

# ── Creature type classification for dialog color theme ──────────────────────

UNDEAD = {
    "Skeleton", "Zombie", "Ghoul", "Ghast", "Shadow", "Wraith", "Specter",
    "Wight", "Draugar", "Haugbui", "Alp", "Myling", "Vaettir",
}
SPIRIT_FEY = {
    "Larvae", "Genius_Loci", "Nix", "Strix", "Will-o-Wisp", "Dryad",
}
BEAST = {
    "Wolf", "Dire_Wolf", "Boar", "Brown_Bear", "Giant_Spider",
}


def type_style(stem):
    """Return (accent_color, background_color, attack_box_bg) for creature type."""
    if stem in UNDEAD:
        return "#c0392b", "#1a0000", "#2a1a1a"
    if stem in SPIRIT_FEY:
        return "#8e44ad", "#1a0020", "#2a1a2a"
    if stem in BEAST:
        return "#d4a017", "#1a1200", "#2a1f00"
    return "#2980b9", "#001a2a", "#001f35"   # humanoid


# ── Dice expression parser ───────────────────────────────────────────────────

def parse_dice(dice_str):
    """Parse '2d4+2' into (dice_part, mod_int). Returns (None, 0) if not a dice string."""
    m = re.match(r'^(\d+d\d+)([+-]\d+)?$', str(dice_str).strip())
    if not m:
        return None, 0
    dice = m.group(1)
    mod = int(m.group(2)) if m.group(2) else 0
    return dice, mod


def mod_expr(mod):
    """Return '+2', '-1', or '' for a modifier int."""
    if mod > 0:
        return f"+{mod}"
    if mod < 0:
        return str(mod)
    return ""


# ── Attack dialog macro builder ──────────────────────────────────────────────

def build_attack_command(stem, stats):
    """Return the raw (unescaped) MTScript command for the Attack dialog macro."""
    name_display = stem.replace("_", " ")
    ac = stats["ac"]
    hp = stats["hp"]
    speed = stats["speed"]
    cr = stats.get("cr", "?")
    attacks = stats.get("attacks", [])
    traits = stats.get("traits", [])
    color, bg, ab_bg = type_style(stem)

    lines = [
        f"<!-- {name_display} (CR {cr}) -->",
        "[h: tokenName = getName()]",
        f'[dialog("{name_display} Attacks", "width=420; height=460; temporary=true;")]',
        "<html><head><style>",
        f"  body{{font-family:Georgia,serif;background:{bg};color:#e0e0e0;padding:12px;margin:0}}",
        f"  h2{{color:{color};margin:0 0 6px 0;font-size:15px;border-bottom:1px solid {color};padding-bottom:4px}}",
        "  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}",
        f"  .ab{{background:{ab_bg};border:1px solid {color};border-radius:4px;padding:10px;margin-bottom:8px}}",
        f"  .lb{{font-size:11px;color:{color};text-transform:uppercase;letter-spacing:1px}}",
        "  .rv{font-size:24px;font-weight:bold;color:#fff}",
        "  .dt{font-size:12px;color:#bbb;margin-top:4px}",
        "  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:8px}",
        f"  .tr{{font-size:11px;color:#bbb;background:#111;border-left:3px solid {color};padding:6px;margin-bottom:6px}}",
        "</style></head><body>",
        f"<h2>{name_display.upper()} \u2014 [r: tokenName]</h2>",
        f'<div class="sr"><span>AC {ac}</span><span>HP {hp}</span><span>Speed {speed}</span></div>',
    ]

    for i, atk in enumerate(attacks):
        label = atk["label"]
        atk_bonus = atk.get("atk", 0)
        dice_str = str(atk.get("dice", "0"))
        atk_type = atk.get("type", "damage")
        note = atk.get("note", "")
        reach = atk.get("reach", "5 ft.")

        if atk_type == "utility" or dice_str == "0":
            # Special ability — no dice roll
            lines += [
                '<div class="ab" style="border-color:#666;">',
                f'  <div class="lb" style="color:#888;">{label}</div>',
                f'  <div class="dt">{reach}</div>',
            ]
            if note:
                lines.append(f'  <div class="nt">{note}</div>')
            lines.append("</div>")

        elif atk_type == "healing":
            dice, mod = parse_dice(dice_str)
            lines += [
                '<div class="ab" style="border-color:#27ae60;">',
                f'  <div class="lb" style="color:#27ae60;">{label}</div>',
                f"  [h: d_{i} = {dice}]",
                f'  <div class="rv" style="color:#27ae60;">Heal: [r: d_{i}{mod_expr(mod)}]</div>',
                f'  <div class="dt">({dice_str}) \u2014 {reach}</div>',
            ]
            if note:
                lines.append(f'  <div class="nt">{note}</div>')
            lines.append("</div>")

        elif atk_bonus == 0:
            # Save-based attack (cantrip, Sacred Flame, etc.)
            dice, mod = parse_dice(dice_str)
            lines += ['<div class="ab">',
                      f'  <div class="lb">{label} \u2014 {reach}</div>']
            if dice:
                lines += [
                    f"  [h: d_{i} = {dice}]",
                    f'  <div class="rv">Damage: [r: d_{i}{mod_expr(mod)}]'
                    f'  <span style="font-size:14px;color:#aaa;">({dice_str})</span></div>',
                    f'  <div class="dt">{atk_type}</div>',
                ]
            if note:
                lines.append(f'  <div class="nt">{note}</div>')
            lines.append("</div>")

        else:
            # Standard attack roll + damage
            dice, mod = parse_dice(dice_str)
            atk_label = f"+{atk_bonus}" if atk_bonus >= 0 else str(atk_bonus)
            lines += [
                '<div class="ab">',
                f'  <div class="lb">{label} \u2014 {reach}</div>',
                f"  [h: r_{i} = 1d20]",
                f'  <div class="rv">Attack: [r: r_{i} + {atk_bonus}]'
                f'  <span style="font-size:14px;color:#aaa;">(1d20{atk_label})</span></div>',
                f"  [h: d_{i} = {dice}]",
                f'  <div class="dt">Damage: <b>[r: d_{i}{mod_expr(mod)}] {atk_type}</b>'
                f'  ({dice_str})</div>',
            ]
            if note:
                lines.append(f'  <div class="nt">{note}</div>')
            lines.append("</div>")

    for trait in traits:
        lines += [f'<div class="tr">{trait}</div>']

    lines += ["</body></html>", "[/dialog]"]
    return "\n".join(lines)


def make_macro_xml(stem, stats):
    """Build XML entry for the Attack macro (index 100)."""
    cmd = build_attack_command(stem, stats)
    cmd_escaped = html.escape(cmd, quote=False)
    new_uuid = str(uuid.uuid4())
    return f"""  <entry>
    <int>100</int>
    <net.rptools.maptool.model.MacroButtonProperties>
      <macroUUID>{new_uuid}</macroUUID>
      <saveLocation>Token</saveLocation>
      <index>100</index>
      <colorKey>red</colorKey>
      <hotKey>None</hotKey>
      <command>{cmd_escaped}</command>
      <label>Attack</label>
      <group>Combat</group>
      <sortby />
      <autoExecute>true</autoExecute>
      <includeLabel>false</includeLabel>
      <applyToTokens>false</applyToTokens>
      <fontColorKey>white</fontColorKey>
      <fontSize>1.25em</fontSize>
      <minWidth>183px</minWidth>
      <maxWidth />
      <allowPlayerEdits>false</allowPlayerEdits>
      <toolTip></toolTip>
      <displayHotKey>true</displayHotKey>
      <commonMacro>false</commonMacro>
      <compareGroup>true</compareGroup>
      <compareSortPrefix>true</compareSortPrefix>
      <compareCommand>true</compareCommand>
      <compareIncludeLabel>true</compareIncludeLabel>
      <compareAutoExecute>true</compareAutoExecute>
      <compareApplyToSelectedTokens>true</compareApplyToSelectedTokens>
    </net.rptools.maptool.model.MacroButtonProperties>
  </entry>"""


# ── Save proficiency updater ──────────────────────────────────────────────────

SAVE_MAP = [
    ("StrSave", "STR"),
    ("DexSave", "DEX"),
    ("ConSave", "CON"),
    ("IntSave", "INT"),
    ("WisSave", "WIS"),
    ("ChaSave", "CHA"),
]


def update_saves(xml, saves):
    """Set XxxSave property to 1 if creature is proficient, 0 otherwise."""
    for prop, key in SAVE_MAP:
        val = saves.get(key, 0)
        is_prof = val not in (0, None, "0")
        new_val = "1" if is_prof else "0"
        pattern = rf'(<key>{prop}</key>.*?<value class="string">)[01](</value>)'
        xml = re.sub(pattern, rf"\g<1>{new_val}\g<2>", xml, flags=re.DOTALL)
    return xml


# ── Token processor ──────────────────────────────────────────────────────────

def process_token(rptok_path, stem, stats):
    """Update saves, notes, and add attack macro if missing."""
    with zipfile.ZipFile(rptok_path) as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    xml = files["content.xml"].decode("utf-8")
    changed = False

    # 1. Fix saves
    new_xml = update_saves(xml, stats.get("saves", {}))
    if new_xml != xml:
        changed = True
    xml = new_xml

    # 2. Update notes
    new_notes = stats.get("notes", "")
    if new_notes:
        escaped = html.escape(new_notes, quote=False)
        new_xml = re.sub(r"<notes>.*?</notes>", f"<notes>{escaped}</notes>",
                         xml, flags=re.DOTALL)
        if new_xml != xml:
            changed = True
        xml = new_xml

    # 3. Add attack macro if missing and attacks exist
    has_attack_dialog = "dialog(" in xml
    attacks = stats.get("attacks", [])
    macro_added = False
    if not has_attack_dialog and attacks:
        entry = make_macro_xml(stem, stats)
        xml = xml.replace("</macroPropertiesMap>",
                          entry + "\n</macroPropertiesMap>")
        changed = True
        macro_added = True

    if changed:
        files["content.xml"] = xml.encode("utf-8")
        tmp = rptok_path + ".tmp"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for name, data in files.items():
                zout.writestr(name, data)
        os.replace(tmp, rptok_path)

    return changed, macro_added


# ── Name mapping (token filename stem → JSON key) ────────────────────────────

def json_key(stem):
    """Map token filename stem to creature_stats.json key."""
    # Handle em dash in Aquilifer filename
    clean = stem.replace("\u2014", "").replace("  ", " ").replace("_\u2014_", "_")
    # Collapse repeated underscores
    clean = re.sub(r"_+", "_", clean).strip("_")
    return clean


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    stats = json.loads(STATS_FILE.read_text())

    updated = 0
    macros_added = 0
    skipped = 0

    for fname in sorted(os.listdir(CREATURES_DIR)):
        if not fname.endswith(".rptok"):
            continue
        stem = fname[:-6]
        key = json_key(stem)
        if key not in stats:
            print(f"  [skip] {stem} (no JSON entry)")
            skipped += 1
            continue

        rptok_path = str(CREATURES_DIR / fname)
        changed, macro_added = process_token(rptok_path, stem, stats[key])
        tag = "[+atk]" if macro_added else ""
        if changed:
            print(f"  {stem:<50} updated {tag}")
            updated += 1
            if macro_added:
                macros_added += 1
        else:
            print(f"  {stem:<50} (no change)")

    print(f"\nDone. {updated} tokens updated, {macros_added} attack macros added, {skipped} skipped.")


if __name__ == "__main__":
    main()
