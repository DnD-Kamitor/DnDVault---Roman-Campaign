#!/usr/bin/env python3
"""
play_scenario.py — Interactive GM terminal player for running and rehearsing
the 5 pivotal NPC scenarios in 'The Shadow of Mars'.

Features:
- Live terminal dialogue with formatting and turn counter
- D20 dice rolling (manual roll input or auto-roll)
- Corruption level selection (Tiers 1-5)
- Automated non-interactive demo mode via --scenario <id> --auto

Usage:
    python3 scripts/play_scenario.py
    python3 scripts/play_scenario.py --scenario scenario_01_cassia --auto
"""

import argparse
import random
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.scenario_engine import (
    ALL_SCENARIO_BUILDERS,
    ScenarioState,
)

MENU_INFO = [
    ("scenario_01_cassia", "Augur Cassia — The Entrails of Mars (Sacrarium, Act I/II)"),
    ("scenario_02_corvinus", "Legate Corvinus — Midnight in the Principia (Headquarters, Act III/IV)"),
    ("scenario_03_thusnelda", "Thusnelda the Bog Seer — The Will-o'-the-Wisp Passage (Black Bog, Act IV)"),
    ("scenario_04_vercingetorix", "Vercingetorix the Bound — The Lucidity of the Chains (Threshold, Act V)"),
    ("scenario_05_mars", "Avatar of Mars — The War God's Crucible (Sanctum Altar, Act V)"),
]


def print_banner(text: str):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def run_interactive(scenario_key: str, corruption_tier: int = 1, auto_mode: bool = False):
    builder = ALL_SCENARIO_BUILDERS[scenario_key]
    scenario = builder()

    print_banner(f"{scenario.title.upper()} — {scenario.npc_name}")
    print(f"[Location: {scenario.title} | Corruption Tier: {corruption_tier}]")
    if scenario.max_turns:
        print(f"[Strict Time Limit: Max {scenario.max_turns} turns before dissolution]\n")

    state = scenario.start(corruption_tier=corruption_tier)

    while not state.is_finished:
        curr_node = scenario.nodes[state.current_node_id]
        print(f"\n--- Turn {state.turns + 1} ---")
        print(f"\033[1;33m[{curr_node.speaker}]:\033[0m")
        print(f"\"{curr_node.text}\"\n")

        if not curr_node.choices:
            break

        print("\033[1;36mPlayer Options:\033[0m")
        for idx, choice in enumerate(curr_node.choices, 1):
            check_str = f" [Check: {choice.check.skill} DC {choice.check.dc}]" if choice.check else ""
            print(f"  {idx}. {choice.text}{check_str}")

        if auto_mode:
            # Pick first choice and roll high
            chosen_idx = 1
            choice = curr_node.choices[0]
            roll = 15
            print(f"\n[AUTO MODE] Chose option {chosen_idx} with roll {roll}")
            state, detail = scenario.choose(state, choice.choice_id, roll_override=roll)
            print(f"  Result: {detail}")
            continue

        # Interactive input
        while True:
            try:
                raw = input("\nSelect choice (number) or 'q' to quit: ").strip()
                if raw.lower() == 'q':
                    print("Exiting scenario.")
                    return
                val = int(raw)
                if 1 <= val <= len(curr_node.choices):
                    chosen_idx = val
                    choice = curr_node.choices[chosen_idx - 1]
                    break
                print(f"Please enter a number between 1 and {len(curr_node.choices)}.")
            except (ValueError, EOFError):
                # Fallback for non-interactive stdin
                chosen_idx = 1
                choice = curr_node.choices[0]
                break

        roll_val = None
        if choice.check:
            try:
                roll_in = input(f"Enter d20 roll for {choice.check.skill} DC {choice.check.dc} (or press Enter for auto-roll): ").strip()
                if roll_in:
                    roll_val = int(roll_in)
                else:
                    roll_val = random.randint(1, 20)
                    print(f"  [Auto-roll d20]: {roll_val}")
            except (ValueError, EOFError):
                roll_val = random.randint(10, 18)

        state, detail = scenario.choose(state, choice.choice_id, roll_override=roll_val)
        print(f"\n\033[1;32m-> {detail}\033[0m")

    # Terminal node
    final_node = scenario.nodes[state.current_node_id]
    print("\n" + "-" * 70)
    print(f"\033[1;33m[{final_node.speaker}]:\033[0m")
    print(f"\"{final_node.text}\"")
    print("-" * 70)
    print(f"\n\033[1;35m[SCENARIO CONCLUDED]: Outcome = {state.final_outcome}\033[0m\n")


def main():
    parser = argparse.ArgumentParser(description="Interactive GM Scenario Player")
    parser.add_argument("--scenario", choices=list(ALL_SCENARIO_BUILDERS.keys()), help="Scenario ID to launch directly")
    parser.add_argument("--corruption", type=int, default=1, choices=[1, 2, 3, 4, 5], help="Corruption Tier (1-5)")
    parser.add_argument("--auto", action="store_true", help="Run in automated test mode")
    args = parser.parse_args()

    if args.scenario:
        run_interactive(args.scenario, corruption_tier=args.corruption, auto_mode=args.auto)
        return

    print_banner("THE SHADOW OF MARS — 5 VERIFIED NPC SCENARIOS")
    print("Select an encounter to rehearse or run at the table:\n")
    for idx, (key, label) in enumerate(MENU_INFO, 1):
        print(f"  {idx}. {label}")
    print("  6. Run automated test of ALL scenarios\n")

    try:
        choice = input("Enter choice (1-6): ").strip()
        if choice in ["1", "2", "3", "4", "5"]:
            scenario_key = MENU_INFO[int(choice) - 1][0]
            run_interactive(scenario_key, corruption_tier=args.corruption, auto_mode=args.auto)
        elif choice == "6":
            for sc_key, _ in MENU_INFO:
                run_interactive(sc_key, corruption_tier=1, auto_mode=True)
        else:
            print("Invalid choice. Exiting.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")


if __name__ == "__main__":
    main()
