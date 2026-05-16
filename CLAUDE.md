# CLAUDE.md — The Shadow of Mars Campaign Workbook

## Project Overview

A Quarto book structured as a two-part D&D 5e campaign module:
- **Part 1: Player's Workbook** — spoiler-free, read by everyone at the table
- **Part 2: GM's Workbook** — DM-only content, full NPC secrets and session design

Design philosophy: **Guy Sclanders' methodology** throughout. Every design decision should pass the Sclanders checklist below.

---

## File Structure

```
index.qmd           ← Preface (how to use the book)
player_intro.qmd    ← Spoiler-free campaign overview, setting, NPCs (names/roles only)
player_guide.qmd    ← Roman world, character creation, vexillatio extraordinaria concept
peoples.qmd         ← D&D races as Roman world cultures, legal status, province origins
skills.qmd          ← Skill system overview
session0.qmd        ← Session 0 questions (player-facing)
calendar.qmd        ← Roman calendar, festivals, the campaign window
knowledge.qmd       ← DC 13/15/17 three-tier knowledge system (barrier-gated)
player_tome.qmd     ← Deep immersion guide: how to think, talk, and act like a Roman
vindolanda_guide.qmd ← Fort Vindolanda player field manual
professions.qmd     ← Roman professions and downtime activities
roles.qmd           ← The 15 unit roles of the vexillatio extraordinaria
supplies.qmd        ← Regional supply, prices, equipment degradation
food.qmd            ← Food, drink, and rationing mechanics
roman_tactics.qmd   ← Roman military formations, expanded weapons/ammunition
bestiary.qmd        ← D&D 5e stat blocks with full tactical identities
corruption.qmd      ← Expanded corruption system (player-facing)
reputation.qmd      ← Reputation and relationship system
journal.qmd         ← Campaign journal and decision tracker
atmosphere.qmd      ← Music and sound per session
gm_intro.qmd        ← OGAS framework, central mystery, master plot, NPC skill DCs
gm_session0.qmd     ← GM facilitation guide for Session 0
skill_framework.qmd ← Unified skill interaction design principles (GM reference)
germanic_tribes.qmd ← Germanic tribes, society, runes, seiðr, and magic (GM)
locations.qmd       ← Detailed location descriptions, skill check menus, vicus, living world
camp_economy.qmd    ← Six traders, Camp Level 1-3 system, role-gated upgrades (GM)
chapter1.qmd        ← Session 1: Blood and Omens
chapter2.qmd        ← Session 2: The Chieftain's Price
chapter3.qmd        ← Session 3: Through the Dark Forest
chapter4.qmd        ← Session 4: The God's Demand
chapter5.qmd        ← Session 5: The Wrath of Mars
appendix.qmd        ← Quick reference, stat blocks, handouts 1-11
images/             ← All local image assets (downloaded from Wikimedia Commons)
handouts/           ← Rendered HTML handouts (one per appendix handout, print-ready)
gm_tools/           ← GM session reference cards (one per session, browser-tab format)
audio/              ← Ambient audio guide HTML page (audio/index.html)
Maptool/            ← MapTool VTT standalone install (see Milestone 67)
  setup.sh          ← Run once to extract, configure, and download addons
  maptool.sh        ← Launch MapTool (data stays in Maptool/data/)
  tokentool.sh      ← Launch TokenTool
  campaigns/5e/     ← Campaign .cmpgn files
  addons/           ← .rptok library tokens and .mtlib add-ons
  macros/           ← MTScript macro source files (.mts)
  tokens/npcs/      ← NPC token portrait HTML previews
  maps/             ← Map images for MapTool backgrounds
  data/             ← MapTool runtime data (gitignored; created on first launch)
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

## Completed Milestones

All content below is live in the book. No further action required.

| # | Title |
|---|---|
| 1 | Visual Foundation — images downloaded, maps embedded, GitHub Pages .nojekyll fix |
| 2 | Player's Workbook: World Depth — daily life, pantheon, equipment, Latin phrases, session 0 |
| 3 | Session Development (Sessions 2-5) — all five chapters drafted with cold opens and OGAS |
| 4 | NPC Expansion — relationship web, per-session state table, dialogue, reaction tables |
| 5 | Location Design — Vindolanda, ruins, forest, siege arc, sacred grove |
| 6 | Roman Tactics — testudo, wedge, envelopment, siege mechanics, Germanic counter-tactics |
| 7 | Bestiary — 8 creatures with stat blocks, images, propitiation table |
| 8 | Player Assistance Tome — backstory framework, speech/thought patterns, immersion tools |
| 9 | Character Knowledge Tiers — DC 13/15/17 collapsible knowledge system |
| 10 | Professions & Downtime — 10 professions, downtime activities, collegium system |
| 11 | Germanic Tribes & Magic — tribes, society, religion, runes, shamanism, magic items |
| 12 | Handouts & Props Pack — 11 handouts, player tracker, DM quick-reference |
| 13 | Final Polish & Publish — continuity audit, GitHub Pages live |
| 14 | Roman Calendar & Sacred Year — calendar mechanics, festival table, campaign window |
| 15 | Life at the Frontier: Sensory Atlas — daily schedule, food, senses, death on the frontier |
| 16 | Fort Vindolanda: Player Guide — layout, social rules, prices, dangers |
| 17 | Campaign Journal & Decision Tracker — session templates, relationship web, corruption tracker |
| 18 | Expanded Corruption System — six stages in depth, gods, resistance, recovery rules |
| 19 | Languages of the Roman World — D&D translation table, tiers by background, sacred languages |
| 20 | knowledge.qmd Overhaul — baseline preambles, three-layer system, two new categories |
| 21 | Chapter 1 Improvement Pass — chamber read-alouds, spear reveal, OGAS table, scene 4 |
| 22 | Chapter 2 Improvement Pass — Sextus mystery, Vercingetorix voice, session transition table |
| 23 | Chapter 3 Improvement Pass — forest events d8, Thusnelda expanded, sacrifice guidance |
| 24 | Chapter 4 Improvement Pass — siege read-aloud, council stakes, tunnel scenes, antechamber |
| 25 | Chapter 5 Improvement Pass — Option C expanded, corruption level 5, Mars up close, epilogue |
| 26 | Peoples of the Empire — D&D races as Roman world cultures, legal classification, hooks |
| 27 | Legal Status and Social Standing — five legal categories, rank ceilings, status mechanics |
| 28 | Regional Supply, Equipment, Fort Economy — price index, supply cycle, degradation rules |
| 29 | Food, Drink, and Rationing — daily ration, quality tiers, drink mechanics, rationing scenarios |
| 30 | The Legion and the Magical World — Roman magical doctrine, haruspex mechanics, creature classification |
| 31 | Lex Arcana Integration — Custodes concept, virtues, augury mini-game, Fatum mechanics |
| 32 | Session 0: Character Creation Guide Rewrite — personal questions, contubernium events, three questions |
| 33 | Atmosphere: Music and Sound Per Session — per-session soundscapes, player-facing ambient guide |
| 35 | Three-Barrier Knowledge + Living Camp Economy — stat gates, six traders, Camp Level 1-3 |
| 36 | GM Session 0 Guide — consent, aloud questions with annotations, private questions, Fatum cards |
| 37 | Camp NPC Full Treatment — OGAS, per-session states, voice reference, reaction tables, siege behavior |
| 38 | Unified Skill Interaction Framework — no dead ends, cascade design, temporal gates, partial success |
| 39 | The Vicus: Civilian Settlement — layout, four named civilians, information network, siege behavior |
| 40 | Deep Religion, Deep History, Magical World — Mars in 175 AD, völva, bog offerings, flora, raven network |
| 41 | Knowledge Gate Audit — all DC-gated content behind toggles, GitHub Pages verified |
| 42 | Toggle Voice Rewrite — all DM-facing collapsibles in DM voice |
| 43 | Cross-Session Integration Notes — cascade unlocks in GM book, master integration table |
| 44 | Merge Duplicate Origin Chapters — peoples.qmd authoritative, cross-reference in player_guide |
| 45 | Session 0 Questions Audit — deduplicated, each question in the right file |
| 46 | Player Tome Reorganization — three named sections, _quarto.yml reordered |
| 47 | Expanded Roman Weapons and Ammunition — sling ammunition types, pilum, arrow types, melee subtypes |
| 48 | Bestiary Tactical Expansion — distinct tactics per creature, CR increases, tactical summary card |
| 49 | Upgradable Camp and Legionary Companions — Camp Level 1-3, upgrade triggers, companion rules |
| 51 | The Role System: Vexillatio Extraordinaria — 15 unit roles with mechanics, DC knowledge, NPC holders |
| 52 | Contubernium Reframe: The Assembled Unit — vexillatio framing, Corvinus reasoning, unit has no name |
| 53 | Expanded Roman Weapons and Ammunition (renumber of 47) — confirmed live in roman_tactics.qmd |
| 54 | Bestiary Tactical Expansion (renumber of 48) — confirmed live in bestiary.qmd |
| 55 | Upgradable Camp and Legionary Companions (renumber of 49) — role-gated triggers, vacancy degradation |
| 56 | Germanic Weapons + Magical Weapons — framea, seax, francisca, angon, three NPC weapons with story properties |
| 57 | Comprehensive Weapons and Equipment Expansion — new sling ammo (whistling, inscribed, terracotta), arrow types (trilobate, barbed, scythicon), verutum, lancea, contus, falx, siege weapons (scorpio, onager, polybolos), full armor and equipment slot system (body/helmet/arms/gloves/cloak/boots/belt) |
| 58 | Shadar-kai Spartan Shadow-Cursed Origin — racial traits, five bidirectional shadow stages, Vercingetorix reaction, corruption divergence sidebar, death ruling, Session 0 private questions, chapter 4 staging |
| 59 | Starting Level and Character Advancement — Level 3 start, milestone rationale, full arc table L3-7, role/level decoupling (player_guide.qmd) |
| 60 | Role-Based Starting Equipment Packages — all 15 roles with full kit, weight totals, class substitutions, carrying loads system, three-tier role advancement (Standard/Senior), vacancy consequence table, camp-as-living-entity framework |
| 61 | Citizenship Progression as Campaign Goal — commendationes system, active status elevation track, in-play status costs, Session 3/4/5 elevation events (peoples.qmd, session0.qmd, gm_session0.qmd) |
| 67 | MapTool Standalone Setup — MapTool 1.18.6 + TokenTool extracted from .deb into Maptool/ subfolder, both with bundled JREs. MapTool.cfg patched so MAPTOOL_DATADIR points to Maptool/data/ (all state stays local). Launchers: Maptool/maptool.sh, Maptool/tokentool.sh. Addons in Maptool/addons/ (Lib_SpellLibrary 2014+2025, Lib_MonsterMaker, Lib_Date_Time.mtlib). D&D 5e campaigns in Maptool/campaigns/5e/ (Meleks Simple 5e, Automated 5e SRD, demo). dnd5eTokens/ organized by creature type. Maps in Maptool/maps/ (5 campaign-relevant images). Setup script: Maptool/setup.sh (idempotent, re-run after git clone). |
| 68 | Conflict Resolution Protocol — Established that Nextcloud creates conflicted copies when sync detects diverging edits. Correct fix: verify conflicted copies match HEAD (they always will after a commit), then git restore the rolled-back working-tree files and delete the conflicted copies. Never merge: the conflicted copy IS the committed version. |
| 69 | Map Resource Pack — Maptool/maps/download_maps.sh downloads 64 Dice Grimorium battle maps (underground/vault for Ch1, Germanic forest/swamp/river for Ch3, ritual sites/sacred grove for Ch4-5, fort/settlement/roads for Vindolanda) and 17 RPTools art packs (Phergus+Torstan markers, dungeon tiles, four Dorpond tree packs, doors/windows, Torstan map sets). Maps extract to maps/dicegrimorium/ and maps/rptools/ (both gitignored, ~240MB total). Script is idempotent — re-run after clone. Some Dice Grimorium filenames deviate from the PascalCase slug pattern; the script hardcodes those. RPTools Library tab in MapTool 1.18.6 is silently broken (UI bug, server is up); use File > Add Resource to Library > Local Directory tab and point it at maps/dicegrimorium/ or maps/rptools/ instead. |
| 70 | NPC Token Portraits — CSS-only HTML token portraits for all 6 named NPCs in Maptool/tokens/npcs/ (corvinus, cassia, varro, brutus, vercingetorix, thusnelda). Each file has a 200x200 token (circular frame with CSS portrait silhouette) and a 50x50 map-scale version. Frame colours: gold = ally, red = antagonist, grey = unknown. Stat blocks and secrets embedded. build_campaign_maps.sh copies tokens into per-session folders. |
| 71 | Session Map Tables — "Maps for This Session" reference table added to Pre-Session Preparation in all five chapter files. Each table maps scenes to specific Dice Grimorium map files in the Maptool/maps/campaign/ session folders. No playable fort interior battlemap exists in the downloaded pack; saalburg_plan.jpg is an archaeological floor plan for player orientation only. |
| 72 | knowledge.qmd Skill Barrier Format Fix — All 45 DC collapsible headers updated from bare "DC 13" to "DC 13 Intelligence (History) — Recalling [specific topic]". All "What you know without a check" bullets reformatted from *italic:* style to **bold** — style. Section 9 ability check header corrected (Intelligence (Medicine) → Wisdom (Medicine)). Chapters 2-5, roles.qmd, roman_tactics.qmd still need the same audit (planned as agent task). |
| 73 | Full NPC Token Coverage — 13 missing named NPCs added to build_campaign_maps.sh: Lucius_Tribune (Assassin), Paterculus_AugurAssist (Acolyte), Valeria_Medicus (Mage), Quartus_Quartermaster (Thug), Rufus_Smith (Gladiator), Brennus_Taberna (Commoner), Lucilla_Postwoman (Spy), Aldric_Observer (Mage), Titus_HalfGermanic (Scout), Sigrun_Trader (Tribal Warrior), Arnulf_Firekeeper (Tribal Warrior), Edda_SpearMother (Tribal Warrior), Skadi_Healer (Acolyte). Fort_Vindolanda now holds 23 named .rptok tokens. Session folders get only session-relevant tokens (S1: fort staff 15 tokens; S2: fort+road cast 15; S3: Germanic 11; S4: ritual/siege 13; S5: full resolution cast 14). Summary counter fixed to report .rptok counts. |

---

## Active Work Tracks

These are scoped and tested items ready to build out fully. Each has a proof-of-concept file already created.

### Track A: Rendered Handouts
**What:** Convert all 11 handouts from appendix.qmd into standalone HTML files with period-appropriate visual styling. Printable and shareable via MapTool's image handout feature.
**POC:** `handouts/handout_01_legates_orders.html` — wax tablet CSS, Cinzel font, Latin + translation, print-ready. Verify it renders before extending to all 11.
**To build:** One file per handout. Naming: `handout_NN_slug.html`. Style guide: wax tablet (dark red) for military orders; stone inscription (grey/off-white) for the Vault inscription (Handout 2); aged papyrus (warm tan) for letters and scrolls (Handouts 5, 7, 8); blood-on-stone for Handout 10 (Mark of Mars). Each file self-contained (no external dependencies except Google Fonts CDN, with fallbacks).
**Source:** appendix.qmd — all 11 handouts with `{.handout-card}` divs. When-to-give and how-to-present metadata is in `{.handout-meta}` divs; do not include that in the printed output.

### Track B: GM Session Reference Cards
**What:** One condensed HTML reference card per session (5 total). Designed to be open in a browser tab during play: OGAS table, scene flow, DC cheat sheet, contingency tables, three-clue status.
**POC:** `gm_tools/session01_reference.html` — two-column layout, colour-coded by check type (passive/active/key), full OGAS and refusal contingency for Session 1. Verify formatting before extending.
**To build:** Sessions 2-5. Source: chapter2.qmd through chapter5.qmd, specifically the `## DM Notes`, `### OGAS This Session`, `### Skill Audit` sections, and the `## Pre-Session Preparation` props list. Each card should fit one browser viewport without scrolling (print at 80% zoom for single A4 page).
**Key sections per card:** Scene flow (numbered), OGAS table (NPC/goal/secret), DC reference table (room/DC/skill/type/what they learn), contingency boxes (warn-coloured), corruption/vacancy/commendationes state at session start.

