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

## Epic 4: Session 5 Improvement Pass

**Why:** Fresh audit of all 6 Session 5 (finale) deliverables. Close to Session 4's
level of polish going in -- core scene/map/DC structure sound, epilogue does real work
closing out all three OGAS villain threads (Corvinus, Brutus, Mars) plus the
citizenship and corruption tracks.

**Status: DONE** (2026-08-22).

### Story 4.1 — Fix broken script path in chapter05_maptool.qmd
- Same copy-pasted bug as Ch3/Ch4
- **Status: DONE**

### Story 4.2 — Fix wrong Dice Grimorium folder slug
- **Independent:** one string, two occurrences (S3 and S5 blocks of
  build_campaign_maps.sh)
- **Valuable:** `ForestLabyrinthRuins` doesn't exist as a folder; the real one is
  `LabyrinthRuins`. Silently broke the Labyrinth Ruins scene's map copy in S5 (an
  explicit named scene in both chapter5.qmd and chapter05_maptool.qmd) and one
  unreferenced S3 copy.
- **Testable:** script no longer reports `[miss] LabyrinthRuins`
- **Status: DONE** — verified via script re-run

### Story 4.3 — Wire the custom Mars-vault SVGs into the scene table
- **Independent:** one file, one table + one file list
- **Valuable:** `s5_mars_confrontation.html` (the purpose-built arena/final-boss battle
  map) and `s5_mars_vault*.html` (Option B underground retreat maps) exist on disk and
  are already copied into the S5 folder by the build script, but chapter05_maptool.qmd
  routed Scenes 2-4-underground to the generic Dice Grimorium `AncientAltar`/
  `DarkTempleInterior` instead and never listed the custom SVGs at all
- **Testable:** scene table cites the custom SVGs as preferred, generic maps as fallback
  (matching the pattern already used in Ch1-4)
- **Status: DONE**

### Story 4.4 — Fix Brutus's name in chapter05_npcs.html
- **Independent:** one line
- **Valuable:** "Gaius Cornelius Brutus" there vs. "Gaius Cassius Brutus" everywhere
  else in the campaign (chapter2/3.qmd, chapter02_guide.qmd, chapter04_npcs.html, etc.)
- **Status: DONE**

### Story 4.5 — Remove duplicated Mars "Victory Condition" paragraph
- **Independent:** chapter5.qmd, one deletion
- **Valuable:** two slightly different copies of the same victory-condition text
  back to back, a copy-paste artifact from two drafting passes
- **Status: DONE**

### Story 4.6 — Add OGAS-summary cross-reference to DM Notes (low priority)
- **Independent:** additive block
- **Valuable:** every other chapter's DM Notes has an "OGAS This Session" block; Ch5's
  full OGAS content existed only in chapter05_npcs.html with no cross-reference
- **Status: DONE** — added a short resolution-focused summary (this is the finale, so
  framed as "how each villain thread resolves" rather than a full OGAS repeat)

---

## Epic 5: Sessions 1-2 Improvement Pass

**Why:** Fresh audit of Session 1 and Session 2's deliverables, closing out the backlog.
Both sessions already had dedicated improvement milestones (21, 22) and Ch1 got a full
table-readiness audit at Milestone 81 -- expected (and confirmed) to be the lightest
pass of the whole backlog.

**Status: DONE** (2026-08-22). Two real, minor findings; one optional judgment call
taken; one cosmetic item consciously deferred.

### Story 5.1 — Add missing custom SVGs to chapter1.qmd's own map table
- **Independent / small:** chapter1.qmd's "Maps for This Session" table only cited
  generic Dice Grimorium JPGs, never the four purpose-built SVGs
  (`vault_s1_overview/bone_chamber/altar_chamber/courtyard.html`) that
  `gm_tools/chapter01_maptool.qmd` already correctly names as the preferred maps for
  their scenes -- a milder version of the Ch4/Ch5 stale-table pattern (incomplete, not
  actively wrong)
- **Status: DONE**

