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

### Milestone 3 — Session Development (Sessions 2–5)
Goal: Every session chapter matches Chapter 1's quality using full Sclanders methodology.

Each session needs: Strong Opening, Pressure Cooker design, scene-by-scene notes, OGAS per NPC, decision points with cascading consequences, props/handouts list.

- [ ] **Chapter 2 audit** — Does it meet the checklist? Fill gaps.
- [ ] **Chapter 3 audit** — Does it meet the checklist? Fill gaps.
- [ ] **Chapter 4 audit** — Does it meet the checklist? Fill gaps.
- [ ] **Chapter 5 audit** — Does it meet the checklist? Fill gaps.

### Milestone 4 — NPC Expansion
Goal: Any NPC can be improvised perfectly because their voice, knowledge, and agenda are fully documented.

- [ ] **Relationship web** — Visual map of who knows what about whom (faction chart)
- [ ] **Per-session NPC state table** — What each NPC knows, wants, and will do in each session
- [ ] **Sample dialogue** — 3 characteristic lines per NPC showing their voice
- [ ] **Reaction tables** — How each NPC responds to party's 3 most likely approaches

### Milestone 5 — Location Design
Goal: Every major location is described vividly enough to be run without prep.

- [ ] **Fort Vindolanda** — Detailed room/area descriptions; key locations mapped with castra_layout.svg as base
- [ ] **The Ruins Beneath** — 5-Room Dungeon structure (already started in Ch1, needs expansion)
- [ ] **The Germanic Forest** — Encounter zones, tribal camp, sacred grove
- [ ] **Rome (Session 3)** — At minimum: 3 key locations, social encounter frameworks
- [ ] **The Sacred Grove** — Final set-piece location; environmental storytelling

### Milestone 6 — Encounter Library
Goal: The DM has a full toolkit of encounters ready to drop in.

- [ ] **Combat encounter stat blocks** — All unique enemies with tactics notes
- [ ] **Social encounter frameworks** — Structured negotiation/persuasion encounters for key NPCs
- [ ] **Skill challenges** — Investigation, wilderness travel, social infiltration
- [ ] **Frontier encounter tables** — Random events for travel between locations

### Milestone 7 — Handouts & Props Pack
Goal: DM can hand players physical/visual aids at the right moment.

- [ ] **Handout 1 (Ch1)** — Legate's orders in Latin (already designed, format for print)
- [ ] **Handout 2 (Ch1)** — Gaulish rune inscription (already designed, format for print)
- [ ] **Handout 3 (Ch1)** — Omen list (already designed, format for print)
- [ ] **Player tracking sheet** — NPCs met, decisions made, corruption level, session notes
- [ ] **DM quick-reference** — Single-page: all NPC OGASes, corruption rules, spear properties
- [ ] **Campaign epilogues** — Written outcomes for each major ending path

### Milestone 8 — Final Polish & Publish
- [ ] Continuity audit: NPC actions in Sessions 3–5 reflect party choices in Sessions 1–2
- [ ] Cross-reference: all NPC secrets consistent across gm_intro and session chapters
- [ ] `quarto render --to pdf` produces a clean, printable document
- [ ] GitHub Pages deployment verified and live

---

## Conventions

### Writing Tone
- **Player sections** — Present tense, "you" voice, no spoilers. Treat the reader as a capable adult who wants enough information to make interesting characters.
- **GM sections** — Direct and practical. Short sentences. No hedging. Trust the DM to improvise; give them the raw material, not a script.
- **Read-aloud text** — Block quote format (`>`). Slow, atmospheric. Short paragraphs. Specific sensory details. End on a decision or question, never a statement.

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
