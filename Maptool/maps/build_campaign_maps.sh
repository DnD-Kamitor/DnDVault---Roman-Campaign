#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE="$SCRIPT_DIR/.."
DG="$BASE/maps/dicegrimorium"
DEST="$BASE/maps/campaign"
FORT_IMGS="$BASE/../images"
NAMED="$BASE/tokens/npcs/named"
CREATURES="$BASE/tokens/npcs/creatures"

# ---------------------------------------------------------------------------
# Copy one map (find the non-promo image in a dicegrimorium folder)
# ---------------------------------------------------------------------------
copy_map() {
  local folder="$DG/$1"
  local dest_dir="$2"
  if [[ ! -d "$folder" ]]; then echo " [miss] $1"; return; fi
  while IFS= read -r -d '' img; do
    local fname
    fname="$(basename "$img")"
    cp "$img" "$dest_dir/$fname"
    echo "   + $1 → $fname"
  done < <(find "$folder" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.webp" \) ! -iname "*promo*" ! -name "._*" -print0)
}

# ---------------------------------------------------------------------------
# Copy a token by slug — searches named/ then creatures/
# Handles parenthetical suffixes: "Aemilia_Secunda" matches
# "Aemilia_Secunda_(Frumentarius).rptok"
# ---------------------------------------------------------------------------
copy_npc() {
  local slug="$1" dest_dir="$2"
  for dir in "$NAMED" "$CREATURES"; do
    if [[ -f "$dir/$slug.rptok" ]]; then
      cp "$dir/$slug.rptok" "$dest_dir/$slug.rptok"
      echo "   + token: $slug"
      return 0
    fi
    # prefix match for files with parenthetical suffixes
    for f in "$dir/$slug"*.rptok; do
      [[ -f "$f" ]] || continue
      cp "$f" "$dest_dir/$(basename "$f")"
      echo "   + token: $(basename "$f" .rptok)"
      return 0
    done
  done
  echo " [miss] token: $slug"
}

mkdir -p "$DEST"

# Clean and rebuild all session folders so stale files never accumulate
for d in "$DEST"/S*; do
  [[ -d "$d" ]] && rm -rf "$d"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Fort Vindolanda (permanent camp folder) ==="
F="$DEST/Fort_Vindolanda"
mkdir -p "$F"

copy_map CityGates            "$F"
copy_map CityStreets          "$F"
copy_map CastleWall           "$F"
copy_map NatureGoddessTemple  "$F"
copy_map GoldVaults           "$F"
copy_map AbandonedVillageVol2 "$F"
copy_map AbandonedVillage     "$F"
copy_map RiversideVillage     "$F"
copy_map BridgeCheckpoint     "$F"
copy_map DarkTempleEntrance   "$F"
copy_map DarkTempleInterior   "$F"

cp "$FORT_IMGS/saalburg_plan.jpg"     "$F/" 2>/dev/null && echo "   + saalburg_plan"     || true
cp "$FORT_IMGS/saalburg_fort.jpg"     "$F/" 2>/dev/null && echo "   + saalburg_fort"     || true
cp "$FORT_IMGS/castra_layout.svg"     "$F/" 2>/dev/null && echo "   + castra_layout"     || true
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$F/" 2>/dev/null && echo "   + vindolanda_aerial" || true

# All NPC and creature tokens go into the fort folder
cp "$NAMED"/*.rptok    "$F/" 2>/dev/null && echo "   + named NPC tokens"     || true
cp "$CREATURES"/*.rptok "$F/" 2>/dev/null && echo "   + creature/generic tokens" || true

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 1: Blood and Omens ==="
S="$DEST/S1_Blood_and_Omens"
mkdir -p "$S"

copy_map DarkTempleEntrance   "$S"
copy_map DungeonVol2          "$S"
copy_map DarkTempleInterior   "$S"

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/saalburg_fort.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/castra_layout.svg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/" 2>/dev/null || true
echo "   + fort reference images"

# S1 NPCs: fort staff + cult encounter
for slug in Legate_Corvinus Tribune_Lucius Augur_Cassia Centurion_Varro \
            Paterculus Valeria_the_Medicus Quartus Rufus_the_Smith \
            Brennus Lucilla_the_Postwoman Aemilia_Secunda; do
  copy_npc "$slug" "$S"
done

# S1 creatures: vault undead + scene 4 cult
for slug in Guard Legionary Skeleton Ghoul Ghast Shadow Wight \
            Berserker Cultist_of_Mars; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 2: The Chieftain's Price ==="
S="$DEST/S2_Chieftains_Price"
mkdir -p "$S"

copy_map ForestPath           "$S"
copy_map ForestPathVol2       "$S"
copy_map RockyRoad            "$S"
copy_map MountainPass         "$S"
copy_map Crossroads           "$S"
copy_map AltarByTheRoad       "$S"
copy_map AbandonedVillage     "$S"
copy_map AbandonedVillageVol2 "$S"
copy_map RiversideVillage     "$S"
copy_map SmallFarm            "$S"
copy_map ForestBanditCamp     "$S"

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/saalburg_fort.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/castra_layout.svg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/" 2>/dev/null || true
echo "   + fort reference images"

for slug in Legate_Corvinus Tribune_Lucius Augur_Cassia Centurion_Varro \
            Vercingetorix_the_Red Valeria_the_Medicus Quartus Rufus_the_Smith \
            Brennus Lucilla_the_Postwoman Aemilia_Secunda \
            Titus_Half-Germanic; do
  copy_npc "$slug" "$S"
done

for slug in Guard Scout Bandit Bandit_Captain Wolf Boar; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 3: Through the Dark Forest ==="
S="$DEST/S3_Through_the_Dark_Forest"
mkdir -p "$S"

copy_map ForestPath           "$S"
copy_map ForestPathVol2       "$S"
copy_map ForestPathVol3       "$S"
copy_map ForestPathVol4       "$S"
copy_map ForestPathVol5       "$S"
copy_map ForestWildernessVol2 "$S"
copy_map ForestEncounter      "$S"
copy_map ForestBridgeCrossing "$S"
copy_map ForestBanditFort     "$S"
copy_map ForestBarbicanGate   "$S"
copy_map ForestCaveEntrance   "$S"
copy_map ForestRuins          "$S"
copy_map ForestLabyrinthRuins "$S"
copy_map ForestRiverConfluence "$S"
copy_map RiverCrossing        "$S"
copy_map Swamp                "$S"
copy_map SwampVol2            "$S"
copy_map SwampForestVol3      "$S"
copy_map SwampBridges         "$S"
copy_map SwampPath            "$S"
copy_map HighGroundForest     "$S"

for slug in Tribune_Lucius Centurion_Varro Vercingetorix_the_Red Thusnelda \
            Titus_Half-Germanic Sigrun_the_Trader Arnulf_the_Firekeeper \
            Edda_the_Spear-Mother Skadi_the_Healer Aldric_the_Gaul; do
  copy_npc "$slug" "$S"
done

for slug in Wolf Dire_Wolf Brown_Bear Giant_Spider Haugbui Myling Vaettir; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 4: The God's Demand ==="
S="$DEST/S4_The_Gods_Demand"
mkdir -p "$S"

copy_map CastleWall           "$S"
copy_map BridgeCheckpoint     "$S"
copy_map CaveTunnelsVol3      "$S"
copy_map DungeonVol2          "$S"
copy_map ForestRuins          "$S"
copy_map ForestLabyrinthRuins "$S"
copy_map NatureGoddessTemple  "$S"

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/saalburg_fort.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/castra_layout.svg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/" 2>/dev/null || true
echo "   + fort reference images"

for slug in Tribune_Lucius Augur_Cassia Centurion_Varro Vercingetorix_the_Red \
            Thusnelda Senator_Brutus Valeria_the_Medicus \
            Sigrun_the_Trader Arnulf_the_Firekeeper Edda_the_Spear-Mother \
            Skadi_the_Healer Aldric_the_Gaul; do
  copy_npc "$slug" "$S"
done

for slug in Guard Legionary Berserker Cultist_of_Mars Tribal_Warrior \
            Wight Will-o-Wisp; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 5: The Wrath of Mars ==="
S="$DEST/S5_The_Wrath_of_Mars"
mkdir -p "$S"

copy_map DarkTempleEntrance   "$S"
copy_map DarkTempleInterior   "$S"
copy_map AncientTombs         "$S"
copy_map CathedralCatacombs   "$S"
copy_map ForestLabyrinthRuins "$S"
copy_map AncientAltar         "$S"
copy_map NatureGoddessTemple  "$S"

for slug in Legate_Corvinus Tribune_Lucius Augur_Cassia Centurion_Varro \
            Vercingetorix_the_Red Thusnelda Senator_Brutus Valeria_the_Medicus \
            Sigrun_the_Trader Arnulf_the_Firekeeper Edda_the_Spear-Mother \
            Skadi_the_Healer Aldric_the_Gaul; do
  copy_npc "$slug" "$S"
done

for slug in Guard Legionary Berserker Cultist_of_Mars Tribal_Warrior \
            Wraith Wight Shadow Specter Zombie; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Summary ==="
for d in "$DEST"/S*; do
  maps=$(find "$d" \( -name "*.jpg" -o -name "*.png" -o -name "*.webp" -o -name "*.svg" \) 2>/dev/null | wc -l)
  tokens=$(find "$d" -name "*.rptok" 2>/dev/null | wc -l)
  printf "  %-42s %2d maps  %2d tokens\n" "$(basename "$d")" "$maps" "$tokens"
done
