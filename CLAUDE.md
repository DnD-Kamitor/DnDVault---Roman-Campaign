# CLAUDE.md — The Shadow of Mars Campaign Workbook

## Project Overview

A Quarto book structured as a two-part D&D 5e campaign module:
- **Part 1: Player's Workbook** — spoiler-free, read by everyone at the table
- **Part 2: GM's Workbook** — DM-only content, full NPC secrets and session design

Design philosophy: **Guy Sclanders' methodology** throughout. Every design decision should pass the Sclanders checklist below.

---

## File Structure

```
index.qmd          ← Preface (how to use the book)
player_intro.qmd   ← Spoiler-free campaign overview, setting, NPCs (names/roles only)
session0.qmd       ← Session 0 questions
player_guide.qmd   ← Roman world, character creation, corruption mechanic
gm_intro.qmd       ← OGAS framework, central mystery, master plot
chapter1.qmd       ← Session 1: Blood and Omens
chapter2.qmd       ← Session 2: The Chieftain's Price
chapter3.qmd       ← Session 3: Shadows in Rome
chapter4.qmd       ← Session 4: The God's Demand
chapter5.qmd       ← Session 5: The Triumph of Mars
appendix.qmd       ← Quick reference, stat blocks, handouts
images/            ← All local image assets (downloaded from Wikimedia Commons)
```

### Image Assets (all verified HTTP 200, Wikimedia Commons)

| File | Subject | License |
|---|---|---|
| `roman_empire_125.svg` | Roman Empire map, 125 AD | Public domain |
| `limes_germanicus.jpg` | Limes Germanicus frontier map | CC BY-SA 4.0 |
| `germanic_tribes.svg` | Germanic tribes, 50 AD | Public domain |
| `castra_layout.svg` | Standard Roman fort plan | CC BY-SA 4.0 |
| `vindolanda_aerial.jpg` | Vindolanda aerial photo, 2010 | CC BY-SA 2.0 |
| `saalburg_fort.jpg` | Saalburg reconstructed fort | CC BY-SA 3.0 |
| `saalburg_plan.jpg` | Saalburg fort floor plan | CC BY 2.5 |
| `legionaries.jpg` | Roman legionaries on the march | CC BY-SA 3.0 |
| `lorica_segmentata.jpg` | Roman armour, Antonine period | CC BY-SA 3.0 |
| `hadrians_wall_map.svg` | Hadrian's Wall map with Vindolanda | CC BY-SA 3.0 |
| `strix_owl.jpg` | Athenian tetradrachm owl coin, 454–404 BC | CC BY-SA 4.0 |
| `lemures_fresco.jpg` | Pompeii Lares and Serpents fresco | CC BY 2.0 |
| `genius_loci.jpg` | Pompeii lararium serpent painting | Public domain |
| `alp_nightmare.jpg` | Fuseli, *The Nightmare*, 1781 | Public domain |
| `draugar.jpg` | Norse draugr illustration, Kim Diaz Holm | CC BY 4.0 |
| `lindworm.png` | Nidhogg Norse serpent | Public domain |
| `nix_nokken.jpg` | Kittelsen, *Nøkken*, 1887–92 | Public domain |
| `lar_bronze.jpg` | Bronze statuette of a Lar, Metropolitan Museum | CC0 |

Attribution format for CC images: `*Image: [Author], Wikimedia Commons, [License].*`

---

## Guy Sclanders Methodology Checklist

Apply these to every session chapter. Before marking a session "complete", verify each box.

### Core Systems

- [ ] **OGAS per NPC** — Every NPC appearing in the session has active Objective / Goal / Agenda / Secret
- [ ] **Strong Opening** — In media res, no preamble, visceral hook in the first 5 minutes
- [ ] **Pressure Cooker** — Time pressure + incomplete information + escalating stakes
- [ ] **Meaningful Choices** — No "correct" answer; every major decision has real consequences in later sessions
- [ ] **Three Clue Rule** — Every mystery/discovery has at least 3 independent paths to find it
- [ ] **Reactive World** — NPCs advance their OGAS between sessions whether or not the party engages them

