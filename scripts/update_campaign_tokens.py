#!/usr/bin/env python3
"""
Update tokens embedded inside MapTool campaign files (.cmpgn).
Injects Sclanders architecture, Box Cataclysm GM notes, audio macros,
and canonical pronouns across all zones/maps in the campaign.
"""

import re
import shutil
import uuid
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CMPGN_PATH = BASE / "Maptool/campaigns/5e/2aug.cmpgn"

RIVIA_NOTES = """[BOX CATACLYSM - SESSION 4/5 ACTIVE CAMPAIGN STATE]
Rivia carries the iron-bound Artificer's containment box.
CONTENTS:
1. The Spear of Mars (iron-chained, psychic bloodlust, ancient divine relic).
2. Ursula's Goliath Berserker Greataxe (placed inside by Rivia after the forest battle in a misguided attempt to 'nullify' the dark magic).

METAPHYSICAL RESONANCE:
The two cursed weapons resonated violently, scorching the ancient OTHALAN rune into the ironbound wood. The box hums with a palpable sub-bass vibration.

MECHANICAL EFFECTS:
- +2 bonus to Intimidation checks while carrying the humming box.
- Double undead detection radius: Undead sense the party from double range (Scene 0 Farbog crossing; group DC 14 Stealth at disadvantage if carried unshielded).
- Disadvantage on calm diplomacy: If the box is within 30 ft of Thusnelda in Scene 3, he feels Mars's bloodlust and recoils with hostility (disadvantage on Persuasion checks to stop his suicide ritual).
- Mars's connection: In Scene 4/5, Mars immediately detects the greataxe and spear feeding each other inside the box and mocks Rivia's naivety."""

URSULA_NOTES = """[SESSION 4/5 COMBAT STATE - WEAPON LOSS & TRAUMA]
- PRIMARY WEAPON SEALED: Ursula's Goliath Berserker Greataxe was possessed by dark blood-magic during the forest battle (Session 3) and is currently locked inside Rivia's containment box.
- CURRENT ARMAMENT: Ursula is fighting with secondary Roman spatha, legionary hunting spear, and heavy throwing javelins.
- PSYCHIC TRAUMA: Ursula suffers phantom twitches and lingering berserker exhaustion from the weapon's influence. Hearing the box hum triggers a DC 12 Wisdom check to avoid brief battle rage or disorientation."""

