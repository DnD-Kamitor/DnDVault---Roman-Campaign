#!/usr/bin/env python3
"""
Link voice audio cues to MapTool tokens for Sessions 4 & 5.
Injects audio trigger macros and updates token notes/gmNotes for:
- Mars (named/Mars.rptok)
- Vercingetorix Bound (named/Vercingetorix_Bound.rptok)
- Banshee (creatures/Banshee.rptok)
- Wraith (creatures/Wraith.rptok)
- Glabrezu (creatures/Glabrezu.rptok)
"""

import html
import os
import re
import uuid
import zipfile
from pathlib import Path

BASE = Path(__file__).parent.parent
NAMED_DIR = BASE / "Maptool/tokens/npcs/named"
CREATURES_DIR = BASE / "Maptool/tokens/npcs/creatures"

TOKEN_AUDIO_CONFIG = {
    NAMED_DIR / "Mars.rptok": {
        "audio_note": "AUDIO CUES: audio/clips/s5_mars_challenge.mp3 | s5_mars_destroy_reaction.mp3 | s5_mars_depart_reaction.mp3 (also in gm_tools/cheat_card_ch5.html)",
        "macros": [
            {
                "label": "Voice: Challenge",
                "color": "maroon",
                "cmd": "/me [r: \"<b style='color:#e74c3c'>🔊 AUDIO:</b> <i>audio/clips/s5_mars_challenge.mp3</i><br><b style='color:#c0392b'>MARS:</b> 'MORTALS. You have carried my anchor through ash and blood... Give me the spear and be remembered, or stand between a god and his war and be erased!'\"]"
            },
            {
                "label": "Voice: Chained Roar",
                "color": "red",
                "cmd": "/me [r: \"<b style='color:#e74c3c'>🔊 AUDIO:</b> <i>audio/clips/s5_mars_destroy_reaction.mp3</i><br><b style='color:#c0392b'>MARS (ROARING):</b> 'The chains! The Gallic chains! Fools... mortals... you have starved me, but you have not ended what I am!'\"]"
            },
            {
                "label": "Voice: Depart Cold",
                "color": "darkgray",
                "cmd": "/me [r: \"<b style='color:#e74c3c'>🔊 AUDIO:</b> <i>audio/clips/s5_mars_depart_reaction.mp3</i><br><b style='color:#c0392b'>MARS:</b> 'You chose wisely, mortals. The spear returns to its forge. Rome will bleed, but it will bleed under my banners.'\"]"
            }
        ]
    },
    NAMED_DIR / "Vercingetorix_Bound.rptok": {
        "audio_note": "AUDIO CUES: audio/clips/s5_vercingetorix_entrance.mp3 | s5_vercingetorix_final_death.mp3 (also in gm_tools/cheat_card_ch5.html)",
        "macros": [
            {
                "label": "Voice: Entrance",
                "color": "purple",
                "cmd": "/me [r: \"<b style='color:#9b59b6'>🔊 AUDIO:</b> <i>audio/clips/s5_vercingetorix_entrance.mp3</i><br><b style='color:#8e44ad'>VERCINGETORIX:</b> 'Again. Always again. Three hundred years beneath the frost... Tell me this time is the one that ends it.'\"]"
            },
            {
                "label": "Voice: Final Death",
                "color": "orange",
                "cmd": "/me [r: \"<b style='color:#9b59b6'>🔊 AUDIO:</b> <i>audio/clips/s5_vercingetorix_final_death.mp3</i><br><b style='color:#8e44ad'>VERCINGETORIX (FINAL DEATH):</b> 'The four iron chain winches at the granite altar... forged by Caesar\\'s engineers to bind a god. Lock the four iron rings... shatter his armor... only then can the spear break! Tell me... does Gaul still stand?'\"]"
            }
        ]
    },
    CREATURES_DIR / "Banshee.rptok": {
        "audio_note": "AUDIO CUES: audio/clips/s4_banshee_dread_mother.mp3 (also in gm_tools/cheat_card_ch4.html)",
        "macros": [
            {
                "label": "Voice: Dread Wail",
                "color": "cyan",
                "cmd": "/me [r: \"<b style='color:#1abc9c'>🔊 AUDIO:</b> <i>audio/clips/s4_banshee_dread_mother.mp3</i><br><b style='color:#16a085'>BANSHEE:</b> 'My sons drowned here... and their bones paved the altar! You walk upon the unavenged! Hear our sorrow and PERISH!'\"]"
            }
        ]
    },
    CREATURES_DIR / "Wraith.rptok": {
        "audio_note": "AUDIO CUES: audio/clips/s4_wraith_chieftain_confession.mp3 (also in gm_tools/cheat_card_ch4.html)",
        "macros": [
            {
                "label": "Voice: Confession",
                "color": "blue",
                "cmd": "/me [r: \"<b style='color:#3498db'>🔊 AUDIO:</b> <i>audio/clips/s4_wraith_chieftain_confession.mp3</i><br><b style='color:#2980b9'>WRAITH CHIEFTAIN:</b> 'We asked for victory... It asked for blood. It did not stop when the legions retreated. It never stops.'\"]"
            }
        ]
    },
    CREATURES_DIR / "Glabrezu.rptok": {
        "audio_note": "AUDIO CUES: audio/clips/s4_glabrezu_core_entrance.mp3 (also in gm_tools/cheat_card_ch4.html)",
        "macros": [
            {
                "label": "Voice: Mocking Entrance",
                "color": "red",
                "cmd": "/me [r: \"<b style='color:#e67e22'>🔊 AUDIO:</b> <i>audio/clips/s4_glabrezu_core_entrance.mp3</i><br><b style='color:#d35400'>GLABREZU:</b> 'Little soldiers in iron rings! The star does not break for mortals. Come, feed what waits below!'\"]"
            }
        ]
    }
}


