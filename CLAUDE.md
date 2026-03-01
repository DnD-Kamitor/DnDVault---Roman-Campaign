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

- [ ] **Handouts 1-3 (Ch1)** — Already written; format for print layout
- [ ] **Handouts 4-5 (Ch2)** — Already written; format for print layout
- [ ] **Handouts 6-7 (Ch3)** — Already written; format for print layout
- [ ] **Handouts 8-9 (Ch4)** — Already written; format for print layout
- [ ] **Handout 10-11 (Ch5)** — Already written; format for print layout
- [ ] **Player tracking sheet** — NPCs met, decisions, corruption checkbox, session notes
- [ ] **DM quick-reference** — Single page: all NPC OGASes, corruption rules, spear properties

### Milestone 13 — Final Polish & Publish ✅ COMPLETE
- [ ] Continuity audit: NPC actions consistent across all sessions
- [ ] `quarto render --to pdf` produces a clean printable document
- [ ] GitHub Pages deployment verified and live

---

## New Milestones: Player Experience & Worldbuilding Depth

The following milestones deepen what players experience at the table: richer daily life, a grounded sense of Roman time, Rome as a living city, structured tools for tracking their story, and the historical world that surrounds the campaign.

### Milestone 14 — The Roman Calendar & Sacred Year ✅ COMPLETE
Goal: Players understand Roman time. Sessions reference the calendar naturally, and players know which festivals are relevant, which gods are ascendant, and what the rhythm of Roman life sounds like.

**File:** New section in `player_guide.qmd` OR standalone `calendar.qmd` (decide at build time based on length)

- [ ] **Roman calendar mechanics** — How to give a date: Kalends, Nones, Ides; AUC dating vs. consul-year dating; how soldiers would actually say "it is the third day before the Ides of July"
- [ ] **The campaign window (April-October 175 AD)** — Which festivals fall within the five sessions; how the DM can anchor events to real festival dates
- [ ] **Mars-specific festivals** — *Quinquatria* (March 19-23): Mars' main festival, games and weapon-blessing; *Armilustrium* (October 19): purification of weapons, end of the military season; *Tubilustrium* (March 23): trumpet purification, start of campaign season
- [ ] **Other relevant festivals** — *Lemuria* (May 9, 11, 13): appeasing the restless dead (connects to Lemur creature entry); *Parentalia* (February 13-21): ancestor veneration; *Saturnalia* (December): what soldiers on the frontier do when it comes
- [ ] **Festival gameplay mechanics** — What a character gains from observing a festival properly; what bad things happen if a sacred day is desecrated; how the DM uses festival timing as a story clock
- [ ] **The Roman day** — How they divide daylight into hours, what the watches of the night are called, what soldiers say when they mean "dawn" or "midnight"
- [ ] **Historical events timeline (150-180 AD)** — A one-page player-safe timeline: Marcomannic Wars, the Antonine Plague, Marcus Aurelius' accession, the Danube campaigns; what common soldiers know vs. what is rumor

### Milestone 15 — Life at the Frontier: Sensory Atlas ✅ COMPLETE
Goal: Players can close their eyes and *be* at Vindolanda. They describe their surroundings without GM prompting because they know what the place smells like, sounds like, and costs.

**File:** New section added to `player_tome.qmd`

- [ ] **A day in the life** — Hour-by-hour schedule of a legionary at a Germanic frontier fort: before-dawn watch, morning *exercitatio*, midday rations, afternoon duties, evening at the *thermopolium*, night watch; what each part of the day feels like physically
- [ ] **Food and drink** — What soldiers actually eat: *bucellatum* (hard tack), *posca* (vinegar-water), *puls* (porridge), salt fish, olives, local game; what constitutes a good day's food vs. a bad one; what men complain about; what they pay for luxuries from traders
- [ ] **The senses of Vindolanda** — Specific sensory details: smell of the latrines, the sound of the gate changing at the third watch, the weight of armour in summer heat, the cold of a Germanic January, the noise of a contubernium (8-man tent unit) at dinner
- [ ] **Weather and seasons on the frontier** — How Germanic climate differs from Italy, Spain, or Egypt (wherever the character is from); what winter on the Danube does to morale; what rain means for a march; what it means when the river freezes
- [ ] **Entertainment and social life** — Dice games (*tesserae*), gambling debts, gossip, who is popular and who is hated in the barracks, how men deal with boredom between campaigns; the role of the fort tavern (*taberna*) and bathhouse (*balneum*)
- [ ] **Death on the frontier** — What happens when a soldier dies: how the body is prepared, who writes to the family, what the unit does collectively; funeral rites for Romans vs. what a soldier buried on the frontier gets; the emotional reality of watching your tent-mate buried far from home

### Milestone 16 — The City of Rome: Player Guide ✅ COMPLETE
Goal: When the party arrives in Rome for Sessions 3-4, players have enough grounding to roleplay the culture shock and social complexity without the GM needing to explain the city constantly.

