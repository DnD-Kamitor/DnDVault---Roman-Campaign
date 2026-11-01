# RuFlo V3 Workflow Guide — The Shadow of Mars Campaign

This guide documents the persistent agent architecture, Guy Sclanders D&D mentorship workflow, and Autopilot persistent execution loop configured for **The Shadow of Mars Campaign Workbook** (`DnDVault---Roman-Campaign`).

---

## 1. Quick Start Cheat Sheet

```bash
# Check system health & initialized memory
ruflo init check
ruflo memory stats
ruflo swarm status

# Inspect Autopilot status & remaining tasks
ruflo autopilot status

# Configure safety bounds (iterations & timeout)
ruflo autopilot config --max-iterations 40 --timeout 180

# Enable persistent loop before launching a long goal
ruflo autopilot enable

# Spawn Guy Sclanders (The Great GM)
ruflo agent spawn -t coordinator --name great-gm

# Stop/disable Autopilot at any time
ruflo autopilot disable
```

---

## 2. Specialized Campaign Agents (`.claude/agents/`)

The default software engineering agents were replaced with 8 specialized campaign roles:

| Agent | File Path | Archetype (`-t`) | Role & Focus |
| :--- | :--- | :--- | :--- |
| `guy-sclanders` | `.claude/agents/core/guy-sclanders.md` | `coordinator` | **Lead D&D Campaign Mentor**: Guy Sclanders methodology, OGAS character dynamics, dramatic questions in combat, pressure cookers, 4-tab table deliverables. |
| `campaign-coordinator` | `.claude/agents/core/campaign-coordinator.md` | `coordinator` | **Campaign Scrum Master**: Milestone planning, epic tracking in `SCRUM_BACKLOG.md`, cross-agent task dispatch. |
| `roman-historian` | `.claude/agents/campaign/roman-historian.md` | `researcher` | **Antiquity Scholar**: 175 AD Roman Britannia, Fort Vindolanda, Cohors I Tungrorum, Latin terms, Etruscan *haruspicina*, augury, Germanic tribes. |
| `dnd-mechanics` | `.claude/agents/campaign/dnd-mechanics.md` | `architect` | **D&D 5e Rules Engineer**: Monster stat blocks, CR encounter math, 6-stage corruption system, DC 13/15/17 knowledge tiers. |
| `npc-persona-director` | `.claude/agents/campaign/npc-persona-director.md` | `coordinator` | **NPC Characterization & AI Simulation**: `ai_personas/*.json` (Cassia, Corvinus, Thusnelda, Vercingetorix, Mars), dialogue trees, `scripts/scenario_engine.py`. |
| `maptool-cartographer` | `.claude/agents/campaign/maptool-cartographer.md` | `coder` | **MapTool VTT Specialist**: `Maptool/campaigns/5e/`, `.rptok` token macros, XML properties, lighting/VBL layers, scene guides. |
| `quarto-publisher` | `.claude/agents/campaign/quarto-publisher.md` | `coder` | **Book Publisher & Layout Designer**: `_quarto.yml`, custom SCSS styling, two-column A4 print modules, responsive web layout. |
| `continuity-qa` | `.claude/agents/campaign/continuity-qa.md` | `tester` | **Test Guardian & Continuity Auditor**: `pytest` test suite execution, `CAMPAIGN_LOG.md` truth enforcement, Zero False Completion. |

---

## 3. Dynamic Keyword Routing (`.claude/helpers/router.js`)

When a user prompt or task is submitted, RuFlo automatically routes it to the optimal specialist:
* `"ask Guy Sclanders about encounter pacing"` ➔ `guy-sclanders`
* `"prep session 4 boss fight"` ➔ `guy-sclanders`
* `"balance Bone Naga statblock"` ➔ `dnd-mechanics`
* `"haruspex liver omen terminology"` ➔ `roman-historian`
* `"update Cassia dialogue tree"` ➔ `npc-persona-director`
* `"build MapTool vision blocking layer"` ➔ `maptool-cartographer`
* `"render quarto book"` ➔ `quarto-publisher`
* `"run pytest on deceased NPC status"` ➔ `continuity-qa`
* `"plan next sprint milestone"` ➔ `campaign-coordinator`