### Story 5.2 — Add Tribune Lucius and Marius Coda to chapter1.qmd's OGAS table
- **Independent:** Lucius has a full card in `chapter01_npcs.html` and appears
  throughout Ch1 (Scene 1 arrival, Scene 5 reactions) with no OGAS cross-reference in
  the chapter itself -- same pattern already fixed in Ch3. Marius Coda (Scene 4's
  corrupted antagonist) is a judgment call, not a clear gap -- he's chapter-local, not a
  recurring campaign NPC -- but he has real narrative weight and an existing
  `chapter01_npcs.html` card, so added for consistency.
- **Status: DONE** — condensed both into chapter1.qmd's existing OGAS table format

### Deferred — S2 folder variable name mismatch
`Maptool/maps/build_campaign_maps.sh`'s S2 folder variable is still
`S2_Chieftains_Price` even though the chapter title was corrected campaign-wide to "The
Tribune's Gambit" earlier in this pass. Purely an internal path/variable name invisible
to a GM at the table -- consciously left alone rather than risk an incomplete rename
across the 4 files that reference it for a cosmetic-only fix.
## Epic 6: Skill Barrier Format Audit

**Why:** `AGENT_TASK_skill_barrier_audit.md` specs a mechanical DC-header format fix
(bare `DC 13` -> `DC 13 Ability (Skill) — trigger phrase`) across the campaign.
`knowledge.qmd` and `chapter3.qmd` (via the Session 3 pass) were already fixed.

**Status: DONE** (2026-08-22). chapter5.qmd's DC fixes landed inside the Epic 4 commit
(a concurrent process shared the same working tree). ~90 fixes in chapter1.qmd, ~61 in
chapter2.qmd, ~39 in chapter5.qmd, ~20 in roles.qmd, ~19 in roman_tactics.qmd. Verified
by hand: `<details>`/`<summary>` tag balance unchanged in all files, sample diffs
correct, remaining `DC \d+ \w+` matches are false positives (degree-of-success prose,
tool-proficiency checks, grapple DCs) rather than real gate-format violations.

---

# Second Backlog Pass: Sessions 3-5 Story Alignment (2026-08-22, later)

A live table session surfaced a major continuity gap (Varro's betrayal, Lucius's
takeover) that led to a full session working out the campaign's real throughline —
see `CAMPAIGN_LOG.md`'s "THE REAL STORY" and "What Sessions 3, 4, and 5 need to
reflect" sections before working any story below. This backlog implements that design
pass. Read the story sections first; these epics assume that context.

## Epic 7: Session 3 Story Alignment

**Why:** Session 3 already carries the Prologue, the corrected river crossing, and
updated OGAS for Varro/Lucius/Corvinus from today's earlier pass. Two threads from the
newer, deeper story (Alesia, the assassins, the six-generation guardianship) aren't
reflected yet.

### Story 7.1 — Deepen Thusnelda's seal-history dialogue
- **Independent/Small:** a few lines in chapter3.qmd's Scene 2
- **Valuable:** she currently says only "my teacher's teacher sealed it" -- thin, given
  the seal's real history (Alesia, the assassins, six generations of guardianship) is
  now settled. Should land with more weight for a GM who knows what she's guarding,
  without lecturing the players or revealing Vercingetorix's true nature early.
- **Testable:** her dialogue reads as informed by the deeper history without stating it
  outright
- **Status:** not started

### Story 7.2 — Update Vercingetorix's chapter3.qmd OGAS
- **Independent/Small:** one DM Notes entry
- **Valuable:** his current entry ("he is dying, this is his final campaign") predates
  the fuller truth (bound since 46 BC, possibly the historical man himself). The GM
  running the table needs this in the chapter, not only in CAMPAIGN_LOG.md.
- **Testable:** entry matches CAMPAIGN_LOG.md's telling; does not spill the reveal to
  players (this stays a GM-only note, not read-aloud text)
- **Status:** not started

## Epic 8: Session 4 — The Blood Cult Dungeon

