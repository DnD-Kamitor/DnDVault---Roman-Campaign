#!/usr/bin/env python3
"""
Unit tests for GM Cheat Cards & HTML5 Audio Player Integration (Story 13.3).
Validates gm_tools/cheat_card_ch4.html and cheat_card_ch5.html DOM, JS audio players,
file path resolution, and Quarto resource bundling.
"""

import os
import re
import unittest
from pathlib import Path
import yaml

BASE = Path(__file__).resolve().parent.parent
CH4_CARD = BASE / "gm_tools/cheat_card_ch4.html"
CH5_CARD = BASE / "gm_tools/cheat_card_ch5.html"
QUARTO_YML = BASE / "_quarto.yml"


class TestCheatCards(unittest.TestCase):

    def setUp(self):
        self.assertTrue(CH4_CARD.exists(), "cheat_card_ch4.html must exist")
        self.assertTrue(CH5_CARD.exists(), "cheat_card_ch5.html must exist")
        self.ch4_html = CH4_CARD.read_text(encoding="utf-8")
        self.ch5_html = CH5_CARD.read_text(encoding="utf-8")

    def test_01_ch4_card_exists_and_non_empty(self):
        self.assertGreater(len(self.ch4_html), 1000)

    def test_02_ch5_card_exists_and_non_empty(self):
        self.assertGreater(len(self.ch5_html), 1000)

    def test_03_ch4_has_playaudio_js_function(self):
        self.assertIn("function playAudio(btn, file)", self.ch4_html)
        self.assertIn("new Audio(file)", self.ch4_html)
        self.assertIn("audio.play()", self.ch4_html)

    def test_04_ch5_has_playaudio_js_function(self):
        self.assertIn("function playAudio(btn, file)", self.ch5_html)
        self.assertIn("new Audio(file)", self.ch5_html)
        self.assertIn("audio.play()", self.ch5_html)

    def test_05_ch4_has_audio_btn_css(self):
        self.assertIn(".audio-btn {", self.ch4_html)
        self.assertIn(".audio-btn.playing", self.ch4_html)

    def test_06_ch5_has_audio_btn_css(self):
        self.assertIn(".audio-btn {", self.ch5_html)
        self.assertIn(".audio-btn.playing", self.ch5_html)

    def test_07_ch4_contains_all_4_s4_audio_clips(self):
        expected_clips = [
            "s4_scene0_marsh_readaloud.mp3",
            "s4_banshee_dread_mother.mp3",
            "s4_wraith_chieftain_confession.mp3",
            "s4_glabrezu_core_entrance.mp3"
        ]
        for clip in expected_clips:
            self.assertIn(clip, self.ch4_html, f"Clip {clip} missing in cheat_card_ch4.html")

    def test_08_ch5_contains_all_7_s5_audio_clips(self):
        expected_clips = [
            "s5_scene0_descent_readaloud.mp3",
            "s5_vercingetorix_entrance.mp3",
            "s5_vercingetorix_final_death.mp3",
            "s5_janus_threshold.mp3",
            "s5_mars_challenge.mp3",
            "s5_mars_destroy_reaction.mp3",
            "s5_mars_depart_reaction.mp3"
        ]
        for clip in expected_clips:
            self.assertIn(clip, self.ch5_html, f"Clip {clip} missing in cheat_card_ch5.html")

    def test_09_ch4_audio_relative_paths_resolve_to_real_files(self):
        pattern = re.compile(r"playAudio\(this,\s*'([^']+)'\)")
        matches = pattern.findall(self.ch4_html)
        self.assertEqual(len(matches), 4, f"Expected 4 audio buttons in ch4, found {len(matches)}")
        for rel_path in matches:
            resolved = (CH4_CARD.parent / rel_path).resolve()
            self.assertTrue(resolved.exists(), f"Path '{rel_path}' in ch4 does not exist on disk ({resolved})")

    def test_10_ch5_audio_relative_paths_resolve_to_real_files(self):
        pattern = re.compile(r"playAudio\(this,\s*'([^']+)'\)")
        matches = pattern.findall(self.ch5_html)
        self.assertEqual(len(matches), 7, f"Expected 7 audio buttons in ch5, found {len(matches)}")
        for rel_path in matches:
            resolved = (CH5_CARD.parent / rel_path).resolve()
            self.assertTrue(resolved.exists(), f"Path '{rel_path}' in ch5 does not exist on disk ({resolved})")

    def test_11_ch4_tab_pane_navigation_consistency(self):
        btn_tabs = set(re.findall(r"showTab\('([^']+)'", self.ch4_html))
        panes = set(re.findall(r'id="tab-([^"]+)"', self.ch4_html))
        self.assertEqual(btn_tabs, panes, "Tab buttons do not match pane IDs in ch4")

    def test_12_ch5_tab_pane_navigation_consistency(self):
        btn_tabs = set(re.findall(r"showTab\('([^']+)'", self.ch5_html))
        panes = set(re.findall(r'id="tab-([^"]+)"', self.ch5_html))
        self.assertEqual(btn_tabs, panes, "Tab buttons do not match pane IDs in ch5")

    def test_13_quarto_yml_includes_audio_resources(self):
        self.assertTrue(QUARTO_YML.exists())
        with open(QUARTO_YML, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        resources = cfg.get("project", {}).get("resources", [])
        self.assertIn("audio/clips/*.mp3", resources, "_quarto.yml must include 'audio/clips/*.mp3' in resources")

    def test_14_ch4_monster_manual_dndbeyond_links(self):
        self.assertIn("https://www.dndbeyond.com/monsters/16799-banshee", self.ch4_html)
        self.assertIn("https://www.dndbeyond.com/monsters/16812-bone-naga", self.ch4_html)
        self.assertIn("https://www.dndbeyond.com/monsters/17068-yochlol", self.ch4_html)
        self.assertIn("https://www.dndbeyond.com/monsters/16870-glabrezu", self.ch4_html)

    def test_15_ch5_monster_manual_dndbeyond_links(self):
        self.assertIn("https://www.dndbeyond.com/monsters/17069-zombie", self.ch5_html)
        self.assertIn("https://www.dndbeyond.com/monsters/17054-wight", self.ch5_html)
        self.assertIn("https://www.dndbeyond.com/monsters/17017-specter", self.ch5_html)

    def test_16_html_tags_well_formed(self):
        for name, doc in [("ch4", self.ch4_html), ("ch5", self.ch5_html)]:
            self.assertIn("<!DOCTYPE html>", doc, f"{name} missing DOCTYPE")
            self.assertIn("<html", doc, f"{name} missing <html>")
            self.assertIn("</html>", doc, f"{name} missing </html>")
            self.assertIn("<body", doc, f"{name} missing <body>")
            self.assertIn("</body>", doc, f"{name} missing </body>")


if __name__ == "__main__":
    unittest.main()
