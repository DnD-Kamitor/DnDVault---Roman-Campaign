#!/usr/bin/env python3
"""
Generate MapTool .rptok information/prop tokens from JSON files in locations/.
Output to Maptool/tokens/locations/.

Location tokens are placed on the NPC layer (GM can toggle visibility).
They carry player description in <notes> and DM notes in <gmNotes>.

Usage:
  python scripts/generate_location_tokens.py           # all files in locations/
  python scripts/generate_location_tokens.py locations/fort_gate.json
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

REPO_ROOT   = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent
LOCS_DIR    = REPO_ROOT / "locations"
OUTPUT_DIR  = REPO_ROOT / "Maptool" / "tokens" / "locations"
MACROS_XML  = SCRIPTS_DIR / "standard_token_macros.xml"

# Location type colors (overridden by token_color in JSON if present)
LOCATION_TYPE_COLORS = {
    "fort":       "#5c3a1e",
    "vault":      "#1a1a2e",
    "settlement": "#6b4c2a",
    "road":       "#4a4a3a",
    "forest":     "#2a3a1a",
    "grove":      "#1a3a1a",
    "river":      "#1a3a4a",
    "default":    "#4a4a4a",
}


# ── PNG helpers (shared with other generators) ────────────────────────────────

def _chunk(tag, data):
    tag_b = tag.encode() if isinstance(tag, str) else tag
    crc   = struct.pack(">I", zlib.crc32(tag_b + data) & 0xFFFFFFFF)
    return struct.pack(">I", len(data)) + tag_b + data + crc

def make_color_png(r, g, b, size=100):
    ihdr = _chunk("IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
    raw  = b"".join(b"\x00" + bytes([r, g, b] * size) for _ in range(size))
    return b"\x89PNG\r\n\x1a\n" + ihdr + _chunk("IDAT", zlib.compress(raw)) + _chunk("IEND", b"")

def hex_to_rgb(h):
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def _pil_to_png(img, size=100):
    img  = img.convert("RGBA")
    w, h = img.size
    side = min(w, h)
    img  = img.crop(((w-side)//2, (h-side)//2, (w+side)//2, (h+side)//2))
    img  = img.resize((size, size), PILImage.LANCZOS)
    buf  = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def new_baguid():
    import base64
    return base64.b64encode(uuid.uuid4().bytes).decode()


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


def build_location_content_xml(loc, image_md5):
    """Build content.xml for a location information token."""
    name        = loc["name"]
    player_desc = loc.get("player_description", "")
    gm_notes    = loc.get("gm_notes", "")
    session     = loc.get("session", 0)
    loc_type    = loc.get("location_type", "default")

    # Minimal properties -- locations don't need combat stats
    props = {}
    props["Name"]         = name
    props["Notes"]        = player_desc
    props["Description"]  = player_desc
    props["LocationType"] = loc_type
    props["Session"]      = session

    entries = "\n".join(_prop(k, v) for k, v in props.items())

    # Minimal macros -- just initiative for if somehow this ends up in combat
    # Location tokens typically have no macros; include empty map
    macros_xml = "<macroPropertiesMap/>"

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
  <isVisible>false</isVisible>
  <visibleOnlyToOwner>true</visibleOnlyToOwner>
  <vblColorSensitivity>-1</vblColorSensitivity>
  <alwaysVisibleTolerance>2</alwaysVisibleTolerance>
  <isAlwaysVisible>false</isAlwaysVisible>
  <name>{_xe(name)}</name>
  <ownerList/>
  <ownerType>1</ownerType>
  <tokenShape>SQUARE</tokenShape>
  <tokenType>NPC</tokenType>
  <layer>OBJECT</layer>
  <propertyType>Basic</propertyType>
  <tokenOpacity>0.85</tokenOpacity>
  <isFlippedX>false</isFlippedX>
  <isFlippedY>false</isFlippedY>
  <isFlippedIso>false</isFlippedIso>
  <uniqueLightSources class="linked-hash-map"/>
  <lightSourceList/>
  <hasSight>false</hasSight>
  <sightType>Normal</sightType>
  <notes>{_xe(player_desc)}</notes>
  <gmNotes>{_xe(gm_notes)}</gmNotes>
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


# ── Token packager ────────────────────────────────────────────────────────────

def generate_token(sheet_path):
    with open(sheet_path) as f:
        loc = json.load(f)

    # Determine color
    color_hex = loc.get("token_color") or LOCATION_TYPE_COLORS.get(
        loc.get("location_type", "default"), LOCATION_TYPE_COLORS["default"]
    )
    r, g, b = hex_to_rgb(color_hex)
    png     = make_color_png(r, g, b, 100)
    thumb   = _pil_to_png(PILImage.open(io.BytesIO(png)), 50) if HAS_PIL else png
    md5     = hashlib.md5(png).hexdigest()

    asset_name = loc["name"].replace(" ", "_").lower()
    asset_xml  = (
        f"<net.rptools.maptool.model.Asset>\n"
        f"  <id>\n    <id>{md5}</id>\n  </id>\n"
        f"  <name>{asset_name}</name>\n"
        f"  <extension>png</extension>\n"
        f"  <type>image</type>\n"
        f"  <image/>\n"
        f"</net.rptools.maptool.model.Asset>"
    )

    safe_name = loc["name"].replace(" ", "_").replace("/", "-")
    out_path  = OUTPUT_DIR / f"{safe_name}.rptok"
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.xml",    build_location_content_xml(loc, md5))
        zf.writestr("properties.xml", build_properties_xml())
        zf.writestr(f"assets/{md5}",  asset_xml)
        zf.writestr(f"assets/{md5}.png", png)
        zf.writestr("thumbnail",      thumb)
        zf.writestr("thumbnail_large", png)

    loc_type = loc.get("location_type", "?")
    session  = loc.get("session", 0)
    print(f"  {loc['name']:<35} type={loc_type:<12} S{session}  [{color_hex}]")


def main():
    global OUTPUT_DIR

    args = sys.argv[1:]
    # --output-dir <path> overrides OUTPUT_DIR
    if "--output-dir" in args:
        idx = args.index("--output-dir")
        OUTPUT_DIR = Path(args[idx + 1])
        args = args[:idx] + args[idx + 2:]
    # --input-dir <path> overrides LOCS_DIR
    input_dir = LOCS_DIR
    if "--input-dir" in args:
        idx = args.index("--input-dir")
        input_dir = Path(args[idx + 1])
        args = args[:idx] + args[idx + 2:]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args:
        sheets = [Path(p) for p in args]
    else:
        sheets = sorted(p for p in input_dir.glob("*.json")
                        if not p.name.startswith("_"))
    if not sheets:
        print(f"No location files found in {input_dir}")
        return

    print(f"Generating location tokens -> {OUTPUT_DIR}")
    print()
    for sheet in sheets:
        generate_token(sheet)

    print()
    print(f"Done. Generated {len(sheets)} location token(s).")


if __name__ == "__main__":
    main()
