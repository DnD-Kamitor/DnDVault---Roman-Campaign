"""
scenario_engine.py — Core roleplay scenario state machine and AI simulation engine
for the 5 pivotal NPC encounters in 'The Shadow of Mars' campaign.

Supports deterministic graph execution, skill check resolution, turn tracking,
corruption scaling, and integration with local LLM personas (OpenWebUI/Ollama).
"""

from dataclasses import dataclass, field
from enum import Enum
import json
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Any

REPO_ROOT = Path(__file__).resolve().parent.parent


class CheckType(Enum):
    D20 = "d20"
    AUTO = "auto"


@dataclass
class SkillCheck:
    skill: str  # e.g. "Religion", "Insight", "Persuasion", "Survival", "Athletics"
    dc: int
    success_node: str
    failure_node: str
    advantage_if_flag: Optional[str] = None


@dataclass
class Choice:
    choice_id: str
    text: str
    target_node: Optional[str] = None
    check: Optional[SkillCheck] = None
    sets_flag: Optional[str] = None
    requires_flag: Optional[str] = None


@dataclass
class ScenarioNode:
    node_id: str
    speaker: str
    text: str
    choices: List[Choice] = field(default_factory=list)
    is_terminal: bool = False
    outcome: Optional[str] = None  # e.g. "SUCCESS_AUSPICES", "DEATH_DISSOLUTION"
    on_enter_action: Optional[Callable[["ScenarioState"], None]] = None


@dataclass
class ScenarioState:
    scenario_id: str
    current_node_id: str
    turns: int = 0
    max_turns: Optional[int] = None
    flags: Dict[str, Any] = field(default_factory=dict)
    history: List[Tuple[str, str, str]] = field(default_factory=list)  # (node_id, speaker, text)
    is_finished: bool = False
    final_outcome: Optional[str] = None
    corruption_tier: int = 1


