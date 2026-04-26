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
player_tome.qmd    ← Deep immersion guide: how to think, talk, and act like a Roman
knowledge.qmd      ← DC 13/15/17 knowledge tiers for History, Religion, Nature checks
professions.qmd    ← Roman professions and downtime activities
roman_tactics.qmd  ← Roman military formations as D&D mechanics
bestiary.qmd       ← D&D 5e stat blocks for Roman and Germanic creatures
gm_intro.qmd       ← OGAS framework, central mystery, master plot
germanic_tribes.qmd ← Germanic tribes, society, runes, seiðr, and magic (GM)
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
| `strix_owl.jpg` | Athenian tetradrachm owl coin, 454-404 BC | CC BY-SA 4.0 |
| `lemures_fresco.jpg` | Pompeii Lares and Serpents fresco | CC BY 2.0 |
| `genius_loci.jpg` | Pompeii lararium serpent painting | Public domain |
| `alp_nightmare.jpg` | Fuseli, *The Nightmare*, 1781 | Public domain |
| `draugar.jpg` | Norse draugr illustration, Kim Diaz Holm | CC BY 4.0 |
| `lindworm.png` | Nidhogg Norse serpent | Public domain |
| `nix_nokken.jpg` | Kittelsen, *Nokken*, 1887-92 | Public domain |
| `lar_bronze.jpg` | Bronze statuette of a Lar, Metropolitan Museum | CC0 |
| `kylver_runestone.jpg` | Kylver Runestone, Elder Futhark inscription | Public domain |
| `tollund_man.jpg` | Tollund Man, bog mummy, 400 BC | CC BY-SA 2.0 DK |
| `germanic_longhouse.jpg` | Reconstructed Germanic longhouse | CC BY-SA 3.0 |
| `vendel_helmet.jpg` | Vendel period helmet, 6th-7th century | Public domain |
| `amber_figurine.jpg` | Bronze Age amber figurine | CC BY-SA 2.5 DK |
| `odin_sacrifice.svg` | Odin at Yggdrasil, Lorenz Frolich | Public domain |
| `yggdrasil.jpg` | Yggdrasil, Norse World Tree | Public domain |

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
3. **Scene 1-N: Pressure Cooker Escalation** (each scene raises stakes)
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

### Milestone 3 — Session Development (Sessions 2-5) ✅ COMPLETE
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

### Milestone 5 — Location Design ✅ COMPLETE
Goal: Every major location is described vividly enough to be run without prep.

- [x] **Fort Vindolanda** — Detailed room/area descriptions keyed to castra_layout.svg
- [x] **The Ruins Beneath** — Full 5-Room Dungeon structure
- [x] **The Germanic Forest** — Encounter zones, tribal camp, sacred grove detailed description
- [x] **Vindolanda Under Siege (Session 4)** — Arc redesigned to stay at fort; siege locations, tunnel scenes, antechamber fully detailed in locations.qmd
- [x] **The Sacred Grove** — Environmental storytelling, standing stone descriptions

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

### Milestone 8 — Player Assistance Tome ✅ COMPLETE
Goal: A dedicated, deeply immersive player-facing resource that goes beyond the player_guide. A companion that helps players *become* their Roman character before session 1.

**File:** `player_tome.qmd`

- [x] **Who Were You Before?** — Backstory framework: province tables, path to the legion, obligations
- [x] **How to Talk Like a Roman** — Speech patterns, honorifics, address registers, swearing in Latin
- [x] **How to Think Like a Roman** — Fate vs. free will, pietas, omens, death, what Romans find obvious
- [x] **Immersion Tools** — Instinctive Roman reactions table, social rituals, salt, salutatio, vows
- [x] **The Corruption Mechanic — Player Version** — How corruption feels at each level; journal prompts per stage
- [x] **Playing the Gods** — How to pray, make offerings, roleplay genuine Roman religious belief
- [x] **Roman Relationships** — Amicitia system, patron-client bonds, cohort as family, loyalty table
- [x] **Suggested Bonds, Ideals, Flaws** — 6 of each, all campaign-specific

### Milestone 9 — Character Knowledge Tiers ✅ COMPLETE
Goal: When players make History, Religion, or Nature checks, give them layered, collapsible information at DC 13/15/17.

**File:** `knowledge.qmd`

Design rule: Three tiers using HTML `<details>`/`<summary>` collapsible blocks per entry.

- [x] **Roman Military Lore** — Legionary structure, famous battles, frontier history, Varus disaster
- [x] **Roman Religion** — Gods' domains, augury, the Lemuria festival, how sacrifice functions
- [x] **The Gods (campaign-specific)** — Mars: history, moods, what pleases and displeases him
- [x] **Germanic Tribes** — Marcomanni/Quadi/Cherusci, Teutoburg Forest, Germanic religion
- [x] **The Frontier** — The Limes, how the legions hold the line, what traders report
- [x] **Roman Law & Politics** — The Senate, the Emperor's power, Triumphs, treason prosecution
- [x] **Poisons & Medicine** — Field medic knowledge (DC 13), physician (DC 15), assassin (DC 17)
- [x] **Divine Signs & Omens** — How Romans read the world for divine messages; bad omens in practice

### Milestone 10 — Professions & Downtime Activities ✅ COMPLETE
Goal: Characters have lives between sessions. Professions give them something to do and know in downtime.

**File:** `professions.qmd`

