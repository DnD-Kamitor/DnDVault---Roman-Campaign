# 5 Verified NPC Scenarios & AI Simulation Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and thoroughly verify 5 interactive NPC roleplay scenarios with AI personas, GM guides, branching dialogue state machines, skill check mechanics, and an automated verification test suite.

**Domain Concept:**
The campaign features 5 central NPCs who anchor the pivotal scenes of Acts III, IV, and V:
1. **Augur Cassia** (Haruspex & Diviner) — *The Entrails of Mars* (Augury consultation, reading bird flights, Mars's hunger, maintaining divine dignity).
2. **Legate Corvinus** (Commanding Officer) — *Midnight in the Principia* (Aftermath of Varro & Lucius's deaths, secret desire to destroy the spear, fear of Brutus).
3. **Thusnelda** (Mystic of the Northern Bogs) — *The Will-o'-the-Wisp Passage* (Crossing the Black Bog, testing party motives, ancient seal of Alesia).
4. **Vercingetorix the Bound** (Eternal Vault Warden) — *The Lucidity of the Chains* (*Speak with Dead* 3-question limit, unmaking the altar chains, ash dissolution).
5. **The Avatar of Mars** (Divine Antagonist) — *The Crucible of Blood & Temptation* (Corruption Tiers 1-5 dream trial, taunting mortality, urging eternal warfare).

---

## File Structure

- `ai_personas/`:
  - `augur_cassia.json` (Existing, verified)
  - `legate_corvinus.json` (New OpenWebUI persona)
  - `thusnelda_seer.json` (New OpenWebUI persona)
  - `vercingetorix_sparring.json` (Existing, verified)
  - `whispers_of_mars.json` (Existing, verified)
- `gm_tools/scenarios/`:
  - `scenario_01_cassia_augury.md`
  - `scenario_02_corvinus_principia.md`
  - `scenario_03_thusnelda_bog.md`
  - `scenario_04_vercingetorix_lucidity.md`
  - `scenario_05_mars_crucible.md`
- `scripts/`:
  - `scenario_engine.py` (Core scenario runner & state machine)
  - `verify_npc_scenarios.py` (Verification script running automated playthroughs)
  - `play_scenario.py` (Interactive CLI tool for GM table use)
- `tests/`:
  - `test_npc_scenarios.py` (Comprehensive automated unit test suite with 25+ tests)
- Backlog:
  - `SCRUM_BACKLOG.md` (Epic 14 with Stories 14.1 through 14.6)

---

## Tasks

- [ ] **Task 1: AI Personas & NPC Lore Refinement for 5 Characters**
  - Create `ai_personas/legate_corvinus.json` with strict OGAS and post-Varro mindset.
  - Create `ai_personas/thusnelda_seer.json` with bog mysticism and ancient seal history.
  - Verify existing personas (`augur_cassia.json`, `vercingetorix_sparring.json`, `whispers_of_mars.json`).
  - Update `npcs/corvinus.json` and `npcs/thusnelda.json` with canonical continuity (Lucius dead, Varro dead, Wight connection).
  - Verify with json schema checks.
  - Commit & push: `feat(npc): define 5 interactive NPC personas for simulation engine (Task 1)`

- [ ] **Task 2: Detailed GM Scenario Guides & Branching Dialogue Trees**
  - Create `gm_tools/scenarios/scenario_01_cassia_augury.md`
  - Create `gm_tools/scenarios/scenario_02_corvinus_principia.md`
  - Create `gm_tools/scenarios/scenario_03_thusnelda_bog.md`
  - Create `gm_tools/scenarios/scenario_04_vercingetorix_lucidity.md`
  - Create `gm_tools/scenarios/scenario_05_mars_crucible.md`
  - Document setup, DCs, sensory cues, branching conditions, and outcomes.
  - Commit & push: `docs(scenarios): create detailed GM guides and branching dialogue trees for 5 scenarios (Task 2)`

- [ ] **Task 3: Scenario Engine & Automated Simulation Framework**
  - Implement `scripts/scenario_engine.py` with Scenario, Node, Choice, Check, and Persona classes.
  - Implement deterministic evaluation & mock LLM playthroughs.
  - Implement `scripts/verify_npc_scenarios.py` for headless execution.
  - Verify engine runs cleanly across all 5 scenarios.
  - Commit & push: `feat(engine): build core scenario engine and verification framework (Task 3)`

- [ ] **Task 4: Interactive CLI Player for GM Table Play**
  - Implement `scripts/play_scenario.py` with terminal UI, dice rolling (d20 + modifiers), corruption tier selector, and turn tracking.
  - Test execution with simulated stdin.
  - Commit & push: `feat(cli): create interactive GM scenario player with dice rolling & corruption tracking (Task 4)`

- [ ] **Task 5: Comprehensive Automated Unit Test Suite (25+ Tests)**
  - Implement `tests/test_npc_scenarios.py` with 25+ unit tests covering:
    - Persona structure and rules
    - Scenario graph connectivity
    - Skill check resolution
    - Guardrails (3-question limit, Corvinus secret DC, Mars corruption scaling)
    - Full simulated playthroughs of each scenario
  - Run `python3 -m unittest tests/test_npc_scenarios.py` and ensure 100% pass rate.
  - Commit & push: `test(scenarios): add 25+ automated tests for 5 verified NPC scenarios (Task 5)`

- [ ] **Task 6: Epic 14 Backlog Documentation & Full System Verification**
  - Add Epic 14 (Stories 14.1 - 14.6) to `SCRUM_BACKLOG.md` and mark complete.
  - Update `_quarto.yml` resources to include `gm_tools/scenarios/*.md`.
  - Run full discovery test suite (`python3 -m unittest discover tests -v`) verifying 140+ passing tests.
  - Commit & push: `chore(scrum): finalize Epic 14 and verify 140+ passing tests across campaign stack (Task 6)`
