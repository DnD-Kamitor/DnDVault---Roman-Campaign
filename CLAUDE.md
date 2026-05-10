# CLAUDE.md — The Shadow of Mars Campaign Workbook

Notes from the DM: 
- Some chapters like https://dnd-kamitor.github.io/DnDVault---Roman-Campaign/knowledge.html have things that are NOT hidden behind toggles, making them read immediately visible to players (Without a check) this is very bad, make sure all skills like these are hidden behind toggles. 
- Some of the information behind the toggles is very... robotic, and factual; Rather it should be described like its me the DM telling them something not like "in chapter 2 you can potentially find this".
- Information that ties the world together like "in chapter 2 characters that have this unlocked can now identify it comes from this legion" is stuff you need to put into the DM book. 
- A lot of the information is really double or can be confusing like "Where does your character comes from and "the people's of the empire" where you go into races, this should be just one chapter. 
- The player session 0 and the GM session 0 includes a lot of questions each character needs to ask themselves to flush out a great character. Don't delete questions unless they are double, they are good questions.
- The player tome should be definded into :SECTION 2 the camp (where there is everything about the camp, vendors, resources, new weapons, new beasts, layout, behavoir, professions; SECTION 1 The world (where the player creates the character) including everything about the history of the world player assistance, Section 3 the campaign where there are things about corruption or things they might need afterwards (more mechanical)  
- I would like more roman weapons and ammunition included in the possible weapons. Slings were very deadly for example and have different uses at different ranges depending on the ammunition. Same goes for arrows or melee weapons. Or things like Pillum (That romans throw)
- I would like the Beast manual to be included into the gitbook, but then expanded with more usages (making them more unique; the only difference between the beast is now some hp or attack stats, but I would like the beast to have more tactics similar to the animals in the real world, you may increase the CR as a result). 
- The camp should be upgradable, and to the option for the players to take the legionaires with them, (for example for the tutenborg forest). 


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

- [x] **Trader OGAS tables** — Objective / Goal / Agenda / Secret for all six traders (Quartus, Rufus, Valeria, Paterculus, Cato, Sigrun), hidden in collapsible `<details>` blocks
- [x] **Per-session trader state table** — Where each trader is, what they know, what they are doing across Sessions 1-5
- [x] **Trader voice reference** — 3 characteristic lines per trader showing their voice in different situations (not just the opening line)
- [x] **Trader reaction tables** — How each trader responds to the party's 3 most likely approaches
- [x] **Siege behavior** — Specific DM notes on what each trader does when the siege begins in Sessions 3-4

### Milestone 38 — Unified Skill Interaction Framework (Book-Wide)
Goal: Every skill-based interaction across the entire book uses a coherent, interesting DC design. Not uniform — each NPC and location has its own personality expressed through which skills matter and what failure opens. Design principle: **no dead ends, different tools open different doors, cascade unlocks reward investment, partial success is always more interesting than binary pass/fail**.

**Files:** `camp_economy.qmd` (trader DCs), `reputation.qmd` (integration), `gm_intro.qmd` (main NPC DCs), `locations.qmd` (exploration DCs), `knowledge.qmd` (knowledge tier polish), `chapter1.qmd`–`chapter5.qmd` (in-scene skill checks audit), new standalone `skill_framework.qmd` (GM reference, both the rules and the design principles)

#### Design Principles (document these in skill_framework.qmd)

- [x] **No dead ends** — Every failed check opens a different door, not a wall.
- [x] **Wrong tool, different door** — Wrong skills succeed into different outcomes, not failure.
- [x] **Cascade design** — Early success reveals the existence of harder, more rewarding checks.
- [x] **Signature skills** — Every major NPC and trader has one non-Persuasion bypass skill.
- [x] **Investment checks** — Some checks cost a resource in addition to the roll.
- [x] **Temporal gates** — Specific checks are session-locked; miss the window, miss the information.
- [x] **Tier memory** — Failed checks require re-approach conditions before retrying.

#### Camp Traders (camp_economy.qmd)

- [x] **Four-tier DC table per trader** — Stranger / Acquaintance (DC 12) / Trusted (DC 15) / Ally (DC 18) for all six traders
- [x] **Signature skill per trader** — Non-Persuasion auto-advance per trader documented
- [x] **Failure states per trader** — What each failed approach opens (not closes)
- [x] **Cascade unlocks per trader** — What each Ally tier reveals that unlocks a new check
- [x] **Investment check options** — Per-trader resource costs that earn advantage or skip tiers

#### Main NPCs (gm_intro.qmd)

- [x] **Per-NPC primary and signature skill table** — All 7 main NPCs with DC tables and signature skills
- [x] **Wrong-approach consequence table** — Per NPC: wrong skill textures documented
- [x] **Temporal gate table** — Session-locked checks per NPC with what they reveal and cost of missing
- [x] **Partial success text per NPC** — 5-below / exact DC / 5-above structure for all 7 NPCs

#### Exploration and Locations (locations.qmd)

- [x] **Per-location skill check menu** — DC 12/16/20 tiers for all major locations (principia, ruins rooms, forest zones, grove, siege areas)
- [x] **Skill substitution menus for exploration** — Investigation/History/Religion/Arcana/Nature per location
- [x] **Time cost for deep checks** — 10-minute cost documented per location; tactical impact noted

#### Session Skill Audits (chapter1.qmd–chapter5.qmd)

- [x] **Session 1 skill audit** — Partial success reframes; temporal gate (worker behavior); Corvinus temporal gate added
- [x] **Session 2 skill audit** — Medicine/Investigation partial success text; Tribune temporal gate; cascade for soldier at the wall (DC 17 → named ally Flavus)
- [x] **Session 3 skill audit** — Forest event skills matrix; river crossing temporal gate; Thusnelda DC structure; Vercingetorix cascade unlock
- [x] **Session 4 skill audit** — Crisis partial success reframes; named soldier cascade; Mars carry direction temporal gate; kneeling witnesses partial success
- [x] **Session 5 skill audit** — Mars arrival insight temporal gate; Option C partial success structure; failure recovery path (DC 14 Virtus demonstration); Varro closing check

#### Knowledge System Polish (knowledge.qmd)

- [x] **Qualitative difference at each tier** — Facts / implications / dangerous knowledge reframe added at chapter top
- [x] **Cross-reference skill unlocks** — Three cross-reference unlocks documented (Military DC 17 → ruins check; Germanic DC 15 → Vercingetorix approach; Divine Signs DC 17 → Session 4 augury)

#### Reputation Integration (reputation.qmd)

- [x] **Relationship statement → DC modifier table** — Numerical modifiers (-2/-4/-6) with special access per tier
- [x] **Debt calling mechanics** — Auto-success rules, major debt tier advance, per-NPC debt limits
- [x] **Reputation damage rules** — Standard damage table, critical damage table, recovery conditions, behavioral description of damage

### Milestone 39 — The Vicus: Civilian Settlement
Goal: The civilian settlement outside the fort walls has named characters, its own information network, and its own stakes in the siege. Currently the vicus is mentioned but has no people.

**File:** New section added to `locations.qmd` and `camp_economy.qmd`

- [x] **Vicus layout** — Physical description: where it sits relative to the fort gate, what buildings it contains (taberna, workshop row, the shrine, the bathhouse annex, the trader stalls), how many civilians live there (approximately 200)
- [x] **Named vicus characters** — 4 named civilians, each with a brief OGAS and one distinctive thing: (1) the *taberna* operator who owes a favor to a Germanic trader, (2) a former soldier's wife who runs the informal mail relay, (3) a young local boy (half-Roman, half-Germanic) who knows every tunnel and weak point in the outer wall, (4) a Gallic craftsman who repairs civilian equipment and has been here longer than any current soldier
- [x] **The vicus information network** — What the vicus knows that the fort does not: which soldiers are in debt, which officers have civilian relationships, what comes through the trade gate that is not on the manifest, whether the Germanic raiders have been seen near the settlement recently
- [x] **Vicus under siege** — What happens to the civilian settlement when the fort is besieged in Session 4: do they shelter inside, try to flee, send a delegation, or become a liability? Specific DM guidance per outcome
- [x] **Vicus as adventure space** — Three specific things players can do in the vicus that they cannot do inside the fort: access the black market, send unofficial messages, get information that no officer would give them

### Milestone 40 — Deep Religion, Deep History, and the Magical World Around Vindolanda
Goal: The campaign currently scratches the surface on religion and historical context around Vindolanda and gives beasts and flora only passing mentions. This milestone goes deep: layered religion (Roman and Germanic) hidden behind knowledge barriers, historical depth that rewards curious players, and a fully realized magical ecosystem of animals, plants, and spirits in and around the camp. Everything is hidden by collapsible barriers to keep it out of the way until needed.

**Files:**
- `knowledge.qmd` (new entries: Deep Religion, Deep History of Vindolanda and the Frontier)
- `locations.qmd` (new section: The Living World Around Vindolanda -- creatures, flora, magical fauna)
- `player_tome.qmd` (player-facing summary: what a Roman soldier would know about local spirits and animals)
- `bestiary.qmd` (extend with: local creatures near Vindolanda, magical plants, the Genius Loci of the spring)
- Possibly new standalone `frontier_nature.qmd` if scope warrants

#### Deep Religion: Roman Side (knowledge.qmd, barrier-gated)

- [x] **Mars in 175 AD** — Not the clean civic war-god of Rome but the frontier version: older, bloodier, associated with the liminal space between Rome and the uncontrolled world. DC 13: standard cult facts. DC 15: the frontier cult of Mars Ultor (the Avenger), what soldiers actually believe he wants, why frontier Mars and city Mars feel like different gods. DC 17: the *ancilia* tradition (twelve sacred shields kept in Rome said to have fallen from heaven), the specific prayer language that constitutes a binding vow to Mars, and why some priests believe the spear in the vault is one of three divine weapons that should not coexist in one place.
- [x] **The spirits under the fort** — Roman religion acknowledges the *genius loci* (spirit of a place) and the *lares compitales* (crossroads spirits). DC 13: every Roman soldier knows not to build over sacred springs without proper propitiation. DC 15: what the specific indicators of an active *genius loci* look like (temperature changes, specific plant growth, animal avoidance patterns); how to perform a basic propitiation. DC 17: the Vindolanda spring beneath the northeast corner of the fort has a *genius loci* that predates Rome and was active before the Germanic temple below was built; it is not the same spirit as the ruins' guardian but it has been watching both.
- [x] **The Lemuria festival and its camp application** — Lemuria (May 9, 11, 13) is the festival for appeasing the restless dead. DC 13: soldiers know the basic protective rites; you throw black beans over your shoulder nine times and say the formula. DC 15: the formula in full Latin (player-facing); why frontier postings have higher rates of Lemuria observance (more soldiers die far from family burial; more unquiet dead). DC 17: the Lemures from the bestiary are real and distinguishable from other undead by specific signs; a character with DC 17 knowledge automatically recognizes them and knows that Lemuria rites performed at their grave site work with advantage.
- [x] **The *haruspex* tradition in depth** — DC 13: augury basics already covered. DC 15: the *libri haruspicini* (the books of divination); what the *extispicy* procedure actually involves; which organs predict which outcomes. DC 17: the specific omen category called *prodigia* (prodigies: unusual events that require state response); the twelve specific signs that constitute a prodigium in military law; and why Paterculus has been filing them as ordinary bad omens because he knows that officially declaring a prodigium would bring the Senate to Vindolanda.
- [x] **Mithras on the frontier** — Mithraism is widespread among Roman soldiers by 175 AD but officially unrecognized. DC 13: soldiers know who is in the cult (you can tell by the symbolic meal-sharing behavior). DC 15: the seven grades of initiation; what the Mithraic mystery claims about death and rebirth; how Mithraism and official Mars worship interact (they are not in conflict; most Mithraists also honor Mars publicly). DC 17: Vindolanda has a small Mithraic chapel in the bathhouse annex, known only to initiates; it has been used as a secure dead-drop by at least one faction in the campaign (the DM assigns which based on current session state).

#### Deep Religion: Germanic Side (knowledge.qmd, barrier-gated)

- [x] **Wotan/Odin on the frontier** — Germanic religion as encountered by Roman soldiers. DC 13: soldiers know the Germanic equivalent of Jupiter is a one-eyed wandering god who collects the war-dead. DC 15: the specific aspects of Wotan worship that appear in the Marcomanni and Cherusci territories (sacrifice at the sacred trees, the *seiðr* tradition, why Germanic warriors sometimes behave in ways Romans cannot predict because they have made a death-vow to Wotan). DC 17: the rune set carved into the Hall of Shields corresponds to a specific Wotan dedication; the shields were not collected as trophies but as *votive offerings* -- the tribes whose shields are here did so voluntarily, offering their war-god's weapons to a greater war-god's temple.
- [x] **The *völva* tradition** — DC 13: soldiers know Germanic shamans exist and are to be avoided or bribed. DC 15: the specific role of the *völva* (staff-carrier, female seer) in Germanic tribal structure; why they are not the same as Roman augurs; what they actually do when they perform *seiðr*. DC 17: Thusnelda is a *völva* of the third tier (she has performed the death-rite three times and returned each time); this makes her opinion on the spear not religious interpretation but eyewitness testimony about what happens to mortals who approach divine objects without the correct standing.
- [x] **Sacred groves and the Thing** — DC 13: soldiers know Germanic tribes hold councils in sacred groves. DC 15: the *Thing* as legal and religious institution; what decisions require grove ritual and why; what it means that the grove the party is going to visit is a *Thingstätte* (council place) and not just a temple. DC 17: the standing stones in Thusnelda's grove are not natural formations; they were carried from three different locations over the course of two centuries; each represents a tribe's original territorial claim; the grove is simultaneously a temple, a court, and a treaty document in stone.
- [x] **Bog offerings and their meaning** — DC 13: soldiers know to avoid the bogs; bodies have been found there. DC 15: Germanic bog sacrifice tradition; what types of offerings are made in bogs (objects and persons, both); what distinguishes a bog sacrifice from a murder (the specific preparation of the body). DC 17: the bog northeast of Vindolanda, three hours' walk, contains a preserved offering that is approximately 200 years old and is wearing Roman armor from a period before Rome reached this far north; someone was doing ritual exchange with the Germanic world long before the official frontier.

#### Deep History of Vindolanda (knowledge.qmd, barrier-gated)

- [x] **What was here before Rome** — DC 13: soldiers know the fort is built on old ground. DC 15: archaeological evidence in the fort construction (strange stone alignments the engineers routed around; a spring they sealed rather than redirected; tool-marks in the bedrock that do not match Roman or Germanic techniques). DC 17: the location was a sacred assembly ground for a pre-Germanic people whose name is not known; they left the ruins below and the spring; they are not related to either the Romans or the current Germanic tribes; Thusnelda knows this and considers the grove above the ruins a legacy-in-trust rather than an inheritance.
- [x] **The Teutoburg aftermath** — DC 13: soldiers know the disaster. DC 15: what the Roman response was in the thirty years after Teutoburg -- the punitive campaigns, the deliberate destruction of Germanic sacred sites, why those campaigns succeeded militarily and failed strategically. DC 17: three of the Germanic sacred sites destroyed during the punitive campaigns were this general region; the destruction created the specific spiritual instability that the ruins below Vindolanda are a response to; the Germanic tribes sealed the spear here partly because Rome had destroyed everywhere else they could have put it safely.
- [x] **The Antonine Plague at the frontier** — DC 13: soldiers know there is a plague and people die of it. DC 15: specific symptoms; mortality rates in military vs. civilian populations; why frontier postings have slightly lower rates than Rome (isolation as accidental quarantine). DC 17: the plague is not evenly distributed in the military because someone has been making deliberate policy choices about which units are rotated to exposed positions; this is not random and is a live political question; Brutus's faction has used plague mortality rates in Senate debates about frontier policy.
- [x] **Marcus Aurelius and the frontier war** — DC 13: soldiers know the Emperor is campaigning on the Danube. DC 15: the strategic context; what Marcus Aurelius is actually trying to accomplish (province creation, not just defense); why this is opposed in the Senate; what the Marcomannic War looked like from the soldiers who fought it (differently from the official dispatches). DC 17: Marcus Aurelius keeps a philosophical diary; excerpts have circulated among educated soldiers and officers; one passage, dated three months before the campaign, asks whether a just man can serve an Empire that does things unjust men do, and does not resolve the question.

#### Magical Ecosystem Around Vindolanda (locations.qmd new section)

- [x] **The Vindolanda spring (Genius Loci)** — The spring in the fort's northeast corner (currently sealed under the granary floor) is alive in a way the Romans have intuited without naming. Its *genius loci* predates the fort and the Germanic temple; it does not align with either Roman or Germanic religious categories cleanly. DC 12 Nature: the spring water has unusual clarity and a consistent temperature that does not match the seasonal range. DC 15 Religion: the *genius loci* is active and has been performing minor protective function for the settlement above it; the sealed cover is causing it to concentrate energy into the ground rather than release it; this is contributing to the unusual plant growth in the northeast corner (see flora section). DC 17 Arcana: the *genius loci* is aware of the spear and has been suppressing its influence within a 50-foot radius of the spring; this is why the northeast barracks has had fewer corruption dreams than the rest of the fort. Use this as a player discovery: the one part of the fort that is quieter is the part above the old spring.
- [x] **Magical animals near the camp** — Not monsters: animals that behave in ways that encode information about the local magical state. Each is a player-available signal. Document: (1) *The raven colony* (six ravens that roost in the principia tower; Germanic soldiers interpret raven behavior as omen; Roman soldiers think the Germanic soldiers are superstitious; the ravens are actually responsive to divine presence -- they relocated to the principia tower three days before the spear was excavated). (2) *The spring-keeper lizards* (a species of large pale lizard that lives only near the spring; harmless; they disappear from their basking spots when corruption is actively spreading; their absence is a reliable early warning system that no one has noticed yet). (3) *The bog-light moths* (large pale moths that emerge from the direction of the bog at specific times of the year; DC 13 Nature to recognize them as native to the bog region; DC 15 Nature to note they have arrived three weeks early this year; DC 17 Nature or Religion to interpret correctly: early arrival means the bog is active, which means a sacrifice was accepted or rejected recently).
- [x] **Flora of the frontier (medicinal and magical)** — Plants that Valeria wants, plants that Sigrun sells, plants that connect to the magical world. Hidden by barriers. (1) *Wolfsbane (aconitum)* -- DC 13 Medicine: it is a poison. DC 15 Medicine: specific symptoms, dosage threshold, antidote window. DC 17 Medicine: used correctly it is also a preparation that slows the corruption mechanic's physical symptoms by 24 hours per dose; Valeria does not know this yet but will if the party brings her a sample with the DC 17 Nature identification result. (2) *Sacred mistletoe* -- found only on specific oak trees marked by the Germanic tribes; DC 13 Nature: Romans know mistletoe has religious significance. DC 15 Nature: specific identification and where it grows near Vindolanda. DC 17 Religion: fresh mistletoe harvested with a bronze knife (not iron) and offered to the grove altar counts as a valid sacrifice for the grove ritual; this is one of the three items that the grove will accept without requiring something personal. (3) *Bog rosemary (Andromeda polifolia)* -- DC 12 Nature: native to the bog region. DC 14 Survival: can be used to mark a path through bog terrain (animals avoid it, so paths through it indicate stable ground). DC 16 Medicine + Herbalist kit: tea made from dried bog rosemary provides advantage on saving throws against the Alp's Sleep Paralysis for 8 hours; Valeria does not know this; a player who discovers it becomes more useful to her than a patient. (4) *Elder (Sambucus nigra)* -- DC 13 Nature: common near settlements. DC 15 Religion: in both Roman and Germanic tradition, elder trees are considered inhabited by protective spirits; cutting one without asking permission causes the spirit to leave; Germanic soldiers will not camp near a felled elder tree. DC 17 Arcana: the elder tree near the south gate has been marked with a specific rune by Sigrun; it marks her dead-drop location; she leaves messages there for trusted contacts.
- [x] **The bog northeast of the camp** — A three-hour walk from the fort, the bog is a landscape feature that encodes several active plot elements. Document for DM: current state (one body in the bog from approximately six months ago; unidentified, Roman military sandal type); what the bog offers players who investigate (the preservation; the offering tradition; DC 15 Investigation to determine the body is not a Germanic sacrifice but a Roman soldier who was placed here deliberately); what the bog's *genius loci* is doing (quietly upset about being used as a dumping ground; it accepted one genuine offering placed here by Thusnelda two months ago and rejected everything else; players who find and identify the genuine offering learn something about Thusnelda's state of mind two months ago -- she was asking the bog whether the party, whose existence she did not know then, would be trustworthy).
- [x] **The raven network** — Ravens appear across all five sessions. Document a consistent rule: ravens near the ruins increase in number as the spear's influence grows; ravens near a character who is corrupted begin following them specifically; ravens near Cassia behave differently than they do near anyone else (they land near her, look at her, and leave without taking anything; she does not explain this). Players who track raven behavior across sessions can decode information the DM has embedded. Create a raven behavior table: six specific behaviors and what each encodes about the current divine state of the campaign.

