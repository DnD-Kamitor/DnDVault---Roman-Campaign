#!/usr/bin/env python3
"""
Unit tests for scripts/generate_voice_clips.py
"""

import json
import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.generate_voice_clips import generate_clip


class TestVoiceGenerator(unittest.TestCase):
    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "test.mp3")
            ok = generate_clip(
                endpoint="http://example.com/api",
                model="tts-1",
                voice="onyx",
                text="Test text",
                output_path=out_file,
                dry_run=True
            )
            self.assertTrue(ok)
            self.assertFalse(os.path.exists(out_file))

    @patch("urllib.request.urlopen")
    def test_successful_generation(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b"fake-audio-bytes-12345"
        mock_urlopen.return_value.__enter__.return_value = mock_resp

        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "test.mp3")
            ok = generate_clip(
                endpoint="http://localhost:8001/v1/audio/speech",
                model="tts-1",
                voice="onyx",
                text="Salve!",
                output_path=out_file,
                dry_run=False
            )
            self.assertTrue(ok)
            self.assertTrue(os.path.exists(out_file))
            with open(out_file, "rb") as f:
                content = f.read()
            self.assertEqual(content, b"fake-audio-bytes-12345")


if __name__ == "__main__":
    unittest.main()
