"""
test_npc_scenarios.py — Automated verification test suite for the 5 interactive
NPC scenarios, roleplay state machines, OpenWebUI AI personas, and GM scenario guides.

Part of Epic 14.
"""

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

from scripts.scenario_engine import (
    ALL_SCENARIO_BUILDERS,
    Scenario,
    ScenarioState,
    build_scenario_01_cassia,
    build_scenario_02_corvinus,
    build_scenario_03_thusnelda,
    build_scenario_04_vercingetorix,
    build_scenario_05_mars,
)


class TestNPCScenarios(unittest.TestCase):
    """Automated test suite verifying the 5 NPC scenarios & AI simulation engine."""

    def setUp(self):
        self.persona_files = {
            "cassia": REPO_ROOT / "ai_personas" / "augur_cassia.json",
            "corvinus": REPO_ROOT / "ai_personas" / "legate_corvinus.json",
            "thusnelda": REPO_ROOT / "ai_personas" / "thusnelda_seer.json",
            "vercingetorix": REPO_ROOT / "ai_personas" / "vercingetorix_sparring.json",
            "mars": REPO_ROOT / "ai_personas" / "whispers_of_mars.json",
        }
        self.guide_files = {
            "s1": REPO_ROOT / "gm_tools" / "scenarios" / "scenario_01_cassia_augury.md",
            "s2": REPO_ROOT / "gm_tools" / "scenarios" / "scenario_02_corvinus_principia.md",
            "s3": REPO_ROOT / "gm_tools" / "scenarios" / "scenario_03_thusnelda_bog.md",
            "s4": REPO_ROOT / "gm_tools" / "scenarios" / "scenario_04_vercingetorix_lucidity.md",
            "s5": REPO_ROOT / "gm_tools" / "scenarios" / "scenario_05_mars_crucible.md",
        }

    # ── 1. PERSONA SCHEMA & RULE VERIFICATION ─────────────────────────────────

    def test_01_all_5_persona_json_files_exist_and_valid(self):
        """All 5 persona files exist and parse as valid JSON."""
        for name, path in self.persona_files.items():
            self.assertTrue(path.is_file(), f"Persona file missing: {path}")
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIsInstance(data, dict)

    def test_02_all_5_personas_have_required_openwebui_fields(self):
        """All 5 personas follow OpenWebUI standard schema."""
        required_keys = {"id", "name", "meta", "params"}
        for name, path in self.persona_files.items():
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertTrue(required_keys.issubset(set(data.keys())), f"Missing keys in {name}")
            self.assertIn("system", data["params"])
            self.assertIn("description", data["meta"])

    def test_03_corvinus_persona_system_prompt_rules(self):
        """Corvinus persona includes post-Varro context, Lucius death, and secret desire to unmake spear."""
        with open(self.persona_files["corvinus"], "r", encoding="utf-8") as f:
            data = json.load(f)
        sys_prompt = data["params"]["system"]
        self.assertIn("Varro", sys_prompt)
        self.assertIn("Lucius", sys_prompt)
        self.assertIn("Senator Brutus", sys_prompt)
        self.assertIn("secretly want", sys_prompt.lower())
        self.assertIn("contubernium", sys_prompt.lower())

    def test_04_thusnelda_persona_system_prompt_rules(self):
        """Thusnelda persona includes Black Bog, ancient Alesia oath, and amber token lore."""
        with open(self.persona_files["thusnelda"], "r", encoding="utf-8") as f:
            data = json.load(f)
        sys_prompt = data["params"]["system"]
        self.assertIn("Black Bog", sys_prompt)
        self.assertIn("Alesia", sys_prompt)
        self.assertIn("teacher's teacher", sys_prompt.lower())
        self.assertIn("amber", sys_prompt.lower())

    # ── 2. GM SCENARIO GUIDES VERIFICATION ────────────────────────────────────

    def test_05_all_5_scenario_markdown_guides_exist_in_gm_tools(self):
        """All 5 GM scenario documentation markdown files exist in gm_tools/scenarios/."""
        for name, path in self.guide_files.items():
            self.assertTrue(path.is_file(), f"Scenario guide missing: {path}")
            self.assertGreater(path.stat().st_size, 500, f"Guide too small: {path}")

    def test_06_scenario_markdown_guides_have_read_aloud_and_mechanics(self):
        """All 5 scenario guides include Read-Aloud text and Branching Dialogue sections."""
        for name, path in self.guide_files.items():
            content = path.read_text(encoding="utf-8")
            self.assertIn("Read-Aloud", content, f"{name} missing Read-Aloud")
            self.assertIn("Branching Dialogue", content, f"{name} missing Branching Dialogue")
            self.assertTrue(
                "Skill Checks" in content or "Question Log" in content or "Unmaking Ritual Mechanics" in content,
                f"{name} missing mechanics or skill check section",
            )

    def test_07_scenario_engine_builders_registered(self):
        """ALL_SCENARIO_BUILDERS registers all 5 scenarios."""
        expected_keys = {
            "scenario_01_cassia",
            "scenario_02_corvinus",
            "scenario_03_thusnelda",
            "scenario_04_vercingetorix",
            "scenario_05_mars",
        }
        self.assertEqual(set(ALL_SCENARIO_BUILDERS.keys()), expected_keys)

    # ── 3. SCENARIO 01 (CASSIA) GRAPH & BRANCHES ─────────────────────────────

    def test_08_scenario_01_cassia_graph_structure(self):
        """Scenario 1 graph contains required nodes and choices."""
        sc = build_scenario_01_cassia()
        self.assertEqual(sc.initial_node_id, "n_greet")
        self.assertIn("n_mars_hunger", sc.nodes)
        self.assertIn("n_veiled_warning", sc.nodes)
        self.assertIn("n_rebuke", sc.nodes)
        self.assertIn("n_blessing", sc.nodes)

    def test_09_scenario_01_cassia_religion_success_path(self):
        """Scenario 1: Successful Religion check awards GRANTED_AUSPICES."""
        sc = build_scenario_01_cassia()
        st = sc.start()
        st, msg = sc.choose(st, "c1_omens", roll_override=15)
        self.assertEqual(st.current_node_id, "n_mars_hunger")
        st, msg = sc.choose(st, "c_prayer")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "GRANTED_AUSPICES")

    def test_10_scenario_01_cassia_religion_failure_path(self):
        """Scenario 1: Failed Religion check leads to VEILED_WARNING."""
        sc = build_scenario_01_cassia()
        st = sc.start()
        st, msg = sc.choose(st, "c1_omens", roll_override=5)
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "VEILED_WARNING")

    def test_11_scenario_01_cassia_disrespect_path(self):
        """Scenario 1: Failed Persuasion check when challenging rites leads to HARUSPEX_REBUKE."""
        sc = build_scenario_01_cassia()
        st = sc.start()
        st, msg = sc.choose(st, "c2_challenge", roll_override=8)
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "HARUSPEX_REBUKE")

    # ── 4. SCENARIO 02 (CORVINUS) GRAPH & BRANCHES ───────────────────────────

    def test_12_scenario_02_corvinus_graph_structure(self):
        """Scenario 2 graph contains required nodes and choices."""
        sc = build_scenario_02_corvinus()
        self.assertEqual(sc.initial_node_id, "n_greet")
        self.assertIn("n_lucius_honor", sc.nodes)
        self.assertIn("n_secret_revealed", sc.nodes)
        self.assertIn("n_pact_accepted", sc.nodes)

    def test_13_scenario_02_corvinus_pact_of_deniability_path(self):
        """Scenario 2: Delivering Lucius box with high Persuasion secures PACT_OF_DENIABILITY."""
        sc = build_scenario_02_corvinus()
        st = sc.start()
        st, _ = sc.choose(st, "c1_lucius_box", roll_override=14)
        self.assertEqual(st.current_node_id, "n_lucius_honor")
        st, _ = sc.choose(st, "c_push_secret", roll_override=17)
        self.assertEqual(st.current_node_id, "n_secret_revealed")
        st, _ = sc.choose(st, "c_accept_pact")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "PACT_OF_DENIABILITY")
        self.assertTrue(st.flags.get("deniability_pact"))

    def test_14_scenario_02_corvinus_defensive_dismissal_path(self):
        """Scenario 2: Failed confrontation on Varro leads to COLD_DISMISSAL."""
        sc = build_scenario_02_corvinus()
        st = sc.start()
        st, _ = sc.choose(st, "c2_varro_treason", roll_override=10)
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "COLD_DISMISSAL")

    # ── 5. SCENARIO 03 (THUSNELDA) GRAPH & BRANCHES ──────────────────────────

    def test_15_scenario_03_thusnelda_graph_structure(self):
        """Scenario 3 graph contains required nodes and choices."""
        sc = build_scenario_03_thusnelda()
        self.assertEqual(sc.initial_node_id, "n_greet")
        self.assertIn("n_honor_lucius", sc.nodes)
        self.assertIn("n_alesia_seal", sc.nodes)

    def test_16_scenario_03_thusnelda_honor_lucius_path(self):
        """Scenario 3: Showing Lucius's Germanic token grants AMBER_RUNE_GRANTED."""
        sc = build_scenario_03_thusnelda()
        st = sc.start()
        st, _ = sc.choose(st, "c1_token")
        self.assertEqual(st.current_node_id, "n_honor_lucius")
        st, _ = sc.choose(st, "c_ask_seal")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "AMBER_RUNE_GRANTED")

    def test_17_scenario_03_thusnelda_mud_hazard_path(self):
        """Scenario 3: Threatening with iron and failing check leads to BOG_HAZARD_PENALTY."""
        sc = build_scenario_03_thusnelda()
        st = sc.start()
        st, _ = sc.choose(st, "c3_iron", roll_override=10)
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "BOG_HAZARD_PENALTY")

    # ── 6. SCENARIO 04 (VERCINGETORIX) GRAPH & TURN LIMIT ────────────────────

    def test_18_scenario_04_vercingetorix_max_turns_constraint(self):
        """Scenario 4 strictly enforces a 3-turn max limit."""
        sc = build_scenario_04_vercingetorix()
        self.assertEqual(sc.max_turns, 3)

    def test_19_scenario_04_vercingetorix_3_questions_sequence(self):
        """Scenario 4 permits exactly 3 questions delivering lore."""
        sc = build_scenario_04_vercingetorix()
        st = sc.start()

        # Question 1: Unmake lore
        st, _ = sc.choose(st, "q_unmake")
        self.assertEqual(st.turns, 1)
        self.assertEqual(st.current_node_id, "n_unmake_lore")

        # Question 2: Alesia lore
        st, _ = sc.choose(st, "q2_alesia")
        self.assertEqual(st.turns, 2)
        self.assertEqual(st.current_node_id, "n_caesar_lore")

        # Question 3: Vindolanda raid lore
        st, _ = sc.choose(st, "q2_raid2")
        self.assertEqual(st.turns, 3)
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "WARRIOR_DISSOLUTION_TO_ASH")

    def test_20_scenario_04_vercingetorix_dissolution_outcome(self):
        """Scenario 4 ends in WARRIOR_DISSOLUTION_TO_ASH when questions are exhausted."""
        sc = build_scenario_04_vercingetorix()
        st = sc.start()
        st, _ = sc.choose(st, "q_save")
        st, _ = sc.choose(st, "q2_unmake3")
        st, _ = sc.choose(st, "q2_alesia")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "WARRIOR_DISSOLUTION_TO_ASH")

    # ── 7. SCENARIO 05 (MARS) GRAPH & CAMPAIGN ENDINGS ───────────────────────

    def test_21_scenario_05_mars_graph_structure(self):
        """Scenario 5 graph contains all 4 campaign ending nodes."""
        sc = build_scenario_05_mars()
        self.assertIn("n_unmaking_ritual", sc.nodes)
        self.assertIn("n_unmade_success", sc.nodes)
        self.assertIn("n_rome_curse", sc.nodes)
        self.assertIn("n_mars_harvest", sc.nodes)
        self.assertIn("n_combat_wrath", sc.nodes)

    def test_22_scenario_05_mars_destroy_ending_with_sacrifice(self):
        """Scenario 5: Destroy ending with willing PC sacrifice yields SPEAR_UNMADE_WARDEN_BORN."""
        sc = build_scenario_05_mars()
        st = sc.start(corruption_tier=3)
        st, _ = sc.choose(st, "c1_destroy")
        self.assertEqual(st.current_node_id, "n_unmaking_ritual")
        st, _ = sc.choose(st, "c_step_forward")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "SPEAR_UNMADE_WARDEN_BORN")
        self.assertTrue(st.flags.get("sacrifice_made"))

    def test_23_scenario_05_mars_destroy_ending_without_sacrifice(self):
        """Scenario 5: Refusing chains during unmaking triggers AVATAR_COMBAT_ENGAGED."""
        sc = build_scenario_05_mars()
        st = sc.start()
        st, _ = sc.choose(st, "c1_destroy")
        st, _ = sc.choose(st, "c_refuse_chains")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "AVATAR_COMBAT_ENGAGED")

    def test_24_scenario_05_mars_claim_for_rome_ending(self):
        """Scenario 5: Option 2 claims the spear for Rome (CLAIMED_FOR_ROME)."""
        sc = build_scenario_05_mars()
        st = sc.start()
        st, _ = sc.choose(st, "c2_rome")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "CLAIMED_FOR_ROME")

    def test_25_scenario_05_mars_give_to_mars_ending(self):
        """Scenario 5: Option 3 yields spear back to Mars (RETURNED_TO_MARS)."""
        sc = build_scenario_05_mars()
        st = sc.start()
        st, _ = sc.choose(st, "c3_give")
        self.assertTrue(st.is_finished)
        self.assertEqual(st.final_outcome, "RETURNED_TO_MARS")

    # ── 8. ERROR HANDLING & DATA INTEGRITY ───────────────────────────────────

    def test_26_invalid_choice_raises_value_error(self):
        """Engine raises ValueError on unknown choice_id."""
        sc = build_scenario_01_cassia()
        st = sc.start()
        with self.assertRaises(ValueError):
            sc.choose(st, "nonexistent_choice_id")

    def test_27_choice_on_concluded_scenario_safely_rejected(self):
        """Engine safely rejects actions on concluded scenarios."""
        sc = build_scenario_01_cassia()
        st = sc.start()
        st, _ = sc.choose(st, "c1_omens", roll_override=5)  # terminates in VEILED_WARNING
        self.assertTrue(st.is_finished)
        st_after, msg = sc.choose(st, "c1_omens")
        self.assertEqual(msg, "Scenario already concluded.")

    def test_28_corvinus_and_thusnelda_npc_jsons_consistent_with_personas(self):
        """NPC data JSON files match scenario persona lore."""
        with open(REPO_ROOT / "npcs" / "corvinus.json", "r", encoding="utf-8") as f:
            corvinus_npc = json.load(f)
        self.assertIn("Varro", corvinus_npc["gm_notes"])
        self.assertIn("Lucius", corvinus_npc["gm_notes"])
        self.assertIn("wants the Spear of Mars destroyed", corvinus_npc["secret"])

        with open(REPO_ROOT / "npcs" / "thusnelda.json", "r", encoding="utf-8") as f:
            thusnelda_npc = json.load(f)
        self.assertIn("Alesia", thusnelda_npc["notes"])
        self.assertIn("teacher's teacher", thusnelda_npc["gm_notes"])


if __name__ == "__main__":
    unittest.main()