#### Player-Facing Frontier Nature (player_tome.qmd addition)

- [x] **What a Roman soldier knows about local spirits** — A single page in player_tome.qmd (not gated by barriers) covering: how a Roman soldier relates to the *genius loci* of an unfamiliar place (you acknowledge it, you make a small offering, you ask permission); what the standard signs of a hostile spirit versus a neutral one are; why Germanic peoples are considered better at identifying local spirits (they have been here longer); and a brief guide to the three animal behaviors that a frontier soldier learns to watch: raven behavior near the tree line, unusual silence in the forest, and why dogs that stop barking at night are not a good sign.

### Milestone 41 — Knowledge Gate Audit: Enforce All DC Barriers
Goal: Nothing in knowledge.qmd (or any player-facing file) should be readable without a DC check or explicit "what every soldier knows" preamble. Every DC-gated entry must be inside a `<details>`/`<summary>` collapsible block. This audit sweeps the entire player-facing book.

**Files:** `knowledge.qmd`, `player_guide.qmd`, `player_tome.qmd`, `peoples.qmd`, `corruption.qmd`, `vindolanda_guide.qmd`

- [x] **Audit knowledge.qmd** — Every DC 13/15/17 block must be inside `<details>`. Any DC-gated fact appearing in the open preamble without a roll context must be moved behind a toggle or into the "what every soldier knows" baseline paragraph
- [x] **Audit player_guide.qmd** — Check for spoiler-adjacent content (corruption detail, divine mechanics) that requires a check rather than free reading
- [x] **Audit player_tome.qmd** — Frontier nature section: any specific mechanical information (wolfsbane doses, raven behavior table) must be gated; flavour and instinct knowledge stays open
- [x] **Audit vindolanda_guide.qmd** — Location descriptions fine; skill DCs and tunnel routes should be gated for GM only (move to locations.qmd if needed)
- [x] **Audit peoples.qmd and corruption.qmd** — Check for any cross-file leakage where DM context bled into player text
- [ ] **Fix: live link check** — Verify the knowledge.html page in the deployed site matches the corrected file after audit

