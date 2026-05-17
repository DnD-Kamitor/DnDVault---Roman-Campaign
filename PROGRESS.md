# Session Progress

Last updated after each completed task. Check here to see current status.

---

## Done this session

- [x] **Milestone 79** — Source book integration (Glory of Rome + Lex Arcana Britannia): Coronae, Lemures, Belatucadrus in knowledge.qmd; Peoples Near the Vallum + Alaisiagae + Agrona in germanic_tribes.qmd; Vindolanda decline narrative + Belatucadrus shrine in vindolanda_guide.qmd
- [x] **fort_vindolanda_prompt.md** — Generation prompt for Fort Vindolanda (4591 chars)
- [x] **Style cleanup** — Removed all `---` dividers and prose em-dashes from all .qmd files
- [x] **Books/ gitignore** — PDFs removed from tracking
- [x] **Milestone 80** — GitHub CI `if: success()` guard; professions.qmd campaign hooks rewritten (removed 8 plot spoilers: Brutus named, Marius Coda named, chapter callouts, replica spear, Brutus agents, Brutus cult in Collegium section)

---

## Done this session (continued)

- [x] **Milestone 81** — knowledge.qmd: 60 passive gates converted to `<details>` collapsibles; intro text updated. vindolanda_guide.qmd: 41 passive gates converted. All .qmd files: zero remaining open passive gate bullets.
- [x] **Milestone 82** — MapTool monster attack macros (Session 1): shadow_attacks.mts, ghoul_attacks.mts, ghast_attacks.mts, wight_attacks.mts, berserker_attacks.mts, cultist_attacks.mts, skeleton_attacks.mts. Each opens an HTML dialog with live dice rolls and campaign-specific behaviour notes. Import via Campaign Macros panel; select token then click macro button.
- [x] **Encounter scaling (5 players)** — chapter1.qmd updated: Flooded Gallery 3→4 Shadows (Easy→Medium), XP text updated from four-player to five-player throughout. Bone Chamber (Hard 1,700 XP) and Altar Chamber (near-Deadly 1,800 XP) already appropriate for 5 players. Difficulty table in macros/monsters/README.md.

---

## Queued (in order)
- [ ] **Em-dash sweep** — Pre-existing prose em-dashes in content written before this session (not the structural `**Bold** —` gate format, which is kept)
- [ ] **Task D** (roman_tactics.qmd) — Pilum bending mechanics sidebar, coronae section, auxiliaries entry
- [ ] **Task E** (bestiary.qmd) — Lemures entry with Roman context, May festival mechanics, bean ritual
- [ ] **Task F** (chapter flavor) — Selgovi NPC in chapter2.qmd; Agrona cult traces in chapter3.qmd; Alaisiagae raven omen in chapter5.qmd
- [ ] **Task G** (vindolanda_guide.qmd) — Vallum five-layer defense diagram description; road names (Via Imperialis, Via Liminalis, Via Puellarum)
- [ ] **Track A** (Handouts) — 10 remaining HTML handouts (handout_02 through handout_11)
- [ ] **Track B** (GM reference cards) — Sessions 2–5
- [ ] **Track C** (MapTool macros) — corruption_increase/decrease/reset.mts, commendationes_tracker.mts, role_display.mts, roman_calendar.mts
- [ ] **Encyclopaedia Arcana** (Spanish ed.) — De Re Militari translation still pending

---

## Format rules (quick ref)

- No em-dashes in prose. Use colon, semicolon, or comma instead.
- No `---` dividers in .qmd files.
- `**Bold** — description` in bullet gate format is structural — preserve it.
- Passive gate collapsible format:
  ```html
  <details>
  <summary><strong>History proficiency</strong></summary>
  
  Gate content here.
  
  </details>
  ```
- DC gate format: `<details><summary><strong>DC 13 Intelligence (History) — trigger phrase</strong></summary>`
