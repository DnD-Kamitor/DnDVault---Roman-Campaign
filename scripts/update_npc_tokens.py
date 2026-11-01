#!/usr/bin/env python3
"""
Update NPC and Creature MapTool tokens with Guy Sclanders OGAS,
tactical AI, 3-round ritual clocks, and sensory details.
"""

import uuid
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NAMED_DIR = BASE / "Maptool/tokens/npcs/named"
CREATURES_DIR = BASE / "Maptool/tokens/npcs/creatures"


def update_token(token_path: Path, new_gm_notes: str = None, new_macros: list = None):
    with zipfile.ZipFile(token_path, "r") as z:
        file_map = {name: z.read(name) for name in z.namelist()}

    xml_str = file_map["content.xml"].decode("utf-8")
    root = ET.fromstring(xml_str)

    if new_gm_notes is not None:
        gm_elem = root.find("gmNotes")
        if gm_elem is None:
            idx = 0
            for i, child in enumerate(root):
                if child.tag == "sightType":
                    idx = i + 1
                    break
            gm_elem = ET.Element("gmNotes")
            root.insert(idx, gm_elem)
        gm_elem.text = new_gm_notes

    if new_macros:
        macro_map = root.find("macroPropertiesMap")
        if macro_map is None:
            macro_map = ET.SubElement(root, "macroPropertiesMap")

        # Check existing labels to avoid duplicates
        existing_labels = {
            m.findtext("label")
            for m in macro_map.findall(
                ".//net.rptools.maptool.model.MacroButtonProperties"
            )
        }

        max_idx = 150
        for entry in macro_map.findall("entry"):
            idx_elem = entry.find("int")
            if idx_elem is not None and idx_elem.text:
                try:
                    max_idx = max(max_idx, int(idx_elem.text))
                except ValueError:
                    pass

        for m in new_macros:
            if m.get("label") in existing_labels:
                continue
            max_idx += 1
            entry = ET.SubElement(macro_map, "entry")
            int_elem = ET.SubElement(entry, "int")
            int_elem.text = str(max_idx)

            mbp = ET.SubElement(
                entry, "net.rptools.maptool.model.MacroButtonProperties"
            )
            ET.SubElement(mbp, "macroUUID").text = str(uuid.uuid4())
            ET.SubElement(mbp, "saveLocation").text = "Token"
            ET.SubElement(mbp, "index").text = str(max_idx)
            ET.SubElement(mbp, "colorKey").text = m.get("color", "default")
            ET.SubElement(mbp, "hotKey").text = "None"
            ET.SubElement(mbp, "command").text = m.get("command", "")
            ET.SubElement(mbp, "label").text = m.get("label", "Macro")
            ET.SubElement(mbp, "group").text = m.get("group", "Campaign")
            ET.SubElement(mbp, "sortby").text = m.get("sortby", "4.0")
            ET.SubElement(mbp, "autoExecute").text = "true"
            ET.SubElement(mbp, "includeLabel").text = "false"
            ET.SubElement(mbp, "applyToTokens").text = "false"
            ET.SubElement(mbp, "fontColorKey").text = m.get(
                "fontcolor", "white"
            )
            ET.SubElement(mbp, "fontSize").text = "1.15em"
            ET.SubElement(mbp, "minWidth").text = "120px"
            ET.SubElement(mbp, "maxWidth").text = ""
            ET.SubElement(mbp, "allowPlayerEdits").text = "false"
            ET.SubElement(mbp, "toolTip").text = m.get("tooltip", "")
            ET.SubElement(mbp, "displayHotKey").text = "true"
            ET.SubElement(mbp, "commonMacro").text = "false"
            ET.SubElement(mbp, "compareGroup").text = "true"
            ET.SubElement(mbp, "compareSortPrefix").text = "true"
            ET.SubElement(mbp, "compareCommand").text = "true"
            ET.SubElement(mbp, "compareIncludeLabel").text = "true"
            ET.SubElement(mbp, "compareAutoExecute").text = "true"
            ET.SubElement(mbp, "compareApplyToSelectedTokens").text = "true"

    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    file_map["content.xml"] = new_xml

    with zipfile.ZipFile(token_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in file_map.items():
            z.writestr(name, data)
    print(f"  + Updated {token_path.name}")


def main():
    print("Updating NPC and Creature tokens with Sclanders Architecture...")

    # 1. Thusnelda
    # Fix any stale pronouns or legacy notes on Thusnelda across entire XML
    p_thus = NAMED_DIR / "Thusnelda.rptok"
    with zipfile.ZipFile(p_thus, "r") as z:
        file_map = {name: z.read(name) for name in z.namelist()}
    xml_str = file_map["content.xml"].decode("utf-8")
    xml_str = xml_str.replace("she shows", "he shows")
    xml_str = xml_str.replace("She shows", "He shows")
    xml_str = xml_str.replace("Knows more than she shows", "Knows more than he shows")
    xml_str = xml_str.replace("AC 12. Vercingetorix's contact in the vicus.", "AC 13. Male völva seer.")
    file_map["content.xml"] = xml_str.encode("utf-8")
    with zipfile.ZipFile(p_thus, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in file_map.items():
            z.writestr(name, data)

    thusnelda_notes = """[THUSNELDA - MALE VÖLVA SEER (DRUID CIRCLE OF THE LAND 5)]
Pronouns: He/Him | AC: 13 | HP: 38 | Speed: 30 ft | Spell DC: 13
OGAS:
- Objective: Avert Mars's catastrophic awakening or die sanctifying his tribe's soil.
- Goal: Test the Roman vanguard's moral and spiritual resolve before surrendering the ossuary key.
- Agenda: Force the party to confront Rome's ancestral slaughter; test if they carry Mars's corrupting flame.
- Secret: Knows the Spear of Mars can only be unmade on the Granite Anvil through a willing blood sacrifice or the ancient Gaul's death-curse.

3-ROUND RITUAL SUICIDE CLOCK (Scene 3 Sacred Grove):
- Round 1: Slashes wrists with ceremonial flint blade over the 7-stone blood ring.
- Round 2: Chants the blood-song of Arminius invoking the dormant wrath.
- Round 3: Completes ritual suicide; spilled life-blood corrupts the grove and empowers the bone guardians.

INTERVENTION PATHS (DCs):
- Path A (Diplomacy): DC 14 Charisma (Persuasion).
  * BOX CATACLYSM PENALTY: Disadvantage on this check if Rivia's box is within 30 ft! (He smells Mars's bloodlust trapped in the wood and recoils in horror).
- Path B (Spiritual Accord): DC 14 Religion or Insight.
- Path C (Physical Restraint): DC 13 Athletics (grapple) + DC 12 Medicine to bind wounds.
- Path D (Failure/Suicide): Ritual completes; party must harvest the bone key from his remains.

VOICE LINE:
"The earth under your iron boots is gorged on legionary blood! You carry his slaughter in that wooden cage!"""

    thusnelda_macros = [
        {
            "label": "<b>Ritual Clock (Round 1-3)</b>",
            "group": "Ritual",
            "color": "red",
            "command": '/me [r: "<b style=\'color:#c0392b\'>⏳ RITUAL SUICIDE CLOCK:</b> Thusnelda bleeds into the 7-stone circle. Round 1: Wrists cut. Round 2: Trance-song rises. Round 3: Death triggers the bone-ward! (Intervene via DC 14 Persuasion [Disadv if box <30ft], DC 14 Religion, or DC 13 Grapple)."]',
        },
        {
            "label": "Voice: Blood Prophecy",
            "group": "Audio",
            "color": "cyan",
            "command": '/me [r: "<b style=\'color:#1abc9c\'>🔮 THUSNELDA:</b> \'The earth under your iron boots is gorged on legionary blood! You carry his slaughter in that wooden cage! Turn back, or feed the anvil!\'"]',
        },
    ]
    update_token(
        NAMED_DIR / "Thusnelda.rptok", thusnelda_notes, thusnelda_macros
    )

    # 2. Bone Naga
    bone_naga_notes = """[BONE NAGA - OSSUARY GUARDIAN]
CR 4 | AC 15 (natural armor) | HP 58 (9d10 + 9) | Speed 30 ft
SCLANDERS TACTICAL AI:
- Opening: Burrows from the calcified skull wall, hissing in ancient Latin.
- Tactic: Casts Hold Person (DC 12 Wis) on heavily armored melee fighters, then strikes paralyzed targets with Bite (3d6 piercing + 3d6 poison).
- Sensory Texture: Sound of clattering bone vertebrae scraping damp stone; heavy copper tang of stagnant ossuary dust; sickening sweet rot.
- Three Clue Rule (Vault Entrance): Defeating the Naga reveals the runic skull eye socket where a blood-offering or bone key unlocks the descent to Session 5."""

    bone_naga_macros = [
        {
            "label": "<b>Tactics & Three Clue</b>",
            "group": "Tactics",
            "color": "darkgray",
            "command": '/me [r: "<b style=\'color:#7f8c8d\'>💀 BONE NAGA:</b> Casts Hold Person (DC 12 Wis), strikes paralyzed targets with Bite (3d6 pierce + 3d6 poison). Defeat reveals the runic skull socket to unlock the descent."]',
        }
    ]
    update_token(
        CREATURES_DIR / "Bone_Naga.rptok", bone_naga_notes, bone_naga_macros
    )

    # 3. Yochlol
    yochlol_notes = """[YOCHLOL - CORRUPTING HANDMAIDEN]
CR 6 | AC 15 (natural armor) | HP 65 (10d8 + 20) | Speed 30 ft, climb 30 ft
SCLANDERS TACTICAL AI:
- Environment: Manifests within the pulsating fleshy wall-growths of the Blood Cult Dungeon.
- Opening: Uses Mist Form or casts Web / Insect Plague to divide the party into narrow kill zones.
- Tactic: Slams targets (1d6+3 bludgeoning + 6d6 poison), telepathically whispering doubt about Rome's leadership and the Spear's hunger.
- Sensory Texture: Stench of burning sulfur mixed with damp mold; wet, sickening squelch as it morphs from humanoid to yellow slime."""

    yochlol_macros = [
        {
            "label": "<b>Tactics: Web & Mist</b>",
            "group": "Tactics",
            "color": "yellow",
            "fontcolor": "black",
            "command": '/me [r: "<b style=\'color:#f39c12\'>🕷️ YOCHLOL:</b> Uses Mist Form or casts Web/Insect Plague to divide the party. Telepathically whispers corrupting doubts into the minds of Roman soldiers."]',
        }
    ]
    update_token(CREATURES_DIR / "Yochlol.rptok", yochlol_notes, yochlol_macros)

    # 4. Shadow Demon
    shadow_demon_notes = """[SHADOW DEMON - ALTAR STALKER]
CR 4 | AC 12 (15 in dim light/darkness) | HP 66 (12d8 + 12) | Speed 30 ft, fly 30 ft
SCLANDERS TACTICAL AI:
- Shadows: Uses Shadow Stealth (bonus action Hide in dim light) behind altar pillars.
- Tactic: Claws with advantage from darkness (2d6+3 psychic damage). Evades bright light (light vulnerability / disadvantage in bright illumination).
- Sensory Texture: Sudden drop in room temperature to freezing; smell of ozone and burnt candles; flickers of extinguishing torchlight."""

    shadow_demon_macros = [
        {
            "label": "<b>Tactics: Shadow Stealth</b>",
            "group": "Tactics",
            "color": "darkgray",
            "command": '/me [r: "<b style=\'color:#34495e\'>👤 SHADOW DEMON:</b> Hides as Bonus Action in dim light/darkness. Claws with advantage from the shadows (2d6+3 psychic). Vulnerable to bright light."]',
        }
    ]
    update_token(
        CREATURES_DIR / "Shadow_Demon.rptok",
        shadow_demon_notes,
        shadow_demon_macros,
    )

    # 5. Skeleton
    skeleton_notes = """[SKELETON - VAULT MILES]
CR 1/4 | AC 13 (armor scraps) | HP 13 (2d8 + 4) | Speed 30 ft
TACTICS & MECHANICS:
- Vulnerability: Vulnerable to BLUDGEONING damage (clubs, warhammers, maces deal double damage).
- Sclanders AI: Form Roman shield lines or swarm in tight phalanxes under orders from the Chieftain Wraith.
- Sensory Texture: Dry clicking of yellowed teeth, hollow clanking of rusted iron gladii against rotted lorica hamata."""

    skeleton_macros = [
        {
            "label": "<b>Tactics: Bludgeon Vulnerability</b>",
            "group": "Tactics",
            "color": "gray",
            "fontcolor": "black",
            "command": '/me [r: "<b style=\'color:#bdc3c7\'>⚔️ SKELETON:</b> Vulnerable to BLUDGEONING damage (double damage from hammers/maces/clubs). Moves in disciplined Roman cohort ranks."]',
        }
    ]
    update_token(
        CREATURES_DIR / "Skeleton.rptok", skeleton_notes, skeleton_macros
    )

    print("NPC and Creature tokens updated successfully!")


if __name__ == "__main__":
    main()
