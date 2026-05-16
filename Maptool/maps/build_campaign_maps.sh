#!/usr/bin/env bash
set -euo pipefail

BASE=/home/chris/Documents/NextCloud/Github/DnDVault---Roman-Campaign/Maptool
DG="$BASE/maps/dicegrimorium"
FORT_TOKENS="$BASE/maps/campaign/Fort_Vindolanda"
DEST="$BASE/maps/campaign"
FORT_IMGS="$BASE/../images"   # saalburg_plan, castra_layout, vindolanda_aerial

# Copy one map (find the non-promo image in a dicegrimorium folder)
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

# Copy a named NPC token (.rptok) from the Fort_Vindolanda folder
copy_token() {
  local src="$FORT_TOKENS/$1"
  local dest_dir="$2"
  if [[ -f "$src" ]]; then
    cp "$src" "$dest_dir/$(basename "$src")"
    echo "   + token: $1"
  else
    echo " [miss] token: $1"
  fi
}

mkdir -p "$DEST"

# Clean and rebuild all session folders so stale files never accumulate
for d in "$DEST"/S*; do
  [[ -d "$d" ]] && rm -rf "$d"
done

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Fort Vindolanda (permanent camp folder) ==="
F="$DEST/Fort_Vindolanda"
mkdir -p "$F"

# Fort zone battlemaps — assembled from downloaded Dice Grimorium maps
# Each map covers a specific zone inside or around the fort
copy_map CityGates          "$F"   # South gate / fort entrance with towers and road
copy_map CityStreets        "$F"   # Via principalis — main street between buildings
copy_map CastleWall         "$F"   # Rampart / wall walk — wall defense scenes
copy_map NatureGoddessTemple "$F"  # Principia (HQ) — cross-shaped stone building with courtyard
copy_map GoldVaults         "$F"   # Horrea / treasury — vaulted stone corridor with side bays
copy_map AbandonedVillageVol2 "$F" # Barracks block — stone-walled rooms with visible interiors
copy_map AbandonedVillage   "$F"   # Vicus (civilian quarter) — settlement overview
copy_map RiversideVillage   "$F"   # Vicus alternative — riverside civilian buildings
copy_map BridgeCheckpoint   "$F"   # Road approach / bridge to the fort
copy_map DarkTempleEntrance "$F"   # Vault entrance — sealed stair beneath principia
copy_map DarkTempleInterior "$F"   # Vault interior — spear chamber, altar

# Fort reference images
cp "$FORT_IMGS/saalburg_plan.jpg"     "$F/saalburg_plan.jpg"     2>/dev/null && echo "   + saalburg_plan"
cp "$FORT_IMGS/saalburg_fort.jpg"     "$F/saalburg_fort.jpg"     2>/dev/null && echo "   + saalburg_fort"
cp "$FORT_IMGS/castra_layout.svg"     "$F/castra_layout.svg"     2>/dev/null && echo "   + castra_layout"
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$F/vindolanda_aerial.jpg" 2>/dev/null && echo "   + vindolanda_aerial"

# All NPC tokens — copy from dnd5eTokens source, not from self
HUM="$BASE/dnd5eTokens/humanoid"
cp "$HUM/Knight.rptok"       "$F/Corvinus_Legate.rptok"       && echo "   + token: Corvinus_Legate"
cp "$HUM/Priest.rptok"       "$F/Cassia_Augur.rptok"          && echo "   + token: Cassia_Augur"
cp "$HUM/Veteran.rptok"      "$F/Varro_Centurion.rptok"       && echo "   + token: Varro_Centurion"
cp "$HUM/Noble.rptok"        "$F/Brutus_Senator.rptok"        && echo "   + token: Brutus_Senator"
cp "$HUM/Berserker.rptok"    "$F/Vercingetorix_Chieftain.rptok" && echo "   + token: Vercingetorix_Chieftain"
cp "$HUM/Druid.rptok"        "$F/Thusnelda_Volva.rptok"       && echo "   + token: Thusnelda_Volva"
cp "$HUM/Guard.rptok"        "$F/Legionary_Guard.rptok"       && echo "   + token: Legionary_Guard"
cp "$HUM/Scout.rptok"        "$F/Explorator_Scout.rptok"      && echo "   + token: Explorator_Scout"
cp "$HUM/Commoner.rptok"     "$F/Vicus_Civilian.rptok"        && echo "   + token: Vicus_Civilian"
cp "$HUM/Spy.rptok"          "$F/Frumentarius_Agent.rptok"    && echo "   + token: Frumentarius_Agent"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Session 1: Blood and Omens ==="
S="$DEST/S1_Blood_and_Omens"
mkdir -p "$S"