### NPC Archetypes (from Sclanders' villain framework)
- **Blunt Force Nemesis** — Direct opposition (Legate Corvinus, Sessions 1-2)
- **Never Present Villain** — Manipulation from shadows until reveal (Senator Brutus, Sessions 1-4)
- **Divine Antagonist** — Ultimate challenge beyond mortal scale (Mars, Sessions 4-5)

### Session Structure Template
Each chapter should follow this skeleton:
1. **Read-Aloud Opening** (in media res)
2. **Scene 0: Cold Open** (hook, no choices yet)
3. **Scene 1–N: Pressure Cooker Escalation** (each scene raises stakes)
4. **Decision Point** (party makes an irreversible choice)
5. **Consequence Setup** (seeds for next session)
6. **Level Advancement note**
7. **DM Notes** (NPC states, contingencies, optional encounters)

### Escalation Arc
Sessions must escalate:
- S1: Personal → Fort-level stakes
- S2: Fort → Regional stakes
- S3: Regional → Imperial stakes
- S4: Imperial → Divine stakes
- S5: All threads resolve (divine + political + personal)

---

## Milestone Plan

### Milestone 1 — Visual Foundation ✅ COMPLETE
- [x] Download and verify 10 historical images
- [x] Create CLAUDE.md
- [x] Embed maps in player_intro.qmd (Roman Empire, Limes, Germanic tribes)
- [x] Embed images in player_guide.qmd (castra layout, Vindolanda, Saalburg, legionaries)
- [x] Fix GitHub Pages .nojekyll issue (Jekyll was eating all non-index HTML files)

### Milestone 2 — Player's Workbook: World Depth ✅ COMPLETE
Goal: Players can read Part 1 and feel fully immersed without needing the GM's sections.

- [x] **Roman daily life** — food, money (denarii/sestertii), calendar, timekeeping
- [x] **Roman Pantheon** — player-facing profiles for the 12 major gods + Mithras + Fortuna
- [x] **Equipment list** — Roman weapons and armor with D&D stat translations
- [x] **Key Latin phrases** — commands, titles, places, common speech with pronunciation
- [x] **Session 0 expansion** — setting-specific questions (Roman identity, gods, frontier, corruption, character hooks)

### Milestone 3 — Session Development (Sessions 2–5) ✅ COMPLETE
- [x] Chapter 2: cold open, Three Clue Rule, OGAS refs, props, reactive world, Vercingetorix expanded
- [x] Chapter 3: cold open, influenced-NPC mechanic, Thusnelda built, Mars divine presence, sacrifice table
- [x] Chapter 4: cold open, Rome establishing description, Three Clue Rule, Brutus argument scene, Triumph countdown
- [x] Chapter 5: continuity tracker, three trial options fully statted, Mars full stat block, consequence table, epilogue NPC table

### Milestone 4 — NPC Expansion ✅ COMPLETE
Goal: Any NPC can be improvised perfectly because their voice, knowledge, and agenda are fully documented.

- [x] **Relationship web** — ASCII faction chart showing who knows what about whom
- [x] **Per-session NPC state table** — What each NPC knows, wants, and will do across all 5 sessions
- [x] **Sample dialogue** — 3 characteristic lines per NPC showing their voice
- [x] **Reaction tables** — How each NPC responds to party's 3 most likely approaches

### Milestone 5 — Location Design
Goal: Every major location is described vividly enough to be run without prep.

- [ ] **Fort Vindolanda** — Detailed room/area descriptions keyed to castra_layout.svg
- [ ] **The Ruins Beneath** — Full 5-Room Dungeon structure
- [ ] **The Germanic Forest** — Encounter zones, tribal camp, sacred grove detailed description
- [ ] **Rome (Session 4)** — 3 key locations with sensory descriptions and social encounter frameworks
- [ ] **The Sacred Grove** — Environmental storytelling, standing stone descriptions

### Milestone 6 — Roman Tactics & D&D 5e Adaptation ✅ COMPLETE
Goal: DM can run authentic Roman military tactics as D&D mechanics.

