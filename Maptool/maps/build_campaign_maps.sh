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
# Copy a custom SVG/HTML battle map from Maptool/maps/
# Also copies the companion .jpg if it exists.
# ---------------------------------------------------------------------------
copy_svg() {
  local slug="$1" dest_dir="$2"
  local html="$SCRIPT_DIR/${slug}.html"
  local jpg="$SCRIPT_DIR/${slug}.jpg"
  if [[ -f "$html" ]]; then
    cp "$html" "$dest_dir/${slug}.html"
    echo "   + SVG: ${slug}.html"
  else
    echo " [miss] SVG: ${slug}.html"
  fi
  if [[ -f "$jpg" ]]; then
    cp "$jpg" "$dest_dir/${slug}.jpg"
    echo "   + JPG: ${slug}.jpg"
  fi
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

# Dice Grimorium reference maps
copy_map DarkTempleEntrance   "$S"   # Scene 0 cold open: temple gate
copy_map DungeonVol2          "$S"   # Scenes 1-3: vault corridors
copy_map DarkTempleInterior   "$S"   # Scene 3: altar area backup

# Custom SVG battle maps (built from chapter1 scenes)
copy_svg vault_s1_overview    "$S"   # Full vault layout reference
copy_svg vault_s1_bone_chamber "$S"  # Scene 2b: 2 Ghouls + 1 Ghast
copy_svg vault_s1_altar_chamber "$S" # Scene 3: Wight + 2 Shadows
copy_svg vault_s1_courtyard   "$S"   # Scene 0: outdoor cold open

# Fort reference images (orientation, not battle maps)
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
echo "=== Session 2: The Tribune's Gambit ==="
S="$DEST/S2_Chieftains_Price"
mkdir -p "$S"

# Battle maps — fort siege (Scenes 0-4 all at Fort Vindolanda)
copy_map CastleWall           "$S"
copy_map CityGates            "$S"

# Road encounter maps (d8 optional table)
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

# Custom SVG battle maps
copy_svg s2_fort_overview     "$S"   # Full fort overview reference
copy_svg s2_approach_north    "$S"   # Scene 1: north approach (pre-raid)
copy_svg s2_north_wall        "$S"   # Scene 2: Phase 1 wall defense
copy_svg s2_west_gate         "$S"   # Scene 3: Phase 2 gate assault

cp "$FORT_IMGS/saalburg_plan.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/saalburg_fort.jpg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/castra_layout.svg"     "$S/" 2>/dev/null || true
cp "$FORT_IMGS/vindolanda_aerial.jpg" "$S/" 2>/dev/null || true
echo "   + fort reference images"

# Named NPCs
for slug in Legate_Corvinus Tribune_Lucius Augur_Cassia Centurion_Varro \
            Vercingetorix_the_Red Valeria_the_Medicus Quartus Rufus_the_Smith \
            Brennus Lucilla_the_Postwoman Aemilia_Secunda Titus_Half-Germanic \
            Quintus_Flavius Aelius_Rufus; do
  copy_npc "$slug" "$S"
done

# Raid creatures (Ph1 wall + Ph2 gate + Ph3 Vercingetorix)
# Road encounters: Shadow (enc 2), Cultist_of_Mars (enc 6)
for slug in Tribal_Warrior Berserker Praetorian_Guard Guard Scout Shadow Cultist_of_Mars \
            Dire_Wolf Druid Ogre Worg Brown_Bear Wolf Boar Bandit Bandit_Captain; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 3: Through the Dark Forest ==="
S="$DEST/S3_Through_the_Dark_Forest"
mkdir -p "$S"

# Dice Grimorium forest/wilderness maps (road encounters + general forest)
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
copy_map LabyrinthRuins "$S"
copy_map ForestRiverConfluence "$S"
copy_map RiverCrossing        "$S"
copy_map Swamp                "$S"
copy_map SwampVol2            "$S"
copy_map SwampForestVol3      "$S"
copy_map SwampBridges         "$S"
copy_map SwampPath            "$S"
copy_map HighGroundForest     "$S"

# Custom SVG battle maps
copy_svg s3_forest_overview    "$S"  # Chapter 3 region overview
copy_svg s3_forest_path        "$S"  # Scene 1: ambush on the road
copy_svg s3_germanic_village   "$S"  # Scene 4: Thusnelda's village
copy_svg s3_farbog_crossing    "$S"  # Scene 3b: Farbog encounter

for slug in Legate_Corvinus Tribune_Lucius Augur_Cassia Centurion_Varro Vercingetorix_the_Red Thusnelda \
            Titus_Half-Germanic Sigrun_the_Trader Arnulf_the_Firekeeper \
            Edda_the_Spear-Mother Skadi_the_Healer Aldric_the_Gaul; do
  copy_npc "$slug" "$S"
done

# Creatures: forest wildlife, bog spirits, pursuit force
# Scene 3b Farbog: Wight (Vaettir deep bog), Specter, Will-o-Wisp
# Scene 4 Sacred Grove: Dryad guardian
# Scene 5: Stone_Golem (avatars of Mars' anger at the grove ritual — not killable at L5)
for slug in Wolf Dire_Wolf Brown_Bear Giant_Spider Haugbui Myling Vaettir \
            Wight Dryad Tribal_Warrior Scout Will-o-Wisp Specter Guard Knight Stone_Golem; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 4: The Blood Cult Dungeon ==="
S="$DEST/S4_The_Gods_Demand"
mkdir -p "$S"

# Dice Grimorium maps -- the marsh entrance, the main dungeon, the Core Room
cp "$DG/SkeletonFortressEntrance/Skeleton Fortress Entrance Public/SkeletonFortressEntrancePublic.jpg" "$S/" 2>/dev/null \
  && echo "   + SkeletonFortressEntrance" || echo " [miss] SkeletonFortressEntrance"
cp "$DG/BloodCultDungeon/Blood Cult Dungeon Public/Blood-Cult-Dungeon-Gridded-29x43-MapPublic.jpg" "$S/" 2>/dev/null \
  && echo "   + BloodCultDungeon" || echo " [miss] BloodCultDungeon"
cp "$DG/CastleCoreRoom/Castle Core Room Public/CastleCoreRoomPublic.jpg" "$S/" 2>/dev/null \
  && echo "   + CastleCoreRoom" || echo " [miss] CastleCoreRoom"

# NPCs: only Lucius travels with the party this session (Corvinus/Varro/Cassia stay at the fort)
copy_npc "Tribune_Lucius" "$S"

# Creatures: the Blood Cult Dungeon's monster roster (all real Monster Manual
# demons/undead, no generic filler -- see SCRUM_BACKLOG.md Epic 8)
for slug in Banshee Bone_Naga Yochlol Dretch Shadow_Demon Wraith Glabrezu; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Session 5: The Wrath of Mars ==="
S="$DEST/S5_The_Wrath_of_Mars"
mkdir -p "$S"

# Custom SVG battle maps -- the dungeon continues down from Chapter 4's Core Room
copy_svg s5_mars_vault_overview "$S" # Full vault overview: Sunken Armory -> Choking Hall -> Elder Stair -> Antechamber
copy_svg s5_mars_vault          "$S" # Scene 1-2: entry corridor, antechamber, Convergence Hall 3-passage choice
copy_svg s5_mars_confrontation  "$S" # Scene 4: the Sanctum, Mars's staged manifestation

# NPCs: only Lucius travels with the party this session (Corvinus/Varro/Cassia
# stay at the fort per Chapter 4, reappear only in the epilogue back at the fort)
copy_npc "Tribune_Lucius" "$S"
copy_npc "Vercingetorix_Bound" "$S"
copy_npc "Mars" "$S"

# Creatures: reused corridor undead from earlier sessions, no new pipeline work needed
for slug in Wraith Wight Shadow Specter Zombie; do
  copy_npc "$slug" "$S"
done

# ---------------------------------------------------------------------------
echo ""
echo "=== Summary ==="
for d in "$DEST"/S*; do
  maps=$(find "$d" \( -name "*.jpg" -o -name "*.png" -o -name "*.webp" -o -name "*.svg" -o -name "*.html" \) 2>/dev/null | wc -l)
  tokens=$(find "$d" -name "*.rptok" 2>/dev/null | wc -l)
  printf "  %-42s %2d maps  %2d tokens\n" "$(basename "$d")" "$maps" "$tokens"
done
