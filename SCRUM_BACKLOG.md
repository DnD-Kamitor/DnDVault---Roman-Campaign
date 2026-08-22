# Shadow of Mars — SCRUM Backlog

Living backlog for campaign improvement work. Organized as Epics with INVEST-scored
Stories. Update status inline as stories complete. Superseded stories get struck through,
not deleted, so the history of what was tried stays visible.

INVEST = Independent, Negotiable, Valuable, Estimable, Small, Testable. Each story below
states its INVEST case briefly; if a story can't clear all six, it gets split before work
starts.

---

## Epic 1: Repo Hygiene

**Why:** `.git` is 2.3GB, tracked working tree is 1.8GB. `Maptool/maps/Public/` (1.3GB,
156 files) is untracked-anywhere-in-code dead weight. Several duplicate/backup `.cmpgn`
files and a couple of stale scratch docs add noise. `demo5e.cmpgn` at 99MB sits right at
GitHub's 100MB hard file limit.

**Status: DONE** (2026-08-22)

### Story 1.1 — Untrack dead weight and delete stale scratch docs
- **Independent:** pure git/file operations, no content dependency
- **Negotiable:** exact file list open to revision
- **Valuable:** stops future repo bloat, removes confusing/superseded docs
- **Estimable:** ~30 min
- **Small:** one commit
- **Testable:** `git status` clean, files gone, `.gitignore` covers the untracked paths
- **Acceptance criteria:** `Maptool/maps/Public/`, backup/duplicate `.cmpgn` files, and
  tracked `__pycache__/*.pyc` are untracked and gitignored; `PROGRESS.md`, `WORKPLAN.md`,
  `fort_vindolanda_prompt.md`, `exampleniceattack.md`, `gm_tools/cheat_card_ch1_finish.html`
  are deleted (all confirmed superseded by CLAUDE.md's own milestone table / the live
  cheat card).

### Story 1.2 — Rewrite git history to reclaim the space
- **Independent:** depends on 1.1 landing first (need the current tree clean)
- **Negotiable:** tool choice (git-filter-repo) is fixed, exact blob list follows 1.1
- **Valuable:** shrinks `.git` from 2.3GB permanently, not just stops growth
- **Estimable:** ~20 min
- **Small:** one operation + force-push
- **Testable:** `du -sh .git` shrinks materially; `git log` still walks cleanly;
  push/clone succeeds
- **Acceptance criteria:** history rewritten with `git-filter-repo` to strip the Story 1.1
  paths from every commit; force-pushed to `origin/main`. **Any other clone of this repo
  (other machines, other sessions) must delete and re-clone — a `git pull` will not work
  cleanly against rewritten history.**
- **Result:** `.git` went from 2.3GB to 370MB (also caught `Books/` — 171MB of dead PDF
  history not in the original Story 1.1 scope, added to the purge). A full pre-rewrite
  bundle backup was taken before touching history. Still-tracked, still-live campaign
  files (`5juliromans.cmpgn`, `RomanCampaign.cmpgn`, the `Meleks`/`JMR` variants) were
  left untouched — ambiguous ownership, real risk of losing live game state, out of
  scope for an automated pass. Worth a manual look if further shrinkage is wanted.

---

## Epic 2: Session 3 Improvement Pass

**Why:** Fresh audit of all 6 Session 3 deliverables (`chapter3.qmd` +
`gm_tools/chapter03_{guide,maptool,npcs,print}` + `cheat_card_ch3.html`). The three
story holes from `GM_UPGRADE_PLAN.md` (S3→S4 transition, sacrifice tiers, influenced-NPC
note) are already implemented — not in scope here. This pass is reconciliation and
polish, not a rewrite.

**Status: DONE** (2026-08-22). Hilde, Aldric, and Arnulf now appear in `chapter3.qmd`
Scene 2/3b text (not just as unused `chapter03_npcs.html` cards), Cassia has a full OGAS
entry + npcs.html card, `chapter03_maptool.qmd` and `build_campaign_maps.sh` were updated
to match, and the cheat card's token lists were synced to match.

### Story 2.1 — Fix broken script path in MapTool reference
- **Independent / Small:** one-line fix
- **Valuable:** a GM following the reference cold hits a dead path
- **Testable:** path resolves to a real file
- **Acceptance criteria:** `gm_tools/chapter03_maptool.qmd` points to
  `Maptool/maps/build_campaign_maps.sh`, not `Maptool/build_campaign_maps.sh`
- **Status: DONE**

### Story 2.2 — Remove contradictory "Wight placeholder" token note
- **Independent / Small:** one-line fix
- **Valuable:** Scene 4 row contradicts Scene 5's correct Stone_Golem token count
- **Testable:** no remaining reference to Wights as golem placeholders in Scene 4
- **Status: DONE**

### Story 2.3 — Add missing Tribune Lucius OGAS entry
- **Independent:** additive, no other file depends on it
- **Valuable:** he appears throughout the chapter (cast table, dialogue, citizenship
  co-sponsor mechanic) with no OGAS — every appearing NPC should have one per the
  Sclanders checklist