- [x] **Legionary** — The standard soldier; training, weapon maintenance, fort construction
- [x] **Optio / Decanus** — NCO roles; leadership, intelligence gathering, unit command
- [x] **Medicus** — Field surgeon; herbalism, anatomy, trauma care, poisons
- [x] **Haruspex / Augur** — Divination specialist; reading entrails, bird signs, lightning, omens
- [x] **Scribe / Librarius** — Administrative officer; forgery, intelligence, legal knowledge
- [x] **Faber** — Blacksmith/engineer; weapon crafting, siege equipment, fort repair
- [x] **Mercator** — Merchant/trader; contacts, smuggling, languages, supply networks
- [x] **Gladiator (former)** — Arena fighter; combat techniques, underworld contacts, fame
- [x] **Sacerdos** — Priest/temple keeper; divine knowledge, temple networks, ritual
- [x] **Explorator** — Scout/spy; tracking, languages, knowledge of Germanic territory
- [x] **Downtime activities** — Earn Living, Craft Item, Research, Religious Observance, Train, Network, Recover
- [x] **The Collegium System** — Roman guilds: joining, dues, benefits, illegal collegia

### Milestone 11 — Germanic Tribes & Magic ✅ COMPLETE
Goal: The Germanic world feels as fully realized as the Roman one.