---

### Milestone 42 — Toggle Voice Rewrite: DM-Facing Content in DM Voice
Goal: All collapsible DM sections currently read like encyclopedia entries or AI output. Rewrite them so they read like a DM writing notes to themselves: direct, specific, confident. First-person where appropriate ("Here is what I do when..."), not third-person clinical.

**Files:** `camp_economy.qmd` (trader OGAS), `gm_intro.qmd` (NPC DC tables), `locations.qmd` (skill check menus), `knowledge.qmd` (deep sections), `chapter1.qmd`–`chapter5.qmd` (DM Notes)

- [x] **camp_economy.qmd OGAS blocks** — Rewrite all 6 trader OGAS sections in DM voice: "Quartus wants X. He will do Y if Z. His secret: he knows about..." not "Objective: Maintain supply integrity"
- [x] **gm_intro.qmd NPC DC tables** — Partial success text and temporal gate descriptions should sound like DM coaching, not rules text: "If they hit this, give them the information straight; do not make them ask twice"
- [x] **locations.qmd skill menus** — Discovery text should feel like a DM reminder, not a lookup table: "They will find the slow-burn candle. When they do, let the silence sit for a moment before you describe it"
- [x] **chapter1-5.qmd DM Notes** — Audit each Skill Audit section; remove any clinical phrasing; replace with the voice of a prepared DM who has thought about what this moment should feel like
- [x] **knowledge.qmd deep sections** — The DC 17 payoff text in particular should feel earned: write as if the DM is handing the player something valuable, not filing a report

---

### Milestone 43 — Cross-Session Integration Notes: Move to GM Book
Goal: Any text that says "characters who unlocked X in session 2 can now do Y" belongs in the GM's Workbook, not in player-facing knowledge tiers. Audit and relocate.

**Files:** `knowledge.qmd` (cross-reference section), `chapter1.qmd`–`chapter5.qmd` (cascade unlock notes), `skill_framework.qmd` (temporal gate table)

- [x] **Audit knowledge.qmd cross-references** — The three "Cross-Reference Skill Unlocks" entries must be in gm_intro.qmd or the relevant chapter, not in the player-facing knowledge file; replace with a DM-only note in the skill_framework
- [x] **Audit chapter cascade unlocks** — Ensure all cascade text (e.g., "Flavus appears in Session 4 if DC 17 hit in Session 2") is inside `<details>` DM blocks, not in open session text
- [x] **Create cross-session integration table in gm_intro.qmd** — A single master table: Session → DC achieved → Session N+X payoff; DM can see the full chain at a glance
- [x] **Audit skill_framework.qmd temporal gates table** — Verify all entries are DM-facing; none should contain player-visible reward descriptions in open text

