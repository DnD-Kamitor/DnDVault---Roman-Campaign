#!/usr/bin/env python3
"""
Unit tests for AI Personas & Campaign RAG Ingestion (Story 13.5).
Validates OpenWebUI persona schemas, system prompt constraints,
markdown/JSON RAG chunking logic, and Qdrant collection connectivity.
"""

import json
import unittest
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PERSONAS_DIR = BASE / "ai_personas"
RAG_SCRIPT = BASE / "scripts/index_campaign_rag.py"
QDRANT_URL = "http://localhost:6333"


class TestAIPersonasAndRAG(unittest.TestCase):

    def setUp(self):
        self.assertTrue(PERSONAS_DIR.exists())
        self.cassia_path = PERSONAS_DIR / "augur_cassia.json"
        self.mars_path = PERSONAS_DIR / "whispers_of_mars.json"
        self.v_path = PERSONAS_DIR / "vercingetorix_sparring.json"

    def test_01_all_persona_files_exist(self):
        self.assertTrue(self.cassia_path.exists())
        self.assertTrue(self.mars_path.exists())
        self.assertTrue(self.v_path.exists())

    def test_02_augur_cassia_valid_openwebui_format(self):
        data = json.loads(self.cassia_path.read_text(encoding="utf-8"))
        self.assertEqual(data["id"], "augur-cassia")
        self.assertIn("name", data)
        self.assertIn("system", data.get("params", {}))
        self.assertEqual(data.get("rag", {}).get("collection"), "shadow-of-mars")

    def test_03_whispers_of_mars_valid_openwebui_format(self):
        data = json.loads(self.mars_path.read_text(encoding="utf-8"))
        self.assertEqual(data["id"], "whispers-of-mars")
        self.assertIn("system", data.get("params", {}))
        self.assertEqual(data.get("rag", {}).get("collection"), "shadow-of-mars")

    def test_04_vercingetorix_sparring_valid_openwebui_format(self):
        data = json.loads(self.v_path.read_text(encoding="utf-8"))
        self.assertEqual(data["id"], "vercingetorix-sparring")
        self.assertIn("system", data.get("params", {}))
        self.assertEqual(data.get("rag", {}).get("collection"), "shadow-of-mars")

    def test_05_augur_cassia_prompt_haruspex_keywords(self):
        data = json.loads(self.cassia_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        keywords = ["haruspicina", "Clavis Caeli", "Caput extorum", "Fas", "Nefas"]
        for kw in keywords:
            self.assertIn(kw.lower(), system.lower(), f"Augur Cassia prompt missing '{kw}'")

    def test_06_augur_cassia_prompt_enforces_objective(self):
        data = json.loads(self.cassia_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        self.assertIn("prevent the spear from leaving the vault", system.lower())
        self.assertIn("shadow-touched", system.lower())

    def test_07_whispers_of_mars_corruption_tiers_1_to_5(self):
        data = json.loads(self.mars_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        for tier in ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]:
            self.assertIn(tier, system, f"Whispers of Mars prompt missing guidance for {tier}")

    def test_08_whispers_of_mars_ogas_enforcement(self):
        data = json.loads(self.mars_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        self.assertIn("hesitation", system.lower())
        self.assertIn("starved", system.lower())
        self.assertIn("granite altar", system.lower())

    def test_09_vercingetorix_3_question_limit_enforced(self):
        data = json.loads(self.v_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        self.assertIn("three (3) questions", system.lower())
        self.assertIn("question 1", system.lower())
        self.assertIn("question 2", system.lower())
        self.assertIn("question 3", system.lower())

    def test_10_vercingetorix_chain_unmaking_secret(self):
        data = json.loads(self.v_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        self.assertIn("four massive iron chain winches", system.lower())
        self.assertIn("caesar", system.lower())
        self.assertIn("shatter his armor", system.lower())

    def test_11_vercingetorix_dissolution_to_ash(self):
        data = json.loads(self.v_path.read_text(encoding="utf-8"))
        system = data["params"]["system"]
        self.assertIn("ash", system.lower())
        self.assertIn("gaul still stand", system.lower())

    def test_12_rag_script_exists_and_callable(self):
        self.assertTrue(RAG_SCRIPT.exists())
        code = RAG_SCRIPT.read_text(encoding="utf-8")
        self.assertIn("def chunk_markdown(", code)
        self.assertIn("def chunk_npc(", code)
        self.assertIn("def get_embedding(", code)
        self.assertIn("def ensure_qdrant_collection(", code)

    def test_13_chunk_markdown_logic(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("rag", str(RAG_SCRIPT))
        rag = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rag)

        # Chunk chapter4.qmd
        chunks = rag.chunk_markdown(BASE / "chapter4.qmd")
        self.assertGreater(len(chunks), 5)
        for c in chunks:
            self.assertIn("source", c)
            self.assertIn("heading", c)
            self.assertIn("text", c)
            self.assertGreater(len(c["text"]), 20)

    def test_14_chunk_npc_logic(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("rag", str(RAG_SCRIPT))
        rag = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rag)

        c = rag.chunk_npc(BASE / "npcs/mars.json")
        self.assertIsNotNone(c)
        self.assertEqual(c["npc_name"], "Mars")
        self.assertIn("Challenge Rating: 20", c["text"])
        self.assertIn("HP: 100", c["text"])

    def test_15_live_qdrant_collection_status(self):
        try:
            url = f"{QDRANT_URL}/collections/shadow-of-mars"
            with urllib.request.urlopen(url, timeout=3) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            result = data.get("result", {})
            self.assertIn(result.get("status"), ["green", "yellow", "ok"])
            vec_size = result.get("config", {}).get("params", {}).get("vectors", {}).get("size")
            self.assertEqual(vec_size, 768, f"Expected vector size 768, got {vec_size}")
            points_count = result.get("points_count", 0)
            self.assertGreater(points_count, 100, f"Expected >100 indexed points, got {points_count}")
        except urllib.error.URLError:
            self.skipTest("Qdrant service not reachable at http://localhost:6333")


if __name__ == "__main__":
    unittest.main()
