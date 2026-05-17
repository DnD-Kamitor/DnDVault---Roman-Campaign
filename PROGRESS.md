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

## In progress

- [ ] **knowledge.qmd toggle fix** — Proficiency/stat/role passive gates are open (visible to all players). Must wrap each `**X proficiency** — ...` / `**Stat N+** — ...` / `**X role** — ...` bullet in `<details>` collapsibles. Affects: knowledge.qmd (confirmed), potentially vindolanda_guide.qmd and other files.

---

## Queued (in order)

- [ ] **Scan for same toggle issue** in vindolanda_guide.qmd, roles.qmd, roman_tactics.qmd
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