---

### Milestone 44 — Merge Duplicate Origin Chapters
Goal: `player_guide.qmd` contains province-of-origin and character background material. `peoples.qmd` covers the same territory via the D&D race lens. These overlap badly. Merge into a single authoritative chapter.

**Files:** `player_guide.qmd`, `peoples.qmd`, `_quarto.yml`

- [x] **Audit both files** — List every section in each; mark which sections are genuinely unique vs. duplicated or redundant
- [x] **Decide canonical home** — `peoples.qmd` covers race + legal status + background hooks; `player_guide.qmd` covers daily life + equipment + corruption intro; keep the division there
- [x] **Move province/origin tables** — Any province-of-origin content in `player_guide.qmd` (where are you from, what did you do before the legion) moves into `peoples.qmd` as a third section after race and legal status
- [x] **Remove/redirect duplicates** — Delete the duplicate sections from whichever file loses them; add a one-line cross-reference: "See Peoples of the Empire for province origin tables"
- [x] **Update `_quarto.yml` order** — `peoples.qmd` should appear immediately after `player_guide.qmd` in the chapter list; verify the order makes narrative sense

---

### Milestone 45 — Session 0 Questions Audit: Preserve, Deduplicate, Clarify
Goal: The player session0.qmd and GM gm_session0.qmd both contain character questions. No question should appear twice. No question should be deleted unless it is genuinely identical to another. Every surviving question should be in the right file.

**Files:** `session0.qmd`, `gm_session0.qmd`

- [x] **Full question inventory** — List every question in both files with file and section labels
- [x] **Mark genuinely doubled questions** — Questions that ask the same thing in slightly different words count as one; pick the better phrasing and keep it
- [x] **Assign each unique question to the right file** — Questions about the character's inner life, history, and bonds: `session0.qmd`. Questions about player consent, arc appetite, breaking points, and sacrifice threshold: `gm_session0.qmd`
- [x] **Do not delete** — Unless two questions are word-for-word identical, the DM note says keep them; move rather than delete
- [x] **Final check** — After redistribution, both files should feel complete on their own; a player reading `session0.qmd` should not need `gm_session0.qmd`, and vice versa

---

### Milestone 46 — Player Tome Reorganization: Three Sections
Goal: The player-facing material is currently scattered across multiple files with no clear structure. Reorganize the player's workbook into three named sections so players know where to look.

**Section 1 — The World** (who you are, where you come from, the history around you): `player_guide.qmd`, `peoples.qmd`, `session0.qmd`, `calendar.qmd`, `knowledge.qmd`
**Section 2 — The Camp** (everything about Vindolanda and frontier life): `player_tome.qmd`, `vindolanda_guide.qmd`, `professions.qmd`, `supplies.qmd`, `food.qmd`, `roman_tactics.qmd`, `bestiary.qmd`
**Section 3 — The Campaign** (mechanics that matter during and after play): `corruption.qmd`, `reputation.qmd`, `journal.qmd`, `atmosphere.qmd`

- [x] **Update `_quarto.yml`** — Reorganize chapter order to match the three-section structure; add section divider pages or titles
- [x] **Create section landing pages** — A short intro paragraph at the start of each section explaining what it contains and when to read it; these can be the first few lines of the first file in each section
- [x] **Audit cross-references** — After reordering, check that any "see chapter X" references still point to the right place
- [x] **player_tome.qmd internal reorganization** — The tome itself covers immersion, language, thinking, senses, and corruption; internally tag or header-label which sub-section belongs to which book section so they can be split if needed later

---

### Milestone 47 — Expanded Roman Weapons and Ammunition
Goal: The weapons section currently has basic D&D stats. Roman weapons had real tactical variety -- slings with different ammunition for different ranges, heavy vs. light pilum, arrow types (bodkin, broadhead, fire), melee weapon subtypes. Add all of these with D&D mechanics.

