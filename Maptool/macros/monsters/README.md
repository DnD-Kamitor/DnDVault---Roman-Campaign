# Monster Attack Macros — All Sessions

One MTScript file per creature. Each opens a styled HTML dialog with live dice rolls, stat reminders, and campaign-specific behaviour notes.

## How to import into MapTool

1. Open MapTool and load your campaign.
2. Go to **Window > Campaign Macros**.
3. Click **New Macro**.
4. Paste the contents of the `.mts` file into the macro editor.
5. Name it (e.g. "Shadow Attacks") and optionally assign a colour.
6. Click **Apply**.

To run: select the creature's token on the map, then click the macro button in the Campaign Macros panel. The dialog opens with fresh dice rolls each click.

---

## Session 1 — The Vault

| File | Creature | CR | Scene |
|---|---|---|---|
| `shadow_attacks.mts` | Shadow | 1/2 | Flooded Gallery (×4), Altar Chamber (×2) |
| `ghoul_attacks.mts` | Ghoul | 1 | Bone Chamber (×2) |
| `ghast_attacks.mts` | Ghast | 2 | Bone Chamber (×1) |
| `wight_attacks.mts` | Wight | 3 | Altar Chamber (×1) — vault guardian, speaks first |
| `berserker_attacks.mts` | Berserker | 2 | Scene 4 exterior (×1) |
| `cultist_attacks.mts` | Cultist of Mars | 1/8 | Scene 4 exterior (×2) — not attacking yet |
| `skeleton_attacks.mts` | Skeleton | 1/4 | General vault use |

**Encounter difficulty (5 players, Level 3):**

| Encounter | Adjusted XP | Difficulty |
|---|---|---|
| Flooded Gallery (4 Shadows) | 800 | Medium |
| Bone Chamber (2 Ghouls + 1 Ghast) | 1,700 | Hard |
| Altar Chamber (1 Wight + 2 Shadows) | 1,800 | Hard / near-Deadly |
| Scene 4 (Berserker + 2 Cultists) | 1,000 | Medium-Hard |

---

## Session 2 — The Road and the River

| File | Creature | CR | Scene |
|---|---|---|---|
| `wolf_attacks.mts` | Wolf | 1/2 | Road wildlife |
| `boar_attacks.mts` | Boar | 1/4 | Road wildlife |
| `bandit_attacks.mts` | Bandit | 1/8 | Road encounter |
| `bandit_captain_attacks.mts` | Bandit Captain | 2 | Road encounter leader |
| `gladiator_attacks.mts` | Gladiator (Vercingetorix) | 5 | Does NOT attack unless provoked |
| `veteran_attacks.mts` | Veteran (Varro) | 3 | Ally — run his attacks to keep combat moving |
| `guard_attacks.mts` | Guard / Praetorian | 1/8 | Tribune + 6 Praetorians — extremely dangerous |
| `nix_attacks.mts` | Nix | 3 | Rhine river crossing — shapechanger, starts disguised |

---

## Session 3 — The Dark Forest

| File | Creature | CR | Scene |
|---|---|---|---|
| `wolf_attacks.mts` | Wolf | 1/2 | Forest encounter |
| `dire_wolf_attacks.mts` | Dire Wolf | 1 | Forest encounter |
| `brown_bear_attacks.mts` | Brown Bear | 1 | Forest encounter |
| `giant_spider_attacks.mts` | Giant Spider | 1 | Forest encounter |
| `tribal_warrior_attacks.mts` | Tribal Warrior | 1/8 | Germanic ambush (×12) |
| `scout_attacks.mts` | Scout | 1/2 | Germanic ambush (×2) |
| `haugbui_attacks.mts` | Haugbui | 3 | Burial mound guardian — territory-bound |
| `myling_attacks.mts` | Myling | 2 | Unburied dead — wants burial, begs first |
| `vaettir_attacks.mts` | Vættir | 2 | Nature spirits — propitiable mid-combat |
| `alp_attacks.mts` | Alp | 4 | Extended rest encounter — iron at thresholds counters |
| `draugar_attacks.mts` | Draugar | 6 | Burial mound boss — Undead Fortitude, grows Large at 60 HP |
| `genius_loci_attacks.mts` | Genius Loci | 4 | Sacred grove spirit — cannot initiate, first action is Compel Respect |

---

## Session 4 — The God's Demand

| File | Creature | CR | Scene |
|---|---|---|---|
| `animated_armor_attacks.mts` | Animated Armor | 1 | Sunken Armory — divine construct, NOT undead |
| `will_o_wisp_attacks.mts` | Will-o'-Wisp | 2 | Grove spirit — optional, nearly unhittable when invisible |
| `larvae_attacks.mts` | Larvae | 5 | Principia basement — wears the face of someone the target wronged |
| `strix_attacks.mts` | Strix | 4 | Night encounter — targets light sources first |
| `lemur_attacks.mts` | Lemur | 1 | Battlefield aftermath — burial ends it; combat just delays |

---

## Session 5 — The Wrath of Mars

| File | Creature | CR | Scene |
|---|---|---|---|
| `wraith_attacks.mts` | Wraith | 5 | Final vault — creates Specters from the fallen |
| `specter_attacks.mts` | Specter | 1 | Final vault — also Wraith-created |
| `zombie_attacks.mts` | Zombie | 1/4 | Final vault |
| `stone_golem_attacks.mts` | Stone Golem (120 HP) | 10* | Animated Standing Stones — flee or bypass, not fight |
| `fausta_luperci_attacks.mts` | Fausta Luperci | ~8 | Option A: Trial of Champions — victory at 0 HP or 10 rounds |
| `mars_attacks.mts` | Mars | divine | Option B: Trial of Blades — victory at 150 HP |

*Modified: HP capped at 120. Still Deadly × 3.

---

## Token sources

Token `.rptok` files live in `Maptool/dnd5eTokens/undead/`, `/humanoid/`, and `/beast/`. The `build_campaign_maps.sh` script copies them into per-session folders. These macros work against any selected token — token name is used only for display.
