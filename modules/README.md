# Reference Modules

Pre-made D&D 5e adventure modules downloaded as adaptation references for the Shadow of Mars campaign.
Use these for room descriptions, encounter structure, and map extraction — not as drop-in replacements.

---

## army_of_the_damned.pdf

**License:** CC0 Public Domain — no restrictions.
**Source:** <https://archive.org/details/army-of-the-damned>
**Setting:** Innistrad (Magic: The Gathering gothic horror). Vampires, werewolves, undead military.

**Structure (5 parts, mirrors Shadow of Mars):**

| Module part | Shadow of Mars parallel | Status |
|---|---|---|
| Part 2: Shadowgrange — village investigation, cult infiltration | Session 2: road intrigue, missing soldiers, Brutus network | **Integrated** (commit dd70457) |
| Part 3: Night of the Dead — undead siege of a settlement | Session 4: siege of Fort Vindolanda, Cult of Mars | Pending |
| Part 4: Into the Farbog — bog/swamp wilderness, ancient spirits | Session 3: Scene 3b (The Farbog), Myling, Vættir, bog sacrifice site | **Integrated** (Scene 3b) |
| Part 5: The Perfect Storm — climactic divine/undead confrontation | Session 5: vault, Mars manifest, undead horde | Pending |

**What to steal:** The undead-siege encounter design (Part 3) and bog-spirits tension (Part 4).
The NPC structure in Shadowgrange maps reasonably to Vindolanda's vicus cast.
Ignore the vampire/werewolf content entirely — wrong tone.

---

## death_pit_of_moloch.pdf

**License:** CC BY-NC 4.0 — free for personal/non-commercial use with attribution.
**Credit:** CJ Leung
**Source:** <https://archive.org/details/death-pit-of-moloch-dd-adventure>
**Setting:** Generic fantasy, underground cult dungeon. 4 rooms, beginner-level.

**Rooms:**
1. Sink Cavern — entry via collapse, trapped chest nearby
2. Cultist Guard Room — guards, spike trap
3. Goblin's Den — goblin allies of the cult
4. Ritual Hall — cult leader + zombies + stone altar, boss fight

**Shadow of Mars parallel:** The Altar Chamber and Binding Chamber in chapter1.qmd.
The ritual hall layout (altar + cracked demonic statue + zombie pit) is a direct template
for the Altar Chamber where the Wight holds court.

**What to steal:** The ritual hall read-aloud, the lever/sliding-door mechanic for the exit,
and the cult-leader-with-minions encounter structure. Replace goblins with Cult of Mars initiates.

---

## haunt_of_hightower.pdf

**License:** CC0 Public Domain — no restrictions.
**Setting:** Gothic undead dungeon one-shot. Four rooms, beginner-level.
**Status: Partially integrated into Session 1** (commit dd70457)

Adapted elements:
- Sicus, the wounded soldier in the Shield Hall: pre-fight intel source, drops second OTHALAN token
- Stone lever mechanic in the Altar Chamber: seals the Runic Corridor as Difficult Terrain, reversible
- OTHALAN contract token as tactical lever during the Wight fight

---

## adventures_in_the_night.pdf

**License:** CC0 Public Domain — no restrictions.
**Setting:** Wilderness/forest one-shot, Level 1.
**Status: Integrated into Session 3**

Adapted elements:
- d10 entry 9 (Abandoned Camp): recently-vacated drover's camp, bog warning, supply cache
- d10 entry 10 (Boundary Stone): pre-Roman liminal stone, Vættir territory threshold
- Optional Location: The Old Watching Post (roofless stone chamber, sealed compartment with flask + Latin wax tablet from Vercingetorix's grandfather's failed warband)

---

## wild_sheep_chase.pdf

**License:** CC BY-NC 4.0 — free for personal/non-commercial use with attribution.
**Setting:** Single-session magic comedy adventure.
**Status: Not integrated — wrong tone**

This module is a lighthearted magical farce. Nothing in it maps to Shadow of Mars' register. Keep as reference only.

---

## Maps

For VTT battlemaps, use the Dice Grimorium maps downloaded by `../Maptool/maps/download_maps.sh`.

| Session | Room type | Recommended DG map |
|---|---|---|
| S1 | Shield Hall (Entry) | `DungeonEntrance` or `DarkTempleEntrance` |
| S1 | Flooded Gallery | `FloodedCave` |
| S1 | Bone Chamber | `AncientCryptDungeon` |
| S1 | Binding Chamber | `DarkTempleInterior` |
| S1 | Altar Chamber | `AncientAltar` |
| S1/S5 | Full vault layout | `SecretVaultDungeon` |
| S2 | Road encounter | `CrossRoads` or `RockyRoad` |
| S3 | Forest path | `ForestPath3` or `WindingForestPath` |
| S3 | Bog ritual | `Swamp2` or `ForestRitualSite` |
| S4 | Sacred grove | `SacredGrove` or `DruidCircle` |
| S4 | Fort siege | `SkeletonFortressEntrance` |
| S5 | Final vault | `SecretVaultDungeon` |
