#!/usr/bin/env python3
"""
verify_npc_scenarios.py — Automated verification script that runs all 5 NPC scenarios
through simulated playthroughs, testing success and failure branches, DC checks,
and turn limits.

Usage:
    python3 scripts/verify_npc_scenarios.py
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.scenario_engine import (
    ALL_SCENARIO_BUILDERS,
    ScenarioState,
)


def verify_scenario_01_cassia():
    print("Testing Scenario 01: Augur Cassia...")
    builder = ALL_SCENARIO_BUILDERS["scenario_01_cassia"]

    # Branch A: Religion success -> Granted Auspices
    sc = builder()
    st = sc.start()
    st, msg = sc.choose(st, "c1_omens", roll_override=15)
    assert st.current_node_id == "n_mars_hunger", f"Expected n_mars_hunger, got {st.current_node_id}"
    st, msg = sc.choose(st, "c_prayer")
    assert st.is_finished and st.final_outcome == "GRANTED_AUSPICES"

    # Branch B: Religion failure -> Veiled Warning
    st2 = sc.start()
    st2, _ = sc.choose(st2, "c1_omens", roll_override=5)
    assert st2.is_finished and st2.final_outcome == "VEILED_WARNING"

    # Branch C: Disrespect -> Haruspex Rebuke
    st3 = sc.start()
    st3, _ = sc.choose(st3, "c2_challenge", roll_override=8)
    assert st3.is_finished and st3.final_outcome == "HARUSPEX_REBUKE"
    print("  ✓ Scenario 01 verified (3 distinct branches)")


def verify_scenario_02_corvinus():
    print("Testing Scenario 02: Legate Corvinus...")
    builder = ALL_SCENARIO_BUILDERS["scenario_02_corvinus"]

    # Branch A: Lucius box + High Persuasion -> Secret Revealed -> Pact of Deniability
    sc = builder()
    st = sc.start()
    st, _ = sc.choose(st, "c1_lucius_box", roll_override=14)
    assert st.current_node_id == "n_lucius_honor"
    st, _ = sc.choose(st, "c_push_secret", roll_override=18)
    assert st.current_node_id == "n_secret_revealed"
    st, _ = sc.choose(st, "c_accept_pact")
    assert st.is_finished and st.final_outcome == "PACT_OF_DENIABILITY"
    assert st.flags.get("deniability_pact") is True

    # Branch B: Aggressive confrontation fail -> Cold Dismissal
    st2 = sc.start()
    st2, _ = sc.choose(st2, "c2_varro_treason", roll_override=10)
    assert st2.is_finished and st2.final_outcome == "COLD_DISMISSAL"
    print("  ✓ Scenario 02 verified (2 distinct branches)")


def verify_scenario_03_thusnelda():
    print("Testing Scenario 03: Thusnelda the Bog Seer...")
    builder = ALL_SCENARIO_BUILDERS["scenario_03_thusnelda"]

    # Branch A: Show Lucius token -> Amber Rune Granted
    sc = builder()
    st = sc.start()
    st, _ = sc.choose(st, "c1_token")
    assert st.current_node_id == "n_honor_lucius"
    st, _ = sc.choose(st, "c_ask_seal")
    assert st.is_finished and st.final_outcome == "AMBER_RUNE_GRANTED"

    # Branch B: Threaten force fail -> Bog Hazard Penalty
    st2 = sc.start()
    st2, _ = sc.choose(st2, "c3_iron", roll_override=10)
    assert st2.is_finished and st2.final_outcome == "BOG_HAZARD_PENALTY"
    print("  ✓ Scenario 03 verified (2 distinct branches)")


def verify_scenario_04_vercingetorix():
    print("Testing Scenario 04: Vercingetorix the Bound...")
    builder = ALL_SCENARIO_BUILDERS["scenario_04_vercingetorix"]

    # 3-question sequence -> Turn limit reached -> Dissolution to ash
    sc = builder()
    st = sc.start()
    assert st.max_turns == 3

    st, _ = sc.choose(st, "q_unmake")
    assert st.turns == 1
    assert st.current_node_id == "n_unmake_lore"

    st, _ = sc.choose(st, "q2_alesia")
    assert st.turns == 2
    assert st.current_node_id == "n_caesar_lore"

    st, _ = sc.choose(st, "q2_raid2")
    assert st.turns == 3
    assert st.is_finished
    assert st.final_outcome == "WARRIOR_DISSOLUTION_TO_ASH"
    print("  ✓ Scenario 04 verified (Strict 3-question limit enforced)")


def verify_scenario_05_mars():
    print("Testing Scenario 05: Avatar of Mars...")
    builder = ALL_SCENARIO_BUILDERS["scenario_05_mars"]

    # Ending B: Unmake spear with sacrifice
    sc = builder()
    st = sc.start(corruption_tier=3)
    st, _ = sc.choose(st, "c1_destroy")
    assert st.current_node_id == "n_unmaking_ritual"
    st, _ = sc.choose(st, "c_step_forward")
    assert st.is_finished and st.final_outcome == "SPEAR_UNMADE_WARDEN_BORN"

    # Ending A: Claim for Rome
    st2 = sc.start()
    st2, _ = sc.choose(st2, "c2_rome")
    assert st2.is_finished and st2.final_outcome == "CLAIMED_FOR_ROME"

    # Ending C: Return to Mars
    st3 = sc.start()
    st3, _ = sc.choose(st3, "c3_give")
    assert st3.is_finished and st3.final_outcome == "RETURNED_TO_MARS"

    # Defiance -> Combat
    st4 = sc.start()
    st4, _ = sc.choose(st4, "c4_defy")
    assert st4.is_finished and st4.final_outcome == "AVATAR_COMBAT_ENGAGED"
    print("  ✓ Scenario 05 verified (All 4 ending paths)")


def main():
    print("=================================================================")
    print("VERIFYING 5 NPC ROLEPLAY SCENARIOS & AI SIMULATION ENGINE")
    print("=================================================================")
    verify_scenario_01_cassia()
    verify_scenario_02_corvinus()
    verify_scenario_03_thusnelda()
    verify_scenario_04_vercingetorix()
    verify_scenario_05_mars()
    print("=================================================================")
    print("ALL 5 SCENARIOS VERIFIED SUCCESSFULLY WITH ZERO ERRORS!")
    print("=================================================================")


if __name__ == "__main__":
    main()