THUSNELDA_NOTES = """[THUSNELDA - MALE VÖLVA SEER (DRUID CIRCLE OF THE LAND 5)]
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

BONE_NAGA_NOTES = """[BONE NAGA - OSSUARY GUARDIAN]
CR 4 | AC 15 (natural armor) | HP 58 (9d10 + 9) | Speed 30 ft
SCLANDERS TACTICAL AI:
- Opening: Burrows from the calcified skull wall, hissing in ancient Latin.
- Tactic: Casts Hold Person (DC 12 Wis) on heavily armored melee fighters, then strikes paralyzed targets with Bite (3d6 piercing + 3d6 poison).
- Sensory Texture: Sound of clattering bone vertebrae scraping damp stone; heavy copper tang of stagnant ossuary dust; sickening sweet rot.
- Three Clue Rule (Vault Entrance): Defeating the Naga reveals the runic skull eye socket where a blood-offering or bone key unlocks the descent to Session 5."""


def add_macro(root, label, command, group="Campaign", color="red"):
    macro_map = root.find("macroPropertiesMap")
    if macro_map is None:
        macro_map = ET.SubElement(root, "macroPropertiesMap")

    # Check if macro label already exists
    for mbp in macro_map.findall(
        ".//net.rptools.maptool.model.MacroButtonProperties"
    ):
        if mbp.findtext("label") == label:
            return  # Already exists

    max_idx = 150
    for entry in macro_map.findall("entry"):
        idx_elem = entry.find("int")
        if idx_elem is not None and idx_elem.text:
            try:
                max_idx = max(max_idx, int(idx_elem.text))
            except ValueError:
                pass

    max_idx += 1
    entry = ET.SubElement(macro_map, "entry")
    int_elem = ET.SubElement(entry, "int")
    int_elem.text = str(max_idx)

    mbp = ET.SubElement(entry, "net.rptools.maptool.model.MacroButtonProperties")
    ET.SubElement(mbp, "macroUUID").text = str(uuid.uuid4())
    ET.SubElement(mbp, "saveLocation").text = "Token"
    ET.SubElement(mbp, "index").text = str(max_idx)
    ET.SubElement(mbp, "colorKey").text = color
    ET.SubElement(mbp, "hotKey").text = "None"
    ET.SubElement(mbp, "command").text = command
    ET.SubElement(mbp, "label").text = label
    ET.SubElement(mbp, "group").text = group
    ET.SubElement(mbp, "sortby").text = "4.0"
    ET.SubElement(mbp, "autoExecute").text = "true"
    ET.SubElement(mbp, "includeLabel").text = "false"
    ET.SubElement(mbp, "applyToTokens").text = "false"
    ET.SubElement(mbp, "fontColorKey").text = "white"
    ET.SubElement(mbp, "fontSize").text = "1.15em"
    ET.SubElement(mbp, "minWidth").text = "120px"
    ET.SubElement(mbp, "maxWidth").text = ""
    ET.SubElement(mbp, "allowPlayerEdits").text = "false"
    ET.SubElement(mbp, "toolTip").text = ""
    ET.SubElement(mbp, "displayHotKey").text = "true"
    ET.SubElement(mbp, "commonMacro").text = "false"
    ET.SubElement(mbp, "compareGroup").text = "true"
    ET.SubElement(mbp, "compareSortPrefix").text = "true"
    ET.SubElement(mbp, "compareCommand").text = "true"
    ET.SubElement(mbp, "compareIncludeLabel").text = "true"
    ET.SubElement(mbp, "compareAutoExecute").text = "true"
    ET.SubElement(mbp, "compareApplyToSelectedTokens").text = "true"


def update_token_xml(token_xml_str):
    root = ET.fromstring(token_xml_str)
    name = root.findtext("name", "")

    # Skip Lib: tokens
    if name.startswith("Lib:"):
        return token_xml_str, False

    modified = False

    if name == "Rivia Calida Mendera":
        gm = root.find("gmNotes")
        if gm is None:
            gm = ET.Element("gmNotes")
            root.append(gm)
        gm.text = RIVIA_NOTES
        add_macro(
            root,
            "<b>Box Cataclysm Aura</b>",
            "/me [r: \"<b style='color:#c0392b'>⚠️ THE BOX CATACLYSM:</b> The scorched OTHALAN box hums with a sickening sub-bass resonance. Mars's aura pulses outward (+2 Intimidation, Undead detect party at 2x range, Disadvantage on calm diplomacy within 30ft).\"]",
            group="Campaign",
            color="red",
        )
        modified = True

    elif name == "Ursula Günther":
        gm = root.find("gmNotes")
        if gm is None:
            gm = ET.Element("gmNotes")
            root.append(gm)
        gm.text = URSULA_NOTES
        add_macro(
            root,
            "<b>Secondary Weapons</b>",
            "/me [r: \"<b style='color:#2980b9'>⚔️ SECONDARY WEAPONS:</b> Ursula draws her legionary spatha and hunting spear — her cursed Goliath Greataxe remains locked inside Rivia's scorched box.\"]",
            group="Combat",
            color="blue",
        )
        modified = True

    elif name == "Thusnelda":
        gm = root.find("gmNotes")
        if gm is None:
            gm = ET.Element("gmNotes")
            root.append(gm)
        gm.text = THUSNELDA_NOTES

        # Fix notes element
        notes_elem = root.find("notes")
        if notes_elem is not None and notes_elem.text:
            notes_elem.text = notes_elem.text.replace(
                "she shows", "he shows"
            ).replace("She shows", "He shows")

        # Fix any macro command containing "she shows"
        for cmd in root.findall(".//macroPropertiesMap/entry//command"):
            if cmd.text and "she shows" in cmd.text:
                cmd.text = '/me [r: "AC 13 | HP 38 | Speed 30 ft. | CR 2 | Senses: Passive Perception 16 | Völva: Druid Circle of the Land 5 (Spell DC 13, Spell Atk +5). | GM: Male völva seer (he/him). Leads ritual sacrifice at Scene 3. Knows more than he shows."]'

        add_macro(
            root,
            "<b>Ritual Clock (Round 1-3)</b>",
            '/me [r: "<b style=\'color:#c0392b\'>⏳ RITUAL SUICIDE CLOCK:</b> Thusnelda bleeds into the 7-stone circle. Round 1: Wrists cut. Round 2: Trance-song rises. Round 3: Death triggers the bone-ward! (Intervene via DC 14 Persuasion [Disadv if box <30ft], DC 14 Religion, or DC 13 Grapple)."]',
            group="Ritual",
            color="red",
        )
        add_macro(
            root,
            "Voice: Blood Prophecy",
            '/me [r: "<b style=\'color:#1abc9c\'>🔮 THUSNELDA:</b> \'The earth under your iron boots is gorged on legionary blood! You carry his slaughter in that wooden cage! Turn back, or feed the anvil!\'"]',
            group="Audio",
            color="cyan",
        )
        modified = True

    elif name == "Bone Naga":
        gm = root.find("gmNotes")
        if gm is None:
            gm = ET.Element("gmNotes")
            root.append(gm)
        gm.text = BONE_NAGA_NOTES
        add_macro(
            root,
            "<b>Tactics & Three Clue</b>",
            '/me [r: "<b style=\'color:#7f8c8d\'>💀 BONE NAGA:</b> Casts Hold Person (DC 12 Wis), strikes paralyzed targets with Bite (3d6 pierce + 3d6 poison). Defeat reveals the runic skull socket to unlock the descent."]',
            group="Tactics",
            color="darkgray",
        )
        modified = True

    if modified:
        return (
            ET.tostring(root, encoding="utf-8").decode("utf-8"),
            True,
        )
    return token_xml_str, False


def process_campaign(cmpgn_path: Path):
    print(f"Opening campaign: {cmpgn_path.name}")
    backup_path = cmpgn_path.with_name(cmpgn_path.name + ".bak_script")
    shutil.copy2(cmpgn_path, backup_path)
    print(f"Safety backup created at: {backup_path.name}")

    with zipfile.ZipFile(cmpgn_path, "r") as z:
        file_map = {name: z.read(name) for name in z.namelist()}

    content_xml = file_map["content.xml"].decode("utf-8")

    token_pattern = re.compile(
        r"(<net\.rptools\.maptool\.model\.Token>.*?</net\.rptools\.maptool\.model\.Token>)",
        re.DOTALL,
    )

    updated_count = 0

    def replacer(match):
        nonlocal updated_count
        token_str = match.group(1)
        new_str, changed = update_token_xml(token_str)
        if changed:
            updated_count += 1
            return new_str
        return token_str

    new_content_xml = token_pattern.sub(replacer, content_xml)

    print(
        f"Updated {updated_count} token instances across all zones in the campaign."
    )

    file_map["content.xml"] = new_content_xml.encode("utf-8")

    with zipfile.ZipFile(cmpgn_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in file_map.items():
            z.writestr(name, data)

    print(f"Successfully saved updated campaign: {cmpgn_path.name}")


if __name__ == "__main__":
    process_campaign(CMPGN_PATH)