**Why:** Session 4 is now confirmed as its own dungeon crawl (the forest journey leads
the party to the cult's hideout), built on 3 real maps already scouted room-by-room
(Skeleton Fortress Entrance → Blood Cult Dungeon → Castle Core Room) with a locked
monster roster (all real Monster Manual demons/undead, no generic filler, escalated via
numbers not oversized solo CR). This replaces the vaguer "cult faction in the siege"
framing Epic 8 started with. Party is level 5 crossing the marsh, level 6 for the rest
of the dungeon.

Each story below is one physical room or beat, matching the map layout. Every story
needs: a read-aloud, the monster placement + trigger condition, any RP/puzzle content
specific to that room, and a clear hand-off to the next room.

### Story 8.1 — The Marsh (entrance approach)
- **Independent:** one scene, self-contained map (part of Skeleton Fortress Entrance)
- **Valuable:** first impression of the dungeon; sets tone before the skull-mouth
  entrance
- **Small:** one encounter, one hazard terrain feature (the causeway across the toxic
  marsh)
- **Testable:** read-aloud written, 2 Banshees placed with a trigger, causeway/marsh
  hazard rules defined (what happens if a PC steps off the bone path)
- **Subtasks:**
  - Read-aloud for the approach (giant skull entrance, glowing marsh, bone causeway)
  - Trigger condition for the 2 Banshees (do they rise as the party crosses, or ambush
    from the two flanking supply caches?)
  - Hazard rule for leaving the causeway (marsh terrain effect)
  - Loot/evidence at the two supply caches (cult sentry posts) — a clue confirming this
    is the right place
- **Status:** not started

### Story 8.2 — The Ossuary (west, skull-shaped chamber)
- **Independent:** one room
- **Valuable:** first interior room, establishes the "bone" motif carried from the
  entrance
- **Testable:** read-aloud written, 2 Bone Nagas placed with a trigger, at least one
  piece of environmental storytelling (whose bones are these?)
- **Subtasks:**
  - Read-aloud for the circular skull-shaped room
  - Trigger for the 2 Bone Nagas (guarding something specific, not just standing around)
  - A discoverable detail tying these bones to the cult's earlier victims/workers
- **Status:** not started

### Story 8.3 — The Blood-Growth Rooms (east)
- **Independent:** two connected rooms
- **Valuable:** the most visually "blood cult" horror rooms on the map — needs to read
  as such in prose, not just in the monster stat block
- **Testable:** read-aloud written, Yochlol + 2 Dretches placed with a trigger,
  insect plague or the fleshy growths themselves defined as a battlefield hazard
- **Subtasks:**
  - Read-aloud describing the growths (what they are, what happens if touched/disturbed)
  - Yochlol's ambush behavior (shapechange into spider, ceiling/wall approach)
  - Dretch placement and Fetid Cloud usage
- **Status:** not started

### Story 8.4 — The Minor Altar (center)
- **Independent:** one room
- **Valuable:** first real ritual space the party sees — foreshadows the Core Room
  without being the main event
- **Testable:** read-aloud written, 2 Shadow Demons placed, the altar itself described
  (what it's for, what it shows about the cult's practice)
- **Subtasks:**
  - Read-aloud for the glowing dais + 4 pillars
  - Shadow Demon ambush behavior (Shadow Stealth between pillars, not a stand-and-fight)
  - What examining the altar reveals (a clue pointing toward the Core Room / the
    chieftains)
- **Status:** not started

### Story 8.5 — The Rune Puzzle Room
- **Independent:** one room, no combat by default
- **Valuable:** the map has a literal 4-tile rune puzzle built in; matches the
  established puzzle convention from Ch1/Ch3
- **Testable:** puzzle solution defined, a wrong-answer consequence exists, a
  fail-forward option exists (matches "no dead ends" campaign convention)
- **Subtasks:**
  - Assign meaning/order to the 4 glowing sigils
  - Define success (what it unlocks/reveals) and failure (cost, not a hard stop)
  - Decide whether this room ever has combat (an interrupted-puzzle ambush) or stays a
    pure breather beat before the gathering hall
- **Status:** not started

### Story 8.6 — The Gathering Hall (the transformed chieftains)
- **Independent:** one room, the emotional pivot of the dungeon
- **Valuable:** this is where the two cult chieftains are found — not as living
  cultists, but as 3 Wraiths (the chieftains plus what their "success" cost them). Needs
  real RP/horror writing, not just a stat block.
- **Testable:** read-aloud written, the reveal that the ritual already consumed its own
  leaders is explicit, 3 Wraiths placed with Create Specter escalation rules spelled out
- **Subtasks:**
  - Read-aloud for the hall itself (what a gathering place for a cult that's now gone
    looks like)
  - The reveal beat: evidence identifying these Wraiths as the chieftains specifically
  - Fight escalation rules (when/how Create Specter triggers, how many specters is too
    many for the table to handle)
  - What (if anything) can be learned from them if the party tries to talk first
- **Status:** not started

### Story 8.7 — The Core Room (final ritual chamber)
- **Independent:** the dungeon's capstone
- **Valuable:** this is the actual point of Session 4 — confirming what the cult was
  doing and ending it (or not)
- **Testable:** read-aloud written, Glabrezu placed as the guardian, the ritual/focus
  (the glowing crystal-star) explained mechanically, a clear hand-off to Session 5
- **Subtasks:**
  - Read-aloud for the circular sanctum, the four gargoyle reliefs, the dais and stair
  - What the crystal-star focus actually is/does (tie to "feeding Mars" mechanically)
  - Glabrezu's role: guardian of the focus, not just a random strong monster in a room
  - The session's actual payoff: what the party learns/gains here that sets up Session
    5's dungeon and the destruction ritual
- **Status:** not started

### Story 8.8 — Wire maps and tokens
- **Independent:** mechanical wiring, depends on 8.1-8.7 existing first
- **Valuable:** none of the above is usable at the table without the MapTool reference
  and build script actually pointing at it
- **Testable:** chapter04_maptool.qmd has a scene table for this dungeon; the three maps
  (Skeleton Fortress Entrance, Blood Cult Dungeon, Castle Core Room) and all new monster
  tokens (Banshee, Bone_Naga, Yochlol, Shadow_Demon, Dretch, existing Wraith/Glabrezu) are
  wired into build_campaign_maps.sh's S4 block
- **Status:** not started — do this last, once room content is locked

## Epic 9: Session 5 — Three Options With Real Teeth

**Why:** The ending currently exists as narrative framing (destroy / give to Rome / give
to Mars) without the same mechanical structure the existing Option A/B/C trial has.

### Story 9.1 — Build mechanical structure for the three horrible options
- **Independent:** chapter5.qmd's finale, largest story in this backlog
- **Valuable:** this is the campaign's actual thesis; it needs to play as three
  distinct, weighted costs, not the same fight reskinned three times
- **Estimable:** large -- likely needs its own dedicated design pass, not a quick edit
- **Testable:** each option has a distinct mechanical cost and resolution, playable
  without DM improvisation filling major gaps
- **Status:** not started

### Story 9.2 — Vercingetorix's resolution
- **Independent:** conditional on his survival to Session 5
- **Valuable:** destruction as his first chance to die since 46 BC is a real emotional
  payoff per CAMPAIGN_LOG.md; needs to be reachable in play, not just implied
- **Testable:** a concrete beat exists for this if he's present
- **Status:** not started

### Story 9.3 — Decide the Wight-general's connection to the finale
- **Independent:** a design decision plus whatever content follows from it
- **Valuable:** he's the same figure whose weapon this is; leaving the connection
  entirely unaddressed wastes a strong callback
- **Testable:** a decision is made and documented, whichever way it goes
- **Status:** not started -- decision not yet made

### Story 9.4 — Guard against reopening "who is really behind Mars"
- **Independent:** a consistency check, not new content
- **Valuable:** the impostor-god idea was explicitly rejected; nothing in Session 5
  should imply the campaign is building toward that reveal
- **Testable:** a read-through of Session 5 content finds no dangling "is this really
  Mars" thread presented as a mystery to solve
- **Status:** not started
