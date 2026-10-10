#!/usr/bin/env python3
"""
Unit tests for Voice Audio Clips & Audio Manifest Integrity (Story 13.2).
Validates audio/voice_manifest.json and all 11 generated MP3 clips in audio/clips/.
"""

import json
import os
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MANIFEST_FILE = BASE / "audio/voice_manifest.json"
CLIPS_DIR = BASE / "audio/clips"

EXPECTED_CLIP_IDS = [
    "s4_scene0_marsh_readaloud",
    "s4_banshee_dread_mother",
    "s4_wraith_chieftain_confession",
    "s4_glabrezu_core_entrance",
    "s5_scene0_descent_readaloud",
    "s5_vercingetorix_entrance",
    "s5_vercingetorix_final_death",
    "s5_janus_threshold",
    "s5_mars_challenge",
    "s5_mars_destroy_reaction",
    "s5_mars_depart_reaction"
]

ALLOWED_VOICES = {"onyx", "fable", "shimmer", "echo", "nova", "alloy"}


def is_valid_mp3_header(file_path: Path) -> bool:
    """Check if file starts with ID3 header or MP3 frame sync bytes."""
    with open(file_path, "rb") as f:
        head = f.read(10)
    if head[:3] == b"ID3":
        return True
    if len(head) >= 2 and head[0] == 0xFF and (head[1] & 0xE0) == 0xE0:
        return True
    return False


class TestAudioIntegrity(unittest.TestCase):

    def setUp(self):
        self.assertTrue(MANIFEST_FILE.exists(), "audio/voice_manifest.json must exist")
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            self.manifest = json.load(f)

    def test_01_voice_manifest_valid_json(self):
        self.assertIn("endpoint", self.manifest)
        self.assertIn("clips", self.manifest)
        self.assertIsInstance(self.manifest["clips"], list)

    def test_02_voice_manifest_has_all_11_clips(self):
        manifest_ids = [c["id"] for c in self.manifest["clips"]]
        for cid in EXPECTED_CLIP_IDS:
            self.assertIn(cid, manifest_ids, f"Clip {cid} missing from manifest")
        self.assertEqual(len(self.manifest["clips"]), 11)

    def test_03_voice_manifest_fields_structure(self):
        required = ["id", "session", "scene", "character", "voice", "text"]
        for c in self.manifest["clips"]:
            for f in required:
                self.assertIn(f, c, f"Clip {c.get('id')} missing field {f}")
                self.assertTrue(bool(c[f]), f"Clip {c.get('id')} field {f} cannot be empty")

    def test_04_voice_manifest_uses_valid_voices(self):
        for c in self.manifest["clips"]:
            self.assertIn(c["voice"], ALLOWED_VOICES, f"Clip {c['id']} uses invalid voice {c['voice']}")

    def test_05_all_11_audio_files_exist_on_disk(self):
        for cid in EXPECTED_CLIP_IDS:
            p = CLIPS_DIR / f"{cid}.mp3"
            self.assertTrue(p.exists(), f"Audio file missing on disk: {p.name}")

    def test_06_all_audio_files_above_minimum_size(self):
        for cid in EXPECTED_CLIP_IDS:
            p = CLIPS_DIR / f"{cid}.mp3"
            size = p.stat().st_size
            self.assertGreater(size, 10000, f"Clip {p.name} too small ({size} bytes), might be truncated")

    def test_07_all_audio_files_have_valid_mp3_header(self):
        for cid in EXPECTED_CLIP_IDS:
            p = CLIPS_DIR / f"{cid}.mp3"
            self.assertTrue(is_valid_mp3_header(p), f"Clip {p.name} does not have valid MP3/ID3 header")

    def test_08_s4_marsh_readaloud_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s4_scene0_marsh_readaloud")
        self.assertEqual(clip["session"], 4)
        self.assertEqual(clip["voice"], "fable")
        self.assertIn("causeway of bone", clip["text"].lower())

    def test_09_s4_banshee_audio_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s4_banshee_dread_mother")
        self.assertIn("Banshee", clip["character"])
        self.assertEqual(clip["voice"], "shimmer")
        self.assertIn("water remembers", clip["text"].lower())

    def test_10_s4_wraith_chieftain_audio_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s4_wraith_chieftain_confession")
        self.assertIn("Wraith", clip["character"])
        self.assertEqual(clip["voice"], "echo")
        self.assertIn("blood", clip["text"].lower())

    def test_11_s4_glabrezu_core_entrance_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s4_glabrezu_core_entrance")
        self.assertIn("Glabrezu", clip["character"])
        self.assertEqual(clip["voice"], "onyx")
        self.assertIn("harvest", clip["text"].lower())

    def test_12_s5_descent_readaloud_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_scene0_descent_readaloud")
        self.assertEqual(clip["session"], 5)
        self.assertEqual(clip["voice"], "fable")
        self.assertIn("crystal", clip["text"].lower())

    def test_13_s5_vercingetorix_entrance_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_vercingetorix_entrance")
        self.assertIn("Vercingetorix", clip["character"])
        self.assertEqual(clip["voice"], "onyx")
        self.assertIn("always again", clip["text"].lower())

    def test_14_s5_vercingetorix_final_death_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_vercingetorix_final_death")
        self.assertIn("caesar", clip["text"].lower())
        self.assertIn("four iron ring", clip["text"].lower())
        self.assertIn("gaul still stand", clip["text"].lower())

    def test_15_s5_janus_threshold_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_janus_threshold")
        self.assertIn("Janus", clip["character"])
        self.assertEqual(clip["voice"], "echo")
        self.assertIn("war itself", clip["text"].lower())

    def test_16_s5_mars_challenge_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_mars_challenge")
        self.assertIn("Mars", clip["character"])
        self.assertEqual(clip["voice"], "onyx")
        self.assertIn("mortals", clip["text"].lower())

    def test_17_s5_mars_destroy_reaction_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_mars_destroy_reaction")
        self.assertIn("chains", clip["text"].lower())

    def test_18_s5_mars_depart_reaction_properties(self):
        clip = next(c for c in self.manifest["clips"] if c["id"] == "s5_mars_depart_reaction")
        self.assertIn("wise", clip["text"].lower())


if __name__ == "__main__":
    unittest.main()