class Scenario:
    def __init__(
        self,
        scenario_id: str,
        title: str,
        npc_name: str,
        persona_file: str,
        initial_node_id: str,
        nodes: Dict[str, ScenarioNode],
        max_turns: Optional[int] = None,
    ):
        self.scenario_id = scenario_id
        self.title = title
        self.npc_name = npc_name
        self.persona_file = REPO_ROOT / persona_file
        self.initial_node_id = initial_node_id
        self.nodes = nodes
        self.max_turns = max_turns

    def load_persona(self) -> dict:
        if not self.persona_file.is_file():
            raise FileNotFoundError(f"Persona file not found: {self.persona_file}")
        with open(self.persona_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def start(self, corruption_tier: int = 1, initial_flags: Optional[Dict[str, Any]] = None) -> ScenarioState:
        state = ScenarioState(
            scenario_id=self.scenario_id,
            current_node_id=self.initial_node_id,
            turns=0,
            max_turns=self.max_turns,
            flags=initial_flags or {},
            corruption_tier=corruption_tier,
        )
        first_node = self.nodes[self.initial_node_id]
        if first_node.on_enter_action:
            first_node.on_enter_action(state)
        state.history.append((first_node.node_id, first_node.speaker, first_node.text))
        if first_node.is_terminal:
            state.is_finished = True
            state.final_outcome = first_node.outcome
        return state

    def choose(
        self,
        state: ScenarioState,
        choice_id: str,
        roll_override: Optional[int] = None,
        roll_modifier: int = 0,
    ) -> Tuple[ScenarioState, str]:
        """Advance scenario state via player choice. roll_override allows deterministic testing."""
        if state.is_finished:
            return state, "Scenario already concluded."

        current_node = self.nodes[state.current_node_id]
        matched_choice = next((c for c in current_node.choices if c.choice_id == choice_id), None)
        if not matched_choice:
            raise ValueError(f"Invalid choice '{choice_id}' from node '{state.current_node_id}'")

        if matched_choice.requires_flag and not state.flags.get(matched_choice.requires_flag):
            raise PermissionError(f"Choice '{choice_id}' requires flag '{matched_choice.requires_flag}'")

        if matched_choice.sets_flag:
            state.flags[matched_choice.sets_flag] = True

        state.turns += 1

        # Check turn limit constraint (e.g. Vercingetorix 3-question limit)
        if state.max_turns and state.turns >= state.max_turns:
            for n in self.nodes.values():
                if n.is_terminal and "DISSOLUTION" in (n.outcome or ""):
                    state.current_node_id = n.node_id
                    state.is_finished = True
                    state.final_outcome = n.outcome
                    state.history.append((n.node_id, n.speaker, n.text))
                    return state, f"Turn limit of {state.max_turns} reached. Terminal dissolution."

        # Handle skill check or direct transition
        if matched_choice.check:
            check = matched_choice.check
            roll = roll_override if roll_override is not None else 10
            total = roll + roll_modifier
            has_advantage = check.advantage_if_flag and state.flags.get(check.advantage_if_flag)
            if has_advantage and roll_override is None:
                total += 5  # Passive advantage bonus

            success = total >= check.dc
            next_node_id = check.success_node if success else check.failure_node
            detail_msg = f"{check.skill} DC {check.dc} check: rolled {roll}+{roll_modifier}={total} -> {'SUCCESS' if success else 'FAILURE'}"
        else:
            next_node_id = matched_choice.target_node
            detail_msg = f"Transitioned to {next_node_id}"

        if not next_node_id or next_node_id not in self.nodes:
            raise KeyError(f"Next node '{next_node_id}' does not exist in scenario")

        next_node = self.nodes[next_node_id]
        state.current_node_id = next_node_id

        if next_node.on_enter_action:
            next_node.on_enter_action(state)

        state.history.append((next_node.node_id, next_node.speaker, next_node.text))

        if next_node.is_terminal:
            state.is_finished = True
            state.final_outcome = next_node.outcome

        return state, detail_msg


# ── SCENARIO FACTORY DEFINITIONS ─────────────────────────────────────────────

def build_scenario_01_cassia() -> Scenario:
    """Scenario 1: The Entrails of Mars — Augur Cassia consultation."""
    nodes = {
        "n_greet": ScenarioNode(
            node_id="n_greet",
            speaker="Augur Cassia",
            text="The vital head of the liver is blackened by necrotic bile. Mars did not turn away; he turned toward us hungry. Why do you seek the haruspex?",
            choices=[
                Choice("c1_omens", "Interpret the omens of the liver.", check=SkillCheck("Religion", 13, "n_mars_hunger", "n_veiled_warning")),
                Choice("c2_challenge", "Rome conquered with iron, not sheep guts.", check=SkillCheck("Persuasion", 14, "n_mars_hunger", "n_rebuke")),
                Choice("c3_spear", "We know Caesar's spear rests below. What power lies within it?", check=SkillCheck("History", 15, "n_alesia_lore", "n_veiled_warning")),
            ],
        ),
        "n_mars_hunger": ScenarioNode(
            node_id="n_mars_hunger",
            speaker="Augur Cassia",
            text="Mars starves in the Pax Romana. This spear is his open mouth. If you pull it into the daylight, you feed him the entire frontier.",
            choices=[
                Choice("c_prayer", "Offer respectful prayer and promise to stop the slaughter.", target_node="n_blessing", sets_flag="respectful_prayer"),
            ],
        ),
        "n_alesia_lore": ScenarioNode(
            node_id="n_alesia_lore",
            speaker="Augur Cassia",
            text="It was forged under a blood pact at Alesia. The druids and legionaries bound it in granite. If unmade, someone must step into the guardian's chains.",
            choices=[
                Choice("c_swear_warden", "We will see the weapon ended, whatever the cost.", target_node="n_blessing", sets_flag="vowed_end"),
            ],
        ),
        "n_veiled_warning": ScenarioNode(
            node_id="n_veiled_warning",
            speaker="Augur Cassia",
            text="The signs are nefas. Tread with your shields raised, soldiers of Rome.",
            is_terminal=True,
            outcome="VEILED_WARNING",
        ),
        "n_rebuke": ScenarioNode(
            node_id="n_rebuke",
            speaker="Augur Cassia",
            text="You bring blasphemy before the altar. Leave before Mars marks you for his first offering.",
            is_terminal=True,
            outcome="HARUSPEX_REBUKE",
        ),
        "n_blessing": ScenarioNode(
            node_id="n_blessing",
            speaker="Augur Cassia",
            text="Take this sacred ash of bay leaves upon your brow. When the dread of Mars tests your heart, remember you fight for the living.",
            is_terminal=True,
            outcome="GRANTED_AUSPICES",
        ),
    }
    return Scenario("scenario_01_cassia", "The Entrails of Mars", "Augur Cassia", "ai_personas/augur_cassia.json", "n_greet", nodes)


def build_scenario_02_corvinus() -> Scenario:
    """Scenario 2: Midnight in the Principia — Legate Corvinus debrief."""
    nodes = {
        "n_greet": ScenarioNode(
            node_id="n_greet",
            speaker="Legate Corvinus",
            text="Varro dead at the north gate. Lucius dead in the pine woods. Rome sends me patrician boys and leaves me with five irregulars. What did you bring out of the woods?",
            choices=[
                Choice("c1_lucius_box", "Deliver Lucius's locked box with respect.", check=SkillCheck("Insight", 12, "n_lucius_honor", "n_dismissive")),
                Choice("c2_varro_treason", "Confront him about Varro's treason and madness.", check=SkillCheck("Persuasion", 15, "n_varro_truth", "n_defensive")),
                Choice("c3_demand_orders", "Demand official marching orders and supplies.", target_node="n_dismissive"),
            ],
        ),
        "n_lucius_honor": ScenarioNode(
            node_id="n_lucius_honor",
            speaker="Legate Corvinus",
            text="Personal letters... and a carved wooden horse of the Rhine. Lucius was caught between two worlds. If you honored his bones, you are better men than the Senate.",
            choices=[
                Choice("c_push_secret", "Show Varro's blackened token and ask what he really fears.", check=SkillCheck("Persuasion", 16, "n_secret_revealed", "n_dismissive")),
            ],
        ),
        "n_varro_truth": ScenarioNode(
            node_id="n_varro_truth",
            speaker="Legate Corvinus",
            text="Varro was no traitor! He was poisoned by what's buried out there. He heard it calling across twenty miles.",
            choices=[
                Choice("c_push_secret2", "Then help us stop it, Legate. What is your real order?", check=SkillCheck("Insight", 15, "n_secret_revealed", "n_defensive")),
            ],
        ),
        "n_defensive": ScenarioNode(
            node_id="n_defensive",
            speaker="Legate Corvinus",
            text="Mind your rank, auxiliary! I answer to the Senate and the Emperor, not to irregulars. Take your rations and get out.",
            is_terminal=True,
            outcome="COLD_DISMISSAL",
        ),
        "n_dismissive": ScenarioNode(
            node_id="n_dismissive",
            speaker="Legate Corvinus",
            text="You have your scout mandate. If you die in the bog, the cohort has no record of your deployment.",
            is_terminal=True,
            outcome="MINIMAL_SUPPORT",
        ),
        "n_secret_revealed": ScenarioNode(
            node_id="n_secret_revealed",
            speaker="Legate Corvinus",
            text="Listen to me: Brutus wants the spear in Rome. But if it enters Rome, it will poison the Caesars until the empire burns. It must not leave the vault! Unmake it in the dark, and I will co-sign your imperial citizenship myself.",
            choices=[
                Choice("c_accept_pact", "We agree. It ends in the dark.", target_node="n_pact_accepted", sets_flag="deniability_pact"),
            ],
        ),
        "n_pact_accepted": ScenarioNode(
            node_id="n_pact_accepted",
            speaker="Legate Corvinus",
            text="Take my signet dispensation: medical spirits and horses from the vicus. Do not fail Rome.",
            is_terminal=True,
            outcome="PACT_OF_DENIABILITY",
        ),
    }
    return Scenario("scenario_02_corvinus", "Midnight in the Principia", "Legate Corvinus", "ai_personas/legate_corvinus.json", "n_greet", nodes)


def build_scenario_03_thusnelda() -> Scenario:
    """Scenario 3: The Will-o'-the-Wisp Passage — Thusnelda the Bog Seer."""
    nodes = {
        "n_greet": ScenarioNode(
            node_id="n_greet",
            speaker="Thusnelda",
            text="Another squad of Roman iron come to feed the bog. Three paces left, a centurion's horse sank eighty winters ago. Why should I show you the dry stone?",
            choices=[
                Choice("c1_token", "Show Lucius's Germanic carved rune token.", target_node="n_honor_lucius", sets_flag="showed_lucius_token"),
                Choice("c2_nature", "Appeal to the sanctity of the marsh and offer respect.", check=SkillCheck("Survival", 13, "n_peat_wisdom", "n_sinking_mud")),
                Choice("c3_iron", "Demand passage by right of Roman steel.", check=SkillCheck("Intimidation", 16, "n_peat_wisdom", "n_sinking_mud")),
            ],
        ),
        "n_honor_lucius": ScenarioNode(
            node_id="n_honor_lucius",
            speaker="Thusnelda",
            text="The boy with two mothers... The spiders took his breath, but the earth did not curse him. If you walked with him, the mud will not drink you today.",
            choices=[
                Choice("c_ask_seal", "Tell us of the ancient seal beneath the marsh.", target_node="n_alesia_seal"),
            ],
        ),
        "n_peat_wisdom": ScenarioNode(
            node_id="n_peat_wisdom",
            speaker="Thusnelda",
            text="You look at the earth with open eyes, not blind iron boots. The blood cult has dug into the sunken shrine, feeding throats to wake the Red Hunger.",
            choices=[
                Choice("c_stop_cult", "We go to sever the cult and put the god back to sleep.", target_node="n_alesia_seal"),
            ],
        ),
        "n_sinking_mud": ScenarioNode(
            node_id="n_sinking_mud",
            speaker="Thusnelda",
            text="The bog is deaf to commands. The wisps will dance above your drowned armor.",
            is_terminal=True,
            outcome="BOG_HAZARD_PENALTY",
        ),
        "n_alesia_seal": ScenarioNode(
            node_id="n_alesia_seal",
            speaker="Thusnelda",
            text="My teacher's teacher bound it with cold silver two centuries back. Take this raw amber brooch. It remembers the sunlight before the blood fell. It will turn aside the screaming banshees at the sunken gate.",
            is_terminal=True,
            outcome="AMBER_RUNE_GRANTED",
        ),
    }
    return Scenario("scenario_03_thusnelda", "The Will-o'-the-Wisp Passage", "Thusnelda", "ai_personas/thusnelda_seer.json", "n_greet", nodes)


def build_scenario_04_vercingetorix() -> Scenario:
    """Scenario 4: The Lucidity of the Chains — Vercingetorix the Bound (Strict 3-question limit)."""
    nodes = {
        "n_greet": ScenarioNode(
            node_id="n_greet",
            speaker="Vercingetorix",
            text="The haze... is gone. For two centuries I was a hound on the god's leash. The grip slips for sixty seconds, no more. Ask what you must before the dust claims my name.",
            choices=[
                Choice("q_unmake", "How do we unmake the Spear of Mars?", target_node="n_unmake_lore"),
                Choice("q_alesia", "What happened between Caesar and the spear at Alesia?", target_node="n_caesar_lore"),
                Choice("q_vindolanda", "Why did you attack Fort Vindolanda during the raid?", target_node="n_raid_lore"),
                Choice("q_save", "Can we save your life from the chains?", target_node="n_save_lore"),
            ],
        ),
        "n_unmake_lore": ScenarioNode(
            node_id="n_unmake_lore",
            speaker="Vercingetorix",
            text="The granite altar has three iron winches. Turn Northern, Western, Eastern counter-clockwise. But balance demands: someone must step into the guardian's shackles forever. If no one takes the chains, Mars walks free.",
            choices=[
                Choice("q2_alesia", "What happened with Caesar at Alesia?", target_node="n_caesar_lore"),
                Choice("q2_raid", "Why did you attack Vindolanda?", target_node="n_raid_lore"),
                Choice("q2_save", "Can we save you?", target_node="n_save_lore"),
            ],
        ),
        "n_caesar_lore": ScenarioNode(
            node_id="n_caesar_lore",
            speaker="Vercingetorix",
            text="Caesar took the spear believing it was Rome's glory. But it devoured his sanity. The Roman senators did not kill a tyrant; they killed a broken man whose mind was eaten by the god.",
            choices=[
                Choice("q2_unmake", "How do we unmake the spear?", target_node="n_unmake_lore"),
                Choice("q2_raid2", "Why attack Vindolanda?", target_node="n_raid_lore"),
            ],
        ),
        "n_raid_lore": ScenarioNode(
            node_id="n_raid_lore",
            speaker="Vercingetorix",
            text="Mars was starving in the Pax Romana. He jerked my leash. But when your squad held the line with honor, it broke his trance for an instant.",
            choices=[
                Choice("q2_unmake2", "How do we unmake the spear?", target_node="n_unmake_lore"),
            ],
        ),
        "n_save_lore": ScenarioNode(
            node_id="n_save_lore",
            speaker="Vercingetorix",
            text="No. My death was stolen in Rome two hundred years ago. Grant me silence.",
            choices=[
                Choice("q2_unmake3", "How do we unmake the spear?", target_node="n_unmake_lore"),
            ],
        ),
        "n_dissolution": ScenarioNode(
            node_id="n_dissolution",
            speaker="Vercingetorix",
            text="The sun... warms Auvergne at last. Strike well, soldiers of the frontier...",
            is_terminal=True,
            outcome="WARRIOR_DISSOLUTION_TO_ASH",
        ),
    }
    return Scenario("scenario_04_vercingetorix", "The Lucidity of the Chains", "Vercingetorix", "ai_personas/vercingetorix_sparring.json", "n_greet", nodes, max_turns=3)


def build_scenario_05_mars() -> Scenario:
    """Scenario 5: The War God's Crucible — The Avatar of Mars."""
    nodes = {
        "n_greet": ScenarioNode(
            node_id="n_greet",
            speaker="Avatar of Mars",
            text="MORTALS. You stand before the altar not as beggars, but as warriors. Did you come to feed the harvest, or to starve like dogs?",
            choices=[
                Choice("c1_destroy", "We unmake the spear on this altar!", target_node="n_unmaking_ritual"),
                Choice("c2_rome", "We claim the spear in the name of the Senate and People of Rome!", target_node="n_rome_curse"),
                Choice("c3_give", "We yield to you, Lord of War. Take your weapon.", target_node="n_mars_harvest"),
                Choice("c4_defy", "You are a parasite of blood, not a god. We defy you!", target_node="n_combat_wrath"),
            ],
        ),
        "n_unmaking_ritual": ScenarioNode(
            node_id="n_unmaking_ritual",
            speaker="Avatar of Mars",
            text="You dare touch the meteor winches? The unmaking demands a soul in the shackles! Who among you is worthy to bear my eternal chains?",
            choices=[
                Choice("c_step_forward", "A PC willingly takes the guardian's chains.", target_node="n_unmade_success", sets_flag="sacrifice_made"),
                Choice("c_refuse_chains", "No one will take the chains!", target_node="n_combat_wrath"),
            ],
        ),
        "n_unmade_success": ScenarioNode(
            node_id="n_unmade_success",
            speaker="Avatar of Mars",
            text="A worthy warden... You take the iron, mortal. Let the spear turn to ash!",
            is_terminal=True,
            outcome="SPEAR_UNMADE_WARDEN_BORN",
        ),
        "n_rome_curse": ScenarioNode(
            node_id="n_rome_curse",
            speaker="Avatar of Mars",
            text="Take it to Rome, fools! It will drink the blood of your Caesars until your empire has no walls left!",
            is_terminal=True,
            outcome="CLAIMED_FOR_ROME",
        ),
        "n_mars_harvest": ScenarioNode(
            node_id="n_mars_harvest",
            speaker="Avatar of Mars",
            text="You know your place in the harvest. Go, mortals. When the frontier bleeds again, know that I smile upon you.",
            is_terminal=True,
            outcome="RETURNED_TO_MARS",
        ),
        "n_combat_wrath": ScenarioNode(
            node_id="n_combat_wrath",
            speaker="Avatar of Mars",
            text="Then bleed! Your bones will pave my sanctuary!",
            is_terminal=True,
            outcome="AVATAR_COMBAT_ENGAGED",
        ),
    }
    return Scenario("scenario_05_mars", "The War God's Crucible", "Avatar of Mars", "ai_personas/whispers_of_mars.json", "n_greet", nodes)


ALL_SCENARIO_BUILDERS = {
    "scenario_01_cassia": build_scenario_01_cassia,
    "scenario_02_corvinus": build_scenario_02_corvinus,
    "scenario_03_thusnelda": build_scenario_03_thusnelda,
    "scenario_04_vercingetorix": build_scenario_04_vercingetorix,
    "scenario_05_mars": build_scenario_05_mars,
}