**File:** `rome_guide.qmd` (added to Player's Workbook before Session 3)

- [ ] **First impressions** — What a frontier soldier notices first about Rome: the smell, the noise, the crowds, the height of the *insulae* (apartment blocks), the beggars, the wealth on display in the same street as utter poverty
- [ ] **The shape of the city** — The 14 Augustan regions; which matter for the campaign: the Forum Romanum (political heart), the Palatine (imperial power), the Subura (criminal underworld), the Aventine (plebeian neighborhoods, foreign temples), the Tiber docks (commerce and danger)
- [ ] **Social rules in Rome** — Who a frontier soldier can actually talk to; how patronage works in the city vs. the frontier; how to get an audience with a senator; what happens if you insult the wrong person; the danger of political informers (*delatores*)
- [ ] **Prices and money in the city** — Costs for lodging, food, bribes, lawyers, a private bath; what a soldier's pay actually buys in Rome vs. on the frontier; who gets robbed and how
- [ ] **Key locations (player-safe)** — The Forum (where to find legal help, public notices, moneylenders), the Palatine Hill approaches (where to petition the Emperor's staff), a named tavern in the Subura (where information flows freely but so do knives), the relevant temple districts
- [ ] **Navigating Roman social climbing** — Patronage dinners (*cena*): what to wear, what to say, what not to say; how to secure a letter of introduction; what favors are currency; how a frontier soldier makes himself useful to a senator without becoming a pawn
- [ ] **Dangers unique to Rome** — The night watch (*vigiles*): corrupt, dangerous; criminal *collegia* (gangs) with territorial boundaries players should not cross unknowingly; political informers who report private conversations to the imperial intelligence network; the social danger of being seen with the wrong person

### Milestone 17 — Campaign Journal & Decision Tracker ✅ COMPLETE
Goal: Players have a structured, beautiful one-page tool for each session that helps them track their own story arc, their relationships, and their corruption state.

**File:** `journal.qmd` (added to Player's Workbook, positioned last)

- [ ] **Session journal template (x5)** — One structured page per session: date (in-world and real), opening situation, decisions made (with space for "what I chose" and "why"), NPCs encountered, corruption level at end, divine standing (favored/neutral/cursed by which god), one sentence about where my character ends the session emotionally
- [ ] **Relationship web** — A blank diagram with NPC names pre-filled (major NPCs only); players mark trust level and what they owe each NPC or are owed
- [ ] **Corruption tracker** — Levels 0-5 laid out visually with experiential descriptions from `player_tome.qmd`; a checkbox per level; space to note what triggered the change
- [ ] **The Open Questions list** — Space for players to note things they do not understand yet, clues they have not followed up, and mysteries they want to pursue; this prevents "we forgot about that" between sessions
- [ ] **End-of-campaign reflection** — One page of prompts for each character after Session 5: what did your character become? What do they regret? What did they protect? What did they lose? What do they believe now that they did not believe at the start?
- [ ] **Print-ready formatting** — The journal is designed to be printed, folded, and used physically at the table; minimal color use; space for handwriting

### Milestone 18 — Expanded Corruption System (Player-Facing) ✅ COMPLETE
Goal: Corruption is the campaign's central mechanical spine. It deserves a full player-facing chapter, not just a brief mention in player_guide.qmd.

**File:** New dedicated `corruption.qmd` (Player's Workbook), replacing the brief corruption section currently in player_guide.qmd

- [ ] **What corruption is (player version)** — Written entirely from the character's perspective, no mechanical language in the opening; what it feels like to want something too much, to serve a god who is not entirely good, to notice the world bending toward you
- [ ] **The six stages in depth** — Each stage (0-5) gets a full page: the physical signs (what others notice), the psychological shift (what the character now finds normal that once horrified them), the mechanical effect (what changes in D&D terms), and a journal prompt to roleplay the transition
- [ ] **Corruption and the gods** — How each major god responds to a character's corruption level; which gods become interested at higher levels; what it means that Mars *wants* players to corrupt
- [ ] **Resisting corruption** — What works, what does not, what is too late; the difference between characters who resist together vs. those who resist alone; how the party's collective corruption level shifts the campaign's ending
- [ ] **Corruption as story, not punishment** — A direct address to players: corruption is a story tool, not a failure state; the most interesting session 5 choices come from characters who are corrupted but still trying; how to play a level-4 corrupted character at the table without being disruptive
- [ ] **Corruption recovery rules** — Specific, concrete conditions for reducing corruption at each level; which professions or downtime activities help; what gods can help and what they ask in return; the hard cap (level 5 is permanent without divine intervention)

### Milestone 19 — Languages of the Roman World (D&D Translation) ✅ COMPLETE
Goal: Every language a character might speak maps cleanly to a D&D 5e language. Players pick languages from the character creation tables in the PHB and know exactly what that means at this table.

**File:** New section added to `player_guide.qmd` (under Character Creation) or `session0.qmd` (under Before You Build)

- [ ] **The translation table** — A clear two-column table: Real-World Language → D&D Equivalent, with a note on who speaks it and where it matters in the campaign
  - *Latin* → Common (the imperial tongue; all soldiers, citizens, traders; the language of law and command)
  - *Greek* → Elvish (language of philosophy, medicine, magic, and the educated elite; doctors, priests, scholars)
  - *Germanic (Gothic/Suebian/Cherusci dialect)* → Goblin (pragmatic, guttural, underestimated by Romans; key for frontier diplomacy)
  - *Celtic (Gallic, Brittonic)* → Dwarvish (ancient, earthy, territorial; spoken by auxiliaries from Gaul and Britannia)
  - *Aramaic / Syriac* → Halfling (trade language of the eastern frontier and merchant networks)
  - *Egyptian (Demotic)* → Gnomish (arcane and priestly; spoken near temple cults and by initiates of Isis)
  - *Hebrew* → Primordial (sacred, old, carried by communities who predate Rome)
  - *Persian / Parthian* → Draconic (the language of the empire's greatest rival; rare, valued, dangerous to know)
  - *Thracian / Illyrian* → Sylvan (spoken by auxiliaries from the Balkans; wild, regional, fading)
  - *Druidic* → Druidic (unchanged; spoken by the last practitioners of Celtic sacred tradition in hidden groves)
  - *Thieves' Cant* → Thieves' Cant (unchanged; the universal language of criminal networks, from Rome's Subura to the Rhine traders)
- [ ] **Language tiers by background** — Which languages a soldier from each province realistically knows; which cost a language slot vs. which are free from background; a note that Greek is the campaign's "second language of power" and worth taking
- [ ] **Languages in play** — When it matters: German-speaking NPCs who will not speak Latin until trust is earned; Greek texts in the temple archives; a Latin document the party finds in Germanic territory that raises questions; what happens when no one speaks a language
- [ ] **Learning a new language** — Which downtime activity covers it; how many sessions it realistically takes; which NPCs can teach which languages (connects to Professions chapter)
- [ ] **Secret and sacred languages** — Runic (can be learned as a scholar language, different from casting with runes); the priestly language of the Druids (connects to Milestone 11 Germanic content); what the volva's ritual speech sounds like to someone who does not know it

### Milestone 21 — Chapter 1: Blood and Omens (Improvement Pass)
Goal: Every scene in Chapter 1 is runnable without the DM reading anything twice. The ruins feel ancient and hostile, not like a list of features.

**File:** `chapter1.qmd`

- [ ] **Underground chamber read-alouds** — Full atmospheric read-aloud text for all three chambers (Hall of Shields, Chamber of Chains, The Vault); currently bare bullet lists with no sensory language
- [ ] **The Spear reveal** — A dedicated read-aloud moment when the party first sees the spear on its altar; the current text has no such moment
- [ ] **NPC OGAS table** — Corvinus, Cassia, and Varro each need Objective / Goal / Agenda / Secret (like chapters 2-5); currently missing entirely from Chapter 1
- [ ] **Fix: Germanic runes** — Handout 2 calls the inscription "Gaulish/Celtic"; this is inconsistent with germanic_tribes.qmd which uses Elder Futhark for all in-world runic content; change to Germanic with an Elder Futhark reference
- [ ] **Scene 4 expansion** — The mad worker encounter is two bullet points; add read-aloud for his appearance, dialogue lines, and a resolution table (subdue, kill, or the worker breaks free and flees into the night)
- [ ] **Refusal contingency table** — What if the party refuses the Legate's mission? Currently nothing; add a small decision table with 3 outcomes and consequences

### Milestone 22 — Chapter 2: The Tribune's Gambit (Improvement Pass)
Goal: The dead sentry becomes a resolved mystery, not a dropped thread. Vercingetorix gets the depth he deserves. All five session endings have explicit Session 3 seeds.

**File:** `chapter2.qmd`

- [ ] **Resolve the Sextus murder** — Who killed the sentry? Currently introduced and forgotten; add a Three Clue Rule mini-mystery (answer: Brutus' sleeper agent in the fort, who also carved "ROMA CADIT" and then left with the Tribune's party)
- [ ] **Vercingetorix knowledge table** — What he specifically knows about the spear's history, where the sacred grove is, and what the destruction ritual requires; DM notes say he "knows more than any Roman" but never list what he knows
- [ ] **Expanded Vercingetorix dialogue** — 3 more sample lines beyond the battle scene; he needs a distinct voice across the whole session
- [ ] **Session 2 → Session 3 transition table** — Five distinct Session 2 endings (exposed Tribune / fought Praetorians / negotiated / fled with Vercingetorix / surrendered), each with an explicit Session 3 opening position
- [ ] **Varro contingency** — What happens to the party's position if Varro dies during the raid? He's load-bearing for the session's resolution; need a fallback

### Milestone 23 — Chapter 3: Through the Dark Forest (Improvement Pass)
Goal: The two-day forest journey feels like a journey, not a teleport to the next scene. The sacrifice mechanic has enough DM guidance to land every time.

**File:** `chapter3.qmd`

- [ ] **Forest travel events table** — A d8 table of events during the two-day journey (omens, encounters, spear manifestations, NPC moments); currently the forest travel has no mechanical content between leaving the fort and arriving at Thusnelda's scouts
- [ ] **Thusnelda expanded** — 4 more sample lines and a "what she will and will not say" table; she is the most important new NPC in the session and needs more voice
- [ ] **Sacrifice mechanic DM guidance** — "The grove knows" is correct but needs clearer DM instruction: what signs indicate the grove accepted or rejected the sacrifice? How does Thusnelda react to each offer? What if no one is willing to offer anything real?
- [ ] **Post-ritual NPC states** — A table showing where each NPC stands emotionally and practically after the spear is destroyed (or after failure); needed for Session 4 handoff
- [ ] **Influenced NPC roleplay expansion** — The private note is good; add 3 specific things the influenced player should do or say during Scenes 1-3 that feel natural but are later recognisable in hindsight

### Milestone 24 — Chapter 4: Return to Rome (Improvement Pass)
Goal: The Triumph is the campaign's most cinematic set piece. It needs sensory density. Marius Coda deserves to be more than a stat block.

**File:** `chapter4.qmd`

- [ ] **The Triumph read-aloud** — A full paragraph of sensory description: the sound of ten thousand voices, the smell of sacrifice smoke and crushed flowers, what the processional looks like from street level; this is missing entirely before Scene 3 begins
- [ ] **Marius Coda expanded** — His personal history (freed slave, devoted to Brutus, genuinely believes the Emperor must die for Rome); 2 sample dialogue lines; a non-lethal capture path and what happens if he's taken alive (he becomes a witness against Brutus)
- [ ] **The Emperor encounter** — What happens if the party reaches Marcus Aurelius directly during or after the Triumph? A short scene with his voice and his reaction to being told a Senator tried to kill him
- [ ] **Post-Triumph outcome scenes** — 2-sentence read-aloud for each major outcome (saved Emperor / wounded Emperor / Brutus arrested / Brutus escaped); currently the aftermath is handled only in a table, no narration
- [ ] **Brutus extended sample dialogue** — 3 more characteristic lines beyond the main scene; his voice needs to be consistent across the full confrontation
- [ ] **Scene 2 pacing guidance** — Which optional scenes to run, in what order, and how to read the table; currently 4 options with no DM guidance on selection

### Milestone 25 — Chapter 5: The Wrath of Mars (Improvement Pass)
Goal: Option C (the argument) gets the depth it deserves. Corruption level 5 is fully mechanised. Every ending has its own emotional beat.

**File:** `chapter5.qmd`

- [ ] **Corruption level 5 in the arena** — Currently mentioned but undefined; write out exactly what Mars does with a level-5 corrupted character: they fight for Mars in Option A (as an avatar, not themselves), they are the voice Mars uses to tempt the party in Option C, they can be reclaimed at the cost of The Chosen being two characters instead of one
- [ ] **Option C expanded** — 3 specific arguments that move Mars (with example phrasing), 3 that anger him; the failure recovery path (DC 14 demonstration check after a failed DC 17); what Mars looks like when he is actually persuaded vs. when he's humoring them
- [ ] **Post-trial narration** — Distinct read-aloud for the resolution of Option A (champion falls) and Option B (Mars calls it at 150 HP); currently these trail into Scene 3 without their own emotional beat
- [ ] **Mars up close** — When he rises from the throne in Scene 3, a proper physical description read-aloud; "immense" is insufficient for the campaign's climactic god
- [ ] **Call to War mechanic** — How the DM practically runs "Mars will call on them once"; a table of possible calls with their nature and what happens if a Chosen refuses
- [ ] **Epilogue NPC prompts** — 2 specific player questions per NPC (not just where-are-they-now but what-do-you-ask-them-and-what-do-they-say); makes the epilogue feel like a final conversation, not a debrief

### Milestone 20 — Expanded "What Your Character Knows" (knowledge.qmd Overhaul) ✅ COMPLETE
Goal: The knowledge chapter currently goes straight to ability checks. Add a layer of baseline knowledge visible to every player before the collapsible DC sections. Every entry should have three layers: (1) common knowledge no roll needed, (2) DC 13/15 trained knowledge, (3) DC 17 specialist knowledge.

**File:** `knowledge.qmd` (overhaul of existing file)

- [ ] **Add "What every soldier knows" preamble to each category** — A short paragraph (3-5 sentences) of baseline facts that require no roll; what any Roman on the frontier in 175 AD simply knows as common knowledge; visible without expanding any collapsible section
- [ ] **Roman Military Lore** — Add general knowledge preamble: the five campaign legions, why Teutoburg is still talked about 160 years later, what soldiers say about the Marcomanni; then DC 13/15/17 tiers below
- [ ] **Roman Religion** — Add general knowledge preamble: the Capitoline Triad, why you must never swear a false oath to Jupiter, how sacrifice actually works at a fort altar; then DC tiers
- [ ] **The Gods (campaign-specific)** — Add general knowledge preamble: what every soldier knows about Mars before the campaign starts; what Mars' cult at the frontier is like vs. in Rome; then DC tiers
- [ ] **Germanic Tribes** — Add general knowledge preamble: what Roman soldiers say about the Germans (mostly wrong, some right), the Teutoburg disaster as cautionary tale, what the Marcomanni want; then DC tiers
- [ ] **The Frontier** — Add general knowledge preamble: what the Limes looks like day to day, what traders bring across, what happens to soldiers who cross without orders; then DC tiers
- [ ] **Roman Law & Politics** — Add general knowledge preamble: what a legionary actually knows about the Senate and the Emperor (less than he thinks), how a Triumph is declared, what treason means; then DC tiers
- [ ] **Poisons & Medicine** — Add general knowledge preamble: what soldiers know about field injuries, wound fever, and the basic herbal kit; then DC tiers for more dangerous knowledge
- [ ] **Divine Signs & Omens** — Add general knowledge preamble: the three signs every Roman soldier watches for, what to do when lightning strikes near camp, why a crow on the left is worse than a crow on the right; then DC tiers
- [ ] **Two new categories** — Add: (1) *The Antonine Plague* (what soldiers know about the ongoing epidemic, how it affects troop strength, what "plague touched" means socially); (2) *Roman Engineering* (what any legionary knows about building roads, camps, bridges, and siege equipment; connects to Faber profession)
- [ ] **Visual design pass** — Add a brief instructional note at the top of the chapter explaining how to use it: "Read the open section without rolling. Expand the sections below when you make the listed check."

### Milestone 26 — The Peoples of the Empire: D&D Races as Roman World Cultures ✅ COMPLETE
Goal: Every D&D 5e race maps to a specific real-world culture within or adjacent to the Roman Empire in 175 AD. Players pick a race and immediately understand who that people are, where they come from, and how Rome sees them.

**File:** `peoples.qmd` (Player's Workbook, after `player_guide.qmd`)

- [ ] **Human** — Default for most Roman citizens and fully integrated provincials; subraces by province: Italian (patrician flavour, high social standing), Hispanian (pragmatic frontier stock), Gallic (Romanized Celt, earned loyalty), Pannonian (Danube-born, practically bilingual), Syrian/Judaean (educated, cosmopolitan, eastern religious complexity)
- [ ] **Elf** — Greeks and Hellenized Easterners; ancient, philosophical, long cultural memory; Greece is a province now but retains enormous cultural prestige; High Elves = Athenian intellectual class; Wood Elves = rural Greek hill communities and Anatolian interior peoples; how Greeks are perceived by Romans (admired and condescended to simultaneously)
- [ ] **Dwarf** — Germanic and Dacian mountain peoples; clan-based, forge-and-mine culture, honor through craft and kinship; Mountain Dwarves = Dacians (recently conquered, mining tradition, grudge-bearing); Hill Dwarves = Germanics partially integrated along the Limes (traders, smiths, federates); relationship with Rome: wary respect
- [ ] **Halfling** — Phoenician, Syrian, and Nabataean traders; adaptable, mercantile, present everywhere trade flows; lightfoot = Phoenician coastal traders; stout = inland Syrian merchant families; the people who know everyone, owe favors to everyone, and are underestimated by everyone; their relationship to the Roman economy
- [ ] **Gnome** — Egyptians and Alexandrians; inventors, scholars, priests of ancient mystery cults, keepers of knowledge Rome has not yet deciphered; forest gnomes = rural Nile delta peoples with ancient agricultural magic; rock gnomes = Alexandrian scholars and engineers; the Library of Alexandria as a gnomish institution
- [ ] **Half-Elf** — Peoples of mixed Roman/Greek heritage; the Romanized upper class of Greek provinces; soldiers born on the frontier between cultures; also: Dacian nobles who were granted citizenship and Roman education; characters who belong fully to neither world
- [ ] **Half-Orc** — Germanic warriors and mercenaries: the *foederati* who fight for Rome while remaining definitively not Roman; powerful, direct, operating on a different honor code; some are full federates with formal alliance treaties, some are captured warriors granted service in exchange for freedom; how Roman soldiers regard them (useful and frightening)
- [ ] **Tiefling** — Peoples from Carthage's former territories (North Africa, Spain) who carry the cultural inheritance of Baal worship and sacrifice; Rome destroyed Carthage but its traditions persisted underground; also: worshippers of chthonic gods from the eastern mystery cults; their infernal heritage represents the divine bargains their ancestors made with gods Rome considers dangerous
- [ ] **Dragonborn** — Parthians and Persians; Rome's great eastern rival; proud, ancient civilization, draconic cultural mythology; rare in the western Empire but not unknown; former Parthian nobles who came west after diplomatic exchanges or as hostages; how Rome views them: impressive, dangerous, not to be trusted with anything strategic
- [ ] **Aasimar** — Roman noble families claiming divine descent (*gens Julia* from Venus, etc.); also: children of oracular priests or vestal virgins with genuine divine heritage; their celestial nature is interpreted through Roman religion as *numen* (divine presence); Radiant Soul = families with active divine connection; Fallen = those whose divine patron has withdrawn favor
- [ ] **For each race:** Standard D&D stat block plus: (1) how Rome legally classifies this people, (2) what language they speak natively vs. what they've learned, (3) what military roles are open vs. closed to them, (4) 2 sample character hooks specific to their cultural position

### Milestone 27 — Legal Status and Social Standing in the Empire ✅ COMPLETE
Goal: A character's race and origin determines their legal and social standing in Rome. This is not a punishment mechanic: it is the texture of the world. Some doors are open; others require keys; a few are locked for good reasons that the campaign can challenge.

**File:** Section added to `peoples.qmd` (building on Milestone 26)

- [ ] **The five legal categories** — *Cives Romani* (full citizens: Italian humans, Aasimar of noble families, some Half-Elves of the educated class); *Latini* (Latin rights, partial citizenship: provincials two generations from citizenship, Half-Orcs with federate status); *Peregrini* (free non-citizens: most provincial races, Elves, Dwarves, Halflings not formally allied); *Liberti* (freedmen: any race born into slavery and legally freed; they carry the freedman stigma regardless of wealth); *Dediticii* (surrendered peoples with no Roman legal standing: Tieflings of Carthaginian descent, Dragonborn in some regions)
- [ ] **Rank ceilings by status** — Citizens can hold any rank; Latini can reach centurion but rarely tribune; Peregrini earn citizenship after 25 years of auxiliary service; Dediticii cannot hold rank without special imperial dispensation (which exists but is notable when granted)
- [ ] **How status affects character creation** — A table: race + status combination → which backgrounds are available, what starting equipment reflects their social position, which skill proficiencies come naturally from their life experience rather than training
- [ ] **Status and the campaign's themes** — The corruption mechanic interacts with status: a low-status character corrupted by Mars' spear is viewed as a threat to order; a high-status character corrupted is viewed as a tragedy. The different weights of the same corruption on different social bodies.
- [ ] **Gaining and losing status** — Military service is the primary path upward for Peregrini; the party's actions in Sessions 3-4 (stopping Brutus, saving the Emperor) can result in formal citizenship grants for non-citizen party members; losing status (desertion, treason, criminal conviction) and what that means practically

### Milestone 28 — Regional Supply, Equipment, and the Fort Economy ✅ COMPLETE
Goal: The Roman world is radically localized. What you can buy depends entirely on where you are. Fort Vindolanda has a finite stock that replenishes on irregular cycles. Players should feel the material reality of a frontier posting.

**File:** `supplies.qmd` (Player's Workbook) and DM supplement section added to `locations.qmd`

- [ ] **Price index by region** — A table: 15 key items (iron sword, leather armor, papyrus scroll, silk cloth, olive oil, wine, healing herbs, silver denarius exchange, horses, etc.) with prices in Rome vs. at Vindolanda vs. in the Germanic forest. Iron is cheap on the frontier; papyrus is expensive; silk is nearly unavailable; local game is free if you can catch it.
- [ ] **Fort Vindolanda's current stock** — The quartermaster's inventory at campaign start, skill-gated: DC 10 Persuasion or History to ask basic questions; DC 14 Investigation to see the full ledger; DC 17 Sleight of Hand or Deception to access the officer-only supply store. Categories: weapons and armor (limited), medical supplies (adequate), food rations (3 weeks at full strength), luxury goods (officer reserve, locked), tools and construction (plentiful)
- [ ] **The supply cycle** — How supply convoys work: a wagon train arrives every 4-6 weeks from the nearest major fort; it carries grain, replacement weapons, payroll (copper and silver), and whatever the quartermaster managed to requisition. Players can intercept or influence a supply convoy as a downtime or side activity.
- [ ] **Supply missions as adventure hooks** — The convoy is late. Why? Three hooks per session: S1 (the excavation crew's tools were in the late shipment -- pressure on the Legate to proceed without proper equipment); S2 (the Tribune commandeered part of the shipment for his Praetorians); S3 (no supplies reach a party in the forest -- they're living on what Vercingetorix's tribe provides); S4-5 (Rome has everything, but the party can't access it without the right social keys)
- [ ] **Equipment degradation and repair** — Armor takes damage over the campaign. After each combat session involving multiple hits: the DM may rule one piece of armor or a weapon has taken damage (reduced AC by 1 or -1 to attack rolls). The *Faber* profession repairs this during downtime; a frontier posting makes replacement difficult.
- [ ] **Exotic goods and what they mean** — Items that reach the frontier despite cost and difficulty: eastern spices (status symbols, gift for a Germanic chieftain), Alexandrian glass (luxury), Germanic amber (magical component, also valuable trade good), Parthian silk (so expensive at the frontier it is genuinely noteworthy if a soldier owns any)

### Milestone 29 — Food, Drink, and Rationing ✅ COMPLETE
Goal: A dedicated player chapter grounding the campaign in the material reality of eating and drinking in the Roman world. Players should feel the pleasure of good food after hardship and the grinding reality of field rations.

**File:** `food.qmd` (Player's Workbook) -- note: sensory food content from player_tome.qmd can be cross-referenced but this chapter goes deeper with mechanics

- [ ] **The daily ration (baseline)** — Exact quantities: 800g *frumentum* (grain), 60ml olive oil, salt, *posca* mixed on demand; what this costs in *sestertii* per day and how it compares to civilian food prices; how to prepare it in the field (millstone required for flour; baking tiles; field oven construction as a group activity)
- [ ] **Food quality tiers** — Four tiers with mechanical effects: Starvation rations (1 level exhaustion per day without a CON save), Field rations (baseline, no effect), Good rations (remove 1 exhaustion per long rest), Feast (advantage on Persuasion and Performance checks for 8 hours as social currency); what earns each tier in play
- [ ] **Germanic frontier food** — What the local environment provides that is not in official rations: hunting (elk, boar, rabbit), foraging (wild garlic, mushrooms, berries), Germanic traders (barley beer, dried meat, smoked fish, honey); how to integrate this into sessions without turning the game into a survival sim
- [ ] **Drink in depth** — *Posca* (daily soldier drink, not enjoyed), *cervisia* (Germanic barley beer, available from traders, intoxicating faster than wine), wine (rationed, officer-quality wine is a DM bribe currency), mead (Germanic festive drink, encountered in tribal settings), spring water (test before drinking; the frontier has parasites)
- [ ] **Rationing as story** — A supply shortage is not just a logistics problem; it is a morale crisis, a social hierarchy test (who gets the last good rations?), and an opportunity for the party to demonstrate or fail at leadership; 3 rationing scenarios with mechanical stakes and narrative consequences
- [ ] **Equipment for eating and cooking** — What a soldier carries: *patera* (bronze mess bowl), *urceus* (water jug), knife (not a weapon; a tool), millstone fragment (shared by the *contubernium*), fire-starting kit; what they can't carry but want: a proper brazier, a second pot, anything that makes the posca more bearable; equipment weight and pack-load rules adapted for Roman kit

### Milestone 30 — The Legion and the Magical World ✅ COMPLETE
Goal: The Roman legion is one of the most sophisticated military machines in history. It should also be sophisticated about the existence of magic and magical creatures, because in this world those things are real and the army has had 700 years to develop doctrine for dealing with them.

**Files:** New section in `roman_tactics.qmd` (Player's Workbook); DM supplement section added to `gm_intro.qmd`

- [ ] **Official Roman magical doctrine** — The legion acknowledges three categories: *Res Divinae* (divine interventions: augury, portents, the gods' direct actions), *Magia Licita* (licit magic: haruspicy, augury, temple rites, *haruspex* battlefield support), *Magia Illicita* (forbidden magic: necromancy, binding spirits, foreign curse-magic). The *haruspex* is an official army role. The necromancer is a death sentence.
- [ ] **The *haruspex* in the field** — D&D mechanics: the army's battlefield diviner (use *Divination Wizard* subclass flavor); what they can do (Augury 1/day, identify magical creatures as a bonus action with History DC 13, provide the formation bonus "Blessed Standard" once per short rest); how they're deployed (attached to cohort command, not combat line); what happens when they die (morale check for the entire unit, DC 12 Wisdom or Frightened for one round)
- [ ] **Anti-magical formation doctrine** — The legion's empirically developed responses to magical threats: against flying creatures (*ballista* elevation tables; *pilum* volleys in arcs; the "tortoise-and-poke" variant of testudo for overhead attacks); against undead (sacred fire from the camp altar counts as magical fire for damage purposes; the *aquila* standard within 30 feet gives advantage on saving throws against fear effects); against illusion (any soldier who has served 10+ years has advantage on Wisdom saves vs. illusion -- you've seen enough things in the forest to know that what you see is not always what is there)
- [ ] **Creature classification in Roman military records** — How the legion categorizes the creatures from the Bestiary: *Lemures* and *Larvae* are classified as *Umbrae* (shades) and handled by the *haruspex*; the *Genius Loci* is classified as *Numen Loci* and negotiated with rather than fought where possible; the *Strix* is classified as a *Monstrum* and hunted; the *Alp* is classified as *Pestilentia Nocturna* and treated with protective rites; Draugar are classified as *Barbari Mortui* and handled with fire; the *Lindworm* has a dedicated multi-cohort protocol
- [ ] **The *Spolia Opima* for magical kills** — A special military honor exists for soldiers who kill a commanding officer of the enemy in single combat; adapt this for magical creatures: killing a creature above CR 5 in the bestiary earns a specific commendation recorded in the legion's *acta diurna*, the title *Bestiae Victor* (beast-slayer), and a bonus of 50 *denarii* from the legion's special fund. Three confirmed kills: permanent advantage on Intimidation against mundane soldiers.
- [ ] **Magical creature encounters in each session** — Brief DM notes for each session chapter: which creatures might appear as optional encounters, how the Roman doctrine above changes those encounters, what the soldiers' reaction to each creature type would be (trained response vs. panic)

### Milestone 31 — Lex Arcana Integration ✅ COMPLETE
Goal: Borrow the best systems from the *Lex Arcana* tabletop RPG (an Italian RPG set in an alternate Roman Empire where Rome never fell). Adapt its investigative structure, custodian role, and virtue mechanics into this campaign's D&D 5e framework.

**File:** New section in `gm_intro.qmd`; player-facing summary in `player_guide.qmd`

- [ ] **The Custodes concept** — In *Lex Arcana*, the *Cohors Auxiliaria Arcana* are special imperial investigators with authority crossing provincial lines. Adapt: the party is designated as *Exploratores Extraordinarii* after Session 1 (Corvinus formalizes this to give himself deniability). This gives them: authority to investigate without explaining themselves, access to temple records and military archives normally closed to line soldiers, and the specific problem of being accountable directly to the Senate (which Brutus exploits in Session 4)
- [ ] **Roman virtues as character mechanics** — *Lex Arcana* uses seven Roman virtues (*Virtus, Pietas, Fides, Iustitia, Clementia, Frugalitas, Dignitas*) as personality mechanics. Adapt: each virtue functions as a once-per-session advantage trigger when the character acts in accordance with that virtue. A character who acts *against* their declared virtue in a significant moment takes -2 to the relevant ability checks until they perform an act of atonement.
- [ ] **Augury as structured mini-game** — *Lex Arcana* has a detailed augury system. Adapt for D&D 5e: the *haruspex* player (or any character with Religion proficiency) can perform an augury once per session as a structured activity taking 30 minutes of in-game time. Roll Religion DC 13/15/17; on success, the DM answers one question with increasing specificity: "will this action lead to success or failure," "what is the nature of the obstacle," "what specific thing will make the difference." On failure: the omens are unclear (*auspicia turbata*) and the character cannot attempt augury again until the next session.
- [ ] **Investigation structure** — *Lex Arcana* builds missions around the Three Clue Rule but formalizes it as phases: *Investigatio* (gather evidence), *Deliberatio* (analyze and form a theory), *Actio* (act on the theory). Add these phase markers to the existing Three Clue Rule sections in Chapters 2, 3, and 4: each clue gathered moves the party forward one phase; attempting *Actio* before completing *Deliberatio* is possible but harder (add +3 to all relevant DCs)
- [ ] **Destiny mechanics** — *Lex Arcana* gives each character a *Fatum* (fate statement) from the start. Adapt: each player writes a one-sentence fate for their character at Session 0: "I will die in service of something greater than ambition" or "I will see Rome from the inside before I die" or "I will make a choice that the histories will remember." These are player-authored. The DM should ensure the campaign creates a moment where each Fatum is tested. At Session 5: which characters fulfilled their Fatum? What does that earn them? (See epilogue mechanics.)

### Milestone 32 — Session 0: Character Creation Guide (Rewrite) ✅ COMPLETE
Goal: Session 0 currently gives players too much influence over the campaign's pre-set structure. Rewrite it as a character creation guide that asks meaningful personal questions (who are you, what do you fear, what do you love) without inviting players to co-design plot.

**File:** `session0.qmd` (full rewrite)

- [ ] **Opening framing** — Replace the current "let's build this campaign together" framing with "let's build characters who will be interesting inside this campaign." The campaign's structure is set; the characters' interior lives are the players' domain. These are different things and both matter.
- [ ] **Character concept questions (replace plot questions)** — Who were you before the legion? What do you regret? What do you love that you don't talk about? What would you die for? What would you refuse to do even under orders? What does your character think honor means, and has life ever tested that definition?
- [ ] **Relationship web (replace "how do you know each other")** — The party is a *contubernium*: they've served together. The question is not how they met but what they've been through together. A structured list of shared events to choose from: "you pulled them out of a collapsed trench," "you covered for them when they missed a patrol," "you watched them do something you can't forget." Each player chooses one shared event for each other player -- you don't all need to agree on the same events.
- [ ] **The three questions** — At the end of Session 0, each player answers three questions aloud: (1) "What does your character want to prove on this campaign?" (2) "What are they afraid will happen?" (3) "What will they protect, no matter what?" The DM writes these down. They are the basis for the Fatum from Milestone 31 and the personalized sacrifice prompt in Session 3.
- [ ] **Remove:** Collaborative campaign setting choices, "what kind of tone do you want," enemy design questions, anything that implies the campaign plot is adjustable. The campaign is fixed. The characters are flexible. Make this distinction clear.

### Milestone 33 — Atmosphere: Music and Sound Per Session ✅ COMPLETE
Goal: Each session has a recommended soundtrack and ambient sound layer. The DM can open these before the session and let them run.

**File:** Section added to each session chapter's Pre-Session Preparation section; also a standalone `atmosphere.qmd` in Player's Workbook (ambient sounds only, not DM-specific)

- [ ] **Session 1 (Blood and Omens):** Ambient: stone corridors, distant water drip, low wind; the fort's morning noise (crows, trumpet, footsteps on stone); descent into the vault (silence, single heartbeat pulse). Music: Hans Zimmer's *Gladiator* score (specifically "The Battle" and "Elysium") or Nils Frahm for the vault scene. YouTube/Spotify search terms to include.
- [ ] **Session 2 (The Tribune's Gambit):** Ambient: fort courtyard, horses, soldiers' voices; night raid (Germanic war drums, arrow impacts, shouting). Music: Wardruna's *Yggdrasil* album for the Germanic raid sequence; something tense and political (Jóhann Jóhannsson) for the Tribune scenes.
- [ ] **Session 3 (Through the Dark Forest):** Ambient: deep forest soundscape (Teutoburg ambience, old-growth trees, no birds); river crossing (fast water, distant pursuit); the sacred grove (absolute silence, then a low harmonic tone). Music: Heilung's *Ofnir* album throughout; specifically "Othan" for the grove ritual.
- [ ] **Session 4 (Return to Rome):** Ambient: city of Rome at dawn (carts, voices, distant temple bells, crowd noise); the Triumph (crowd roar, trumpets, drums). Music: *Rome: Total War* soundtrack for the arrival; something urban and dangerous for the Subura scenes (Ennio Morricone).
- [ ] **Session 5 (The Wrath of Mars):** Ambient: arena black sand (low wind, no crowd, silence that has weight); divine presence (sub-bass rumble, harmonics). Music: Wardruna's "Helvegen" for the epilogue; the opening of the Triumph from Session 4 for any flashback moments.
- [ ] **Player-facing version** — A page in `atmosphere.qmd` giving players the ambient sound playlists for the settings they're in, framed as worldbuilding: "what Fort Vindolanda sounds like," "what the Teutoburg Forest sounds like at night," "what Rome smells and sounds like." No DM-specific track notes.

### Milestone 34 — Quarto Character Sheets
Goal: A printable, fillable D&D 5e character sheet adapted for this campaign, rendered as a PDF via Quarto's LaTeX pipeline. Designed to be printed, physically filled in, and used at the table.

**File:** `character_sheet.qmd` (standalone, separate from the main book) + `_character_sheet.scss` for styling

- [ ] **Research the Quarto PDF approach** — Use the method from https://nrennie.rbind.io/blog/pdf-quarto/making-pretty-pdf-quarto/ as a starting point; the sheet should use LaTeX layout for precise field placement, with fillable boxes and lines
- [ ] **Campaign-specific fields** — Replace generic PHB fields with campaign-adapted versions: "Province of Origin" instead of generic backstory, "Legion and Rank" instead of organization, the Corruption Track (six checkboxes, 0-5), "Divine Standing" (favored/neutral/cursed + god name), "Fatum" (one line for the character's fate statement from Milestone 31)
- [ ] **Roman aesthetic** — Border treatment mimicking Roman stone inscription style; the SPQR eagle as a watermark; field labels in Latin with English in parentheses (*Nomen* (Name), *Provincia* (Origin), *Gradus* (Rank)); column layout matching Roman text conventions
- [ ] **Second page: Session tracker** — One section per session (5 total): decisions made, NPCs met, corruption delta (+/-), divine standing change, one memorable moment. This replaces the `journal.qmd` session pages as a more compact alternative.
- [ ] **Build and render test** — Confirm `quarto render character_sheet.qmd --to pdf` produces a clean, printable output with all fields correctly positioned; test with both pdflatex and xelatex engines



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
