#!/usr/bin/env python3
"""
Assign CC0 portrait images (pd-portraits-200x200 pack) to NPC JSON files.

Usage:
  python3 scripts/assign_portraits.py [--src /tmp/pd-portraits]

Steps:
  1. Copy selected portrait PNGs from SRC_DIR to npcs/portraits/
  2. Update portrait_file field in each NPC JSON
  3. Print summary
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
NPCS_DIR  = REPO_ROOT / "npcs"
PORTRAITS_DIR = NPCS_DIR / "portraits"

# ── Portrait mapping ──────────────────────────────────────────────────────────
# NPC JSON basename (no .json) → portrait filename from the CC0 pack
# Artists: public domain historical paintings, all CC0 via OpenGameArt pack.
# Selection rationale:
#   Roman military/nobility: Holbein, Velázquez, Breda (formal court portraits)
#   Roman women: Godward (neoclassical women in Roman dress — perfect match)
#   Germanic males: Defregger (Tyrolean/folk genre, bearded rustic men)
#   Germanic women: Blommer (Nordic mythology), Makovsky (Slavic/Eastern European)
#   Dramatic warriors: Regnault (Orientalist), Vasnetsov (Russian epic)
#   Cultists/dark: Goya (dark Spanish Romantic — ideal for sinister NPCs)
#   Divine/mythological: Gérôme (French classical, painted Roman/Greek scenes)
#   Scholarly/older: Bellini, Kellerhoven (Renaissance formal portraits)

PORTRAIT_MAP = {
    # ── Primary Named NPCs ──────────────────────────────────────────────────
    # Roman military/political (male)
    "corvinus":          "hans_holbein1.png",           # stern Renaissance court portrait
    "lucius":            "byron1.png",                  # brooding Romantic noble (Tribune)
    "varro":             "alexey_petrovich_antropov1.png",  # 18th-c formal military bearing
    "brutus":            "velazquez_diego1.png",         # Spanish Baroque authority (Senator)
    "paterculus":        "giovanni_bellini1.png",        # Venetian Renaissance, scholarly
    "quartus":           "jean-baptiste-camille_corot1.png",   # Corot portrait, practical
    "rufus":             "jean-baptiste-camille_corot2.png",   # Corot, craftsman type
    "aelius_rufus":      "carl_fredric_breda1.png",     # formal 18th-c portrait
    "quintus_flavius":   "carl_fredric_breda2.png",     # similar formal style

    # Roman women (Godward painted neoclassical women in Roman settings!)
    "cassia":            "john_william_godward1.png",   # Roman woman, classical dress
    "valeria":           "john_william_godward2.png",   # Roman woman, serene
    "lucilla":           "john_william_godward3.png",   # Roman woman, observant
    "fausta_luperci":    "gaston_bussiere1.png",        # Symbolist female, otherworldly

    # Germanic males
    "vercingetorix":     "regnault_henri1.png",         # dramatic Orientalist warrior
    "arnulf":            "franz_von_defregger2.png",    # Tyrolean/Germanic folk man
    "brennus":           "franz_von_defregger3.png",    # Germanic, rustic, tavern type
    "titus_half_germanic": "franz_von_defregger1.png",  # half-Germanic scout
    "aldric":            "delacroix_eugene_ferdinand_victor1.png",  # Romantic dramatic

    # Germanic women
    "thusnelda":         "nils_johan_olsson_blommer1.png",  # Norse mythology female
    "sigrun":            "hayez_francesco1.png",         # Italian Romantic female portrait
    "edda":              "viktor_vasnetsov1.png",        # Russian epic warrior scene
    "skadi":             "sichel_nathanael1.png",        # orientalist female portrait

    # Divine
    "mars":              "jean-leon_gerome1.png",        # classical mythology (Gérôme)

    # ── Humanoid Creature Tokens (give human portraits) ─────────────────────
    "guard":             "moritz_kellerhoven1.png",      # 18th-c formal guard portrait
    "legionary":         "paolo_veronese1.png",          # Venetian Renaissance, military
    "praetorian":        "leopold_loffler1.png",         # formal Austrian portrait
    "berserker":         "ilja_jefimowitsch_repin1.png", # Russian Realist, dramatic
    "cultist":           "francisco_goya_lucientes1.png", # Goya — ideal for cult member
    "bandit":            "francisco_goya_lucientes2.png", # Goya dark tone
    "bandit_captain":    "domenikos_theotokopoulos1.png", # El Greco, intense face
    "scout":             "nathaniel_jocelyn1.png",       # formal American portrait
    "druid":             "svetoslav_roerich1.png",       # Roerich mystic/nature art
    "knight":            "frederic_westin1.png",         # Swedish Romantic, knight type
    "tribal_warrior":    "francisco_zurbaran1.png",      # Spanish, strong face
}

# ── Dryad / nature spirits — use classical female ───────────────────────────
PORTRAIT_MAP["dryad"] = "john_william_godward1.png"   # reuse Godward (nature spirit)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="/tmp/pd-portraits",
                        help="Directory containing extracted CC0 portrait PNGs")
    args = parser.parse_args()

    src_dir = Path(args.src)
    if not src_dir.exists():
        print(f"ERROR: Source directory not found: {src_dir}")
        sys.exit(1)

    PORTRAITS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Source : {src_dir}")
    print(f"Dest   : {PORTRAITS_DIR}")
    print()

    # Copy unique portrait files
    copied = set()
    for portrait_file in PORTRAIT_MAP.values():
        if portrait_file in copied:
            continue
        src = src_dir / portrait_file
        dst = PORTRAITS_DIR / portrait_file
        if src.exists():
            shutil.copy2(src, dst)
            copied.add(portrait_file)
            print(f"  copy  {portrait_file}")
        else:
            print(f"  MISS  {portrait_file} (not in source dir)")

    print()

    # Update NPC JSONs
    updated = 0
    skipped = 0
    for npc_name, portrait_file in sorted(PORTRAIT_MAP.items()):
        json_path = NPCS_DIR / f"{npc_name}.json"
        if not json_path.exists():
            print(f"  WARN  npcs/{npc_name}.json not found — skip")
            skipped += 1
            continue

        dst = PORTRAITS_DIR / portrait_file
        if not dst.exists():
            print(f"  SKIP  {npc_name} (portrait file missing)")
            skipped += 1
            continue

        data = json.loads(json_path.read_text())
        rel  = f"portraits/{portrait_file}"
        if data.get("portrait_file") == rel:
            skipped += 1
            continue

        data["portrait_file"] = rel
        json_path.write_text(json.dumps(data, indent=2) + "\n")
        print(f"  set   {npc_name:<28} -> {rel}")
        updated += 1

    print()
    print(f"Done. Updated: {updated}  Skipped: {skipped}  Portraits copied: {len(copied)}")


if __name__ == "__main__":
    main()