def create_macro_xml(index, label, color, cmd):
    cmd_escaped = html.escape(cmd, quote=False)
    m_uuid = str(uuid.uuid4())
    return f"""  <entry>
    <int>{index}</int>
    <net.rptools.maptool.model.MacroButtonProperties>
      <macroUUID>{m_uuid}</macroUUID>
      <saveLocation>Token</saveLocation>
      <index>{index}</index>
      <colorKey>{color}</colorKey>
      <hotKey>None</hotKey>
      <command>{cmd_escaped}</command>
      <label>{html.escape(label)}</label>
      <group>Audio</group>
      <sortby />
      <autoExecute>true</autoExecute>
      <includeLabel>false</includeLabel>
      <applyToTokens>false</applyToTokens>
      <fontColorKey>white</fontColorKey>
      <fontSize>1.15em</fontSize>
      <minWidth>140px</minWidth>
      <maxWidth />
      <allowPlayerEdits>false</allowPlayerEdits>
      <toolTip>Plays audio cue and broadcasts dialogue to chat</toolTip>
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


def process_token(token_path, cfg):
    if not token_path.exists():
        print(f"[MISS] {token_path}")
        return False

    with zipfile.ZipFile(token_path, "r") as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    xml = files["content.xml"].decode("utf-8")
    
    # Update notes
    audio_note = cfg["audio_note"]
    notes_match = re.search(r"<notes>(.*?)</notes>", xml, re.DOTALL)
    if notes_match:
        current_notes = notes_match.group(1)
        if "AUDIO CUES:" not in current_notes:
            updated_notes = current_notes.strip() + f"\n\n[{audio_note}]"
            xml = xml.replace(f"<notes>{current_notes}</notes>", f"<notes>{updated_notes}</notes>")
    
    # Update gmNotes
    gm_match = re.search(r"<gmNotes>(.*?)</gmNotes>", xml, re.DOTALL)
    if gm_match:
        current_gm = gm_match.group(1)
        if "AUDIO CUES:" not in current_gm:
            updated_gm = current_gm.strip() + f"\n\n[{audio_note}]"
            xml = xml.replace(f"<gmNotes>{current_gm}</gmNotes>", f"<gmNotes>{updated_gm}</gmNotes>")

    # Add macros
    # Find existing indices
    existing_indices = [int(x) for x in re.findall(r'<int>(\d+)</int>', xml)]
    start_index = max(existing_indices) + 1 if existing_indices else 110
    if start_index < 110:
        start_index = 110

    # Check if macros already exist by label
    macro_entries = []
    for m in cfg["macros"]:
        if f"<label>{m['label']}</label>" in xml:
            continue
        macro_entries.append(create_macro_xml(start_index, m["label"], m["color"], m["cmd"]))
        start_index += 1

    if macro_entries:
        insert_block = "\n".join(macro_entries)
        xml = xml.replace("</macroPropertiesMap>", insert_block + "\n</macroPropertiesMap>")

    files["content.xml"] = xml.encode("utf-8")
    tmp_path = str(token_path) + ".tmp"
    with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    os.replace(tmp_path, token_path)
    print(f"[OK] Updated {token_path.name} with {len(macro_entries)} new audio macros and notes.")
    return True


def main():
    print("Linking voice audio cues to MapTool tokens...")
    for path, cfg in TOKEN_AUDIO_CONFIG.items():
        process_token(path, cfg)


if __name__ == "__main__":
    main()
