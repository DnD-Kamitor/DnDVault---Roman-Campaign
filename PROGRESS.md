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

---

## Queued (in order)

### Session 1 simulation audit — bugs found (chapter1.qmd)

These were found by running a full mental simulation of Session 1. Ordered by severity.

- [ ] **S1-BUG-1: Delete stale Scene 3** — Lines 703-721 of chapter1.qmd are a leftover from an earlier draft. They re-describe the spear with different mechanics (+2 weapon, 1d8 necrotic, different whisper quotes) that contradict the fuller altar chamber content above. Delete Scene 3 and fold its spear attunement properties into the Altar Chamber section and DM Notes where they belong.
- [ ] **S1-BUG-2: Fix Animated Armor ghost reference** — Skill Audit line 888: "the Animated Armor in the Vault does not activate until..." — the vault redesign removed Animated Armor. Replace with correct text referencing the Wight and Shadows.
- [ ] **S1-BUG-3: Specify Runic Corridor safe path** — The chapter says "the shield arrangement maps to the rune sequence" but never provides the actual sequence. A DM at the table cannot run this puzzle. Add an explicit DM note: which tribal order from the Shield Hall maps to which rune per row (e.g. Marcomanni → TIWAZ, Cherusci → HAGALAZ, etc.), and confirm OTHALAN ends each row.
- [ ] **S1-BUG-4: Specify Binding Chamber chain sequence** — "Three outer chains, in a specific order, then the central chain." The order is never given. Add one line: e.g. "leftmost → rightmost → centre, then the master chain." Simple and memorable.
- [ ] **S1-BUG-5: Write Scene 5 (Conclusion)** — After the Berserker fight the chapter ends with 4 bullet questions and "Advance to Level 4." No scene. Add: Corvinus's reaction when the party returns with the spear (read-aloud + branching responses for give vs. refuse); Tribune Lucius's arrival (he is mentioned in the Skill Audit but never introduced in the narrative); what happens if the party refuses to hand over the spear; level-up framing.
- [ ] **S1-BUG-6: Introduce Tribune Lucius in Scene 1** — The Skill Audit temporal gate (line 927) references Lucius arriving during Scene 1 and changing Corvinus's body language. He is never introduced in the scene text. Add a one-paragraph arrival: when, who he is, what he says, how Corvinus reacts.
- [ ] **S1-BUG-7: Name the Berserker and the Cultists** — Marius Coda (the Berserker's name, established in prior work) does not appear anywhere in chapter1.qmd. The chapter tells the DM to "note their names for Session 2" about the two Cultists but provides no names. Add Marius Coda to Scene 4, give the two Cultists Roman names.
- [ ] **S1-BUG-8: Define fallen legionaries in Scene 4** — "Three fallen legionaries" in the Scene 4 read-aloud are neither alive nor dead. If a player reaches for a Medicine check, there's no guidance. Specify: e.g. two dead, one dying (DC 12 Medicine to stabilise), and give the dying soldier a name for potential Session 2 payoff.
- [ ] **S1-BUG-9: Answer the active ritual feeder** — The Medicus collapsible in the Bone Chamber reveals fresh bodies placed within the last five years and a maintained offering cycle. Who has been doing this? Add a DM note with an answer (candidate: a Germanic priest operating inside the vicus, or Cassia's predecessor).
- [ ] **S1-BUG-10: Specify Wight's language + oil lamp origin** — (a) The Wight speaks in "a language three of you do not understand." Name it (pre-Roman Germanic, extinct dialect, no living speaker). (b) The Binding Chamber oil lamp is "still full." Who refilled it through the chain-puzzle lock? Add one DM note sentence each.

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
