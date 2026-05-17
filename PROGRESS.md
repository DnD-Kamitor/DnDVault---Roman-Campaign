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
- [x] **Milestone 82** — MapTool monster attack macros (all sessions): 31 MTScript files covering every creature in S1-5. Each opens an HTML dialog with live dice rolls, campaign-specific DM notes, and tactical callouts. Custom bestiary creatures (Alp, Draugar, Genius Loci, Larvae, Strix, Lemur, Nix) included. S5 includes Fausta Luperci (Option A) and Mars himself (Option B, victory at 150 HP). README updated with full session tables.
- [x] **Encounter scaling (5 players)** — chapter1.qmd updated: Flooded Gallery 3→4 Shadows (Easy→Medium), XP text updated from four-player to five-player throughout. Bone Chamber (Hard 1,700 XP) and Altar Chamber (near-Deadly 1,800 XP) already appropriate for 5 players. Difficulty table in macros/monsters/README.md.
- [x] **Milestone 83** — Session 1 simulation audit: all 10 bugs fixed. BUG-1: stale Scene 3 deleted, attunement properties moved to DM Notes. BUG-2: Animated Armor ghost reference replaced with Wight + Shadows. BUG-3: Runic Corridor explicit DM answer (OTHALAN ends every row; tribal shield order confirmed). BUG-4: chain sequence added (west first, north second, east last, then master). BUG-5: Scene 5 (The Reckoning) written: Corvinus/Lucius confrontation read-aloud, four resolution branches, Cassia private word, Varro closing beat. BUG-6: Tribune Lucius introduced in Scene 1. BUG-7: Marius Coda named in read-aloud; Cultists named Titus Flavinus and Gnaeus Peregrinus. BUG-8: Fallen legionaries specified (Gaius Pullus dead, Marcus Dexter dead, Aelius Rufus dying with DC 12 Medicine and Session 2 payoff). BUG-9: Bone Chamber DM note on Titus Sempronius Caecilius as ritual feeder. BUG-10: Wight language named (pre-Roman Belgic Germanic); lamp origin attributed to Titus.

---

## Queued (in order)

- [x] **Milestone 84** — S0+S1 simulation audit: all 22 bugs fixed across gm_session0.qmd, session0.qmd, and chapter1.qmd. S0 fixes: dream mismatch explained (two escalating contacts, not same dream); Fatum card clarified in both files (one synthesis sentence per player, not three); cover story distribution trigger added; Marius Coda named in Prologue Scene 3 with Session 1 callback note; fifth fort walk location added (Armamentarium with bent blades); Quartus board entries answered (northeast construction crew, four men, Quartus crossed them when they didn't return); Scene 1-to-2 transition added (Varro waiting at barracks); Cassia absence skill check added (DC 13 Persuasion, reveals archive work); Prologue close-out text added; timing overview added at top. S1 fixes: Scene 1 principia read-aloud added; Cassia behavior corrected to OGAS (speaks to party, not Corvinus); Varro behavior corrected to OGAS (skepticism about timeline, not destruction); light source provision added (aide delivers torches at shaft); Shield Hall rune mapping added as DM note; Binding Chamber chain directions changed to spatial (left/far/right wall); Runic Corridor spatial description added (8 rows, 5 runes each, single-file); two Wight skill checks consolidated (DC 14 Persuasion or Insight, player's choice); Handout 2 trigger added to Altar Chamber; Handout 1 trigger added to Scene 1; Scene 5 Cassia entrance given physical context (east entrance, bathhouse side); level-up given in-fiction framing (Varro marks the moment).

### Other queued tasks

- [ ] **Em-dash sweep** — Pre-existing prose em-dashes in content written before this session (not the structural `**Bold** —` gate format, which is kept)
- [ ] **Task D** (roman_tactics.qmd) — Pilum bending mechanics sidebar, coronae section, auxiliaries entry
- [ ] **Task E** (bestiary.qmd) — Lemures entry with Roman context, May festival mechanics, bean ritual
- [ ] **Task F** (chapter flavor) — Selgovi NPC in chapter2.qmd; Agrona cult traces in chapter3.qmd; Alaisiagae raven omen in chapter5.qmd
- [ ] **Task G** (vindolanda_guide.qmd) — Vallum five-layer defense diagram description; road names (Via Imperialis, Via Liminalis, Via Puellarum)
- [ ] **Track A** (Handouts) — 10 remaining HTML handouts (handout_02 through handout_11); prioritise handout_02 (vault inscription) and handout_03 (omens) as S1 essentials
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
