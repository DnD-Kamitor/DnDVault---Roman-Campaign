#!/usr/bin/env python3
"""
Inject real portrait images into creature .rptok token files.
Replaces the text-abbreviation placeholder with actual artwork.
"""

import os
import hashlib
import zipfile
import re
import shutil
from io import BytesIO
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREATURES_DIR = os.path.join(BASE, "Maptool/tokens/npcs/creatures")
IMAGES_DIR = os.path.join(BASE, "images")

# Extract default MapTool portrait images once
def extract_default_portrait(tok_name):
    """Pull portrait from ~/.maptool-rptools default tokens."""
    src = os.path.expanduser(f"~/.maptool-rptools/resource/Default/Tokens/{tok_name}.rptok")
    if not os.path.exists(src):
        return None
    with zipfile.ZipFile(src) as z:
        for name in z.namelist():
            if name.startswith("assets/") and not name.endswith("/"):
                base = os.path.basename(name)
                if "." not in base:
                    # XML wrapper — read base64 image from it
                    try:
                        xml_data = z.read(name).decode("utf-8", errors="replace")
                        m = re.search(r"<image>(.*?)</image>", xml_data, re.DOTALL)
                        if m and len(m.group(1).strip()) > 10:
                            import base64
                            return base64.b64decode(m.group(1).replace("\n", "").replace(" ", ""))
                    except Exception:
                        pass
                elif base.endswith(".png") or base.endswith(".jpg"):
                    return z.read(name)
    return None

# Load images
def load_image_bytes(path):
    with open(path, "rb") as f:
        return f.read()

# Resize to 200x200 square (center-crop)
def square_crop(img_bytes, size=200):
    try:
        img = Image.open(BytesIO(img_bytes)).convert("RGBA")
    except Exception:
        img = Image.open(BytesIO(img_bytes)).convert("RGB")
    w, h = img.size
    m = min(w, h)
    left = (w - m) // 2
    top = (h - m) // 2
    img = img.crop((left, top, left + m, top + m))
    img = img.resize((size, size), Image.LANCZOS)
    out = BytesIO()
    img.save(out, format="PNG")
    return out.getvalue()

def md5(data):
    return hashlib.md5(data).hexdigest()

def make_asset_xml(hash_id, ext, name):
    return f"""<net.rptools.maptool.model.Asset>
  <id>
    <id>{hash_id}</id>
  </id>
  <name>{name}</name>
  <extension>{ext}</extension>
  <type>image</type>
  <image/>
</net.rptools.maptool.model.Asset>""".encode("utf-8")

def inject_portrait(rptok_path, img_bytes):
    """Replace the portrait image in a .rptok file."""
    portrait_data = square_crop(img_bytes)
    new_hash = md5(portrait_data)
    ext = "png"
    tok_name = os.path.splitext(os.path.basename(rptok_path))[0]

    with zipfile.ZipFile(rptok_path, "r") as zin:
        names = zin.namelist()
        files = {}
        old_hash = None

        content_xml = zin.read("content.xml").decode("utf-8")
        m = re.search(r"<net\.rptools\.lib\.MD5Key><id>([0-9a-f]{32})</id>", content_xml)
        if m:
            old_hash = m.group(1)

        for name in names:
            if name.startswith("assets/") and old_hash and old_hash in name:
                continue  # skip old asset files
            if name in ("thumbnail", "thumbnail_large"):
                continue  # regenerate
            files[name] = zin.read(name)

    # Update content.xml: replace old hash with new hash
    if old_hash:
        content_xml = content_xml.replace(old_hash, new_hash)
    files["content.xml"] = content_xml.encode("utf-8")

    # New asset files
    files[f"assets/{new_hash}"] = make_asset_xml(new_hash, ext, tok_name.lower())
    files[f"assets/{new_hash}.{ext}"] = portrait_data

    # Thumbnail = same image, smaller
    thumb_data = square_crop(img_bytes, 50)
    files["thumbnail"] = thumb_data
    files["thumbnail_large"] = square_crop(img_bytes, 100)

    # Repack
    tmp_path = rptok_path + ".tmp"
    with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    os.replace(tmp_path, rptok_path)
    return new_hash

# ── Image sources ──────────────────────────────────────────────────────────
img_cache = {}

def get_img(key):
    if key not in img_cache:
        img_cache[key] = _load_img(key)
    return img_cache[key]