### Track C: MapTool Corruption + Mechanics Macros
**What:** MTScript macros for the campaign's custom mechanics, importable into MapTool via the Campaign macro panel.
**POC:** `Maptool/macros/corruption_tracker.mts` — full MTScript for a token-attached corruption tracker. Frame dialog with pip display, stage name, mechanical effect text, increase/decrease/reset buttons. Uses token property `CorruptionLevel` (Number, default 0). Requires companion macros `corruption_increase`, `corruption_decrease`, `corruption_reset` on the Campaign panel (each is 2-3 lines: get property, modify, set property).
**To build next:**
- `corruption_increase.mts` / `corruption_decrease.mts` / `corruption_reset.mts` — the button targets
- `commendationes_tracker.mts` — same pattern, tracks commendationes count per token (property: CommendationesCount), shows current count and citizenship tier (Peregrinus/Latinus/Civis) thresholds
- `role_display.mts` — campaign-level frame showing the 15 vexillatio roles, who holds each (by token name), and vacancy state (red if unfilled)
- `roman_calendar.mts` — frame showing current campaign date in Roman format (Kalends/Nones/Ides + month + year AUC), advance-day button
**MapTool property setup (add to Campaign Properties > Token Properties):** `CorruptionLevel` (Number, default 0), `CommendationesCount` (Number, default 0), `UnitRole` (String, default ""), `CitizenshipStatus` (String, default "Peregrinus").

