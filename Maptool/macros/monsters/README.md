# Monster Attack Macros — Session 1

One MTScript file per creature. Each opens a dialog showing all attacks with live dice rolls.

## How to import into MapTool

1. Open MapTool and load your campaign.
2. Go to **Window > Campaign Macros** (or right-click the Campaign Macros panel).
3. Click **New Macro**.
4. In the macro editor, paste the contents of the `.mts` file.
5. Set the macro name (e.g. "Shadow Attacks") and assign a colour if you like.
6. Click **Apply**.

To run: select the creature's token on the map, then click the macro button in the Campaign Macros panel. The attack dialog opens with fresh dice rolls each click.

## Files

| File | Creature | CR | S1 Scene |
|---|---|---|---|
| `shadow_attacks.mts` | Shadow | 1/2 | Flooded Gallery (×4), Altar Chamber (×2) |
| `ghoul_attacks.mts` | Ghoul | 1 | Bone Chamber (×2) |
| `ghast_attacks.mts` | Ghast | 2 | Bone Chamber (×1) |
| `wight_attacks.mts` | Wight | 3 | Altar Chamber (×1) — vault guardian |
| `berserker_attacks.mts` | Berserker | 2 | Scene 4 exterior (×1) |
| `cultist_attacks.mts` | Cultist of Mars | 1/8 | Scene 4 exterior (×2) |
| `skeleton_attacks.mts` | Skeleton | 1/4 | General vault use |

## Encounter difficulty (5 players, Level 3)

Thresholds: Easy 375 / Medium 750 / Hard 1,125 / Deadly 2,000 adjusted XP.

| Encounter | Composition | Adjusted XP | Difficulty |
|---|---|---|---|
| Flooded Gallery | 4 Shadows | 800 | Medium |
| Bone Chamber | 2 Ghouls + 1 Ghast | 1,700 | Hard |
| Altar Chamber | 1 Wight + 2 Shadows | 1,800 | Hard (near Deadly) |
| Scene 4 | Berserker + 2 Cultists | 1,000 | Medium-Hard |

The vault is designed to feel like it costs something. The Altar Chamber at near-Deadly is intentional: by that point the party has spent resources in two prior encounters. The Wight has an exit condition (leave the spear, he lets them go), so a depleted party has a real out.

## Token sources

The `.rptok` token files for these creatures are in `Maptool/dnd5eTokens/undead/` and `Maptool/dnd5eTokens/humanoid/`. The `build_campaign_maps.sh` script copies them into each session folder automatically. These macros work with whatever token is currently selected — token name does not matter.
