#!/usr/bin/env bash
# Download Dice Grimorium battle maps + RPTools art packs for the Shadow of Mars campaign.
# Run from the Maptool/maps/ directory, or any directory (uses absolute paths).
# Idempotent: skips files already downloaded.

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DG_DIR="$SCRIPT_DIR/dicegrimorium"
RT_DIR="$SCRIPT_DIR/rptools"
mkdir -p "$DG_DIR" "$RT_DIR"

ok()  { echo "  [ok]  $1"; }
skip(){ echo " [skip] $1 (already downloaded)"; }
fail(){ echo " [FAIL] $1 — $2"; }

# Convert a Dice Grimorium URL slug to a PascalCase filename.
# e.g. "forest-ruins-dnd-battle-map" -> "ForestRuins"
slug_to_pascal() {
  local slug="${1%-dnd-battle-map}"   # strip suffix
  slug="${slug%-dnd-map}"             # alternate suffix
  python3 -c "
import re, sys
s = sys.argv[1]
print(''.join(w.capitalize() for w in s.split('-')))
" "$slug"
}

# Download one Dice Grimorium map.
# Usage: dg_map  slug  [override_url_filename]
# override_url_filename: use when the server filename differs from the PascalCase slug
# e.g. dg_map "road-altar-dnd-battle-map" "AltarByTheRoad" "AltarByTheRoad"
dg_map() {
  local slug="$1"
  local name
  name="$(slug_to_pascal "$slug")"
  # Allow an explicit server filename override (some maps deviate from PascalCase)
  local server_name="${2:-$name}"
  local url="https://dicegrimorium.com/files/${server_name}Public.zip"
  local out="$DG_DIR/${server_name}Public.zip"
  local dest="$DG_DIR/$server_name"

  if [[ -d "$dest" ]]; then
    skip "$name"
    return
  fi
  echo "  Downloading $name ..."
  if curl -fsSL --connect-timeout 15 --max-time 120 -o "$out" "$url" 2>/dev/null; then
    mkdir -p "$dest"
    unzip -qo "$out" -d "$dest" 2>/dev/null || true
    rm -f "$out"
    ok "$name"
  else
    fail "$name" "$url"
  fi
}

# Download one RPTools art pack.
# Usage: rt_pack  "Pack Name"  artpacks/filename.zip
rt_pack() {
  local name="$1"
  local path="$2"
  local url="http://library.rptools.net/1.3/${path}"
  local safe="${name// /_}"
  local out="$RT_DIR/${safe}.zip"
  local dest="$RT_DIR/$safe"

  if [[ -d "$dest" ]]; then
    skip "$name"
    return
  fi
  echo "  Downloading $name ..."
  if curl -fsSL --connect-timeout 15 --max-time 180 -o "$out" "$url" 2>/dev/null; then
    mkdir -p "$dest"
    unzip -qo "$out" -d "$dest" 2>/dev/null || true
    rm -f "$out"
    ok "$name"
  else
    fail "$name" "$url"
  fi
}

# ── Dice Grimorium: Campaign-essential maps ──────────────────────────────────

echo ""
echo "=== Dice Grimorium Maps ==="
echo ""

echo "-- Underground / Vault (Chapter 1 + 5) --"
dg_map "dungeon-entrance-dnd-battle-map"
dg_map "large-cave-dnd-battle-map"
dg_map "cave-tunnels-vol-2-dnd-battle-map"
dg_map "cave-tunnels-vol-3-dnd-battle-map"
dg_map "ancient-tombs-dnd-battle-map"
dg_map "dark-temple-entrance-dnd-battle-map"
dg_map "dark-temple-interior-dnd-battle-map"
dg_map "flooded-cave-dnd-battle-map"
dg_map "decaying-dungeon-dnd-battle-map"           "DungeonVol2"
dg_map "gold-vaults-dnd-battle-map"
dg_map "forest-dungeon-entrance-dnd-battle-map"
dg_map "ancient-altar-dnd-battle-map"
dg_map "small-random-dungeon-dnd-battle-map"        "RandomDungeon"
# Direct-named maps (non-slug pattern — confirmed live)
dg_map "ancient-crypt-dungeon"                      "AncientCryptDungeon"
dg_map "secret-vault-dungeon"                       "SecretVaultDungeon"
dg_map "cavern-pit-dnd-battle-map"
dg_map "cathedral-catacombs-dnd-battle-map"

