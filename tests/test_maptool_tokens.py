#!/usr/bin/env python3
"""
Unit tests for MapTool Tokens & Audio Macro Verification (Story 13.4).
Validates .rptok ZIP archive integrity, XML well-formedness, audio macros,
notes references, and campaign folder builds.
"""

import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NAMED_DIR = BASE / "Maptool/tokens/npcs/named"
CREATURES_DIR = BASE / "Maptool/tokens/npcs/creatures"
S4_CAMP_DIR = BASE / "Maptool/maps/campaign/S4_The_Gods_Demand"
S5_CAMP_DIR = BASE / "Maptool/maps/campaign/S5_The_Wrath_of_Mars"


def get_token_xml(token_path: Path) -> str:
    with zipfile.ZipFile(token_path, "r") as z:
        return z.read("content.xml").decode("utf-8")


class TestMapToolTokens(unittest.TestCase):

    def test_01_mars_rptok_zip_integrity(self):
        p = NAMED_DIR / "Mars.rptok"
        self.assertTrue(p.exists())
        with zipfile.ZipFile(p, "r") as z:
            names = z.namelist()
            self.assertIn("content.xml", names)
            self.assertIn("properties.xml", names)

    def test_02_vercingetorix_bound_rptok_zip_integrity(self):
        p = NAMED_DIR / "Vercingetorix_Bound.rptok"
        self.assertTrue(p.exists())
        with zipfile.ZipFile(p, "r") as z:
            names = z.namelist()
            self.assertIn("content.xml", names)
            self.assertIn("properties.xml", names)

    def test_03_banshee_rptok_zip_integrity(self):
        p = CREATURES_DIR / "Banshee.rptok"
        self.assertTrue(p.exists())
        with zipfile.ZipFile(p, "r") as z:
            self.assertIn("content.xml", z.namelist())

    def test_04_wraith_rptok_zip_integrity(self):
        p = CREATURES_DIR / "Wraith.rptok"
        self.assertTrue(p.exists())
        with zipfile.ZipFile(p, "r") as z:
            self.assertIn("content.xml", z.namelist())

    def test_05_glabrezu_rptok_zip_integrity(self):
        p = CREATURES_DIR / "Glabrezu.rptok"
        self.assertTrue(p.exists())
        with zipfile.ZipFile(p, "r") as z:
            self.assertIn("content.xml", z.namelist())

    def test_06_mars_content_xml_well_formed(self):
        xml_str = get_token_xml(NAMED_DIR / "Mars.rptok")
        try:
            ET.fromstring(xml_str)
        except ET.ParseError as e:
            self.fail(f"Mars.rptok content.xml malformed XML: {e}")

    def test_07_vercingetorix_bound_content_xml_well_formed(self):
        xml_str = get_token_xml(NAMED_DIR / "Vercingetorix_Bound.rptok")
        try:
            ET.fromstring(xml_str)
        except ET.ParseError as e:
            self.fail(f"Vercingetorix_Bound.rptok content.xml malformed XML: {e}")

    def test_08_banshee_content_xml_well_formed(self):
        xml_str = get_token_xml(CREATURES_DIR / "Banshee.rptok")
        try:
            ET.fromstring(xml_str)
        except ET.ParseError as e:
            self.fail(f"Banshee.rptok content.xml malformed XML: {e}")

    def test_09_wraith_content_xml_well_formed(self):
        xml_str = get_token_xml(CREATURES_DIR / "Wraith.rptok")
        try:
            ET.fromstring(xml_str)
        except ET.ParseError as e:
            self.fail(f"Wraith.rptok content.xml malformed XML: {e}")

    def test_10_glabrezu_content_xml_well_formed(self):
        xml_str = get_token_xml(CREATURES_DIR / "Glabrezu.rptok")
        try:
            ET.fromstring(xml_str)
        except ET.ParseError as e:
            self.fail(f"Glabrezu.rptok content.xml malformed XML: {e}")

    def test_11_mars_audio_macros_exist(self):
        xml = get_token_xml(NAMED_DIR / "Mars.rptok")
        self.assertIn("Voice: Challenge", xml)
        self.assertIn("Voice: Chained Roar", xml)
        self.assertIn("Voice: Depart Cold", xml)
        self.assertIn("s5_mars_challenge.mp3", xml)

    def test_12_vercingetorix_bound_audio_macros_exist(self):
        xml = get_token_xml(NAMED_DIR / "Vercingetorix_Bound.rptok")
        self.assertIn("Voice: Entrance", xml)
        self.assertIn("Voice: Final Death", xml)
        self.assertIn("s5_vercingetorix_final_death.mp3", xml)

    def test_13_banshee_audio_macro_exists(self):
        xml = get_token_xml(CREATURES_DIR / "Banshee.rptok")
        self.assertIn("Voice: Dread Wail", xml)
        self.assertIn("s4_banshee_dread_mother.mp3", xml)

    def test_14_wraith_audio_macro_exists(self):
        xml = get_token_xml(CREATURES_DIR / "Wraith.rptok")
        self.assertIn("Voice: Confession", xml)
        self.assertIn("s4_wraith_chieftain_confession.mp3", xml)

    def test_15_glabrezu_audio_macro_exists(self):
        xml = get_token_xml(CREATURES_DIR / "Glabrezu.rptok")
        self.assertIn("Voice: Mocking Entrance", xml)
        self.assertIn("s4_glabrezu_core_entrance.mp3", xml)

    def test_16_mars_notes_contain_audio_references(self):
        xml = get_token_xml(NAMED_DIR / "Mars.rptok")
        self.assertIn("AUDIO CUES:", xml)
        self.assertIn("s5_mars_challenge.mp3", xml)

    def test_17_vercingetorix_bound_notes_contain_audio_references(self):
        xml = get_token_xml(NAMED_DIR / "Vercingetorix_Bound.rptok")
        self.assertIn("AUDIO CUES:", xml)
        self.assertIn("s5_vercingetorix_final_death.mp3", xml)

    def test_18_banshee_notes_contain_audio_references(self):
        xml = get_token_xml(CREATURES_DIR / "Banshee.rptok")
        self.assertIn("AUDIO CUES:", xml)
        self.assertIn("s4_banshee_dread_mother.mp3", xml)

    def test_19_wraith_notes_contain_audio_references(self):
        xml = get_token_xml(CREATURES_DIR / "Wraith.rptok")
        self.assertIn("AUDIO CUES:", xml)
        self.assertIn("s4_wraith_chieftain_confession.mp3", xml)

    def test_20_glabrezu_notes_contain_audio_references(self):
        xml = get_token_xml(CREATURES_DIR / "Glabrezu.rptok")
        self.assertIn("AUDIO CUES:", xml)
        self.assertIn("s4_glabrezu_core_entrance.mp3", xml)

    def test_21_s4_campaign_map_pack_contains_creature_tokens(self):
        self.assertTrue(S4_CAMP_DIR.exists())
        for token_name in ["Banshee.rptok", "Wraith.rptok", "Glabrezu.rptok"]:
            self.assertTrue((S4_CAMP_DIR / token_name).exists(), f"Token {token_name} missing in S4 campaign map pack")

    def test_22_s5_campaign_map_pack_contains_named_tokens(self):
        self.assertTrue(S5_CAMP_DIR.exists())
        for token_name in ["Mars.rptok", "Vercingetorix_Bound.rptok", "Wraith.rptok", "Wight.rptok"]:
            self.assertTrue((S5_CAMP_DIR / token_name).exists(), f"Token {token_name} missing in S5 campaign map pack")


if __name__ == "__main__":
    unittest.main()
