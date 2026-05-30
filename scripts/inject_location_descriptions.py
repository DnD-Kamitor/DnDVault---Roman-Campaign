#!/usr/bin/env python3
"""
Add "Describe" and "GM Checks" macros to all location .rptok tokens.

- Describe (green):  broadcasts the token's Notes to all players as a styled box
- GM Checks (gold):  sends the token's GM Notes only to the running player (/self)

Usage:
  python3 scripts/inject_location_descriptions.py
"""

import html
import os
import re
import uuid
import zipfile
from pathlib import Path

BASE = Path(__file__).parent.parent
LOCATIONS_DIR = BASE / "Maptool/tokens/locations"


# ── Macro command templates ──────────────────────────────────────────────────

DESCRIBE_CMD = """\
[h: tokenName = getName()]
[h: desc = getNotes()]
[broadcast("<div style='background:#0a1a0a;border:1px solid #3a8a3a;border-radius:4px;padding:10px;font-family:Georgia,serif;max-width:460px;'><b style='color:#5aba5a;font-size:13px;'>&#128205; " + tokenName + "</b><br><span style='color:#d0d0d0;font-size:12px;line-height:1.5;'>" + desc + "</span></div>")]"""

GMCHECKS_CMD = """\
[h: tokenName = getName()]
[h: checks = getGMNotes()]
/self <b style='color:#d4a017;'>&#128269; [r: tokenName] \u2014 GM Checks</b><br>[r: checks]"""


# ── Macro XML builder ────────────────────────────────────────────────────────

def make_macro_entry(index, label, cmd, color_key):
    cmd_escaped = html.escape(cmd, quote=False)
    new_uuid = str(uuid.uuid4())
    return f"""  <entry>
    <int>{index}</int>
    <net.rptools.maptool.model.MacroButtonProperties>
      <macroUUID>{new_uuid}</macroUUID>
      <saveLocation>Token</saveLocation>
      <index>{index}</index>
      <colorKey>{color_key}</colorKey>
      <hotKey>None</hotKey>
      <command>{cmd_escaped}</command>
      <label>{label}</label>
      <group>Location</group>
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


# ── Token processor ──────────────────────────────────────────────────────────

def process_token(rptok_path):
    with zipfile.ZipFile(rptok_path) as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    xml = files["content.xml"].decode("utf-8")

    # Skip if macros already injected
    if '<group>Location</group>' in xml:
        return False

    describe_entry = make_macro_entry(1, "Describe", DESCRIBE_CMD, "green")
    gmchecks_entry = make_macro_entry(2, "GM Checks", GMCHECKS_CMD, "yellow")
    macro_block = (
        "<macroPropertiesMap>\n"
        + describe_entry + "\n"
        + gmchecks_entry + "\n"
        + "</macroPropertiesMap>"
    )

    # Replace self-closing tag or empty section
    if "<macroPropertiesMap/>" in xml:
        xml = xml.replace("<macroPropertiesMap/>", macro_block)
    elif "<macroPropertiesMap></macroPropertiesMap>" in xml:
        xml = xml.replace("<macroPropertiesMap></macroPropertiesMap>", macro_block)
    else:
        # Should not happen — log and skip
        print(f"  [warn] no macroPropertiesMap found in {rptok_path}")
        return False

    files["content.xml"] = xml.encode("utf-8")

    tmp = rptok_path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    os.replace(tmp, rptok_path)
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    updated = 0
    skipped = 0

    for fname in sorted(os.listdir(LOCATIONS_DIR)):
        if not fname.endswith(".rptok"):
            continue
        rptok_path = str(LOCATIONS_DIR / fname)
        stem = fname[:-6]
        if process_token(rptok_path):
            print(f"  {stem}")
            updated += 1
        else:
            print(f"  [skip] {stem}")
            skipped += 1

    print(f"\nDone. {updated} location tokens updated, {skipped} skipped.")


if __name__ == "__main__":
    main()