**File:** New section in `roman_tactics.qmd` (Player's Workbook); summary table in `player_guide.qmd` equipment section

- [x] **Ranged weapons expansion** — *Funda* (sling): lead shot (DC 13 Con save on hit, short range), stone (cheap, longer range, less penetration), clay incendiary (sets objects alight); range bands with different stat profiles for each ammunition type
- [x] **The pilum** — Heavy *pilum* (thrown 30/60, piercing, on hit: target's shield unusable until repaired, DC 14 Athletics to retrieve); light *pilum* (thrown 20/40, acts as javelin but +1d4 on first attack vs. unshielded); *plumbata* (weighted dart, thrown 30/60, ignores half cover)
- [x] **Arrow types** — Bodkin (ignores leather armor's damage reduction), broadhead (extra 1d4 bleed on a crit), fire arrow (requires bonus action to light, 1d4 fire additional, only vs. flammable targets), *arcuballista* bolt (crossbow bolt, heavy, -10 ft range but +2 damage)
- [x] **Melee weapon subtypes** — *Gladius* (Roman short sword: advantage on attacks in tight formation); *spatha* (longer cavalry sword: +5 ft reach, disadvantage in formation); *pugio* (dagger: counts as finesse, advantage on grapple damage); *hasta* (infantry spear: reach, brace action); *dolabra* (military pick: ignores stone cover, double damage to structures)
- [x] **Ammunition weight and supply** — Each ammunition type has a weight per 20-unit bundle and a Vindolanda current-stock count; sling stones are free (collected locally); lead shot requires the Quartermaster; pilum are one-use per encounter unless the character spends a bonus action to retrieve
- [x] **Tactics integration** — Cross-reference roman_tactics.qmd formation entries: pilum throw before melee is a formation opener; slings on the wall during the siege; arrow types per session encounter

---

### Milestone 48 — Bestiary Tactical Expansion
Goal: Every creature in `bestiary.qmd` currently differs mainly by HP and attack stats. Give each creature a distinct tactical identity grounded in how that creature type actually behaves: ambush patterns, territory defense, pack behavior, reaction to light/fire/sound. CR increases where the tactics justify it.

**File:** `bestiary.qmd`

- [x] **Strix (CR 3 → CR 4)** — Add: hunts by sound not sight (Blindsight 60 ft); attacks from above and retreats to tree line (never stays in melee more than 1 round); specifically targets spellcasters or those carrying light; *Ill Omen* activates only when it has taken no damage yet (it watches before striking)
- [x] **Lemur (CR 1/2 → CR 1)** — Add: gathers in clusters near unburied bodies; when one is destroyed, all others within 30 ft make a Wisdom save (DC 12) or scatter for 1 round; *Dishonored Rest* now triggers only on the third destruction of the same Lemur (it reforms twice before the rite is needed); they do not attack living creatures unless those creatures disturb a grave
- [x] **Larvae (CR 4 → CR 5)** — Add: chooses a face from someone the target has wronged (DM picks; player must identify the face or take disadvantage on saves); the face changes each round if the Larvae is below half HP (it is cycling through options, looking for a reaction); it retreats through solid surfaces if reduced below 20 HP
- [x] **Genius Loci (CR 4, unchanged)** — Add: does not initiate combat; can only act if its site is desecrated; its first action is always *Compel Respect* (DC 14 Wisdom or creature must make an offering before it can attack the spirit); it communicates through environment (temperature, water behavior, animal response) before resorting to direct action
- [x] **Alp (CR 3 → CR 4)** — Add: targets only sleeping creatures initially; if the target wakes, the Alp shifts to Mist Form immediately; it returns the following night unless iron is placed at the threshold; *Sleep Paralysis* now has a save DC of 14 and lasts until the target takes damage or an ally spends an action to wake them; the Alp makes no sound and has advantage on Stealth checks in darkness
- [x] **Draugar (CR 5 → CR 6)** — Add: territorial; does not pursue more than 100 ft from its barrow; *Swelling Rage* now triggers at 60 HP (not bloodied), meaning it becomes dangerous earlier; it throws grave goods as improvised weapons (1d8) before closing to melee; the smell of fresh-turned earth calms it for 1 round (DC 12 Nature to know this)
- [x] **Lindworm (CR 8 → CR 10)** — Add: guards a specific water source; never found more than 1 mile from its lair; *Serpentine Body* can now be used to encircle terrain features (a tree, a boulder) granting it cover on one side; it uses *Poison Breath* only when 3+ creatures are in a 15-ft cone; it retreats into water when below 50 HP and must be followed into its lair to finish the encounter
- [x] **Nix (CR 4 → CR 5)** — Add: always begins in a non-threatening form (lost traveler, beautiful stranger); *Unearthly Beauty* saves against its true form are at disadvantage if the target has interacted with its disguise for more than 10 minutes; *Drowning Song* now works at range (60 ft, underwater or near water only) and targets the character who has the most unresolved emotional stake in the current session (DM judgment)
- [x] **Tactical summary card** — One-page table: creature name, ambush trigger, retreat condition, terrain preference, one counter-tactic that works

---

### Milestone 49 — Upgradable Camp and Legionary Companions
Goal: Fort Vindolanda should be improvable by player action, and soldiers should be recruitable as field companions for specific missions (like going into the Teutoburg forest). Both systems need full mechanics, not just flavor.

**Files:** `camp_economy.qmd` (camp upgrade system), new section in `roman_tactics.qmd` (legionary companion rules), `locations.qmd` (location unlocks per camp level)

- [x] **Camp upgrade tiers (expand existing Camp Level 1-3 system)** — Tier 1 (default): basic fort, standard trader stock, no wall ballista. Tier 2 (unlocked by party actions): reinforced north gate, one ballista operational, Quartus has heavy equipment access, Valeria has a proper surgery (not just a field kit). Tier 3 (late campaign): siege-ready, Rufus runs weapon upgrades, Sigrun has a permanent stall, the shrine is formally dedicated (bonus to all Religion checks inside the fort)
- [x] **Upgrade triggers** — Specific player actions (not just gold) that advance camp level: completing a supply mission, repairing the gate after Session 4's breach, formally dedicating the spring Genius Loci, negotiating a truce with Vercingetorix's tribe; each trigger is session-anchored so it cannot be rushed
- [x] **Camp upgrade effects on existing mechanics** — Supply stock, trader tier access, DC modifiers inside the fort, morale pool; these should all shift as the camp upgrades
- [x] **Legionary companions: recruitment** — How to recruit a specific soldier: the character must have a Trusted+ relationship with Varro (or equivalent NCO), and the soldier must have been named (cascade unlock from Session 2's DC 17 wall hold); unnamed soldiers are available as generic "legionary" stat blocks; named soldiers have individual stat blocks and personality
- [x] **Legionary companion stat blocks** — Flavus (named from Session 2 cascade): Fighter 3, loyal to the party, has a specific skill (Athletics, Perception, or Intimidation based on DM's Session 2 events); generic legionary: Fighter 2, follows orders, morale check DC 14 when things go very wrong
- [x] **Companion field rules** — How many soldiers can be taken: one named + two generic per party member; they follow orders but have their own initiative; they will not do things that violate their oath (Roman military law applies); if a companion dies, Varro's relationship with the party drops one tier
- [x] **Teutoburg Forest scenario hook** — A specific optional encounter in Session 3 or as a side mission: take three legionaries into the forest to find the site of Varus' disaster; each forest event from the d8 table has a variant for when soldiers are present (they panic at the wrong things and are brave about the wrong things)

---

### Milestone 51 — The Role System: *Vexillatio Extraordinaria* ✅ COMPLETE
Goal: Every player selects a military role at Session 0. Each role has historical prerequisites (citizenship, literacy, guild approval), a pay grade, duties between sessions, and DC-gated knowledge checks behind toggles. NPCs hold all roles too; if an NPC dies, the role becomes vacant and can be inherited. The camp feels like a living institution, not a backdrop.

**Design concept:** The party is a *vexillatio extraordinaria* (special detachment), not a regular *contubernium*. Legate Corvinus assembled one specialist per critical function after the excavation produced results he could not explain and could not officially report. Cover story: construction site oversight. Actual mission: investigate the ruins, contain whatever is down there, keep it off the dispatch rolls. The *frumentarius* in the unit is already filing reports Corvinus has not approved.

**New file:** `roles.qmd` (Player's Workbook, Section 2 — The Camp, after `professions.qmd`)
**Also modify:** `session0.qmd` (role selection step), `gm_session0.qmd` (DM role assignment notes), `gm_intro.qmd` (NPC role holders, vacancy tracking table), `_quarto.yml` (insert roles.qmd)

#### The 15 Roles

Each role entry in `roles.qmd` must contain:
- Latin title + English translation
- Pay grade (denarii/year) and what is deducted
- Prerequisites: citizenship tier, literacy, stat minimums, proficiency requirements, guild/collegium approval where applicable
- Why this role exists (1 paragraph: practical military reason, not flavor)
- Duties between sessions (what the character does during downtime by default)
- Special mechanical benefit (unique to this role, usable in-session)
- DC-gated knowledge checks behind `<details>` toggles (DC 13/15/17, same three-tier system as knowledge.qmd)
- Default NPC holder if no PC takes the role
- What happens if the role is vacant (mechanical consequence)

**Military Command Roles:**

1. *Optio* (Unit second-in-command)
   - Pay: *Duplicarius*, 600 den/year
   - Prerequisites: Citizen preferred (*Latini* with 10+ years service may qualify); CHA 13 or STR 14; Athletics or Persuasion proficiency; appointed by centurion, approved by legate; not available if no existing Optio endorses you
   - Duties: morning briefings, patrol scheduling, casualty reports, drilling the unit
   - Mechanic: once/session, reroll one initiative (yours or an ally's, before or after the roll); can issue an order as a bonus action (one ally within 60 ft moves up to their speed without using their reaction)
   - Knowledge: chain of command and who reports to whom (DC 13); which officers are political appointments vs. soldiers (DC 15); which officers are reporting to Brutus's network and what they have sent (DC 17)
   - Default NPC: Varro (already named)
   - Vacancy consequence: no one can reroll initiative; morale checks for the unit are DC 16 instead of DC 14

2. *Tesserarius* (Watch officer, keeper of the daily password)
   - Pay: *Sesquiplicarius*, 450 den/year
   - Prerequisites: Any legal status; INT 12; Perception proficiency; appointed by centurion; must have clean disciplinary record
   - Duties: assign night watch rotations, deliver the *tessera* (password token) each morning, record who is and is not where they should be
   - Mechanic: always knows current day's password and patrol schedule; can create a false password (DC 14 Deception check, detected on DC 15 Investigation); knows which guards are currently on duty at which post
   - Knowledge: official patrol schedule and gate assignments (DC 13); gaps in the patrol pattern and when the wall is weakest (DC 15); which guards have been bribed, are asleep, or are Brutus's informants (DC 17)
   - Default NPC: Decanus Arvina (new NPC; leaves with the Tribune in Session 3, creating a vacancy)
   - Vacancy consequence: passwords are distributed to all officers (security failure); party loses advance warning of any infiltration

3. *Aquilifer* (Eagle standard bearer, most honored military role)
   - Pay: *Duplicarius*, 600 den/year
   - Prerequisites: Roman citizen (*Cives Romani*) only, no exceptions; STR 15; Athletics proficiency; free-born (not freedman); minimum 5 years service; recommended by the centurion and approved by the legate; must pass the loyalty examination
   - Duties: guard the eagle at all times (it does not leave the *principia* except in formation); lead the standard in formal ceremony; perform unit religious rites at the shrine
   - Mechanic: while you carry the eagle, all allies within 30 ft have advantage on saving throws against fear effects; if the eagle falls (you drop it or die while carrying it), all allies within 60 ft make DC 16 Wisdom save or be frightened for 1 minute; once/session, invoking the eagle before a combat grants the unit a free bonus action on their first turn
   - Knowledge: this legion's history and battle honors (DC 13); where other legions' eagles have been lost and what happened to the men responsible (DC 15); the specific blessing spoken over the eagle that constitutes a binding military oath in Roman law, and why the eagle in the vault below is not a standard eagle (DC 17)
   - Default NPC: Aquilifer Gaius Metellus (new NPC; found dead near the ruins entrance in Session 1, creating an immediate vacancy at the start of play)
   - Vacancy consequence: no unit-wide fear immunity; morale saves are DC 16 across all sessions until the role is filled; the eagle must be guarded by a rotation of two soldiers at all times

4. *Signifer* (Unit standard bearer and unofficial banker)
   - Pay: *Sesquiplicarius*, 450 den/year
   - Prerequisites: Any citizen or *Latini* status; INT 13; must be literate in Latin; History or Persuasion proficiency; appointed by centurion
   - Duties: carry the unit *signum* (not the eagle) in formation; maintain the death benefits ledger; manage the unit savings deposits (soldiers entrust their savings to the signifer because he cannot run)
   - Mechanic: access to the unit savings fund (100 gp collectively at campaign start); can draw on it with DC 14 Persuasion (unit majority vote) or DC 18 Deception (forging the ledger, detected on DC 16 Investigation); the savings fund grows if the party completes supply missions
   - Knowledge: who has savings deposited and how much (DC 13); which soldiers are in debt and to whom (DC 15); which debts are owed to people who would use them as leverage (including which debts connect to Brutus's network) (DC 17)
   - Default NPC: Signifer Publius Afer (new NPC; implicated in the Tribune's financial scheme in Session 2 and transferred out or arrested)
   - Vacancy consequence: unit savings fund frozen (no access without Legate's personal order); death benefits unpaid until a new signifer is appointed

5. *Cornicen* (Horn blower, battlefield signal officer)
   - Pay: *Sesquiplicarius*, 450 den/year
   - Prerequisites: Any legal status; CON 13; Performance proficiency or Musician's instrument tool; must pass practical signals test administered by the existing *cornicen*; appointed by centurion
   - Duties: sound morning *classicum* (reveille), signal formations in drill, sound the watch changes
   - Mechanic: can signal a formation change as a bonus action in combat (all allies within 60 ft who can hear shift into or out of formation without using their movement or reaction); can signal a false retreat (DC 15 Performance, opposed by enemy commander's Insight) to draw enemies out of position
   - Knowledge: the full Roman signal vocabulary and what each call means (DC 13); signals used by the Germanic tribes and what they indicate (DC 15); how to counterfeit a Roman military signal convincingly enough to cause a unit to break formation (DC 17)
   - Default NPC: Cornicen Libo (new NPC; siege casualty in Session 4)
   - Vacancy consequence: formation changes in combat require a standard action instead of bonus action; the morning watch change must be handled by voice (Perception DC 15 to hear across the fort)

**Specialist (*Immunes*) Roles:**

6. *Medicus* (Field surgeon, exempt from all fatigue duties)
   - Pay: *Duplicarius*, 600 den/year
   - Prerequisites: Any legal status; WIS 13; Medicine proficiency; Greek training preferred (character may have Healer's Kit as part of background); appointed by the *praefectus castrorum* (camp prefect), not the centurion
   - Duties: morning sick parade (examine all soldiers reporting ill), wound dressing after any combat, epidemic monitoring and quarantine decisions
   - Mechanic: can stabilize a dying creature with Medicine check (no action cost, just the check); once/day, spend 10 minutes and a healer's kit use to heal 2d6 + WIS modifier HP; can identify poison, disease, or unusual wound cause with DC 13 Medicine
   - Knowledge: field injuries, wound fever timelines, and which soldiers are currently unfit for duty (DC 13); poison identification, antidote preparation, and symptoms of the Antonine Plague vs. other fever (DC 15); Cassia's full knowledge of what the spear's influence does to human bodies at the cellular level, plus the one treatment that works (DC 17, requires Cassia's trust at Ally tier first)
   - Default NPC: Cassia (already named, already developed)
   - Vacancy consequence: no healing between sessions without downtime activity; wound infections become a real mechanical risk (Constitution save DC 12 after each session without medical care)

7. *Haruspex* (Divination specialist, reads omens and entrails)
   - Pay: *Duplicarius*, 600 den/year; plus temple stipend from the fort shrine (100 den/year additional)
   - Prerequisites: Roman citizen preferred; WIS 14; Religion proficiency; must be approved by the *collegium haruspicum* (professional divination guild based in Rome); examination required (DC 16 Religion check representing training); appointed by the legate
   - Duties: read omens before any significant military action (legally required; a commander who ignores a *haruspex*'s warning loses legal protection if the action fails); perform animal sacrifice at festivals; file *prodigia* reports (unusual omens requiring state response)
   - Mechanic: can cast *Augury* once/day without a spell slot; when performing entrail-reading before a session's main conflict, roll 1d20 secretly and give the DM the result (they use it to calibrate one encounter that session); can declare an action *nefastus* (ritually forbidden today), which gives the whole party advantage on the first saving throw of that session but removes one of the DM's encounter options
   - Knowledge: standard divination signs and their accepted interpretations (DC 13); the *libri haruspicini* (the books of divination): what the specific organs predict, full *extispicy* procedure (DC 15); the specific category of omen called *prodigium* (twelve signs in Roman military law requiring Senate response), and that Paterculus has been filing them as ordinary bad omens because he knows an official *prodigium* declaration would bring a Senate investigation to Vindolanda (DC 17)
   - Default NPC: Paterculus (already named, already developed)
   - Vacancy consequence: *Augury* unavailable; the legate cannot legally authorize a major engagement (session-level consequence: attacking without *haruspex* approval causes disadvantage on all saves for the first combat of that session)

8. *Faber* (Military engineer and smith, exempt from fatigue duties)
   - Pay: *Sesquiplicarius*, 450 den/year
   - Prerequisites: Any legal status; STR 13; Smith's Tools or Mason's Tools proficiency; demonstrated skill (practical test); appointed by the *praefectus fabrum* (chief engineer)
   - Duties: weapon maintenance inspections, fort structural repair, siege equipment construction and maintenance, supervise working parties
   - Mechanic: can craft or repair mundane weapons and armor at half cost with access to a forge; can assess structural weaknesses (DC 13 Investigation reveals weak points in wall, door, or structure); once/session, can improvise a piece of siege equipment (battering ram, caltrops, burning pitch) from available materials with a DC 14 Artisan's Tools check
   - Knowledge: current condition of the fort's walls and which sections are weakest (DC 13); what specific repairs would take what time and materials (DC 15); that the northeast foundation has been undermined by the spring below it and will not hold weight during a siege without emergency shoring (DC 17)
   - Default NPC: Faber Rufus (already named as camp trader; his OGAS in camp_economy.qmd covers his dual role)
   - Vacancy consequence: weapon repair costs double; fort structural issues worsen each session without intervention

9. *Librarius* (Administrative scribe and intelligence clerk)
   - Pay: *Duplicarius*, 600 den/year
   - Prerequisites: Must be literate in Latin; citizen preferred; INT 14; History proficiency or Calligrapher's Supplies; appointed by the *cornicularius* (senior scribe at the legate's office)
   - Duties: draft unit dispatches and orders, maintain the official roster, copy and file all incoming orders, maintain the pay ledger
   - Mechanic: can forge military documents (DC 14 Forgery check, detected on DC 15 Investigation); has access to the supply manifests and incoming dispatch copies (knows what Rome officially knows about Vindolanda); can read and produce official Latin documents that are legally binding
   - Knowledge: what is officially in the fort's dispatch records (what Rome knows and does not know) (DC 13); gaps between the official record and what the party has seen (specific things Corvinus has not reported, DC 15); the existence and contents of a sealed dispatch from Brutus's office that arrived three weeks ago and has not been opened by Corvinus (DC 17)
   - Default NPC: Librarius Nerva (new NPC; implicated in the Tribune's document forgery in Session 2, arrested or transferred)
   - Vacancy consequence: the unit's official paperwork falls to Corvinus's staff; the party loses access to incoming dispatch copies

10. *Explorator* (Scout and frontier intelligence officer)
    - Pay: *Duplicarius*, 600 den/year
    - Prerequisites: Any legal status; DEX 13; Stealth proficiency; Perception proficiency; typically recruited from provincial auxiliaries who know the local terrain; appointed by the legate's intelligence officer
    - Duties: reconnaissance beyond the fort perimeter (2-3 day patrols), tracking, reporting on Germanic movement, maintaining contact with border informants
    - Mechanic: can move at full speed without penalty in forest or wilderness terrain; advantage on Perception checks in wilderness; can identify tracks and determine how many creatures passed, their size, and approximately when (DC 12 Survival, no tool required); once/session, can call on a border informant for one piece of local intelligence (DM provides, 1d4 hours wait)
    - Knowledge: current Germanic movement patterns near Vindolanda and where the raiding parties are staging (DC 13); Vercingetorix's tribe's exact location and the route to avoid their sentinels (DC 15); where Thusnelda's scouts have been active in the past month and what they were watching (the answer: they were watching the ruins excavation) (DC 17)
    - Default NPC: Flavus (named in Session 2 cascade unlock; only available if party hit DC 17 in Session 2; otherwise the explorator role is vacant from the start)
    - Vacancy consequence: Germanic movement reports are 2 sessions out of date; the Session 3 forest journey begins with disadvantage on the first two forest event rolls

11. *Frumentarius* (Supply officer, officially; imperial intelligence agent, actually)
    - Pay: *Duplicarius*, 600 den/year from the legion; additional classified allowance from the *Princeps Peregrinorum* in Rome (the head of imperial intelligence)
    - Prerequisites: Roman citizen only; INT 13; Deception proficiency; Insight proficiency; selected by the *Princeps Peregrinorum* in Rome, not the local legate (this is a secondment, not a promotion); Corvinus did not choose this person and cannot remove them
    - Duties: officially manages grain supply manifests and convoy scheduling. Actually: monitors loyalty throughout the fort, identifies dissent, files secret reports to Rome on the legate's decisions, and watches for exactly the kind of unusual activity currently happening at the ruins
    - Mechanic: can request information from the *frumentarii* network across the empire (DM provides after 1d4 days); has a coded communication system that cannot be traced to the unit; once/session, can make a DC 13 Insight check against any named NPC to learn whether they are filing reports to Rome (this check reveals Paterculus is not; it reveals Corvinus does not know what has been reported in his name)
    - **This role is partially hidden:** The player knows they are a *frumentarius*. Other PCs know this person handles supply. The DM knows the full picture. The role entry in roles.qmd is marked as a covert specialist with a separate `<details>` block for the DM covering what this player's reports mean for Sessions 3-5.
    - Knowledge: what is in the official grain manifests and where the discrepancies are (DC 13); which soldiers have been reporting to Brutus's network and what they have said (DC 15); that the sealed dispatch from Brutus arrived before the excavation began, meaning Brutus knew about the site before Corvinus found it (DC 17)
    - Default NPC: The current *frumentarius* is an NPC named Decius Turbo (new NPC; present but not introduced until Session 2 when his role becomes relevant)
    - Vacancy consequence: Rome's intelligence feed from Vindolanda goes dark; this causes Brutus to send the Tribune earlier than planned (accelerates Session 2 timeline by one in-world week)

**Religious Roles:**

12. *Sacerdos* (Fort priest and shrine keeper)
    - Pay: Military pay at basic rate (300 den/year) plus temple stipend from the shrine (200 den/year additional)
    - Prerequisites: Any legal status; WIS 13; Religion proficiency; appointed by the legate on recommendation of the existing priest; must demonstrate knowledge of the full ritual calendar
    - Duties: maintain the fort shrine, lead daily observances, preside at funerals, certify that festival observances have been completed for official records
    - Mechanic: allies who observe your morning rites before a session (in-fiction acknowledgment) gain +1 to death saving throws for that session; can perform a last rites ritual that prevents a dead NPC from rising as a Lemur (removes the *Dishonored Rest* risk); once/session, can ask for a divine sign and receive a yes/no answer (DM decides based on current divine standing)
    - Knowledge: the full Roman religious calendar and which festivals apply to a frontier fort (DC 13); what the specific signs of active divine presence look like versus ordinary omen interpretation (DC 15); that the fort shrine has been receiving offerings from someone other than the official religious personnel, and the offering pattern matches neither Roman nor Germanic tradition (DC 17)
    - Default NPC: Paterculus (doubles as *haruspex*; if both roles are vacant, the fort's religious life collapses with morale consequences)
    - Vacancy consequence: no last rites performed for dead soldiers; morale saves are DC 15 instead of DC 14; Lemur risk for any soldier who dies during the siege

13. *Flamen Martialis* (Priest of Mars, campaign-critical role)
    - Pay: No military pay (the role is technically a civilian religious office); temple stipend from Rome (500 den/year) plus the legate's personal patronage
    - Prerequisites: Roman citizen only; free-born, not freedman; WIS 15; Religion proficiency; must worship Mars (not merely acknowledge him); extremely rare appointment, usually held at the legion level not the fort level; **this role is vacant at campaign start** and can only be filled after Session 2 when the party has sufficient access to the ritual knowledge
    - Duties: perform Mars-specific rites (not general Roman religion but the specialized frontier cult of Mars Ultor); maintain any sacred weapons or objects associated with Mars; pronounce the *devotio* (the self-sacrifice vow that invokes Mars's personal intervention)
    - Mechanic: once/session, invoke Mars directly for +1d6 damage on one weapon attack or one saving throw (Mars notices; this adds 1 to the party's collective corruption track); can perform the *devotio* as a special action (see Session 5 mechanics in chapter5.qmd); has instinctive knowledge of when Mars is actively present (no check required; the DM tells this player privately)
    - Knowledge: Mars's two faces (civic war-god and frontier avenger) and why they feel like different gods (DC 13); the frontier cult of Mars Ultor: what soldiers actually believe he wants, the specific prayer language that constitutes a binding war-vow (DC 15); the *ancilia* tradition (twelve sacred shields said to have fallen from heaven), why some priests believe the spear in the vault is one of three divine weapons that should not coexist in one place, and what happens to a *Flamen Martialis* whose god takes notice of them (DC 17)
    - Default NPC: Vacant; if a PC fills this role after Session 2, Mars takes specific note of that character in Session 4
    - Vacancy consequence: no *devotio* option in Session 5 (closes one of Option C's three arguments); Mars does not send specific signals to the party (they must read omens like everyone else)

**Support Roles:**

14. *Capsarius* (Field medic and medical orderly, under *Medicus*)
    - Pay: *Sesquiplicarius*, 450 den/year
    - Prerequisites: Any legal status; CON 12; Medicine proficiency or Herbalist Kit; trained by the *medicus* (requires Medicus's approval); appointed by the camp prefect
    - Duties: carry the *capsa* (medical supply case) in the field, perform immediate wound care before the *medicus* arrives, assist in surgery, maintain medical supply inventory
    - Mechanic: can stabilize a dying creature as a bonus action (not a full action); if no *Medicus* is present in the party, functions as basic field medic with Medicus mechanic at -1d6 healing; can administer a potion as a bonus action instead of an action
    - Knowledge: standard wound care and which injuries require the *medicus* vs. which can be handled in the field (DC 13); which plants near Vindolanda have medicinal uses (DC 15; cross-references the flora section of locations.qmd); that bog rosemary tea provides advantage against the Alp's Sleep Paralysis, which Valeria does not yet know and which the party can trade to her for Ally tier access (DC 16 Medicine + Herbalist Kit)
    - Default NPC: Capsarius Aemilia (new NPC; female, unusual but not unprecedented; daughter of a military family; present throughout; not a siege casualty unless the DM chooses)
    - Vacancy consequence: stabilizing costs a full action; potions cannot be administered to unconscious allies without a standard action

15. *Custos Armorum* (Weapons keeper and armory officer)
    - Pay: *Sesquiplicarius*, 450 den/year
    - Prerequisites: Any legal status with clean disciplinary record; STR 12; Smith's Tools or Leatherworker's Tools; must be literate enough to maintain inventory (INT 10 minimum); appointed by the centurion; background investigation by the *frumentarius*
    - Duties: daily weapons inspection, armory inventory, issue and return of weapons from the locked armory, ammunition accounting
    - Mechanic: has a key to the armory (normally locked to non-officers); knows current stock of all weapons and ammunition types; can identify a weapon's quality and condition by inspection (DC 11 check, no proficiency needed); once/session, can locate a specific weapon type within the fort's supply chain in 1 hour (barring siege conditions)
    - Knowledge: what weapons and ammunition the fort currently holds, including the expanded Roman weapons from Milestone 47 (DC 12, very accessible); which weapons are substandard, damaged, or have been substituted (DC 15); that someone has been removing pilum heads from the armory without signing them out, and the removal pattern matches the nights when the ruins access point was unsealed (DC 17)
    - Default NPC: Custos Armorum Brutianus (new NPC; has been bribed; leaves with the Tribune's party in Session 3, creating a vacancy and exposing the weapon theft)
    - Vacancy consequence: armory access requires Corvinus's personal authorization; the weapon theft is not discovered until Session 4 when inventory is taken during siege preparation

#### NPC Role Holders: Master Table (for gm_intro.qmd)

This table goes in `gm_intro.qmd` as a DM reference, hidden in a `<details>` block:

| Role | Default NPC | Session vacancy likely | Vacancy trigger |
|------|-------------|----------------------|-----------------|
| Optio | Varro | S4 (high siege risk) | Dies in breach defense; party must decide who leads |
| Tesserarius | Decanus Arvina | S3 | Leaves with Tribune; deliberate sabotage of farewell |
| Aquilifer | Gaius Metellus | S1 | Found dead at ruins entrance; opening mystery |
| Signifer | Publius Afer | S2 | Tribune's financial scandal; arrested or flees |
| Cornicen | Libo | S4 | Siege arrow casualty; horn falls in the mud |
| Medicus | Cassia | S3 or S5 | Sacrifice seed or Session 5 choice |
| Haruspex | Paterculus | S4 | Siege; he will not leave the shrine |
| Faber | Rufus (trader) | — | Survives unless specifically targeted |
| Librarius | Nerva | S2 | Forgery arrest; Tribune's exit |
| Explorator | Flavus (if unlocked) | S5 | Optional; returns from forest mission |
| Frumentarius | Decius Turbo | S3 | Revealed; players decide what to do with him |
| Sacerdos | Paterculus (doubles) | S4 | Same as Haruspex vacancy |
| Flamen Martialis | Vacant | S3 (PC can fill) | Available after grove ritual |
| Capsarius | Aemilia | — | Survives unless specifically targeted |
| Custos Armorum | Brutianus | S3 | Bribed; flees with Tribune |

#### Role Selection at Session 0

Add to `session0.qmd` (player-facing) and `gm_session0.qmd` (DM annotations):

- After character creation, each player selects a role from the 15 available
- Prerequisites must be met (stat, citizenship, proficiency)
- No two players can hold the same role (first come, first served at the table)
- If no player takes a role, the default NPC holds it and the table notes their name
- The Aquilifer role is specifically mentioned as vacant from the first scene (Gaius Metellus is dead)
- The Flamen Martialis role is specifically mentioned as not yet available (players can ask why; the answer is Session 2 content)
- The Frumentarius player gets a private card from the DM after session 0 explaining their actual mission

#### NPC Role-Holders as Peer Characters

Every NPC who holds a role is a peer, not a shopkeeper. They eat at the same table, attend the same briefings, go on the same patrols. Design principle: **a player who has not taken a role should not notice the absence, because the NPC fills it convincingly.** A player who has taken a role should feel the NPC as a colleague who has opinions about how they do the job.

**What peer behavior means in practice:**
- NPC role-holders attend every scene the PCs attend (they are part of the unit, not waiting in a shop)
- They have opinions on the party's decisions and will say so, privately or publicly
- They make their own choices when the party is not watching (Varro drills the unit at dawn whether or not anyone asks him to; Aemilia treats wounds whether or not anyone brings patients to her)
- They ask the party for things: Paterculus needs someone to assist with the festival rite; Flavus wants to know what the explorator-PC found on the north road; Arvina (tesserarius) wants help with a soldier who has been falsifying the watch log
- Their deaths carry weight because the party knew them as colleagues: Libo falling from the wall is not "the cornicen NPC died" but "Libo, who was arguing with you about the watch schedule three sessions ago, is dead"

**Peer NPC behavior table (for gm_intro.qmd):** Each NPC role-holder has a "peer behavior" entry alongside their OGAS:
- What they talk about with the party unprompted (their daily concerns, complaints, professional opinions)
- What they need from the party (a specific request they make once per session if approached)
- What they will do if ignored for a full session (they act on their own; this advances their OGAS whether or not the party engaged)
- What they notice about each PC based on that PC's role (Varro watches the *optio* PC's leadership style and has an opinion; Paterculus watches the *haruspex* PC's omen interpretation and agrees or disagrees)

**The "other player" feeling** is achieved by:
1. NPC role-holders speak in the first person, directly to PCs, not to the room
2. They remember things: "You told me last session you suspected Arvina. Were you right?"
3. They have bad days: the DM can have Cassia be short-tempered after a patient died, or have Flavus be distracted because his scouting report was ignored
4. They die like players: no off-screen death unless the story demands it; their final moments are played, not summarized

**Handoff when a role is vacant:** When an NPC role-holder dies or leaves, the DM says it directly to the players: "Libo is dead. The *cornicen* role is unfilled. Here is what that means mechanically. Here is what Libo's absence feels like in the unit." The role mechanics kick in immediately. The emotional reality is played, not skipped.

#### Build sequence for Milestone 51:
- [x] Create `roles.qmd` with all 15 role entries
- [x] Add role selection section to `session0.qmd`; update contubernium framing to vexillatio extraordinaria
- [x] Add DM role annotation section to `gm_session0.qmd`
- [x] Add NPC Role Holders master table and peer NPC behavior section to `gm_intro.qmd`
- [x] Update `_quarto.yml` to insert `roles.qmd` in Section 2 after `professions.qmd`
- [x] Cross-reference existing NPC entries in `camp_economy.qmd` to note role assignments

---

### Milestone 52 — Contubernium Reframe: The Assembled Unit ✅ COMPLETE
Goal: All player-facing and GM-facing text that currently treats the party as a standard *contubernium* (8-man tent unit) is updated to reflect the *vexillatio extraordinaria* concept. Players understand they were individually recruited, not assigned together. The historical 8-man structure is preserved as world context; the party's special status is distinct.

**Files:** `player_guide.qmd`, `player_tome.qmd`, `session0.qmd`, `gm_intro.qmd`, `gm_session0.qmd`

- [x] **Standard contubernium** — Keep the 8-man historical description in `player_tome.qmd` as world context (what a normal tent unit looks like, how they live together); do not remove or retcon this
- [x] **The party's actual status** — Add a section in `player_guide.qmd` explaining the *vexillatio extraordinaria* concept: individually summoned to the Legate's office, each for a different reason; no one told them about the others; they meet in an anteroom outside Corvinus's office on the morning of Session 1
- [x] **Why Corvinus assembled this unit** — In `gm_intro.qmd`, a DM-only section: Corvinus's reasoning for each pick (what he needed from each specialist, what he does not yet know about the *frumentarius* in his own unit, why he gave them the construction oversight cover)
- [x] **The unit has no name** — Player-facing note: the unit has no formal designation yet; naming it is an optional in-session moment during Session 1; suggest the DM leave space for it but do not script it
- [x] **Session 0 update** — Replace "how do you know each other" framing with "you do not, yet"; the session 0 questions ask who you are individually, not how the group formed; group formation is a Session 1 story beat
- [x] **The cover story** — In `gm_session0.qmd`, DM note: each PC was given a different cover reason for the summons; the *frumentarius* was told they are reviewing supply manifests; the *medicus* was told there is a worker injured in the excavation; the *explorator* was told there is a tracking assignment beyond the north gate; none of these are true; Corvinus tells them the truth in the cold open of Session 1

---

### Milestone 53 — Expanded Roman Weapons and Ammunition ✅ COMPLETE
*(Previously noted as Milestone 47 in planning; renumbered to reflect new sequencing)*

All tasks completed in a prior session as part of `roman_tactics.qmd`. Full weapon system live: sling with three ammunition types (lead shot DC 13 Con save, stone unlimited, clay incendiary), heavy/light pilum and plumbata, five melee subtypes (gladius, spatha, pugio, hasta, dolabra), arcuballista bolt, full Vindolanda stock table, and tactics integration cross-referencing formation entries and session encounters.

---

### Milestone 54 — Bestiary Tactical Expansion ✅ COMPLETE
*(Previously noted as Milestone 48)*

All creatures updated with full tactical identities in bestiary.qmd. CR increases applied (Strix CR 4, Lemur CR 1, Larvae CR 5, Alp CR 4, Draugar CR 6, Lindworm CR 10, Nix CR 5). Tactical summary card present. All unique behaviors confirmed live: Strix Blindsight/Light Seeker/Ill Omen trigger, Lemur Dishonored Rest (reforms twice), Larvae Cycling Faces + Threshold Reset, Genius Loci Compel Respect first action, Alp Mist Form as reaction, Draugar Earth Memory + 100ft territorial limit, Lindworm 50 HP water retreat, Nix Disguised Approach + Chosen Target + Unearthly Beauty disadvantage at 10min mark.

---

### Milestone 55 — Upgradable Camp and Legionary Companions ✅ COMPLETE
*(Previously noted as Milestone 49)*

*(All task items from the previous Milestone 49 entry carry forward unchanged; this renumbering reflects the new sequencing. The role system from M51 integrates directly: camp upgrade triggers should now include role-specific actions, e.g., the *faber* completing the gate repair counts as a camp upgrade trigger independent of gold spent.)*

Additional integration tasks for M55 beyond the original M49 scope:
- [x] **Role-gated upgrade triggers** — Specific upgrade triggers require the relevant role to be filled: the ballista installation requires a living *faber*; the shrine dedication requires a living *sacerdos*; the surgery upgrade requires Cassia at Trusted tier
- [x] **Role vacancy as camp degradation** — If two or more roles are vacant simultaneously, camp functions at Level 1 regardless of previous upgrades (the institution cannot maintain itself without staff)
- [x] **Companion recruitment via roles** — The *optio* role player can recruit companions as an in-role action (not just via relationship tier); the *explorator* can recruit Germanic scouts as non-legionary companions if Vercingetorix's tribe is at Trusted+

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