---

## 4. RuFlo Autopilot: Persistent Swarm Completion

### What It Does
Normally, an AI agent halts after finishing a single turn. **Autopilot** hooks into Claude Code's `Stop` event via `.claude/settings.json`. When an agent attempts to stop while unchecked tasks remain in markdown checklists (e.g. `SCRUM_BACKLOG.md`), RuFlo intercepts the stop and injects the next remaining tasks back into the prompt loop until all tasks are 100% complete.

### Operational Commands
```bash
# View active progress and remaining tasks
ruflo autopilot status

# Configure bounds (prevents runaway execution)
ruflo autopilot config --max-iterations 40 --timeout 180

# Turn on persistent completion
ruflo autopilot enable

# Inspect predicted next action
ruflo autopilot predict

# Inspect log of re-engagement iterations
ruflo autopilot log --last 10

# Disable persistent completion
ruflo autopilot disable
```

---

## 5. The 5 Core Good Practices

1. **Table Truth First (`CAMPAIGN_LOG.md`)**:
   Always read `CAMPAIGN_LOG.md` before altering or designing chapters. Live table history (Varro dead at the north gate, Lucius dead in the forest, Spear chest held by the party) overrides any pre-written outline.

2. **The Zero-Prep 4-Tab Delivery Standard**:
   A session chapter is only complete when the GM has four ready-to-run tabs:
   - **Tab 1: Cheat Card** (`gm_tools/cheat_card_chN.html`) — single dark viewport, fits 1080p with zero scroll, story spine, scene flow with DCs, OGAS summary.
   - **Tab 2: Print Module** (`gm_tools/chapterNN_print.html`) — A4 two-column printout with read-aloud boxes and inline stat blocks.
   - **Tab 3: MapTool Reference** (`gm_tools/chapterNN_maptool.qmd`) — scene-by-scene map files, token positions, VBL/MBL notes.
   - **Tab 4: NPC Cards** (`gm_tools/chapterNN_npcs.html`) — silhouette portraits, OGAS, voice lines, session states.

3. **Absolute Veracity (Zero False Completion)**:
   Never mark a feature or task complete without real verification output:
   - Python mechanics & tokens: `pytest`
   - Publication rendering: `quarto check` / `quarto render`
   - Browser tools: verify HTML structure and viewport CSS.

4. **Bounded Autopilot Runs**:
   Always cap iterations (`--max-iterations 30–50`) and timeouts (`--timeout 120–180`) before enabling autopilot to protect context and token budgets.

5. **Living Checklist Tracking**:
   Autopilot tracks markdown checkboxes (`- [ ]`). Only flip `- [ ]` to `- [x]` after verified deliverables are in place.

---

## 6. Launching a Goal

To launch the fully integrated autonomous run across the swarm with live publication gating:

