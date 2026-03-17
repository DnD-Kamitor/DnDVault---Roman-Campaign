## Shadow of Mars — Internal Work Plan

This repo already captures a huge amount of campaign content. The remaining gaps cluster around locations, table aids, and production polish. The plan below breaks the outstanding work into actionable tasks with owners (default: me), dependencies, and definition of done. Tackle them in order unless a dependency blocks progress.

### 1. Location Design Completion (Milestone 5)
- **Goal:** Every major site can be run straight from the text.
- **Files:** `locations.qmd` (or new sub-files if needed), `images/` for any new art callouts.
- **Actions:**
  1. Outline Fort Vindolanda keyed to `castra_layout.svg` (gate, principia, barracks, workshops, granaries, bath, perimeter).
  2. Detail “The Ruins Beneath” as a 5-Room Dungeon with read-alouds and challenge notes.
  3. Build Germanic Forest encounter zones, tribal camp, and Sacred Grove descriptions (connect to `chapter3.qmd`).
  4. Add Rome Session 4 locations (Forum, Subura, Palatine approach) with sensory cues and social mechanics.
- **Definition of Done:** Each location has sensory read-alouds, keyed areas, hooks to relevant chapters, and cross-links to maps or images.

### 2. Handouts & Props Formatting (Milestone 12)
- **Goal:** All eleven handouts plus trackers exist in print-ready Quarto layouts.
- **Files:** Either dedicated `handouts/handoutXX.qmd` files or a consolidated section in `appendix.qmd`; `journal.qmd` for player tracker reference.
- **Actions:**
  1. Gather existing handout text from chapters; confirm completeness.
  2. Choose format (single multi-chapter file or per-handout files) and create consistent typography.
  3. Build Player Tracking Sheet (decisions, NPCs, corruption, notes) as printable table.
  4. Build DM Quick Reference (NPC OGAS, corruption rules, spear properties) on one page.
- **Definition of Done:** `quarto render` outputs handouts with clear cut lines and attribution, ready for PDF export.

### 3. Production Polish (Milestone 13)
- **Goal:** The book renders cleanly and deploys.
- **Actions:**
  1. Continuity audit: verify NPC actions/session seeds align (log findings).
  2. Run `quarto render --to pdf` and resolve compilation issues (fonts, includes).
  3. Confirm GitHub Pages workflow succeeds (dry-run GH Actions if possible) and document verification steps in `README.md`.
- **Definition of Done:** Audit notes captured, render command succeeds locally, deployment instructions validated.

### 4. Quarto Character Sheet (Milestone 34)
- **Goal:** Campaign-specific printable character sheet + session tracker page.
- **Files:** `character_sheet.qmd`, `_character_sheet.scss`.
- **Actions:**
  1. Design layout referencing the Roman aesthetic guidelines (Latin labels, SPQR eagle watermark).
  2. Implement primary stats, corruption track, divine standing, Fatum line, province/legion fields.
  3. Add page 2 session tracker (decisions, NPCs, corruption delta, divine standing change, memorable moment).
  4. Test `quarto render character_sheet.qmd --to pdf` with both pdflatex and xelatex settings; capture notes.
- **Definition of Done:** PDF renders without layout issues, ready for printing.

### 5. QA: Cross-File Consistency & Links
- **Goal:** Ensure new chapters (calendar, Rome guide, reputation, supplies, food, etc.) interlink without dead anchors.
- **Actions:**
  1. Run `quarto check` or `quarto render` full book; fix warnings (missing references, image paths).
  2. Verify `_quarto.yml` includes all new files in correct order.
  3. Spot-check player vs. GM tone per CLAUDE.md guidelines.
- **Definition of Done:** Build passes cleanly; README documents how to replicate.

### 6. Knowledge System Expansion & Maintenance
- **Goal:** Keep `knowledge.qmd` aligned with the three-barrier design so players unlock lore via character builds and skill checks.
- **Actions:**
  1. Audit all existing categories to ensure Barrier One requirements (proficiencies/attributes/backgrounds) remain consistent with Milestone 35.
  2. Identify additional lore categories needed (e.g., specific NPC factions, magic doctrine, supply chain lore) and define Barrier One + DC 13/15/17 tiers for each.
  3. Coordinate with character creation guidance so recommended proficiencies map cleanly onto knowledge barriers.
  4. Document how GMs should adjudicate Barrier One in Session 0 (what to do if a player lacks the listed proficiency but narratively should know the fact).
- **Definition of Done:** `knowledge.qmd` covers all critical topics with baseline + collapsible tiers; README (or Session 0 notes) references the knowledge system so players understand how to engage it.

### 7. Stretch: Automation & Worker Tasks
- **Goal:** Provide instructions for GitHub Actions (if “workers” hook is desired).
- **Actions:**
  1. Draft CI task list (lint, spellcheck, render) for `.github/workflows/` if/when requested.
  2. Coordinate with maintainers before enabling, since Quarto renders can be heavy.
- **Definition of Done:** Action plan ready; actual workflow deferred until approved.

### How to Use This Plan
Work top-down. Check off subtasks in git commits referencing milestone numbers. Keep commits focused (one milestone per commit) and follow CLAUDE.md instructions for tone and structure.
