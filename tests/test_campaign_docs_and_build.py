"""
test_campaign_docs_and_build.py — Automated verification test suite for Quarto
book configuration, table automation builders, campaign log continuity, and
Monster Manual combat links across Chapter 4 and Chapter 5.

Part of Epic 13 (Story 13.6).
"""

import csv
import re
import subprocess
import unittest
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
QUARTO_YML = REPO_ROOT / "_quarto.yml"
BUILD_TABLES_PY = REPO_ROOT / "scripts" / "build_tables.py"
DATA_EQUIPMENT_CSV = REPO_ROOT / "data" / "equipment.csv"
GENERATED_DIR = REPO_ROOT / "_generated"
CAMPAIGN_LOG_MD = REPO_ROOT / "CAMPAIGN_LOG.md"
CHAPTER4_QMD = REPO_ROOT / "chapter4.qmd"
CHAPTER5_QMD = REPO_ROOT / "chapter5.qmd"

EXPECTED_TABLE_FILES = [
    "ref_weapons_melee.md",
    "ref_weapons_thrown.md",
    "ref_weapons_ranged.md",
    "ref_ammo.md",
    "ref_armor.md",
    "ref_shields.md",
    "ref_helmets.md",
    "ref_gear.md",
    "ref_commission.md",
    "ref_vicus.md",
    "ref_aelius.md",
]