```text
/goal Execute Session 4 & 5 Endgame Polish, Box Cataclysm Integration, Sclanders Zero-Prep Pack & Live GitBook Publication Gate:

1. Canonical Ground Truth & Continuity (Mandatory Check First):
   - Consult CAMPAIGN_LOG.md as immutable truth: Centurion Varro executed at North Gate (S1); Tribune Lucius died in northern woods ambushed by giant spiders (S3).
   - Party travels alone carrying Lucius's locked dispatch box, bronze seal ring, pre-signed citizenship letters, and Corvinus's secret orders to destroy the spear in the field.
   - Vercingetorix is an ancient enemy bound to 200-year unending war against Rome (defeated at fort in S3), waiting in the subterranean vault below (Vercingetorix Bound, CR 11) — NEVER an ally or guide.
   - Mars is genuinely Mars (diminished, corrupted, starved by Pax Romana), never an impostor.

2. The Box Cataclysm & Rivia's Fatal Mistake:
   - Reflect Rivia's action: deposited Spear of Mars into Artificer's box under dark psychic influence; after Ursula was possessed by the Goliath Berserker Greataxe in battle, Rivia mistakenly thought putting the greataxe in the box would "nullify" the dark magic.
   - The two weapons resonated violently, scorching the OTHALAN rune into the wood and projecting Mars's radiating aura:
     * +2 to Intimidation.
     * Disadvantage on calm diplomacy: in Scene 3 (Sacrifice Circle), Persuasion checks with Thusnelda have disadvantage if the box is within 30 ft.
     * Double undead detection radius: in Scene 0 (Farbog Crossing), Wights/Banshees detect the party from double range; group Stealth DC 14 is at disadvantage if box carried unshielded.
     * In Chapter 5 Scene 4 (Antechamber), Mars smells both weapons and mocks Rivia's mortal naivety ("You thought your little wooden cage would choke the flame? You fed it!").

3. Guy Sclanders Session Architecture for Chapters 4 & 5:
   - chapter4.qmd (The God's Demand: Farbog → Germanic Village → Sacred Grove → Sacrifice Circle → Bone Naga Entrance → Ossuary) and chapter5.qmd (The Wrath of Mars: Core Room → Granite Anvil Altar → Unmaking the Spear):
     * Dramatic Questions: Frame every encounter around active tension across all 11 scenes.
     * Pressure Cooker: Sinking causeway hazard (DC 12 Dex/Con), Thusnelda's 3-round ritual clock with DC 13 Wisdom corruption saves, failing core crystal necrotic pulses (DC 14 Con save after 15 rounds).
     * Three Clue Rule: Three independent avenues to locate the vault entrance, three independent avenues to learn how to break the spear.
     * OGAS per NPC: Active Objective, Goal, Agenda, Secret for Thusnelda, Bone Nagas, Chieftain Wraiths, Glabrezu, Mars, Vercingetorix Bound, Wight General, and Janus.

4. Zero-Prep Four-Tab Table Deliverables:
   - Tab 1: Cheat Cards (gm_tools/cheat_card_ch4.html and ch5.html) — Single-viewport dark theme fitting 1080p with zero scroll, 3-sentence story spine, scene flow with DCs, audio macro buttons, and OGAS table.
   - Tab 2: Print Modules (gm_tools/chapter04_print.html and chapter05_print.html) — A4 two-column printouts with read-aloud boxes, inline stat blocks, decision trees, and NPC secrets.
   - Tab 3: MapTool Reference (gm_tools/chapter04_maptool.qmd and chapter05_maptool.qmd) — Scene-by-scene map assets, grid scale (50px / 70px), token initial coordinates (X, Y), and VBL/MBL notes.
   - Tab 4: NPC Cards (gm_tools/chapter04_npcs.html and chapter05_npcs.html) — Silhouette portraits, active OGAS, voice lines, stat links, and session states.

5. MapTool VTT Assets & Campaign Synchronization:
   - Run `bash Maptool/maps/build_campaign_maps.sh` to ensure all creature and named tokens are copied cleanly to S4 and S5. Verify XML well-formedness, audio macros, and GM notes for all S4 and S5 combatants.

6. Live GitBook / GitHub Pages Publication Gate (The Final Delivery Bar):
   - Run pytest and ensure 100% green pass rate across all 147 test cases.
   - Run quarto check and render the full book to HTML (quarto render --to html).
   - Stage, commit with conventional commit format, and push to origin main.
   - Verify .github/workflows/publish.yml triggers, builds, and deploys the live Quarto/GitBook site to GitHub Pages.
   - The goal is ONLY complete when the changes are live online on the published book site.
```
