#!/usr/bin/env bash
set -euo pipefail

BASE=/home/chris/Documents/NextCloud/Github/DnDVault---Roman-Campaign/Maptool
DG="$BASE/maps/dicegrimorium"
TOKENS="$BASE/tokens/npcs"
DEST="$BASE/maps/campaign"

# Copy one map (find the non-promo image in a dicegrimorium folder)
copy_map() {
  local folder="$DG/$1"
  local dest_dir="$2"
  if [[ ! -d "$folder" ]]; then echo " [miss] $1"; return; fi
  # Find the actual map image — exclude anything with "promo" or "Promo" in name
  while IFS= read -r -d '' img; do
    local fname
    fname="$(basename "$img")"
    cp "$img" "$dest_dir/$fname"
    echo "   + $1 → $fname"
  done < <(find "$folder" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.webp" \) ! -iname "*promo*" -print0)
}

# Copy a token HTML file
copy_token() {
  local src="$TOKENS/$1"
  local dest_dir="$2"
  if [[ -f "$src" ]]; then
    cp "$src" "$dest_dir/$(basename "$src")"
    echo "   + token: $1"
  fi
}

mkdir -p "$DEST"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 1: Blood and Omens ==="
S="$DEST/S1_Blood_and_Omens"
mkdir -p "$S"

copy_map CastleWall           "$S"
copy_map BridgeCheckpoint     "$S"
copy_map DungeonEntrance      "$S"
copy_map ForestDungeonEntrance "$S"
copy_map LargeCave            "$S"
copy_map AncientAltar         "$S"
copy_map CaveTunnelsVol2      "$S"
copy_map CaveTunnelsVol3      "$S"
copy_map AncientTombs         "$S"
copy_map GoldVaults           "$S"
copy_map FloodedCave          "$S"
copy_map CathedralCatacombs   "$S"
copy_map CavernPit            "$S"
copy_map RandomDungeon        "$S"
copy_map DungeonVol2          "$S"

copy_token corvinus_token.html  "$S"
copy_token cassia_token.html    "$S"
copy_token varro_token.html     "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 2: The Chieftain's Price ==="
S="$DEST/S2_Chieftains_Price"
mkdir -p "$S"

copy_map ForestPath           "$S"
copy_map ForestPath2          "$S"
copy_map RockyRoad            "$S"
copy_map MountainPass         "$S"
copy_map Crossroads           "$S"
copy_map AltarByTheRoad       "$S"
copy_map AbandonedVillage     "$S"
copy_map AbandonedVillageVol2 "$S"
copy_map RiversideVillage     "$S"
copy_map SmallFarm            "$S"
copy_map ForestBanditCamp     "$S"

copy_token corvinus_token.html     "$S"
copy_token cassia_token.html       "$S"
copy_token varro_token.html        "$S"
copy_token vercingetorix_token.html "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 3: Through the Dark Forest ==="
S="$DEST/S3_Through_the_Dark_Forest"
mkdir -p "$S"

copy_map ForestPath3          "$S"
copy_map ForestPath4          "$S"
copy_map ForestPathVol5       "$S"
copy_map ForestWildernessVol4 "$S"
copy_map ForestWildernessVol8 "$S"
copy_map HGForest             "$S"
copy_map WindingForestPath    "$S"
copy_map ForestSinkhole       "$S"
copy_map ForestEncounter      "$S"
copy_map ForestEncounter2     "$S"
copy_map ForestEncounter3     "$S"
copy_map ForestBridgeCrossing "$S"
copy_map ForestBanditFort     "$S"
copy_map ForestGate           "$S"
copy_map ForestRiver          "$S"
copy_map ForestRiverConfluence "$S"
copy_map RiverCrossing        "$S"
copy_map RiverCrossingVol2    "$S"
copy_map RiverCrossing3       "$S"
copy_map Swamp                "$S"
copy_map Swamp2               "$S"
copy_map Swamp3               "$S"
copy_map SwampBridges         "$S"
copy_map SwampPath            "$S"
copy_map ForestRuins          "$S"
copy_map LabyrinthRuins       "$S"
copy_map ForestCaveEntrance   "$S"

copy_token varro_token.html        "$S"
copy_token vercingetorix_token.html "$S"
copy_token thusnelda_token.html    "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 4: The God's Demand ==="
S="$DEST/S4_The_Gods_Demand"
mkdir -p "$S"

copy_map CastleWall           "$S"
copy_map BridgeCheckpoint     "$S"
copy_map CaveTunnelsVol3      "$S"
copy_map DungeonVol2          "$S"
copy_map ForestRitualSite     "$S"
copy_map ForestWorshippingSite "$S"
copy_map DruidCircle          "$S"
copy_map SacredTree           "$S"
copy_map DryadGrove           "$S"
copy_map NatureGoddessTemple  "$S"
copy_map IslandRuins          "$S"

copy_token cassia_token.html       "$S"
copy_token varro_token.html        "$S"
copy_token vercingetorix_token.html "$S"
copy_token brutus_token.html       "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 5: The Wrath of Mars ==="
S="$DEST/S5_The_Wrath_of_Mars"
mkdir -p "$S"

copy_map DarkTempleEntrance   "$S"
copy_map DarkTempleInterior   "$S"
copy_map AncientTombs         "$S"
copy_map CathedralCatacombs   "$S"
copy_map IslandRuins          "$S"
copy_map LabyrinthRuins       "$S"
copy_map AncientAltar         "$S"
copy_map NatureGoddessTemple  "$S"

copy_token corvinus_token.html     "$S"
copy_token cassia_token.html       "$S"
copy_token varro_token.html        "$S"
copy_token vercingetorix_token.html "$S"
copy_token brutus_token.html       "$S"
copy_token thusnelda_token.html    "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Summary ==="
for d in "$DEST"/S*; do
  maps=$(find "$d" -name "*.jpg" -o -name "*.png" | wc -l)
  tokens=$(find "$d" -name "*_token.html" | wc -l)
  printf "  %-40s %2d maps  %d tokens\n" "$(basename $d)" "$maps" "$tokens"
done
