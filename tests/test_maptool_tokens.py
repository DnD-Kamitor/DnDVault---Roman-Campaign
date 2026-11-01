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
PLAYERS_DIR = BASE / "Maptool/tokens/players"
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

    def test_23_rivia_player_token_has_box_cataclysm_notes(self):
        p = PLAYERS_DIR / "Rivia_Calida_Mendera.rptok"
        self.assertTrue(p.exists())
        xml = get_token_xml(p)
        self.assertIn("BOX CATACLYSM", xml)
        self.assertIn("Spear of Mars", xml)
        self.assertIn("Goliath Berserker Greataxe", xml)
        self.assertIn("Intimidation", xml)

    def test_24_rivia_player_token_has_box_cataclysm_macro(self):
        xml = get_token_xml(PLAYERS_DIR / "Rivia_Calida_Mendera.rptok")
        self.assertIn("Box Cataclysm Aura", xml)

    def test_25_ursula_player_token_has_weapon_sealed_notes(self):
        p = PLAYERS_DIR / "Ursula_Günther.rptok"
        self.assertTrue(p.exists())
        xml = get_token_xml(p)
        self.assertIn("PRIMARY WEAPON SEALED", xml)
        self.assertIn("Goliath Berserker Greataxe", xml)
        self.assertIn("secondary", xml.lower())

    def test_26_ursula_player_token_has_secondary_weapon_macro(self):
        xml = get_token_xml(PLAYERS_DIR / "Ursula_Günther.rptok")
        self.assertIn("Secondary Weapons", xml)

    def test_27_all_player_tokens_have_valid_sight_and_layer(self):
        player_tokens = [
            "Brian.rptok", "Iris.rptok", "Julia_Jana.rptok",
            "Rivia_Calida_Mendera.rptok", "Tanit_bint_Abdmelqart.rptok", "Ursula_Günther.rptok"
        ]
        for name in player_tokens:
            p = PLAYERS_DIR / name
            self.assertTrue(p.exists(), f"Missing player token: {name}")
            with zipfile.ZipFile(p, "r") as z:
                root = ET.fromstring(z.read("content.xml").decode("utf-8"))
                self.assertEqual(root.findtext("hasSight"), "true", f"{name} hasSight not true")
                self.assertEqual(root.findtext("layer"), "TOKEN", f"{name} layer not TOKEN")
                self.assertIn(root.findtext("sightType"), ["Darkvision 120", "Darkvision 60", "Normal"], f"{name} invalid sightType")

    def test_28_thusnelda_token_uses_male_pronouns_and_has_ritual_clock(self):
        p = NAMED_DIR / "Thusnelda.rptok"
        xml = get_token_xml(p)
        self.assertIn("MALE VÖLVA SEER", xml)
        self.assertIn("He/Him", xml)
        self.assertIn("3-ROUND RITUAL SUICIDE CLOCK", xml)
        self.assertIn("BOX CATACLYSM PENALTY", xml)
        self.assertNotIn("she shows", xml.lower())

    def test_29_thusnelda_token_has_ritual_clock_and_audio_macros(self):
        xml = get_token_xml(NAMED_DIR / "Thusnelda.rptok")
        self.assertIn("Ritual Clock (Round 1-3)", xml)
        self.assertIn("Voice: Blood Prophecy", xml)

    def test_30_s4_creatures_have_tactical_ai_notes(self):
        bone_naga_xml = get_token_xml(CREATURES_DIR / "Bone_Naga.rptok")
        self.assertIn("SCLANDERS TACTICAL AI", bone_naga_xml)
        self.assertIn("Three Clue Rule", bone_naga_xml)

        yochlol_xml = get_token_xml(CREATURES_DIR / "Yochlol.rptok")
        self.assertIn("SCLANDERS TACTICAL AI", yochlol_xml)

        shadow_demon_xml = get_token_xml(CREATURES_DIR / "Shadow_Demon.rptok")
        self.assertIn("SCLANDERS TACTICAL AI", shadow_demon_xml)

        skeleton_xml = get_token_xml(CREATURES_DIR / "Skeleton.rptok")
        self.assertIn("BLUDGEONING", skeleton_xml)

    def test_31_janus_threshold_token_and_audio_macro(self):
        janus_xml = get_token_xml(NAMED_DIR / "Janus_(Threshold_Vision).rptok")
        self.assertIn("s5_janus_threshold.mp3", janus_xml)
        self.assertIn("Voice: Threshold of Janus", janus_xml)

    def test_32_wight_general_cameo_token(self):
        wight_gen_xml = get_token_xml(NAMED_DIR / "Wight_General_(Centurion_Cameo).rptok")
        self.assertIn("three hundred years", wight_gen_xml)
        self.assertIn("Voice: Roman Oath Discharged", wight_gen_xml)


if __name__ == "__main__":
    unittest.main()