echo ""
echo "-- Germanic Forest (Chapter 3) --"
dg_map "forest-path-dnd-battle-map"
dg_map "forest-path-vol-2-dnd-battle-map"           "ForestPath2"
dg_map "forest-path-vol-3-dnd-battle-map"           "ForestPath3"
dg_map "forest-path-vol-4-dnd-battle-map"           "ForestPath4"
dg_map "forest-path-vol-5-dnd-battle-map"
dg_map "forest-wilderness-vol-2-dnd-battle-map"     "ForestEncounter2"
dg_map "forest-wilderness-vol-3-dnd-battle-map"     "ForestEncounter3"
dg_map "forest-wilderness-vol-4-dnd-battle-map"
dg_map "forest-wilderness-vol-8-dnd-battle-map"
dg_map "forest-river-dnd-battle-map"
dg_map "forest-river-confluence-dnd-battle-map"
dg_map "forest-bridge-crossing-dnd-battle-map"
dg_map "forest-encounter-dnd-battle-map"
dg_map "forest-bandit-camp-dnd-battle-map"
dg_map "forest-bandit-fort-dnd-battle-map"
dg_map "forest-barbican-gate-dnd-battle-map"         "ForestGate"
dg_map "forest-cave-entrance-dnd-battle-map"
dg_map "forest-ruins-dnd-battle-map"
dg_map "forest-labyrinth-ruins-dnd-battle-map"       "LabyrinthRuins"
dg_map "high-ground-forest-dnd-battle-map"           "HGForest"
dg_map "swamp-dnd-battle-map"
dg_map "swamp-vol-2-dnd-battle-map"                 "Swamp2"
dg_map "swamp-forest-vol-3-dnd-battle-map"         "Swamp3"
dg_map "swamp-bridges-dnd-battle-map"
dg_map "swamp-path-dnd-battle-map"
dg_map "river-crossing-dnd-battle-map"
dg_map "river-crossing-vol-2-dnd-battle-map"
dg_map "river-crossing-vol-3-dnd-battle-map" "RiverCrossing3"
dg_map "winding-forest-path-dnd-battle-map"
dg_map "forest-sinkhole-dnd-battle-map"

echo ""
echo "-- Sacred Grove / Ritual Sites (Chapter 3-5) --"
# Direct-named map (non-slug pattern — confirmed live)
dg_map "sacred-grove"                               "SacredGrove"
dg_map "forest-ritual-site-dnd-battle-map"
dg_map "forest-worshipping-site-dnd-battle-map"
dg_map "sacred-tree-dnd-battle-map"
dg_map "druid-circle-dnd-battle-map"
dg_map "nature-goddess-temple-dnd-battle-map"
dg_map "dryad-grove-dnd-battle-map"
dg_map "road-altar-dnd-battle-map" "AltarByTheRoad"
dg_map "island-ruins-dnd-battle-map"

echo ""
echo "-- Fort / Settlement / Roads (Vindolanda + Siege) --"
# Direct-named maps (non-slug pattern — confirmed live)
dg_map "skeleton-fortress-entrance"                 "SkeletonFortressEntrance"
dg_map "snowy-fortress-entrance"                    "SnowyFortressEntrance"
dg_map "castle-wall-dnd-battle-map"
dg_map "bridge-checkpoint-dnd-battle-map"
dg_map "abandoned-village-dnd-battle-map"
dg_map "abandoned-village-vol-2-dnd-battle-map"
dg_map "riverside-village-dnd-battle-map"
dg_map "small-farm-dnd-battle-map"
dg_map "crossroads-dnd-battle-map"
dg_map "road-altar-dnd-battle-map" "AltarByTheRoad"
dg_map "mountain-pass-dnd-battle-map"
dg_map "rocky-road-dnd-battle-map"
dg_map "city-streets-dnd-battle-map"
dg_map "city-gates-dnd-battle-map"

# ── RPTools Art Packs ────────────────────────────────────────────────────────

echo ""
echo "=== RPTools Art Packs ==="
echo ""

# Markers and overlays
rt_pack "Phergus Markers"         "artpacks/Phergus_Markers.zip"
rt_pack "Torstan Markers"         "artpacks/torstan_markers.zip"

# Dungeon tiles (Grid50 = most MapTool-friendly)
rt_pack "Jshock Dwarf Walls"      "artpacks/jshocksdwarfwalls.zip"
rt_pack "Steel General Sewer Grid50" "artpacks/steelgeneral_sewer-50.zip"
rt_pack "Wyrframe Shady Halls Grid50" "artpacks/WyrframesShadyHalls6x6-Grid50.zip"
rt_pack "CSP Dungeons to Caves Grid50" "artpacks/CSP_Dungeons_to_Caves_Grid50.zip"
rt_pack "CSP Mine Geomorphs Grid50" "artpacks/CSP_Mine_Geomorphs_Grid50.zip"

# Outdoor tiles and map sets
rt_pack "Torstan Basic Map Set"   "artpacks/torstan_basicmap.zip"
rt_pack "Torstan Island Maps"     "artpacks/TorstansIslandMaps.zip"
rt_pack "Torstan Objects"         "artpacks/torstan_objects.zip"
rt_pack "Dorpond Tree Pack 1 Grid50" "artpacks/DorpondTreePack1-50.zip"
rt_pack "Dorpond Tree Pack 2 Grid50" "artpacks/DorpondsTreePack2-50.zip"
rt_pack "Dorpond Tree Pack 3 Grid50" "artpacks/DorpondsTreePack3-50.zip"
rt_pack "Dorpond Tree Pack 4 Grid50" "artpacks/DorpondsTreePack4-50.zip"
rt_pack "Dorpond Generic Town"    "artpacks/dorpond_generic_town.zip"

# Doors / windows for buildings
rt_pack "Doors and Windows Bogie Grid50"  "artpacks/DoorsWindowsBogie-50.zip"
rt_pack "Doors and Windows Bogie Grid100" "artpacks/DoorsWindowsBogie-100.zip"

echo ""
echo "=== Done ==="
echo ""
ls "$DG_DIR" | wc -l
echo "Dice Grimorium map folders"
ls "$RT_DIR" | wc -l
echo "RPTools art pack folders"
