#!/usr/bin/env python3
"""
Unit tests for NPC & Monster Manual Stat Block Integrity (Story 13.1).
Validates all 89 npcs/*.json and scripts/creature_stats.json files.
"""

import glob
import json
import re
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NPC_DIR = BASE / "npcs"
STATS_FILE = BASE / "scripts/creature_stats.json"

VALID_CRS = {
    "0", "1/8", "1/4", "1/2",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "30", "unknown"
}


class TestNPCIntegrity(unittest.TestCase):

    def setUp(self):
        self.npc_files = sorted(NPC_DIR.glob("*.json"))
        self.assertTrue(len(self.npc_files) > 70, f"Expected >70 NPC files, found {len(self.npc_files)}")
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            self.stats = json.load(f)

    def test_01_all_npc_json_files_are_valid_json(self):
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.assertIsInstance(data, dict, f"{p.name} must be a JSON object")
                except json.JSONDecodeError as e:
                    self.fail(f"Invalid JSON in {p.name}: {e}")

    def test_02_all_npcs_have_required_fields(self):
        required = ["name", "cr", "hp", "ac"]
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            for field in required:
                self.assertIn(field, data, f"{p.name} missing required field '{field}'")

    def test_03_all_npcs_have_valid_ability_scores(self):
        abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "ability_scores" in data and isinstance(data["ability_scores"], dict):
                for ab in abilities:
                    self.assertIn(ab, data["ability_scores"], f"{p.name} missing ability {ab}")
                    val = data["ability_scores"][ab]
                    self.assertIsInstance(val, int, f"{p.name} ability {ab} must be int")
                    self.assertTrue(1 <= val <= 30, f"{p.name} {ab} out of range 1-30: {val}")

    def test_04_all_npcs_have_positive_hp_and_ac(self):
        for p in self.npc_files:
            if "vacant" in p.name:
                continue
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            hp = data.get("hp")
            ac = data.get("ac")
            self.assertIsInstance(hp, int, f"{p.name} HP must be int")
            self.assertIsInstance(ac, int, f"{p.name} AC must be int")
            self.assertGreater(hp, 0, f"{p.name} HP must be > 0")
            self.assertGreater(ac, 0, f"{p.name} AC must be > 0")

    def test_05_all_npcs_have_valid_cr_format(self):
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            cr = str(data.get("cr", "")).strip()
            self.assertIn(cr, VALID_CRS, f"{p.name} has invalid CR '{cr}'")

    def test_06_no_duplicate_npc_names(self):
        names = set()
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            name = data.get("name")
            self.assertNotIn(name, names, f"Duplicate NPC name found: {name} in {p.name}")
            names.add(name)

    def test_07_hp_formula_syntax_when_present(self):
        pattern = re.compile(r"^(\d+|\d+d\d+([+-]\d+)?)$")
        for p in self.npc_files:
            if "vacant" in p.name:
                continue
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            formula = data.get("hp_formula")
            if formula:
                self.assertTrue(pattern.match(formula), f"{p.name} invalid hp_formula: {formula}")

    def test_08_mars_stat_block_session5(self):
        mars_file = NPC_DIR / "mars.json"
        self.assertTrue(mars_file.exists())
        data = json.loads(mars_file.read_text())
        self.assertEqual(data["name"], "Mars")
        self.assertEqual(data["cr"], "20")
        self.assertEqual(data["hp"], 100)
        self.assertEqual(data["ac"], 20)
        self.assertEqual(data["speed"], "40 ft.")

    def test_09_vercingetorix_bound_stat_block_session5(self):
        v_file = NPC_DIR / "vercingetorix_bound.json"
        self.assertTrue(v_file.exists())
        data = json.loads(v_file.read_text())
        self.assertEqual(data["name"], "Vercingetorix Bound")
        self.assertEqual(data["cr"], "11")
        self.assertEqual(data["hp"], 75)
        self.assertEqual(data["ac"], 18)

    def test_10_banshee_stat_block_session4(self):
        b_file = NPC_DIR / "banshee.json"
        self.assertTrue(b_file.exists())
        data = json.loads(b_file.read_text())
        self.assertEqual(data["name"], "Banshee")
        self.assertEqual(data["cr"], "4")
        self.assertEqual(data["hp"], 58)
        self.assertEqual(data["ac"], 12)

    def test_11_bone_naga_stat_block_session4(self):
        p = NPC_DIR / "bone_naga.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "4")
        self.assertEqual(data["hp"], 58)
        self.assertEqual(data["ac"], 15)

    def test_12_yochlol_stat_block_session4(self):
        p = NPC_DIR / "yochlol.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "6")
        self.assertEqual(data["hp"], 136)
        self.assertEqual(data["ac"], 15)

    def test_13_dretch_stat_block_session4(self):
        p = NPC_DIR / "dretch.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "1/4")
        self.assertEqual(data["hp"], 18)
        self.assertEqual(data["ac"], 11)

    def test_14_shadow_demon_stat_block_session4(self):
        p = NPC_DIR / "shadow_demon.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "4")
        self.assertEqual(data["hp"], 66)
        self.assertEqual(data["ac"], 12)

    def test_15_wraith_stat_block_session4(self):
        p = NPC_DIR / "wraith.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "5")
        self.assertEqual(data["hp"], 67)
        self.assertEqual(data["ac"], 13)

    def test_16_glabrezu_stat_block_session4(self):
        p = NPC_DIR / "glabrezu.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "9")
        self.assertEqual(data["hp"], 157)
        self.assertEqual(data["ac"], 17)

    def test_17_zombie_stat_block_session5(self):
        p = NPC_DIR / "zombie.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "1/4")
        self.assertEqual(data["hp"], 22)
        self.assertEqual(data["ac"], 8)

    def test_18_specter_stat_block_session5(self):
        p = NPC_DIR / "specter.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "1")
        self.assertEqual(data["hp"], 22)
        self.assertEqual(data["ac"], 12)

    def test_19_wight_stat_block_session5(self):
        p = NPC_DIR / "wight.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "3")
        self.assertEqual(data["hp"], 45)
        self.assertEqual(data["ac"], 14)

    def test_20_shadow_stat_block_session5(self):
        p = NPC_DIR / "shadow.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["cr"], "1/2")
        self.assertEqual(data["hp"], 16)
        self.assertEqual(data["ac"], 12)

    def test_21_augur_cassia_character_lore(self):
        p = NPC_DIR / "cassia.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertIn("Augur", data["name"])
        self.assertIn("secret", data)
        self.assertIn("shadow-touched", data["secret"])

    def test_22_legate_corvinus_character_lore(self):
        p = NPC_DIR / "corvinus.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertIn("Corvinus", data["name"])
        self.assertIn("hp", data)

    def test_23_creature_stats_json_consistency(self):
        self.assertIn("Mars", self.stats)
        self.assertIn("Vercingetorix_Bound", self.stats)
        self.assertIn("Banshee", self.stats)
        self.assertIn("Glabrezu", self.stats)
        self.assertIn("Wraith", self.stats)

    def test_24_creature_stats_mars_multiattack_and_traits(self):
        mars = self.stats["Mars"]
        self.assertEqual(mars["hp"], 100)
        self.assertEqual(mars["ac"], 20)
        self.assertEqual(mars["cr"], "20")
        labels = [a["label"] for a in mars["attacks"]]
        self.assertTrue(any("Divine Pilum" in l for l in labels))
        self.assertTrue(any("War Cry" in l for l in labels))

    def test_25_creature_stats_vercingetorix_relentless_and_death(self):
        v = self.stats["Vercingetorix_Bound"]
        self.assertEqual(v["hp"], 75)
        self.assertEqual(v["ac"], 18)
        self.assertEqual(v["cr"], "11")
        traits_str = " ".join(v.get("traits", []))
        self.assertIn("Relentless", traits_str)
        self.assertIn("Final Death", traits_str)

    def test_26_saving_throw_proficiencies_valid_keys(self):
        valid_saves = {"STR", "DEX", "CON", "INT", "WIS", "CHA"}
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            saves = data.get("saving_throw_proficiencies", [])
            for s in saves:
                self.assertIn(s, valid_saves, f"{p.name} invalid save proficiency '{s}'")

    def test_27_all_npcs_have_speed_string(self):
        for p in self.npc_files:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            speed = data.get("speed", "")
            self.assertIsInstance(speed, str, f"{p.name} speed must be string")
            self.assertIn("ft", speed.lower(), f"{p.name} speed should contain 'ft'")


if __name__ == "__main__":
    unittest.main()
