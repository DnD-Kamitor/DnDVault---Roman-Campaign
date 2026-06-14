#!/usr/bin/env python3
"""Update S1 vault monster tokens with tactical abilities and gmNotes."""

import zipfile, shutil, os, uuid, re
from pathlib import Path

BASE = Path(__file__).parent.parent / "Maptool/tokens/npcs/creatures"

def new_uuid():
    return str(uuid.uuid4())

def macro_xml(index, label, group, command, color="orange", font="white", tooltip=""):
    tip = tooltip.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    cmd = command.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    lbl = label.replace("<", "&lt;").replace(">", "&gt;")
    return f"""
  <entry>
    <int>{index}</int>
    <net.rptools.maptool.model.MacroButtonProperties>
      <macroUUID>{new_uuid()}</macroUUID>
      <saveLocation>Token</saveLocation>
      <index>{index}</index>
      <colorKey>{color}</colorKey>
      <hotKey>None</hotKey>
      <command>{cmd}</command>
      <label>{lbl}</label>
      <group>{group}</group>
      <sortby/>
      <autoExecute>true</autoExecute>
      <includeLabel>false</includeLabel>
      <applyToTokens>false</applyToTokens>
      <fontColorKey>{font}</fontColorKey>
      <fontSize>1.10em</fontSize>
      <minWidth>90px</minWidth>
      <maxWidth/>
      <allowPlayerEdits>false</allowPlayerEdits>
      <toolTip>{tip}</toolTip>
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

TOKENS = {
    "Shadow.rptok": {
        "gmNotes": (
            "Session 1 Flooded Gallery (x4), Altar Chamber (x2). "
            "Life Drain: on hit, STR reduced by 1d4. Creature dies and rises as Shadow if STR drops to 0. "
            "Advantage in dim light or darkness.\n\n"
            "TACTICS:\n"
            "- Extinguish Torch (1/round): target torch-carrier, DC 13 Dex save or light out. Forces darkness.\n"
            "- Emerge Behind: after round 1, move through floor and appear behind rearmost PC. Breaks formation.\n"
            "- Shove from Below (instead of Strength Drain): STR contest, prone in water = half speed + difficult terrain.\n"
            "- In flooded gallery: Shadows do NOT all attack same target. Split across formation."
        ),
        "start_index": 102,
        "macros": [
            {
                "label": "Extinguish Torch",
                "group": "Tactics",
                "color": "orange",
                "command": "/me reaches for a torch-carrier's light — DC 13 Dexterity save or the light goes out. Shadows gain advantage in darkness.",
                "tooltip": "1/round. Forces players into darkness. All Shadows gain advantage.",
            },
            {
                "label": "Emerge Behind",
                "group": "Tactics",
                "color": "orange",
                "command": "/me sinks into the floor and rises behind the rearmost PC. Move token behind party. Stealth DC 14 to notice before it acts.",
                "tooltip": "Use after round 1. Breaks shield formation. Targets rear of marching order.",
            },
            {
                "label": "Shove (Water)",
                "group": "Attacks",
                "color": "red",
                "command": "/me shoves its target prone into the water — STR contest: [t: 1d20 + StrMod]. On win: target prone (half speed, costs action to stand, difficult terrain).",
                "tooltip": "Alternative to Strength Drain. No damage — pure action economy drain.",
            },
        ],
    },

    "Ghoul.rptok": {
        "gmNotes": (
            "Session 1 Bone Chamber (x2). Claws: DC 10 CON save or paralyzed until end of next turn. "
            "Bite does extra damage against paralyzed targets.\n\n"
            "TACTICS:\n"
            "- Drag to Ghast: if both claw attacks hit same turn, grapple (STR +2) and drag 10 ft toward Ghast. "
            "Ghast gains advantage vs dragged target.\n"
            "- Wall Crawl: Ghouls climb (speed 30 ft). One starts on ceiling — drops onto PC, ignores shield wall bonus.\n"
            "- Do NOT both attack same target round 1. Split to force players to cover two fronts."
        ),
        "start_index": 103,
        "macros": [
            {
                "label": "Drag to Ghast",
                "group": "Attacks",
                "color": "red",
                "command": "/me drags its target toward the Ghast — grapple check: [t: 1d20+2]. On success: target pulled 10 ft, Ghast has advantage on all attacks vs them this round.",
                "tooltip": "Requires both claw attacks hitting same target same turn. Coordinates with Ghast.",
            },
            {
                "label": "Wall Crawl Drop",
                "group": "Tactics",
                "color": "orange",
                "command": "/me drops from the ceiling! Shield wall bonus does NOT apply to this attack. Claw: [t: 1d20+4] for [t: 2d6+2] slashing.",
                "tooltip": "One Ghoul starts on ceiling. Drops on a PC to bypass shield formation.",
            },
        ],
    },

    "Ghast.rptok": {
        "gmNotes": (
            "Session 1 Bone Chamber (x1, encounter boss). "
            "Stench: DC 10 CON save or poisoned until start of next turn (5 ft aura, always active). "
            "Claws: DC 13 CON save or paralyzed for 1 minute.\n\n"
            "TACTICS:\n"
            "- Let Ghouls engage first. Ghast emerges from behind benches round 2 after Stench already hit.\n"
            "- Priority: bite any paralyzed PC (auto-crit = max damage).\n"
            "- Death Scream (trigger when drops to 0 HP): both Ghouls gain advantage until end of their next turn.\n"
            "- Ghast does NOT pursue fleeing PCs. It guards the chamber exit."
        ),
        "start_index": 103,
        "macros": [
            {
                "label": "Death Scream",
                "group": "Triggered",
                "color": "#8b0000",
                "font": "white",
                "command": "/me releases a death scream as it falls! Both Ghouls gain advantage on all attacks until end of their next turn.",
                "tooltip": "Trigger when Ghast drops to 0 HP. Punishes players for ignoring Ghast.",
            },
            {
                "label": "Coordinated Bite",
                "group": "Attacks",
                "color": "red",
                "command": "/me bites the paralyzed target — automatic critical hit: [t: 2d8+4] piercing damage.",
                "tooltip": "Only vs paralyzed targets within 5 ft. Auto-crit per RAW. Coordinate with Ghoul paralysis.",
            },
        ],
    },

    "Wight.rptok": {
        "gmNotes": (
            "Session 1 Altar Chamber (guardian). Does NOT attack immediately. "
            "Speaks if party approaches the spear. DC 14 Persuasion or Insight (contract scroll = advantage) pauses combat.\n"
            "Life Drain: DC 13 CON save or HP max reduced by damage dealt. "
            "Fear heal: regains 1d4 HP at start of turn if any creature within 30 ft is Frightened.\n\n"
            "TACTICS:\n"
            "- Command Shadow (bonus action): direct one Shadow to Strength Drain a specific target this round.\n"
            "- Priority for Life Drain: PC closest to the spear or with lowest max HP.\n"
            "- Pincer: one Shadow left flank, one Shadow right. Wight holds centre. Never stack on same target.\n"
            "- Wight does NOT use the lever. He holds the altar line.\n"
            "- If party backs 15 ft from altar and stops: Wight holds. Combat is NOT mandatory."
        ),
        "start_index": 104,
        "macros": [
            {
                "label": "Command Shadow",
                "group": "Tactics",
                "color": "purple",
                "font": "white",
                "command": "/me commands a Shadow to focus on a target — that Shadow uses Strength Drain as a bonus action this round.",
                "tooltip": "Bonus action. Makes Wight feel like a general. Stacks pressure on one target.",
            },
            {
                "label": "Hold the Line",
                "group": "Tactics",
                "color": "orange",
                "command": "/me holds position at the altar. Will not advance beyond 15 ft of the spear. If party retreats, he stops attacking.",
                "tooltip": "Reminder: Wight is a guardian not a pursuer. Reinforces exit condition.",
            },
        ],
    },

    "Cultist_of_Mars.rptok": {
        "gmNotes": (
            "Session 1 vault approach + Altar Chamber. Also Sessions 2-4.\n"
            "Dark Devotion: advantage on saves vs charm and fright.\n"
            "Spellcasting (Wis DC 13, +5 atk): Cantrips: sacred flame, thaumaturgy. "
            "1st (3 slots): bane, inflict wounds, shield of faith. 2nd (2 slots): hold person, spiritual weapon.\n\n"
            "TACTICAL PRIORITY:\n"
            "- Round 1: Bane on 3 PCs (-1d4 attack rolls AND saves). Highest-threat targets first.\n"
            "- Round 2: Hold Person on PC closest to the spear or strongest melee fighter.\n"
            "- Round 3+: Spiritual Weapon vs back-line PC. Sacred Flame vs dodging targets.\n"
            "- Gladius only if cornered (no slots or adjacent).\n"
            "- Goal: spear reaches Corvinus. Will die to achieve this."
        ),
        "start_index": 102,
        "macros": [
            {
                "label": "Round 1: Bane",
                "group": "Tactics",
                "color": "purple",
                "font": "white",
                "command": "/me casts Bane on three targets — DC 13 CHA save or -1d4 to attack rolls and saving throws for 1 minute.",
                "tooltip": "Priority Round 1. Hits 3 PCs. Stacks with Wight pressure and Shadows.",
            },
            {
                "label": "Round 2: Hold Person",
                "group": "Tactics",
                "color": "purple",
                "font": "white",
                "command": "/me casts Hold Person — DC 13 WIS save or paralyzed. Wight and Shadows gain advantage vs paralyzed target.",
                "tooltip": "Priority Round 2. Target: PC closest to spear or highest-damage melee fighter.",
            },
            {
                "label": "Spiritual Weapon",
                "group": "Attacks",
                "color": "#4040cc",
                "font": "white",
                "command": "/me sends the Spiritual Weapon at a back-line target — bonus action: [t: 1d20+5] for [t: 1d8+3] force damage.",
                "tooltip": "Round 3+. Target back-line PC (caster, healer). Keeps pressure on multiple fronts.",
            },
        ],
    },
}


def patch_token(rptok_path: Path, gm_notes: str, start_idx: int, macros: list):
    tmp_dir = Path("/tmp") / rptok_path.stem
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir()

    with zipfile.ZipFile(rptok_path) as zf:
        zf.extractall(tmp_dir)

    xml_path = tmp_dir / "content.xml"
    xml = xml_path.read_text(encoding="utf-8")

    escaped = gm_notes.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    xml = re.sub(r"<gmNotes>[^<]*</gmNotes>", f"<gmNotes>{escaped}</gmNotes>", xml)

    new_macros = ""
    for i, m in enumerate(macros):
        new_macros += macro_xml(
            index=start_idx + i,
            label=m["label"],
            group=m["group"],
            command=m["command"],
            color=m.get("color", "orange"),
            font=m.get("font", "white"),
            tooltip=m.get("tooltip", ""),
        )

    xml = xml.replace("</macroPropertiesMap>", new_macros + "\n</macroPropertiesMap>")
    xml_path.write_text(xml, encoding="utf-8")

    with zipfile.ZipFile(rptok_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(tmp_dir.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(tmp_dir))

    shutil.rmtree(tmp_dir)
    print(f"Updated: {rptok_path.name}")


def main():
    for filename, data in TOKENS.items():
        path = BASE / filename
        if not path.exists():
            print(f"MISSING: {path}")
            continue
        patch_token(path, data["gmNotes"], data["start_index"], data["macros"])
    print("Done.")


if __name__ == "__main__":
    main()