def _load_img(key):
    if key.startswith("default:"):
        tok = key[len("default:"):]
        data = extract_default_portrait(tok)
        if data is None:
            raise FileNotFoundError(f"Default token not found: {tok}")
        return data
    path = os.path.join(IMAGES_DIR, key)
    return load_image_bytes(path)

# ── Token → image mapping ─────────────────────────────────────────────────
PORTRAIT_MAP = {
    # Norse/Germanic undead
    "Draugar":              "draugar.jpg",
    "Haugbui":              "draugar.jpg",
    "Wight":                "draugar.jpg",
    "Zombie":               "draugar.jpg",
    # Dark spirits — Fuseli Nightmare painting
    "Alp":                  "alp_nightmare.jpg",
    "Shadow":               "alp_nightmare.jpg",
    "Specter":              "alp_nightmare.jpg",
    "Wraith":               "alp_nightmare.jpg",
    "Myling":               "alp_nightmare.jpg",
    # Water spirit
    "Nix":                  "nix_nokken.jpg",
    # Roman spirit
    "Genius_Loci":          "genius_loci.jpg",
    # Roman spirit fresco
    "Larvae":               "lemures_fresco.jpg",
    "Vættir":               "lemures_fresco.jpg",
    # Wolves
    "Wolf":                 "default:Wolf",
    "Dire_Wolf":            "default:Wolf",
    # Humanoid warriors (Hero image)
    "Guard":                "default:Hero",
    "Legionary_(Milites)":  "default:Hero",
    "Berserker":            "default:Hero",
    "Bandit_Captain":       "default:Hero",
    "Grunwald_(Foederatus)":"default:Hero",
    "Marcus_Sextius_(Tesserarius)": "default:Hero",
    "Lucius_Calvus_(Signifer)":     "default:Hero",
    # Spellcasters / priests (Mage image)
    "Cultist_of_Mars":      "default:Mage",
    "Cult_Mars_Fanatic":    "default:Mage",
    "Flavius_Martis_(Flamen_Martialis)": "default:Mage",
    "Brennus":              "default:Mage",
    # Female / Fey (Elf image)
    "Dryad":                "default:Elf",
    "Aemilia_Secunda_(Frumentarius)": "default:Elf",
    # Additional undead (draugar image)
    "Ghoul":                "draugar.jpg",
    "Ghast":                "draugar.jpg",
    "Skeleton":             "draugar.jpg",
    "Vaettir":              "draugar.jpg",       # actual filename (no special char)
    # Additional dark spirits
    "Will-o-Wisp":          "nix_nokken.jpg",    # eerie water-light
    "Strix":                "genius_loci.jpg",   # Roman owl-spirit
    # Additional humanoid warriors
    "Bandit":               "default:Hero",
    "Scout":                "default:Hero",
    "Praetorian_Guard":     "default:Hero",
    "Tribal_Warrior":       "default:Hero",
    "Publius_Arma_(Custos_Armorum)":  "default:Hero",
    "Rufus_the_Smith":      "default:Hero",
    "Quartus":              "default:Hero",
    # Additional mage/priest/scholar NPCs
    "Paterculus":           "default:Mage",
    "Quintus_Caelius_(Librarius)": "default:Mage",
    "Titus_Vindex_(Capsarius)":    "default:Mage",
    # Dead soldier (Hero — still a warrior)
    "Aquilifer_(Vacant_—_Metellus_Dead)": "default:Hero",
}

def main():
    tokens = [f for f in os.listdir(CREATURES_DIR) if f.endswith(".rptok")]
    updated = 0
    skipped = 0

    for tok_file in sorted(tokens):
        stem = os.path.splitext(tok_file)[0]
        if stem not in PORTRAIT_MAP:
            skipped += 1
            continue

        img_key = PORTRAIT_MAP[stem]
        rptok_path = os.path.join(CREATURES_DIR, tok_file)

        try:
            img_bytes = get_img(img_key)
            new_hash = inject_portrait(rptok_path, img_bytes)
            print(f"  {stem:<45} → {img_key}  [{new_hash[:8]}]")
            updated += 1
        except Exception as e:
            print(f"  [ERR] {stem}: {e}")

    print(f"\nDone. Updated {updated}, skipped {skipped} (no mapping).")

if __name__ == "__main__":
    main()