- [x] **Testudo formation** — Group action rules, cover bonuses, movement penalties
- [x] **Wedge / cuneus** — Breakthrough mechanic for breaking shield walls
- [x] **Flanking and envelopment** — Adapted flanking rules for Roman double-envelopment
- [x] **Siege mechanics** — Battering ram, ballista, scaling ladders as structured encounters
- [x] **Germanic counter-tactics** — Guerrilla ambush, forest fighting, Varus trap scenario
- [x] **Tactical reference card** — One-page DM reference for all Roman formations in play

### Milestone 7 — Bestiary: Creatures of Roman & Germanic Myth ✅ COMPLETE
Goal: A set of original D&D 5e stat blocks for creatures native to this setting, with historical images.

- [x] **Strix** (CR 3) — Roman vampire-owl; Blood Drain, Flyby, Ill Omen
- [x] **Lemur** (CR 1/2) — Restless Roman dead; Dishonored Rest (reforms unless properly buried)
- [x] **Larvae** (CR 4) — Malevolent dead wearing the faces of the party's victims
- [x] **Genius Loci** (CR 4) — Territorial spirit of a place; propitiation mechanic
- [x] **Alp** (CR 3) — Nightmare spirit; Sleep Paralysis, Mist Form, iron weakness
- [x] **Draugar** (CR 5) — Barrow undead; Undead Fortitude, Grave Stench, Swelling Rage
- [x] **Lindworm** (CR 8) — Wingless serpentine dragon; Poison Breath, Serpentine Body
- [x] **Nix** (CR 4) — Shapeshifting river spirit; Drowning Song, Unearthly Beauty
- [x] **Images** — 8 historical illustrations from Wikimedia Commons, all verified HTTP 200
- [x] **Propitiation table** — Which creatures can be bargained with and how

### Milestone 8 — Player Assistance Tome
Goal: A dedicated, deeply immersive player-facing resource that goes beyond the player_guide — a companion that helps players *become* their Roman character before session 1.