# Fort zone maps (scenes 0-1 happen inside the fort)
copy_map CityGates            "$S"   # Fort south gate — Tribune's arrival, party departure
copy_map CityStreets          "$S"   # Via principalis — Legate summons party
copy_map NatureGoddessTemple  "$S"   # Principia — Legate's audience chamber
copy_map CastleWall           "$S"   # Rampart — sentry scenes, exterior

# Underground vault (scenes 2-5)
copy_map BridgeCheckpoint     "$S"   # Road/ditch approach to vault entrance
copy_map DungeonEntrance      "$S"
copy_map ForestDungeonEntrance "$S"
copy_map LargeCave            "$S"
copy_map AncientAltar         "$S"   # Spear chamber — key scene
copy_map CaveTunnelsVol2      "$S"
copy_map CaveTunnelsVol3      "$S"
copy_map AncientTombs         "$S"
copy_map GoldVaults           "$S"
copy_map FloodedCave          "$S"
copy_map CathedralCatacombs   "$S"
copy_map CavernPit            "$S"
copy_map RandomDungeon        "$S"
copy_map DungeonVol2          "$S"
copy_map DarkTempleEntrance   "$S"   # Sealed stair entrance
copy_map DarkTempleInterior   "$S"   # Vault interior / altar chamber

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/saalburg_plan.jpg"
cp "$FORT_IMGS/saalburg_fort.jpg"     "$S/saalburg_fort.jpg"
cp "$FORT_IMGS/castra_layout.svg"     "$S/castra_layout.svg"
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/vindolanda_aerial.jpg"
echo "   + fort reference images"

# NPC tokens
copy_token Corvinus_Legate.rptok     "$S"
copy_token Cassia_Augur.rptok        "$S"
copy_token Varro_Centurion.rptok     "$S"
copy_token Legionary_Guard.rptok     "$S"
copy_token Vicus_Civilian.rptok      "$S"

# Creature tokens for S1 encounters
CON="$BASE/dnd5eTokens/construct"
cp "$CON/Animated Armor.rptok"  "$S/Creature_AnimatedArmor.rptok"  && echo "   + token: Animated Armor (x2 in vault)"
cp "$HUM/Berserker.rptok"       "$S/Creature_CorruptedWorker.rptok" && echo "   + token: Corrupted Worker (Berserker)"

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

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/saalburg_plan.jpg"
cp "$FORT_IMGS/saalburg_fort.jpg"    "$S/saalburg_fort.jpg"
cp "$FORT_IMGS/castra_layout.svg"    "$S/castra_layout.svg"
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/vindolanda_aerial.jpg"
echo "   + fort reference images"

copy_token Corvinus_Legate.rptok      "$S"
copy_token Cassia_Augur.rptok         "$S"
copy_token Varro_Centurion.rptok      "$S"
copy_token Vercingetorix_Chieftain.rptok "$S"
copy_token Legionary_Guard.rptok      "$S"
copy_token Explorator_Scout.rptok     "$S"
copy_token Vicus_Civilian.rptok       "$S"

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

copy_token Varro_Centurion.rptok         "$S"
copy_token Vercingetorix_Chieftain.rptok "$S"
copy_token Thusnelda_Volva.rptok         "$S"
copy_token Explorator_Scout.rptok        "$S"

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

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/saalburg_plan.jpg"
cp "$FORT_IMGS/saalburg_fort.jpg"    "$S/saalburg_fort.jpg"
cp "$FORT_IMGS/castra_layout.svg"    "$S/castra_layout.svg"
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/vindolanda_aerial.jpg"
echo "   + fort reference images"

copy_token Cassia_Augur.rptok            "$S"
copy_token Varro_Centurion.rptok         "$S"
copy_token Vercingetorix_Chieftain.rptok "$S"
copy_token Brutus_Senator.rptok          "$S"
copy_token Legionary_Guard.rptok         "$S"

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

copy_token Corvinus_Legate.rptok         "$S"
copy_token Cassia_Augur.rptok            "$S"
copy_token Varro_Centurion.rptok         "$S"
copy_token Vercingetorix_Chieftain.rptok "$S"
copy_token Brutus_Senator.rptok          "$S"
copy_token Thusnelda_Volva.rptok         "$S"
copy_token Legionary_Guard.rptok         "$S"

# ─────────────────────────────────────────────────────────────────────────────
echo ""
echo "=== Summary ==="
for d in "$DEST"/S*; do
  maps=$(find "$d" -name "*.jpg" -o -name "*.png" | wc -l)
  tokens=$(find "$d" -name "*_token.html" | wc -l)
  printf "  %-40s %2d maps  %d tokens\n" "$(basename $d)" "$maps" "$tokens"
done