class TestCampaignDocsAndBuild(unittest.TestCase):
    """Verifies Quarto config, table generator, campaign logs, and MM links."""

    def test_01_quarto_yml_exists_and_valid_yaml(self):
        """_quarto.yml exists and parses as valid YAML."""
        self.assertTrue(QUARTO_YML.is_file(), "_quarto.yml must exist at repo root")
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        self.assertIsInstance(cfg, dict, "_quarto.yml must parse into a dictionary")
        self.assertIn("project", cfg)
        self.assertIn("book", cfg)
        self.assertIn("format", cfg)

    def test_02_quarto_yml_project_type_book_and_output_dir(self):
        """_quarto.yml defines project type as book with _book output-dir."""
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        self.assertEqual(cfg["project"].get("type"), "book")
        self.assertEqual(cfg["project"].get("output-dir"), "_book")

    def test_03_quarto_yml_pre_render_hook_builds_tables(self):
        """_quarto.yml specifies scripts/build_tables.py in pre-render hook."""
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        pre_render = cfg["project"].get("pre-render", "")
        self.assertIn("scripts/build_tables.py", str(pre_render), "pre-render hook must invoke scripts/build_tables.py")

    def test_04_quarto_yml_resources_include_html_json_mp3(self):
        """_quarto.yml resources include gm_tools HTML, npc JSON, and audio MP3s."""
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        resources = cfg["project"].get("resources", [])
        self.assertTrue(any("gm_tools" in r for r in resources), "gm_tools/*.html must be in resources")
        self.assertTrue(any("npcs" in r for r in resources), "npcs/*.json must be in resources")
        self.assertTrue(any("audio" in r for r in resources), "audio/clips/*.mp3 must be in resources")

    def test_05_quarto_yml_all_48_referenced_chapters_exist(self):
        """Every chapter and section file referenced in _quarto.yml exists on disk."""
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        def extract_chapters(obj):
            res = []
            if isinstance(obj, list):
                for item in obj:
                    res.extend(extract_chapters(item))
            elif isinstance(obj, dict):
                if "chapters" in obj:
                    res.extend(extract_chapters(obj["chapters"]))
            elif isinstance(obj, str):
                res.append(obj)
            return res

        chapters = extract_chapters(cfg["book"]["chapters"])
        self.assertGreaterEqual(len(chapters), 45, "Campaign book should list at least 45 chapter/section files")

        missing = [c for c in chapters if not (REPO_ROOT / c).exists()]
        self.assertEqual(missing, [], f"Missing chapters referenced in _quarto.yml: {missing}")

    def test_06_data_equipment_csv_exists_and_valid(self):
        """data/equipment.csv exists and contains required column headers and rows."""
        self.assertTrue(DATA_EQUIPMENT_CSV.is_file(), "data/equipment.csv must exist")
        with open(DATA_EQUIPMENT_CSV, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            rows = list(reader)

        required_cols = {"name_latin", "name_english", "category", "damage", "cost_d", "availability"}
        self.assertTrue(required_cols.issubset(set(headers)), f"Missing columns in equipment.csv: {required_cols - set(headers)}")
        self.assertGreater(len(rows), 50, "equipment.csv should have at least 50 equipment items")

    def test_07_build_tables_executes_successfully(self):
        """scripts/build_tables.py executes cleanly without error."""
        self.assertTrue(BUILD_TABLES_PY.is_file(), "scripts/build_tables.py must exist")
        res = subprocess.run(
            ["python3", str(BUILD_TABLES_PY)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(res.returncode, 0, f"build_tables.py failed: {res.stderr}")
        self.assertIn("11 files in _generated/", res.stdout)

    def test_08_generated_tables_all_11_exist(self):
        """All 11 markdown table files exist in _generated/."""
        self.assertTrue(GENERATED_DIR.is_dir(), "_generated directory must exist")
        for expected in EXPECTED_TABLE_FILES:
            table_path = GENERATED_DIR / expected
            self.assertTrue(table_path.is_file(), f"Missing generated table file: {expected}")
            self.assertGreater(table_path.stat().st_size, 100, f"{expected} must not be empty")

    def test_09_generated_tables_have_valid_pipe_structure(self):
        """Generated tables have valid Markdown pipe format (| ... |) and separator rows."""
        for expected in EXPECTED_TABLE_FILES:
            table_path = GENERATED_DIR / expected
            content = table_path.read_text(encoding="utf-8").strip().splitlines()
            self.assertGreaterEqual(len(content), 3, f"{expected} must have header, separator, and data rows")
            header = content[0]
            sep = content[1]
            self.assertTrue(header.startswith("|") and header.endswith("|"), f"{expected} header format invalid")
            self.assertTrue(sep.startswith("|") and "---" in sep, f"{expected} separator format invalid")

    def test_10_campaign_log_exists_and_lucius_recorded_dead(self):
        """CAMPAIGN_LOG.md records Tribune Lucius as dead from the S3 spider lure."""
        self.assertTrue(CAMPAIGN_LOG_MD.is_file(), "CAMPAIGN_LOG.md must exist")
        log_text = CAMPAIGN_LOG_MD.read_text(encoding="utf-8")
        self.assertIn("Tribune Lucius", log_text)
        self.assertRegex(log_text, r"Tribune Lucius\s*\|\s*\*\*Dead\*\*", "Lucius must be recorded as Dead in NPC table")
        self.assertIn("spider", log_text.lower(), "Lucius demise via giant spiders must be documented")

    def test_11_campaign_log_varro_recorded_dead(self):
        """CAMPAIGN_LOG.md records Centurion Varro as dead at the fort gate."""
        log_text = CAMPAIGN_LOG_MD.read_text(encoding="utf-8")
        self.assertIn("Centurion Varro", log_text)
        self.assertRegex(log_text, r"Centurion Varro\s*\|\s*\*\*Dead\*\*", "Varro must be recorded as Dead in NPC table")
        self.assertIn("Ursula", log_text, "Varro duel with Ursula must be referenced")

    def test_12_campaign_log_mars_thematic_motive(self):
        """CAMPAIGN_LOG.md documents Mars as pro-war, diminished by Pax Romana, seeking perpetual strife."""
        log_text = CAMPAIGN_LOG_MD.read_text(encoding="utf-8")
        self.assertIn("Mars", log_text)
        self.assertIn("Pax Romana", log_text)
        self.assertIn("pro-war", log_text)

    def test_13_campaign_log_vercingetorix_and_wight_lore(self):
        """CAMPAIGN_LOG.md details Vercingetorix's ancient binding and Wight general guardian connection."""
        log_text = CAMPAIGN_LOG_MD.read_text(encoding="utf-8")
        self.assertIn("Vercingetorix", log_text)
        self.assertIn("Alesia", log_text)
        self.assertIn("the Wight is the general", log_text)

    def test_14_chapter4_structure_and_scenes(self):
        """chapter4.qmd defines Scenes 1 through 5 in chronological flow."""
        self.assertTrue(CHAPTER4_QMD.is_file(), "chapter4.qmd must exist")
        ch4 = CHAPTER4_QMD.read_text(encoding="utf-8")
        for scene_num in range(1, 6):
            self.assertIn(f"Scene {scene_num}:", ch4, f"chapter4.qmd missing Scene {scene_num}")

    def test_15_chapter4_monster_manual_dndbeyond_links(self):
        """chapter4.qmd links official Monster Manual creatures with D&D Beyond URLs."""
        ch4 = CHAPTER4_QMD.read_text(encoding="utf-8")
        expected_monsters = [
            ("Banshee", "16799-banshee"),
            ("Bone Naga", "16812-bone-naga"),
            ("Skeleton", "17015-skeleton"),
            ("Yochlol", "17068-yochlol"),
            ("Dretch", "16847-dretch"),
            ("Shadow Demon", "17010-shadow-demon"),
            ("Wraith", "17064-wraith"),
            ("Glabrezu", "16870-glabrezu"),
        ]
        for monster_name, url_slug in expected_monsters:
            self.assertIn(f"dndbeyond.com/monsters/{url_slug}", ch4, f"Missing D&D Beyond link for {monster_name} in Chapter 4")
            self.assertIn("Monster Manual", ch4, f"Monster Manual page reference missing for {monster_name}")

    def test_16_chapter5_structure_and_options(self):
        """chapter5.qmd defines the climactic confrontation and all campaign options."""
        self.assertTrue(CHAPTER5_QMD.is_file(), "chapter5.qmd must exist")
        ch5 = CHAPTER5_QMD.read_text(encoding="utf-8")
        self.assertIn("Option 1 — Destroy It Completely", ch5)
        self.assertIn("Option 2 — Give It to Rome", ch5)
        self.assertIn("Option 3 — Give It Back to Mars", ch5)

    def test_17_chapter5_monster_manual_dndbeyond_links(self):
        """chapter5.qmd links official Monster Manual creatures with D&D Beyond URLs."""
        ch5 = CHAPTER5_QMD.read_text(encoding="utf-8")
        expected_monsters = [
            ("Wraith", "17064-wraith"),
            ("Zombie", "17069-zombie"),
            ("Wight", "17054-wight"),
            ("Specter", "17017-specter"),
        ]
        for monster_name, url_slug in expected_monsters:
            self.assertIn(f"dndbeyond.com/monsters/{url_slug}", ch5, f"Missing D&D Beyond link for {monster_name} in Chapter 5")

    def test_18_chapter5_boss_combat_and_binding_mechanics(self):
        """chapter5.qmd details Mars Avatar, Vercingetorix last stand, and unmaking ritual mechanics."""
        ch5 = CHAPTER5_QMD.read_text(encoding="utf-8")
        self.assertIn("Divine Avatar", ch5)
        self.assertIn("Vercingetorix's Last Stand", ch5)
        self.assertIn("Divine Pilum", ch5)
        self.assertIn("Interactive Unmaking", ch5)
        self.assertIn("Legendary Actions", ch5)

    def test_19_chapter4_and_5_respect_lucius_deceased_status(self):
        """Chapters 4 and 5 treat Tribune Lucius as deceased and do not field him as an active living combatant."""
        ch4 = CHAPTER4_QMD.read_text(encoding="utf-8")
        ch5 = CHAPTER5_QMD.read_text(encoding="utf-8")

        # In Chapter 4: Lucius died in Session 3, party travels alone
        self.assertIn("Tribune Lucius died in Session 3", ch4)
        # In Chapter 5: Lucius dead is explicitly noted in endings and epilogue
        self.assertIn("With Tribune Lucius dead", ch5)
        self.assertIn("Tribune Lucius (Deceased)", ch5)


if __name__ == "__main__":
    unittest.main()