**File:** `player_tome.qmd` (added to Player's Workbook in `_quarto.yml`)

- [ ] **Who Were You Before?** — Backstory framework: life events that make sense for a soldier on the Germanic frontier in 175 AD. Where were you born (province tables), what was your path to the legion, what do you owe and to whom?
- [ ] **How to Talk Like a Roman** — Speech patterns, honorifics, how Romans address superiors vs. inferiors vs. equals. Class-based language registers. Swearing (actual Latin). How a soldier would describe the gods, the empire, death, honor.
- [ ] **How to Think Like a Roman** — Roman worldview: fate vs. free will, duty (pietas), the significance of omens, what it means to be Roman vs. barbarian, how they understand death and the afterlife. The things your character would find *obvious* that a modern player might miss.
- [ ] **Immersion Tools** — Practical roleplaying aids: how to react to a bad omen, how to address a senator, what you do when a soldier dies, the ritual of eating together, the significance of salt. "Instinctive Roman reactions" table.
- [ ] **The Corruption Mechanic — Player Version** — How corruption *feels* at each level, not just what it does mechanically. Written from the character's perspective: what changes in how you see the world? Journal prompts for each stage.
- [ ] **Playing the Gods** — How to engage with the Roman pantheon in play. What a soldier prays for, how you make an offering, what it means when a prayer is answered, how to roleplay genuine Roman religious belief rather than D&D-generic clerics.
- [ ] **Roman Relationships** — The *amicitia* system (friendship as political currency), patron-client bonds, the cohort as family. How your character's loyalty works and who they would die for.
- [ ] **Suggested Bonds, Ideals, Flaws** — 6 of each, all campaign-specific, all tied to the Roman frontier setting. Not generic — specific to *this* campaign's themes.

### Milestone 9 — Character Knowledge Tiers
Goal: When players make History, Religion, or Nature checks, give them layered, collapsible information at DC 13/15/17. Rewards investigation without spoiling players who roll low.

**File:** `knowledge.qmd` (added to Player's Workbook in `_quarto.yml`)

Design rule: Each entry has **three tiers** using Quarto's `<details>`/`<summary>` collapsible HTML blocks.
- **DC 13 (General knowledge)** — Visible to all; what any educated Roman soldier knows
- **DC 15 (Trained knowledge)** — Collapsed by default; what an officer, priest, or scholar knows
- **DC 17 (Specialist knowledge)** — Collapsed by default; what a specialist, initiate, or expert knows

Categories:
- [ ] **Roman Military Lore** — Legionary structure, famous battles, frontier history, the Varus disaster, current Emperor's campaigns
- [ ] **Roman Religion** — The gods' domains and relationships, how augury works, the Lemuria festival, how sacrifice functions
- [ ] **The Gods (campaign-specific)** — Mars specifically: his history, his moods, what pleases and displeases him
- [ ] **Germanic Tribes** — Who the Marcomanni/Quadi/Cherusci are, famous leaders, Teutoburg Forest, how Germanic religion differs from Roman
- [ ] **The Frontier** — The Limes, how the legions hold the line, what lies beyond the Rhine/Danube, what traders report
- [ ] **Roman Law & Politics** — The Senate, the Emperor's power, how a Triumph works, how treason is prosecuted
- [ ] **Poisons & Medicine** — What a field medic knows (DC 13), what a physician knows (DC 15), what an assassin knows (DC 17)
- [ ] **Divine Signs & Omens** — How Romans read the world for divine messages; what a bad omen looks like in practice

### Milestone 10 — Professions & Downtime Activities
Goal: Characters have lives between sessions. Professions give them something to *do* and *know* in downtime that connects to the Roman world.

**File:** `professions.qmd` (added to Player's Workbook in `_quarto.yml`)

Each profession has: **Description** (what this person does in the Roman world), **Skill Uses** (which skills this profession uses regularly), **Downtime Activity** (what they can do between sessions), and **Campaign Hooks** (how this profession connects to the story).

Roman professions:
- [ ] **Legionary** — The standard soldier; training, weapon maintenance, fort construction
- [ ] **Optio / Decanus** — NCO roles; leadership, intelligence gathering, unit command
- [ ] **Medicus** — Field surgeon; herbalism, anatomy, trauma care, poisons
- [ ] **Haruspex / Augur** — Divination specialist; reading entrails, bird signs, lightning, omens
- [ ] **Scribe / Librarius** — Administrative officer; forgery, intelligence, legal knowledge
- [ ] **Faber** — Blacksmith/engineer; weapon crafting, siege equipment, fort repair
- [ ] **Mercator** — Merchant/trader; contacts, smuggling, languages, supply networks
- [ ] **Gladiator (former)** — Arena fighter; combat techniques, underworld contacts, fame
- [ ] **Sacerdos** — Priest/temple keeper; divine knowledge, access to temple networks, ritual
- [ ] **Explorator** — Scout/spy; tracking, languages, knowledge of Germanic territory

Downtime activities:
- [ ] **Earn Living** — Standard: 1d4 × profession modifier sp/day; higher professions earn more
- [ ] **Craft Item** — Roman-specific crafting (armor repair, weapon forging, potion brewing)
- [ ] **Research** — Senate archives, temple libraries, questioning informants (costs *denarii*)
- [ ] **Religious Observance** — Make offerings, complete a vow, gain divine favor (+1 on relevant rolls next session)
- [ ] **Train** — Increase a skill or learn a language (requires 250 days per rank — time skips between sessions)
- [ ] **Network** — Build *amicitia* contacts (costs social currency; opens doors later)
- [ ] **Recover** — Corruption recovery (requires specific conditions by corruption level)
- [ ] **The Collegium System** — Roman guilds: joining, dues, what membership provides, illegal collegia

### Milestone 11 — Germanic Tribes & Magic
Goal: The Germanic world feels as fully realized as the Roman one. Players and DMs understand who these people are, what they believe, and why they fight.

**File:** `germanic_tribes.qmd` (added to GM's Workbook; a player-safe summary also added to `player_guide.qmd`)

**Images:** Source from Wikimedia Commons — archaeological finds, tribal territory maps, runic inscriptions, reconstructed Germanic village, bog finds (Tollund Man type), amber artifacts.

- [ ] **The Tribes of the Campaign** — Marcomanni, Quadi, Cherusci, and Suebi: territory, leadership structure, relationship with Rome (ally/neutral/enemy), what they want
- [ ] **How Germanic Society Works** — The *comitatus* (war-band loyalty), the *Thing* (assembly), *wergild* (blood price), gift-giving as political currency — how Roman players should expect them to behave
- [ ] **Germanic Religion** — The gods of the frontier tribes (Wotan/Odin as war-god, Donar/Thor as protector, Nerthus as earth goddess); how they differ from Roman religion; what sacred sites look like
- [ ] **Tribal Shamanism (D&D mechanics)** — The *volva* (seeress/shaman) and her powers in D&D terms; seiðr as a magic tradition; rune-craft; sacrificial magic; how to build a Germanic spellcaster NPC
- [ ] **The Runes** — Elder Futhark as a living tradition: what the runes are, how they're used in divination and carving, what each major rune means for the campaign. As handouts: carved stone runes the party can find
- [ ] **Sacred Sites** — Bog sacrifices, sacred groves, the World Tree cosmology; how the party might encounter and interact with Germanic sacred places
- [ ] **Vercingetorix's Tribe (Campaign-specific)** — Detailed breakdown: village layout, named members, the tribe's relationship with Mars, what they know about the spear, why they help or oppose the party
- [ ] **Germanic Magic Items** — Rune-carved weapons (mechanical bonuses tied to specific runes), sacred amber amulets, the volva's staff, cursed bog-iron

### Milestone 12 — Handouts & Props Pack
Goal: DM can hand players physical/visual aids at the right moment.

- [ ] **Handouts 1–3 (Ch1)** — Already written; format for print layout
- [ ] **Handouts 4–5 (Ch2)** — Already written; format for print layout
- [ ] **Handouts 6–7 (Ch3)** — Already written; format for print layout
- [ ] **Handouts 8–9 (Ch4)** — Already written; format for print layout
- [ ] **Handout 10–11 (Ch5)** — Already written; format for print layout
- [ ] **Player tracking sheet** — NPCs met, decisions, corruption checkbox, session notes
- [ ] **DM quick-reference** — Single page: all NPC OGASes, corruption rules, spear properties

### Milestone 13 — Final Polish & Publish
- [ ] Continuity audit: NPC actions consistent across all sessions
- [ ] `quarto render --to pdf` produces a clean printable document
- [ ] GitHub Pages deployment verified and live

---

## Conventions

### Writing Tone
- **Player sections:** Present tense, "you" voice, no spoilers. Treat the reader as a capable adult who wants enough information to make interesting characters.
- **GM sections:** Direct and practical. Short sentences. No hedging. Trust the DM to improvise; give them the raw material, not a script.
- **Read-aloud text:** Block quote format (`>`). Slow, atmospheric. Short paragraphs. Specific sensory details. End on a decision or question, never a statement.

### Style Rules
- **No em dashes (—).** Use a colon, semicolon, or comma instead. For parenthetical phrases, use parentheses.
- **No AI attribution.** Do not reference AI tools in any content file. CLAUDE.md is internal; nothing from it appears in the rendered book.
- **Latin in italics.** All Latin words and phrases in prose are italicised on first use per page.
- **Active voice.** Passive constructions slow down practical reference writing.

### Images
- Store all images in `images/` directory
- Embed with Quarto figure syntax: `![Caption.](images/file.ext){width=90% fig-align="center"}`
- Always include `fig-alt` for accessibility
- Attribution line immediately below each figure in italics

### Session Chapter Structure
See the Session Structure Template in the Sclanders checklist above. Chapter 1 is the reference implementation — match its format.

### Commit Conventions
One milestone or major feature per commit. Commit message format:
```
[Milestone N] Short description of what was built

- Bullet list of changes
```