### Track D: NPC Token Pack
**What:** Visual token portraits for the campaign's named NPCs, formatted for MapTool import (200×200 PNG with circular frame).
**POC:** `Maptool/tokens/npcs/corvinus_token.html` — CSS-only portrait (helmet silhouette, gold/red token frame), NPC stat block overlay, small 50×50 map-scale preview. Screenshot the `.token` div at 200×200 to get the import-ready PNG.
**To build:** One HTML file per major NPC, plus a batch export method. Named NPCs needing tokens: Corvinus (Sessions 1-2), Cassia Liviana (1-5), Centurion Varro (1-4), Senator Brutus (shadow presence 1-4, physical 4-5), Vercingetorix (2-5), Thusnelda (3), the Legate's rider/messenger (background), Germanic chieftain contacts. Token frame colours: gold = ally/neutral, red = antagonist, grey = unknown allegiance. Stat block data lives in gm_intro.qmd and the chapter DM Notes sections.
**Longer-term:** Script a Python/bash export using `chromium --headless --screenshot` to render the HTML tokens to PNG automatically.

### Track E: Ambient Audio Page
**What:** Single HTML page (`audio/index.html`) open in a browser tab during play. Collapsible per-session sections with track suggestions, YouTube search links, and scene-cue annotations.
**POC:** `audio/index.html` — all 5 sessions covered with track name, artist, scene use annotation, and YouTube search link buttons. Session 1 open by default; others collapsed. Dark Roman styling.
**To build:** The POC is feature-complete for the base use case. Enhancement options: (1) add actual embedded YouTube iframes once the GM identifies preferred uploads (search links are intentionally generic so they degrade gracefully if a specific upload disappears); (2) add a "Now Playing" indicator with JS localStorage so the tab remembers which session is active across browser restarts; (3) add non-YouTube fallback links (Spotify, Bandcamp) for Wardruna and Heilung who have official presences there.

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
- **DM-facing collapsibles:** Write in DM voice -- direct, first-person where natural ("Here is what I do when..."), not encyclopedia entries. The DC 17 payoff should feel like handing something valuable, not filing a report.
- **Knowledge barriers:** Three layers per entry -- (1) what every soldier knows (open), (2) DC 13/15 trained knowledge (collapsible), (3) DC 17 specialist knowledge (collapsible). No DC-gated fact in open text.

### Images
- Store all images in `images/` directory
- Embed with Quarto figure syntax: `![Caption.](images/file.ext){width=90% fig-align="center"}`
- Always include `fig-alt` for accessibility
- Attribution line immediately below each figure in italics

### Session Chapter Structure
See the Session Structure Template in the Sclanders checklist above. Chapter 1 is the reference implementation -- match its format.

### Commit Conventions
One milestone or major feature per commit. Commit message format:
```
[Milestone N] Short description of what was built

- Bullet list of changes
```