- **Estimable/Small:** one OGAS block
- **Testable:** entry present in DM Notes alongside Vercingetorix/Thusnelda/Mars/Brutus
- **Status: DONE**

### Story 2.4 — Reconcile the NPC roster across the 3 GM-tool files
- **Independent:** touches chapter3.qmd, chapter03_maptool.qmd, chapter03_npcs.html
  together as one unit of work (can't split further without leaving inconsistency)
- **Valuable:** the highest-value finding in the audit — Hilde (alternate clue-2 path for
  identifying the influenced PC), Aldric (planted Brutus informant), and Arnulf
  (bog-offering-pole caretaker) have full written OGAS cards sitting in
  `chapter03_npcs.html` that no GM running from the chapter text would ever see. This is
  real Three-Clue-Rule content going to waste. Cassia has the reverse problem: a card in
  `chapter03_print.html` but not in `chapter03_npcs.html`.
- **Estimable:** ~1-2 hours (requires reading the existing cards, deciding wire-in vs.
  cut, then editing 3 files consistently)
- **Testable:** every NPC named in any one of the 3 files appears consistently in all 3
- **Status: DONE**

### Story 2.5 — Trim cheat_card_ch3.html to one viewport
- **Independent:** self-contained HTML file
- **Valuable:** CLAUDE.md's core cheat-card rule ("no scrolling to see all scenes") is
  violated at 728 lines with zero `<details>` elements
- **Estimable:** ~1 hour
- **Testable:** structural parity with Ch1/Ch2 cheat cards (collapsed contingencies,
  3-sentence story box, scene flow visible without expanding anything)
- **Status: NO CHANGE NEEDED.** Checked Ch1/Ch2/Ch4 for comparison first: all of them
  use the identical tabbed-SPA pattern (~15 tab buttons, one `.tab-pane.active` visible
  at a time, zero `<details>` elements, 550-730 lines). This *is* the project's actual
  one-viewport convention -- each tab is its own scrollable pane, so "no scrolling to see
  all scenes" already holds structurally. The original audit finding assumed the literal
  `<details>` wording in CLAUDE.md without cross-checking sibling chapters; rewriting Ch3
  alone would have made it inconsistent with every other chapter for no real gain.

---

## Epic 3: Session 4 Improvement Pass

**Why:** Fresh audit of all 6 Session 4 deliverables. Much cleaner starting point than
Session 3 -- NPC roster, DC format, cheat card structure, and print-module
standalone-ness all checked out clean with no work needed.

**Status: DONE** (2026-08-22).

### Story 3.1 — Fix broken script path in chapter04_maptool.qmd
- Same copy-pasted bug as Ch3's Story 2.1 (`Maptool/build_campaign_maps.sh` instead of
  `Maptool/maps/build_campaign_maps.sh`)
- **Status: DONE**

### Story 3.2 — Replace stale "Maps for This Session" table in chapter4.qmd
- **Independent:** one table, one file
- **Valuable:** highest-value finding of this epic. chapter4.qmd's own prep section
  described a forest/grove ritual scene (`ForestRitualSite`, `DruidCircle`, `SacredTree`,
  `DryadGrove`, `IslandRuins`...) that doesn't exist anywhere in the actual chapter --
  leftover from an earlier draft before the tunnel sequence (Sunken Armory / Choking Hall
  / Elder Stair) was built. A GM trusting chapter4.qmd's own table over the correct
  `gm_tools/chapter04_maptool.qmd` would load entirely the wrong maps for Scene 3.
- **Testable:** table matches chapter04_maptool.qmd's scene list
- **Status: DONE** — replaced with the siege / council / 3 tunnel SVGs / antechamber list

### Story 3.3 — Drop dead-weight map copies from build_campaign_maps.sh's S4 block
- **Independent:** same root cause as 3.2 -- `CaveTunnelsVol3`, `DungeonVol2`,
  `ForestRuins`, `ForestLabyrinthRuins`, `s4_sacred_grove`, `s4_sacred_grove_overview`
  (the last two are actually Ch3 grove assets per CLAUDE.md's own map list) were being
  copied into `S4_The_Gods_Demand/` despite no Session 4 scene using them
- **Testable:** script still runs clean, S4 folder map count drops accordingly
- **Status: DONE** — S4 folder went from 22 maps to 15; script verified to still run clean

---

## Backlog (not yet started)

- **Epic 4: Session 5 Improvement Pass** — fresh audit pending
- **Epic 5: Sessions 1-2 Improvement Pass** — fresh audit pending (lower priority; both
  already had a dedicated improvement milestone)
- **Epic 6: Skill Barrier Format Audit** — `AGENT_TASK_skill_barrier_audit.md` already
  specs this; covers chapter1/2/4/5.qmd, roles.qmd, roman_tactics.qmd (knowledge.qmd and
  chapter3.qmd are done)