**File:** `germanic_tribes.qmd` (GM's Workbook)

- [x] **The Tribes of the Campaign** — Marcomanni, Quadi, Cherusci, Suebi: territory, leadership, relationship with Rome
- [x] **How Germanic Society Works** — Comitatus, Thing, wergild, gift-giving as political currency
- [x] **Germanic Religion** — Wotan, Donar, Nerthus; sacred sites; how Germanic faith differs from Roman
- [x] **Tribal Shamanism (D&D mechanics)** — Volva stat block (CR 5), seiðr as a magic tradition, sacrificial magic
- [x] **The Runes** — Full 24-rune Elder Futhark table with D&D mechanical effects per rune
- [x] **Sacred Sites** — Bog sacrifices, sacred groves, World Tree cosmology, interaction mechanics
- [x] **Vercingetorix's Tribe** — Village layout, named NPCs, relationship with Mars, spear knowledge
- [x] **Germanic Magic Items** — 4 items: rune-carved weapons, sacred amber amulets, volva's staff, cursed bog-iron
- [x] **Images** — 7 images: Kylver Runestone, Tollund Man, Germanic longhouse, Vendel helmet, amber figurine, Odin sacrifice, Yggdrasil

### Milestone 12 — Handouts & Props Pack ✅ COMPLETE
Goal: DM can hand players physical/visual aids at the right moment.

- [x] **Handouts 1-3 (Ch1)** — Print-ready in appendix.qmd with handout-card CSS blocks
- [x] **Handouts 4-5 (Ch2)** — Print-ready in appendix.qmd with handout-card CSS blocks
- [x] **Handouts 6-7 (Ch3)** — Print-ready in appendix.qmd with handout-card CSS blocks
- [x] **Handouts 8-9 (Ch4)** — Print-ready in appendix.qmd with handout-card CSS blocks
- [x] **Handout 10-11 (Ch5)** — Print-ready in appendix.qmd with handout-card CSS blocks
- [x] **Player tracking sheet** — NPCs met, decisions, corruption checkbox, session notes
- [x] **DM quick-reference** — Single page: all NPC OGASes, corruption rules, spear properties

### Milestone 13 — Final Polish & Publish ✅ COMPLETE
- [x] Continuity audit: NPC actions consistent across all sessions
- [ ] `quarto render --to pdf` produces a clean printable document
- [ ] GitHub Pages deployment verified and live

---

## New Milestones: Player Experience & Worldbuilding Depth

The following milestones deepen what players experience at the table: richer daily life, a grounded sense of Roman time, Rome as a living city, structured tools for tracking their story, and the historical world that surrounds the campaign.

### Milestone 14 — The Roman Calendar & Sacred Year ✅ COMPLETE
Goal: Players understand Roman time. Sessions reference the calendar naturally, and players know which festivals are relevant, which gods are ascendant, and what the rhythm of Roman life sounds like.

**File:** New section in `player_guide.qmd` OR standalone `calendar.qmd` (decide at build time based on length)

- [x] **Roman calendar mechanics** — How to give a date: Kalends, Nones, Ides; AUC dating vs. consul-year dating; how soldiers would actually say "it is the third day before the Ides of July"
- [x] **The campaign window (April-October 175 AD)** — Which festivals fall within the five sessions; how the DM can anchor events to real festival dates
- [x] **Mars-specific festivals** — *Quinquatria* (March 19-23): Mars' main festival, games and weapon-blessing; *Armilustrium* (October 19): purification of weapons, end of the military season; *Tubilustrium* (March 23): trumpet purification, start of campaign season
- [x] **Other relevant festivals** — *Lemuria* (May 9, 11, 13): appeasing the restless dead (connects to Lemur creature entry); *Parentalia* (February 13-21): ancestor veneration; *Saturnalia* (December): what soldiers on the frontier do when it comes
- [x] **Festival gameplay mechanics** — What a character gains from observing a festival properly; what bad things happen if a sacred day is desecrated; how the DM uses festival timing as a story clock
- [x] **The Roman day** — How they divide daylight into hours, what the watches of the night are called, what soldiers say when they mean "dawn" or "midnight"
- [x] **Historical events timeline (150-180 AD)** — A one-page player-safe timeline: Marcomannic Wars, the Antonine Plague, Marcus Aurelius' accession, the Danube campaigns; what common soldiers know vs. what is rumor

### Milestone 15 — Life at the Frontier: Sensory Atlas ✅ COMPLETE
Goal: Players can close their eyes and *be* at Vindolanda. They describe their surroundings without GM prompting because they know what the place smells like, sounds like, and costs.

**File:** New section added to `player_tome.qmd`

- [x] **A day in the life** — Hour-by-hour schedule of a legionary at a Germanic frontier fort: before-dawn watch, morning *exercitatio*, midday rations, afternoon duties, evening at the *thermopolium*, night watch; what each part of the day feels like physically
- [x] **Food and drink** — What soldiers actually eat: *bucellatum* (hard tack), *posca* (vinegar-water), *puls* (porridge), salt fish, olives, local game; what constitutes a good day's food vs. a bad one; what men complain about; what they pay for luxuries from traders
- [x] **The senses of Vindolanda** — Specific sensory details: smell of the latrines, the sound of the gate changing at the third watch, the weight of armour in summer heat, the cold of a Germanic January, the noise of a contubernium (8-man tent unit) at dinner
- [x] **Weather and seasons on the frontier** — Embedded in the sensory atlas and food/drink sections of player_tome.qmd
- [x] **Entertainment and social life** — Dice games (*tesserae*), gambling debts, gossip, who is popular and who is hated in the barracks, how men deal with boredom between campaigns; the role of the fort tavern (*taberna*) and bathhouse (*balneum*)
- [x] **Death on the frontier** — What happens when a soldier dies: how the body is prepared, who writes to the family, what the unit does collectively; funeral rites for Romans vs. what a soldier buried on the frontier gets; the emotional reality of watching your tent-mate buried far from home

### Milestone 16 — Fort Vindolanda: Player Guide ✅ COMPLETE
Goal: Because the campaign never leaves Vindolanda and its immediate surroundings, players need a visceral, practical guide to the fort: how it looks, how it runs, and how to survive the siege.

**File:** `vindolanda_guide.qmd` (Player's Workbook, before Session 3)

- [x] **First impressions** — Rain, stone, watchtower smoke, and trumpet calls that define daily life inside the fort walls.
- [x] **The fort's layout** — *Principia*, *praetorium*, barracks, *fabrica*, *vicus*, bathhouse, sacred spaces, and the hidden stair under the headquarters.
- [x] **Social rules at the fort** — Chain of command, the quartermaster's ledger, watch passwords, the vicus compact, and how oaths function when Mars is watching.
- [x] **Prices and supply realities** — What food, bribes, or favors cost inside the walls now that the fort is cut off; how to trade reputation instead of coin.
- [x] **Key locations** — North gate, watchtower loft, granary, bath furnace room, vicus shrine, hidden stair; what each offers players in play.
- [x] **Dangers unique to Vindolanda** — Siege exhaustion, saboteurs, weather, vicus patrols, and the ruins beneath.

### Milestone 17 — Campaign Journal & Decision Tracker ✅ COMPLETE
Goal: Players have a structured, beautiful one-page tool for each session that helps them track their own story arc, their relationships, and their corruption state.

**File:** `journal.qmd` (added to Player's Workbook, positioned last)

- [x] **Session journal template (x5)** — One structured page per session: date (in-world and real), opening situation, decisions made (with space for "what I chose" and "why"), NPCs encountered, corruption level at end, divine standing (favored/neutral/cursed by which god), one sentence about where my character ends the session emotionally
- [x] **Relationship web** — A blank diagram with NPC names pre-filled (major NPCs only); players mark trust level and what they owe each NPC or are owed
- [x] **Corruption tracker** — Levels 0-5 laid out visually with experiential descriptions from `player_tome.qmd`; a checkbox per level; space to note what triggered the change
- [x] **The Open Questions list** — Space for players to note things they do not understand yet, clues they have not followed up, and mysteries they want to pursue; this prevents "we forgot about that" between sessions
- [x] **End-of-campaign reflection** — One page of prompts for each character after Session 5: what did your character become? What do they regret? What did they protect? What did they lose? What do they believe now that they did not believe at the start?
- [x] **Print-ready formatting** — The journal is designed to be printed, folded, and used physically at the table; minimal color use; space for handwriting

### Milestone 18 — Expanded Corruption System (Player-Facing) ✅ COMPLETE
Goal: Corruption is the campaign's central mechanical spine. It deserves a full player-facing chapter, not just a brief mention in player_guide.qmd.

**File:** New dedicated `corruption.qmd` (Player's Workbook), replacing the brief corruption section currently in player_guide.qmd

- [x] **What corruption is (player version)** — Written entirely from the character's perspective, no mechanical language in the opening; what it feels like to want something too much, to serve a god who is not entirely good, to notice the world bending toward you
- [x] **The six stages in depth** — Each stage (0-5) gets a full page: the physical signs (what others notice), the psychological shift (what the character now finds normal that once horrified them), the mechanical effect (what changes in D&D terms), and a journal prompt to roleplay the transition
- [x] **Corruption and the gods** — How each major god responds to a character's corruption level; which gods become interested at higher levels; what it means that Mars *wants* players to corrupt
- [x] **Resisting corruption** — What works, what does not, what is too late; the difference between characters who resist together vs. those who resist alone; how the party's collective corruption level shifts the campaign's ending
- [x] **Corruption as story, not punishment** — A direct address to players: corruption is a story tool, not a failure state; the most interesting session 5 choices come from characters who are corrupted but still trying; how to play a level-4 corrupted character at the table without being disruptive
- [x] **Corruption recovery rules** — Specific, concrete conditions for reducing corruption at each level; which professions or downtime activities help; what gods can help and what they ask in return; the hard cap (level 5 is permanent without divine intervention)

### Milestone 19 — Languages of the Roman World (D&D Translation) ✅ COMPLETE
Goal: Every language a character might speak maps cleanly to a D&D 5e language. Players pick languages from the character creation tables in the PHB and know exactly what that means at this table.

**File:** New section added to `player_guide.qmd` (under Character Creation) or `session0.qmd` (under Before You Build)

- [x] **The translation table** — A clear two-column table: Real-World Language → D&D Equivalent, with a note on who speaks it and where it matters in the campaign (in player_guide.qmd)
- [x] **Language tiers by background** — Which languages a soldier from each province realistically knows; which cost a language slot vs. which are free from background; a note that Greek is the campaign's "second language of power" and worth taking
- [x] **Languages in play** — When it matters: German-speaking NPCs who will not speak Latin until trust is earned; Greek texts in the temple archives; a Latin document the party finds in Germanic territory that raises questions; what happens when no one speaks a language
- [x] **Learning a new language** — Which downtime activity covers it; how many sessions it realistically takes; which NPCs can teach which languages (connects to Professions chapter)
- [x] **Secret and sacred languages** — Runic (can be learned as a scholar language, different from casting with runes); the priestly language of the Druids (connects to Milestone 11 Germanic content); what the volva's ritual speech sounds like to someone who does not know it

### Milestone 21 — Chapter 1: Blood and Omens (Improvement Pass)
Goal: Every scene in Chapter 1 is runnable without the DM reading anything twice. The ruins feel ancient and hostile, not like a list of features.

**File:** `chapter1.qmd`

- [x] **Underground chamber read-alouds** — Full atmospheric read-aloud text for all three chambers (Hall of Shields, Chamber of Chains, The Vault); currently bare bullet lists with no sensory language
- [x] **The Spear reveal** — A dedicated read-aloud moment when the party first sees the spear on its altar; the current text has no such moment
- [x] **NPC OGAS table** — Corvinus, Cassia, and Varro each need Objective / Goal / Agenda / Secret (like chapters 2-5); currently missing entirely from Chapter 1
- [x] **Fix: Germanic runes** — Handout 2 calls the inscription "Gaulish/Celtic"; this is inconsistent with germanic_tribes.qmd which uses Elder Futhark for all in-world runic content; change to Germanic with an Elder Futhark reference
- [x] **Scene 4 expansion** — The mad worker encounter is two bullet points; add read-aloud for his appearance, dialogue lines, and a resolution table (subdue, kill, or the worker breaks free and flees into the night)
- [x] **Refusal contingency table** — What if the party refuses the Legate's mission? Currently nothing; add a small decision table with 3 outcomes and consequences

### Milestone 22 — Chapter 2: The Tribune's Gambit (Improvement Pass)
Goal: The dead sentry becomes a resolved mystery, not a dropped thread. Vercingetorix gets the depth he deserves. All five session endings have explicit Session 3 seeds.

**File:** `chapter2.qmd`

- [x] **Resolve the Sextus murder** — Who killed the sentry? Currently introduced and forgotten; add a Three Clue Rule mini-mystery (answer: Brutus' sleeper agent in the fort, who also carved "ROMA CADIT" and then left with the Tribune's party)
- [x] **Vercingetorix knowledge table** — What he specifically knows about the spear's history, where the sacred grove is, and what the destruction ritual requires; DM notes say he "knows more than any Roman" but never list what he knows
- [x] **Expanded Vercingetorix dialogue** — 3 more sample lines beyond the battle scene; he needs a distinct voice across the whole session
- [x] **Session 2 → Session 3 transition table** — Five distinct Session 2 endings (exposed Tribune / fought Praetorians / negotiated / fled with Vercingetorix / surrendered), each with an explicit Session 3 opening position
- [x] **Varro contingency** — What happens to the party's position if Varro dies during the raid? He's load-bearing for the session's resolution; need a fallback

### Milestone 23 — Chapter 3: Through the Dark Forest (Improvement Pass)
Goal: The two-day forest journey feels like a journey, not a teleport to the next scene. The sacrifice mechanic has enough DM guidance to land every time.

**File:** `chapter3.qmd`

- [x] **Forest travel events table** — A d8 table of events during the two-day journey (omens, encounters, spear manifestations, NPC moments); currently the forest travel has no mechanical content between leaving the fort and arriving at Thusnelda's scouts
- [x] **Thusnelda expanded** — 4 more sample lines and a "what she will and will not say" table; she is the most important new NPC in the session and needs more voice
- [x] **Sacrifice mechanic DM guidance** — "The grove knows" is correct but needs clearer DM instruction: what signs indicate the grove accepted or rejected the sacrifice? How does Thusnelda react to each offer? What if no one is willing to offer anything real?
- [x] **Post-ritual NPC states** — A table showing where each NPC stands emotionally and practically after the spear is destroyed (or after failure); needed for Session 4 handoff
- [x] **Influenced NPC roleplay expansion** — The private note is good; add 3 specific things the influenced player should do or say during Scenes 1-3 that feel natural but are later recognisable in hindsight

### Milestone 24 — Chapter 4: The God's Demand (Improvement Pass)
Goal: Vindolanda's siege and the ritual escort feel like a pressure cooker. Mars' demand is clear, the sabotage plot is concrete, and every faction's OGAS shows in play.

**File:** `chapter4.qmd`

- [x] **Siege read-aloud** — Opening text that captures smoke, rain, trumpets, and Mars' bell (done). Ensure each crisis has mechanics (breach, granary, shrine) with clear stakes.
- [x] **Council stakes** — Flesh out the politics inside the *principia*: what Corvinus, Lucius, Varro, Cassia, and Vercingetorix each want from the escort.
- [x] **Procession prep table** — Concrete options the party can take before descending (scout stair, calm vicus, call favors) with consequences for failure.
- [x] **Tunnel scenes** — Three distinct hazards that escalate tension and foreshadow Mars' arrival.
- [x] **Antechamber demand** — Clarify the requirement for three kneeling witnesses and how that affects Session 5.

### Milestone 25 — Chapter 5: The Wrath of Mars (Improvement Pass)
Goal: Option C (the argument) gets the depth it deserves. Corruption level 5 is fully mechanised. Every ending has its own emotional beat set atop the fort's parade ground.

**File:** `chapter5.qmd`

- [x] **Corruption level 5 in the arena** — Define how Mars manipulates a corrupted PC in each option and how redemption works.
- [x] **Option C expanded** — Three arguments that move Mars, three that anger him, plus the failure recovery path (demonstration DC 14) and visual cues that show when he is persuaded.
- [x] **Post-trial narration** — Distinct read-alouds for Option A (champion falls) and Option B (Mars calls the fight at 150 HP).
- [x] **Mars up close** — Provide the read-aloud for when he rises from the throne and walks across the black sand.
- [x] **Call to War mechanic** — Table of future calls and what happens if the Chosen refuse.
- [x] **Epilogue NPC prompts** — Two example questions or answers per major NPC to make the epilogue conversational instead of a list.

### Milestone 20 — Expanded "What Your Character Knows" (knowledge.qmd Overhaul) ✅ COMPLETE
Goal: The knowledge chapter currently goes straight to ability checks. Add a layer of baseline knowledge visible to every player before the collapsible DC sections. Every entry should have three layers: (1) common knowledge no roll needed, (2) DC 13/15 trained knowledge, (3) DC 17 specialist knowledge.

**File:** `knowledge.qmd` (overhaul of existing file)

- [x] **Add "What every soldier knows" preamble to each category** — A short paragraph (3-5 sentences) of baseline facts that require no roll; what any Roman on the frontier in 175 AD simply knows as common knowledge; visible without expanding any collapsible section
- [x] **Roman Military Lore** — Add general knowledge preamble: the five campaign legions, why Teutoburg is still talked about 160 years later, what soldiers say about the Marcomanni; then DC 13/15/17 tiers below
- [x] **Roman Religion** — Add general knowledge preamble: the Capitoline Triad, why you must never swear a false oath to Jupiter, how sacrifice actually works at a fort altar; then DC tiers
- [x] **The Gods (campaign-specific)** — Add general knowledge preamble: what every soldier knows about Mars before the campaign starts; what Mars' cult at the frontier is like vs. in Rome; then DC tiers
- [x] **Germanic Tribes** — Add general knowledge preamble: what Roman soldiers say about the Germans (mostly wrong, some right), the Teutoburg disaster as cautionary tale, what the Marcomanni want; then DC tiers
- [x] **The Frontier** — Add general knowledge preamble: what the Limes looks like day to day, what traders bring across, what happens to soldiers who cross without orders; then DC tiers
- [x] **Roman Law & Politics** — Add general knowledge preamble: what a legionary actually knows about the Senate and the Emperor (less than he thinks), how a Triumph is declared, what treason means; then DC tiers
- [x] **Poisons & Medicine** — Add general knowledge preamble: what soldiers know about field injuries, wound fever, and the basic herbal kit; then DC tiers for more dangerous knowledge
- [x] **Divine Signs & Omens** — Add general knowledge preamble: the three signs every Roman soldier watches for, what to do when lightning strikes near camp, why a crow on the left is worse than a crow on the right; then DC tiers
- [x] **Two new categories** — Added: (1) *The Antonine Plague*; (2) *Roman Engineering* (both with preamble + DC tiers, in knowledge.qmd)
- [x] **Visual design pass** — Instructional note added at top of knowledge.qmd explaining the three-layer system

### Milestone 26 — The Peoples of the Empire: D&D Races as Roman World Cultures ✅ COMPLETE
Goal: Every D&D 5e race maps to a specific real-world culture within or adjacent to the Roman Empire in 175 AD. Players pick a race and immediately understand who that people are, where they come from, and how Rome sees them.

**File:** `peoples.qmd` (Player's Workbook, after `player_guide.qmd`)

- [x] **Human** — All provincial subraces documented in peoples.qmd
- [x] **Elf** — Greeks and Hellenized Easterners fully documented
- [x] **Dwarf** — Germanic and Dacian mountain peoples fully documented
- [x] **Halfling** — Phoenician, Syrian, and Nabataean traders fully documented
- [x] **Gnome** — Egyptians and Alexandrians fully documented
- [x] **Half-Elf** — Peoples of mixed Roman/Greek heritage fully documented
- [x] **Half-Orc** — Germanic *foederati* warriors fully documented
- [x] **Tiefling** — Carthaginian-heritage peoples fully documented
- [x] **Dragonborn** — Parthians and Persians fully documented
- [x] **Aasimar** — Roman noble families claiming divine descent fully documented
- [x] **For each race:** Legal classification, native language, military roles, and 2 character hooks included

### Milestone 27 — Legal Status and Social Standing in the Empire ✅ COMPLETE
Goal: A character's race and origin determines their legal and social standing in Rome. This is not a punishment mechanic: it is the texture of the world. Some doors are open; others require keys; a few are locked for good reasons that the campaign can challenge.

**File:** Section added to `peoples.qmd` (building on Milestone 26)

- [x] **The five legal categories** — *Cives Romani*, *Latini*, *Peregrini*, *Liberti*, *Dediticii*; all documented with race mappings in peoples.qmd
- [x] **Rank ceilings by status** — Citizens, Latini, Peregrini, Dediticii rank limits documented
- [x] **How status affects character creation** — Table of race + status → backgrounds, equipment, and proficiencies
- [x] **Status and the campaign's themes** — Corruption/status interaction documented
- [x] **Gaining and losing status** — Military service path upward, citizenship grants, and status loss mechanics documented

### Milestone 28 — Regional Supply, Equipment, and the Fort Economy ✅ COMPLETE
Goal: The Roman world is radically localized. What you can buy depends entirely on where you are. Fort Vindolanda has a finite stock that replenishes on irregular cycles. Players should feel the material reality of a frontier posting.

**File:** `supplies.qmd` (Player's Workbook) and DM supplement section added to `locations.qmd`

- [x] **Price index by region** — Rome vs. Vindolanda vs. Germanic forest price table in supplies.qmd
- [x] **Fort Vindolanda's current stock** — Quartermaster inventory, skill-gated access, full categories documented
- [x] **The supply cycle** — Convoy mechanics, wagon arrival frequency, what it carries, player influence options
- [x] **Supply missions as adventure hooks** — Per-session hooks (S1-S5) for supply pressure scenarios
- [x] **Equipment degradation and repair** — Degradation mechanics and Faber repair rules documented
- [x] **Exotic goods and what they mean** — Eastern spices, Alexandrian glass, amber, Parthian silk with social context

### Milestone 29 — Food, Drink, and Rationing ✅ COMPLETE
Goal: A dedicated player chapter grounding the campaign in the material reality of eating and drinking in the Roman world. Players should feel the pleasure of good food after hardship and the grinding reality of field rations.

**File:** `food.qmd` (Player's Workbook) -- note: sensory food content from player_tome.qmd can be cross-referenced but this chapter goes deeper with mechanics

- [x] **The daily ration (baseline)** — Exact quantities, costs, field preparation methods documented in food.qmd
- [x] **Food quality tiers** — Four tiers (Starvation/Field/Good/Feast) with mechanical effects documented
- [x] **Germanic frontier food** — Hunting, foraging, and trader options for frontier supplement documented
- [x] **Drink in depth** — *Posca*, *cervisia*, wine, mead, spring water with intoxication and social effects
- [x] **Rationing as story** — 3 rationing scenarios with morale, hierarchy, and leadership stakes documented
- [x] **Equipment for eating and cooking** — Full Roman kit inventory with weight and pack-load rules documented

### Milestone 30 — The Legion and the Magical World ✅ COMPLETE
Goal: The Roman legion is one of the most sophisticated military machines in history. It should also be sophisticated about the existence of magic and magical creatures, because in this world those things are real and the army has had 700 years to develop doctrine for dealing with them.

**Files:** New section in `roman_tactics.qmd` (Player's Workbook); DM supplement section added to `gm_intro.qmd`

- [x] **Official Roman magical doctrine** — Three categories (*Res Divinae*, *Magia Licita*, *Magia Illicita*) documented in roman_tactics.qmd
- [x] **The *haruspex* in the field** — Full D&D mechanics: Augury 1/day, creature ID, Blessed Standard, death consequence
- [x] **Anti-magical formation doctrine** — Anti-flying, anti-undead, anti-illusion doctrine responses documented
- [x] **Creature classification in Roman military records** — Full bestiary cross-referenced with Roman classification system
- [x] **The *Spolia Opima* for magical kills** — *Bestiae Victor* title, commendation, denarii reward, Intimidation advantage documented
- [x] **Magical creature encounters in each session** — DM notes per session for optional creature encounters

### Milestone 31 — Lex Arcana Integration ✅ COMPLETE
Goal: Borrow the best systems from the *Lex Arcana* tabletop RPG (an Italian RPG set in an alternate Roman Empire where Rome never fell). Adapt its investigative structure, custodian role, and virtue mechanics into this campaign's D&D 5e framework.

**File:** New section in `gm_intro.qmd`; player-facing summary in `player_guide.qmd`

- [x] **The Custodes concept** — *Exploratores Extraordinarii* designation adapted and documented in gm_intro.qmd
- [x] **Roman virtues as character mechanics** — Seven virtues as once-per-session advantage triggers with atonement mechanic
- [x] **Augury as structured mini-game** — DC 13/15/17 Religion mini-game with *auspicia turbata* failure state
- [x] **Investigation structure** — *Investigatio / Deliberatio / Actio* phases integrated into chapters 2-4
- [x] **Destiny mechanics** — *Fatum* system integrated with session0.qmd and epilogue mechanics in chapter5.qmd

### Milestone 32 — Session 0: Character Creation Guide (Rewrite) ✅ COMPLETE
Goal: Session 0 currently gives players too much influence over the campaign's pre-set structure. Rewrite it as a character creation guide that asks meaningful personal questions (who are you, what do you fear, what do you love) without inviting players to co-design plot.

**File:** `session0.qmd` (full rewrite)

- [x] **Opening framing** — Character-focused framing (not plot co-design) in place at top of session0.qmd
- [x] **Character concept questions (replace plot questions)** — Personal-history questions replacing plot-building questions
- [x] **Relationship web (replace "how do you know each other")** — *Contubernium* shared events framework replacing "how did you meet"
- [x] **The three questions** — Three questions (prove/fear/protect) documented and linked to Fatum and Session 3 sacrifice
- [x] **Remove:** Collaborative setting/tone/enemy design choices removed; campaign-is-fixed framing established

### Milestone 33 — Atmosphere: Music and Sound Per Session ✅ COMPLETE
Goal: Each session has a recommended soundtrack and ambient sound layer. The DM can open these before the session and let them run.

**File:** Section added to each session chapter's Pre-Session Preparation section; also a standalone `atmosphere.qmd` in Player's Workbook (ambient sounds only, not DM-specific)

- [x] **Session 1 (Blood and Omens):** Ambient layers and music recommendations documented in atmosphere.qmd and chapter1.qmd Pre-Session Preparation
- [x] **Session 2 (The Tribune's Gambit):** Wardruna / Jóhann Jóhannsson recommendations documented
- [x] **Session 3 (Through the Dark Forest):** Heilung *Ofnir* recommendations documented; grove silence treatment documented
- [x] **Session 4 (The God's Demand):** Vindolanda siege soundscape recommendations documented (arc redesigned from Rome to fort)
- [x] **Session 5 (The Wrath of Mars):** Arena silence, divine presence sub-bass, Wardruna "Helvegen" epilogue documented
- [x] **Player-facing version** — atmosphere.qmd provides player ambient sound guide framed as worldbuilding

### Milestone 34 — Quarto Character Sheets
Goal: A printable, fillable D&D 5e character sheet adapted for this campaign, rendered as a PDF via Quarto's LaTeX pipeline. Designed to be printed, physically filled in, and used at the table.

**File:** `character_sheet.qmd` (standalone, separate from the main book) + `_character_sheet.scss` for styling

- [x] **Research the Quarto PDF approach** — Implemented in character_sheet.qmd using Quarto PDF pipeline
- [x] **Campaign-specific fields** — Province of Origin, Legion and Rank, Corruption Track (0-5), Divine Standing, Fatum all present
- [x] **Roman aesthetic** — Latin/English field labels, Roman border treatment, column layout implemented
- [x] **Second page: Session tracker** — Five-session tracker with decisions, NPCs, corruption delta, divine standing documented
- [ ] **Build and render test** — Pending: confirm `quarto render character_sheet.qmd --to pdf` produces clean output

### Milestone 35 — Three-Barrier Knowledge + Living Camp Economy ✅ COMPLETE
Goal: The knowledge system gains a third barrier (character-creation stat/skill gating before DC checks). Fort Vindolanda becomes a living economy with named traders who upgrade based on player actions and reputation.

**Files:**
- `reputation.qmd` (new, Player's Workbook, after `professions.qmd`)
- `camp_economy.qmd` (new, GM's Workbook, after `locations.qmd`)
- `knowledge.qmd` (modified: Barrier One blocks in all 10 categories)
- `appendix.qmd` (modified: relationship tracking table in DM Quick Reference)
- `_quarto.yml` (modified: both new files inserted)

**Barrier One blocks (knowledge.qmd):**
- [x] Roman Military Lore: History proficiency + Athletics + STR 14
- [x] Roman Religion: Religion proficiency + WIS 14
- [x] Mars (campaign-specific): Religion proficiency + Soldier background
- [x] Germanic Tribes: Survival proficiency + Insight proficiency
- [x] The Frontier: Survival proficiency + Perception proficiency
- [x] Roman Law and Politics: History proficiency + Noble background
- [x] Poisons, Medicine: Medicine proficiency + Herbalist Kit
- [x] Reading Divine Signs: Religion proficiency + WIS 14
- [x] The Antonine Plague: Medicine proficiency + CON 14
- [x] Roman Engineering: Athletics proficiency + Artisan's Tools

**reputation.qmd sections:**
- [x] What reputation means in 175 AD (relational, not scored)
- [x] How the system works: shared party base + individual character modifiers
- [x] Starting relationship statements for all 12 factions/NPCs
- [x] How favor is gained (general principles)
- [x] How favor is spent (what relationships provide; calling in a debt)

**camp_economy.qmd sections:**
- [x] The camp as living system (not static supply list)
- [x] Six camp traders: Quartus, Rufus, Valeria, Paterculus, Cato, Sigrun
- [x] Camp Level system (1-3): triggers, effects, DM tracking
- [x] Raw materials as story currency (amber, herbs, iron ore, rune carvings)
- [x] Supply caravan events table

**appendix.qmd:**
- [x] Relationship Starting States table added after NPC OGAS Summary

### Milestone 36 — GM Session 0 Guide
Goal: DM has a practical working document for running Session 0: what to ask, what to collect, what each answer maps to mechanically. Companion to the player-facing `session0.qmd`.

**File:** `gm_session0.qmd` (GM's Workbook, first chapter)

- [x] **Consent and boundaries section** — Corruption consent per player (compelled actions, stage 5 fate); violence/horror content check; record per player
- [x] **Aloud questions with DM annotations** — 9 table-wide questions, each with "listen for" notes mapping to specific mechanical payoffs
- [x] **Private questions** — 4 one-on-one questions: sacrifice threshold, trust map, arc appetite, breaking point
- [x] **Mechanical collection** — Fatum card format and rules; sacrifice seed card; corruption profile card (3 notes per player)
- [x] **Red flags guide** — How to handle: refuses to answer, anti-corruption character, session-ending line matches campaign pressure point, Germanic character variant
- [x] **Pre-Session 1 checklist** — Fatum mapping to S4-5 moments; sacrifice seed ordering for S3; influenced NPC selection; divine standing setup; personalized opening moment per character
- [x] **Quick reference page** — All questions at a glance for printing

### Milestone 37 — Camp NPC Full Treatment
Goal: The six camp traders receive the same depth as the seven main NPCs: OGAS, per-session state, voice reference, reaction tables, and siege behavior. The camp becomes a fully runnable social system, not just a shop list.

**File:** `camp_economy.qmd` (additions to existing traders section)

- [ ] **Trader OGAS tables** — Objective / Goal / Agenda / Secret for all six traders (Quartus, Rufus, Valeria, Paterculus, Cato, Sigrun), matching the main NPC format in `gm_intro.qmd`
- [ ] **Per-session trader state table** — Where each trader is, what they know, what they are doing across Sessions 1-5; mirrors the main NPC state table in `gm_intro.qmd`
- [ ] **Trader voice reference** — 3 characteristic lines per trader showing their voice in different situations (not just the opening line); follows the format in `gm_intro.qmd`
- [ ] **Trader reaction tables** — How each trader responds to the party's 3 most likely approaches (direct ask, barter/bribe, authority/threat); mirrors the main NPC reaction tables
- [ ] **Siege behavior** — Specific DM notes on what each trader does when the siege begins in Session 4: who panics, who helps, who disappears, who reveals something they have been hiding

### Milestone 38 — Unified Skill Interaction Framework
Goal: Every social and skill-based interaction in the fort uses a consistent DC system. Players know what to roll; DMs know what it means. Currently each trader has ad-hoc DCs or no DCs. The reputation system and the trader trust system need to be connected to actual roll mechanics.

**File:** New section added to `camp_economy.qmd`; short summary box added to `reputation.qmd`

- [ ] **Interaction tier DCs** — Standardize four interaction tiers across all traders: Stranger (no check, baseline service), Acquaintance (DC 12 Persuasion or appropriate skill), Trusted (DC 15, requires prior positive history), Ally (DC 18 or automatic after meaningful shared experience); each tier maps to the existing relationship statement language in `reputation.qmd`
- [ ] **Skill substitutions** — For each trader, list which non-Persuasion skill can substitute: Rufus (Athletics or tool proficiency demonstration), Valeria (Medicine check to show competence), Paterculus (Religion or History relating to omens), Cato (Insight to find the right angle, Performance to tell a story), Quartus (Proficiency with any military tool or supply knowledge), Sigrun (Germanic language or Survival showing forest knowledge)
- [ ] **What failure means** — DC failure does not mean no access; it means the wrong kind of access (Quartus becomes formal and routes everything through official channels; Cato overcharges; Sigrun sells to someone else first). No roll should result in a dead end.
- [ ] **Reputation modifier integration** — Table: how each reputation statement modifier translates into a numerical DC bonus or automatic tier upgrade; connects reputation language to actual mechanic
- [ ] **Camp-wide skill challenges** — Two structured skill challenges for siege scenarios (Session 4): "Hold the Gate" (Athletics/Persuasion/Intimidation/Medicine to prevent panic and hold position) and "Provision the Escort" (Investigation/Persuasion/Survival to gather what the party needs before descending)

### Milestone 39 — The Vicus: Civilian Settlement
Goal: The civilian settlement outside the fort walls has named characters, its own information network, and its own stakes in the siege. Currently the vicus is mentioned but has no people.

**File:** New section added to `locations.qmd` and `camp_economy.qmd`

- [ ] **Vicus layout** — Physical description: where it sits relative to the fort gate, what buildings it contains (taberna, workshop row, the shrine, the bathhouse annex, the trader stalls), how many civilians live there (approximately 200)
- [ ] **Named vicus characters** — 4 named civilians, each with a brief OGAS and one distinctive thing: (1) the *taberna* operator who owes a favor to a Germanic trader, (2) a former soldier's wife who runs the informal mail relay, (3) a young local boy (half-Roman, half-Germanic) who knows every tunnel and weak point in the outer wall, (4) a Gallic craftsman who repairs civilian equipment and has been here longer than any current soldier
- [ ] **The vicus information network** — What the vicus knows that the fort does not: which soldiers are in debt, which officers have civilian relationships, what comes through the trade gate that is not on the manifest, whether the Germanic raiders have been seen near the settlement recently
- [ ] **Vicus under siege** — What happens to the civilian settlement when the fort is besieged in Session 4: do they shelter inside, try to flee, send a delegation, or become a liability? Specific DM guidance per outcome
- [ ] **Vicus as adventure space** — Three specific things players can do in the vicus that they cannot do inside the fort: access the black market, send unofficial messages, get information that no officer would give them

---

## Conventions

### Writing Tone
- **Player sections:** Present tense, "you" voice, no spoilers. Treat the reader as a capable adult who wants enough information to make interesting characters.
- **GM sections:** Direct and practical. Short sentences. No hedging. Trust the DM to improvise; give them the raw material, not a script.
- **Read-aloud text:** Block quote format (`>`). Slow, atmospheric. Short paragraphs. Specific sensory details. End on a decision or question, never a statement.

### Style Rules
- **No em dashes (--).** Use a colon, semicolon, or comma instead. For parenthetical phrases, use parentheses.
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
