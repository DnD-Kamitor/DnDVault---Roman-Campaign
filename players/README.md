# Player Character Sheets

Upload your character sheet here as a JSON file. The GM runs a script to convert it into a MapTool token with all your stats loaded automatically.

## How to submit

1. Copy `template.json` to a new file named after your character (e.g. `Gaius_Vergilius.json`)
2. Fill in every field (see field guide below)
3. Commit and push (or send the file to the GM)
4. The GM runs `python scripts/generate_player_tokens.py` — your `.rptok` token appears in `Maptool/tokens/players/`

## Field guide

| Field | What to put |
|---|---|
| `name` | Your character's full name |
| `player` | Your real name |
| `race` | Your D&D race |
| `class` | Your D&D class |
| `subclass` | Your subclass (leave blank at level 3 if not chosen) |
| `level` | Start at 3 |
| `background` | Your background |
| `role` | Your vexillatio role (see valid roles below) |
| `ability_scores` | Final scores after racial bonuses |
| `hp_max` | Maximum HP at level 3 |
| `skill_proficiencies` | List of skills you are proficient in |
| `expertise` | List of skills you have Expertise in (Rogue/Bard) |
| `saving_throw_proficiencies` | Two ability abbreviations, e.g. `["STR", "CON"]` |
| `spellcasting_ability` | `"INT"`, `"WIS"`, or `"CHA"` — leave blank if not a caster |
| `languages` | Languages your character speaks |
| `citizenship` | `"Peregrinus"`, `"Latinus"`, or `"Civis"` (most start Peregrinus) |
| `corruption_level` | Start at 0 |
| `commendationes` | Start at 0 |
| `portrait_color` | Hex color for your token portrait (any color you like) |
| `ac_override` | Set a number to override the role-calculated AC (e.g. if using class Unarmored Defense). Leave `null` to use role default. |
| `notes` | Anything extra (personality, appearance, etc.) |

## Valid role names

Use exactly one of these in the `role` field:

```
Aquilifer       Capsarius       Cornicen        Custos Armorum
Explorator      Faber           Flamen Martialis Foederatus
Frumentarius    Haruspex        Librarius        Medicus
Optio           Sacerdos        Signifer         Tesserarius
```

## AC calculation

The script calculates your AC from your role's issued armor + DEX modifier automatically:

| Armor | Base AC | DEX cap | Shield |
|---|---|---|---|
| Lorica Segmentata | 17 (flat) | — | Custos Armorum only (+2) |
| Lorica Hamata | 14 | +2 | Role-dependent |
| Lorica Squamata | 14 | +2 | Role-dependent |
| Linothorax | 12 | +3 | Never |

Set `ac_override` if your class uses a different formula (Barbarian Unarmored Defense, Monk Unarmored Defense, Mage Armor, etc.).

## Valid skills for `skill_proficiencies`

```
Acrobatics      Animal Handling  Arcana          Athletics
Deception       History          Insight         Intimidation
Investigation   Medicine         Nature          Perception
Performance     Persuasion       Religion         Sleight of Hand
Stealth         Survival
```
