#!/usr/bin/env python3
"""
Generate MapTool prop/object .rptok tokens for Session 1 campaign props.

Usage: python3 scripts/generate_prop_tokens.py
Output: Maptool/tokens/props/  (one .rptok per prop)
"""

import hashlib
import io
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO     = Path(__file__).parent.parent
OUT_DIR  = REPO / "Maptool/tokens/props"
TORSTAN  = REPO / "Maptool/maps/rptools/Torstan_Objects"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def md5_hex(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def make_thumb(data: bytes, size=(50, 50)) -> bytes:
    img = Image.open(io.BytesIO(data)).convert("RGBA")
    img.thumbnail(size, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def circle_png(color: tuple, size=200, label: str = "", label_color=(255,255,255,230)) -> bytes:
    """Generate a simple colored circle PNG with optional label."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    margin = 10
    draw.ellipse([margin, margin, size-margin, size-margin], fill=color)
    if label:
        # Draw text centered
        try:
            font = ImageFont.truetype("/usr/share/fonts/liberation/LiberationSans-Bold.ttf", size//4)
        except Exception:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text(((size-tw)//2, (size-th)//2), label, fill=label_color, font=font)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def load_png(path: Path) -> bytes:
    """Load and re-encode a PNG to ensure clean bytes."""
    img = Image.open(path).convert("RGBA")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def make_content_xml(name: str, img_md5: str, layer: str, token_type: str,
                     notes: str, gm_notes: str, width=200, height=200) -> str:
    import base64, hashlib
    # Stable token GUID derived from name
    id_bytes  = hashlib.md5(name.encode()).digest()
    id_b64    = base64.b64encode(id_bytes).decode()
    # Stable exposedAreaGUID derived from name + "ea" — must be non-zero
    ea_bytes  = hashlib.md5((name + "ea").encode()).digest()
    ea_b64    = base64.b64encode(ea_bytes).decode()
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<net.rptools.maptool.model.Token>
  <id><baGUID>{id_b64}</baGUID></id>
  <beingImpersonated>false</beingImpersonated>
  <exposedAreaGUID><baGUID>{ea_b64}</baGUID></exposedAreaGUID>
  <imageAssetMap>
    <entry>
      <null/>
      <net.rptools.lib.MD5Key><id>{img_md5}</id></net.rptools.lib.MD5Key>
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
  <name>{name}</name>
  <ownerList/>
  <ownerType>1</ownerType>
  <tokenShape>TOP_DOWN</tokenShape>
  <tokenType>{token_type}</tokenType>
  <layer>{layer}</layer>
  <propertyType>Basic</propertyType>
  <tokenOpacity>1.0</tokenOpacity>
  <isFlippedX>false</isFlippedX>
  <isFlippedY>false</isFlippedY>
  <isFlippedIso>false</isFlippedIso>
  <uniqueLightSources class="linked-hash-map"/>
  <lightSourceList/>
  <hasSight>false</hasSight>
  <notes>{notes}</notes>
  <gmNotes>{gm_notes}</gmNotes>
  <gmNotesType>text/plain</gmNotesType>
  <propertyMapCI><store/></propertyMapCI>
  <state/>
  <macroPropertiesMap/>
  <speechMap/>
</net.rptools.maptool.model.Token>"""


PROPERTIES_XML = """<map>
  <entry>
    <string>version</string>
    <string>1.18.6</string>
  </entry>
  <entry>
    <string>herolab</string>
    <boolean>false</boolean>
  </entry>
</map>"""


def write_rptok(slug: str, img_data: bytes, layer: str, token_type: str,
                notes: str, gm_notes: str):
    img_md5 = md5_hex(img_data)
    content = make_content_xml(slug, img_md5, layer, token_type, notes, gm_notes)
    thumb_sm = make_thumb(img_data, (50, 50))
    thumb_lg = make_thumb(img_data, (200, 200))
    asset_xml = (
        f"<net.rptools.maptool.model.Asset>\n"
        f"  <id>\n    <id>{img_md5}</id>\n  </id>\n"
        f"  <name>{slug.lower()}</name>\n"
        f"  <extension>png</extension>\n"
        f"  <type>image</type>\n"
        f"  <image/>\n"
        f"</net.rptools.maptool.model.Asset>"
    )

    out = OUT_DIR / f"{slug}.rptok"
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("content.xml",           content.encode("utf-8"))
        z.writestr("properties.xml",        PROPERTIES_XML.encode("utf-8"))
        z.writestr(f"assets/{img_md5}",     asset_xml.encode("utf-8"))
        z.writestr(f"assets/{img_md5}.png", img_data)
        z.writestr("thumbnail",             thumb_sm)
        z.writestr("thumbnail_large",       thumb_lg)
    print(f"  OK  {slug}.rptok")


# ---------------------------------------------------------------------------
# Prop definitions
# ---------------------------------------------------------------------------

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Physical objects (Torstan PNGs) ─────────────────────────────────────

    write_rptok(
        "Spear_of_Mars",
        load_png(TORSTAN / "Items/Weapons/Spear.png"),
        layer="TOKEN", token_type="NPC",
        notes="An iron spear eight feet long, so black it seems to swallow light. Runes coil along its haft, glowing ember-red. Within five feet of the altar the air stops moving.",
        gm_notes="DC 14 Wis save on first touch: fail = 1 corruption + Shaken (can't release until next turn start). Attunement: short rest holding it. Wight priority-targets whoever holds this. Pointing toward Rome = consequence clause active. 'What is inside it is older than Rome.'",
    )

    write_rptok(
        "SpearRack_ShieldHall",
        load_png(TORSTAN / "Items/Weapons/SpearRack.png"),
        layer="OBJECT", token_type="NPC",
        notes="A rack of ancient Germanic weapons along the vault wall.",
        gm_notes="Decorative. Shield order on walls: Marcomanni/boar=TIWAZ, Cherusci/hand=HAGALAZ, Suebi/serpent=ISA, Mars/wolf=OTHALAN. DC 13 Int = safe path clue for Runic Corridor.",
    )

    write_rptok(
        "Vault_Shaft_Entrance",
        load_png(TORSTAN / "Items/Miscellaneous set dressing/Grate.png"),
        layer="OBJECT", token_type="NPC",
        notes="A crude shaft dug through Roman stonework into older Germanic structures. 40 feet deep. Rope ladder, poorly anchored.",
        gm_notes="Survival DC 11: draft pulses in/out — space has 2+ rooms, cedar smell = deliberate seal. Torch flame leans downward. Scratched on wall: 7 marks, diagonal, NOLITE.",
    )

    write_rptok(
        "Altar",
        load_png(TORSTAN / "Items/Miscellaneous set dressing/MagicCircle.png"),
        layer="OBJECT", token_type="NPC",
        notes="A granite altar carved from a single block that predates the Roman stones around it. The spear rests in two stone pegs. Within five feet: air stops. Sweat does not fall.",
        gm_notes="Give Handout 2 (Vault Inscription) when party crosses threshold. Spear Reveal read-aloud triggers here. OTHALAN bone token counterpart is here — matches token from alcove/warrior.",
    )

    write_rptok(
        "Chains_Binding_Chamber",
        load_png(TORSTAN / "Items/Miscellaneous set dressing/Manacles.png"),
        layer="OBJECT", token_type="NPC",
        notes="Chains hanging from stone in ranks — wrist-thin to neck-wide. All sway slightly despite still air. TIWAZ carved above. 'We turned back here.'",
        gm_notes="Chain puzzle: pull oldest (left wall) → far wall → newest (right wall) → center grip. Wrong = DC 13 Str save or restrained 1 min. Correct = stone panel opens: oil lamp (filled 2yr ago) + contract scroll (DC 15 Int to read). Arcana DC 14: divine aura. Athletics DC 12: center chain has live tension — something still pulling.",
    )

    write_rptok(
        "Preserved_Warrior",
        load_png(TORSTAN / "Items/Miscellaneous set dressing/Bones.png"),
        layer="TOKEN", token_type="NPC",
        notes="A Germanic warrior preserved in peat water for centuries. Armored, intact. A framea lies across his lap. A bone token carved OTHALAN hangs at his throat. Not undead. Not hostile.",
        gm_notes="Inv DC 12: died voluntarily (seiðr death), not violence. Framea = full spear stats, Germanic craft. Bone token = contract marker — matches alcove token + altar. Taking token disrespectfully: 1 Shadow reactivates behind party, no warning. Religion DC 14: seiðr position = duty completed. Do NOT mark as hostile.",
    )

    write_rptok(
        "Bone_Token_OTHALAN",
        load_png(TORSTAN / "Items/Chests and barrels/SmallChest.png"),
        layer="OBJECT", token_type="NPC",
        notes="A carved bone token bearing the OTHALAN rune (ancestral land). Part of a matched pair — one half of a formal contract between Rome and the Germanic tribes sealed beneath this fort.",
        gm_notes="Found in hidden alcove (left branch) OR on preserved warrior's throat (right branch). Grants advantage on Runic Corridor if player states they use it as a guide — OTHALAN is the safe step in every row. Religion DC 14: formal contract marker, two parties hold matching tokens.",
    )

    write_rptok(
        "Contract_Scroll",
        load_png(TORSTAN / "Items/Chests and barrels/Chest.png"),
        layer="OBJECT", token_type="NPC",
        notes="A scroll in oilskin. Barely legible — Latin and Germanic parallel texts. Fragments describe terms of a binding: the tribes sealed the vault for three Roman generations; Rome agreed never to dig within 50 feet of the principia's eastern wall.",
        gm_notes="DC 15 Int to read damaged text. Grants ADVANTAGE on Wight persuasion check (DC 14). Proves Corvinus broke the bargain, not the party. Evidence for Scene 5 confrontation.",
    )

    write_rptok(
        "Clay_Vessel_Offering",
        load_png(TORSTAN / "Items/Chests and barrels/TreasureUrn.png"),
        layer="OBJECT", token_type="NPC",
        notes="A clay vessel found beneath stone benches in the Bone Chamber. Contains carbonized grain and an iron coin struck with a pre-Roman image of Mars.",
        gm_notes="DC 12 Inv to find. Offering maintained until ~2yr ago (Titus died AD 173). Haruspex: grain + coin = two aspects of Mars, calendar-precise maintenance. Session 2 thread: who was maintaining this?",
    )

    write_rptok(
        "Torch_Light_Source",
        load_png(TORSTAN / "Lightsources/torchWithHalo.png"),
        layer="TOKEN", token_type="NPC",
        notes="A Roman torch. Flame leans downward in the vault's unnatural draft.",
        gm_notes="Shadows are DRAWN to torchlight. Flooded Gallery: carrying torch = Shadows activate (4 of them, CR 1/2 each). Extinguish + Stealth DC 14 group check = free passage. Torch flame leans downward in shaft — worth remarking on.",
    )

    write_rptok(
        "Oil_Lamp_Binding_Chamber",
        load_png(TORSTAN / "Lightsources/Lantern,Lit.png"),
        layer="OBJECT", token_type="NPC",
        notes="A clay oil lamp, Roman manufacture. Still full. The wick is trimmed.",
        gm_notes="Found in hidden panel behind chain mechanism. Oil filled within past 2 years. Same person who maintained offering cycle (Titus Sempronius Caecilius, died AD 173). This was his last visit.",
    )

    # ── Generated color-circle markers ──────────────────────────────────────

    # Flooded water marker (blue, semi-transparent)
    write_rptok(
        "Water_Flooded_Gallery",
        circle_png((20, 80, 180, 160), label="WATER"),
        layer="OBJECT", token_type="NPC",
        notes="Chest-deep black water. Cold, still, smells of peat. 30 feet across at deepest point.",
        gm_notes="Survival DC 12: eastern wall path = shoulder depth only (advantage on Athletics). Athletics DC 11: silent wading. 4 Shadows lurk here — drawn to light. Stealth DC 14 group check (no light) = free passage. Preserved warrior at far wall.",
    )

    # Rune markers for the Runic Corridor — 5 rune types
    rune_colors = {
        "TIWAZ":   ((180, 40,  40,  220), "WAR"),        # red    — danger rune
        "HAGALAZ": ((180, 100, 20,  220), "HAIL"),       # orange — disruption
        "ISA":     ((80,  80,  180, 220), "ICE"),        # blue   — stillness
        "NAUDHIZ": ((140, 140, 20,  220), "NEED"),       # yellow — constraint
        "OTHALAN": ((40,  160, 40,  220), "SAFE"),       # GREEN  — safe step
    }
    for rune, (color, short) in rune_colors.items():
        write_rptok(
            f"Rune_{rune}",
            circle_png(color, label=short),
            layer="OBJECT", token_type="NPC",
            notes=f"{rune} rune. Glows cold blue-white from carved stone.",
            gm_notes=f"{'SAFE STEP — no damage. Place in every row.' if rune == 'OTHALAN' else f'WRONG STEP — 1d8 lightning damage + noise (altar guardians get 1 round prep).'}",
        )

    # Shadow lurk marker (dark grey, for Flooded Gallery positioning)
    write_rptok(
        "Shadow_Lurk_Marker",
        circle_png((30, 30, 30, 180), label="?"),
        layer="HIDDEN", token_type="NPC",
        notes="",
        gm_notes="Hidden Shadow position marker for Flooded Gallery. Move to TOKEN layer and reveal when party triggers (torch present OR failed Stealth DC 14). Replace with Shadow.rptok for actual combat.",
    )

    # T-junction marker
    write_rptok(
        "T_Junction",
        circle_png((100, 80, 50, 200), label="T"),
        layer="OBJECT", token_type="NPC",
        notes="The passage splits. Left: warmer air, dry stone. Right: colder air, sound of slow water below the floor.",
        gm_notes="Ask players which branch first. Sketch on paper. Left = Shield Hall + Alcove (no combat). Right = Flooded Gallery (Shadows) + Bone Chamber (Ghouls+Ghast). Both merge at Binding Chamber.",
    )

    print(f"\nDone — {len(list(OUT_DIR.glob('*.rptok')))} prop tokens in {OUT_DIR}/")


if __name__ == "__main__":
    main()
