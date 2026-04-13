import sys
import unittest
from pathlib import Path

# Provide tests access to src module
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / "src"))

from normalize import normalize_text, clean_raw_spacing, make_doc_id

class TestNormalize(unittest.TestCase):
    def test_normalize_text(self):
        raw = "   This is \n\n a TEST.  \n   "
        clean = normalize_text(raw)
        self.assertEqual(clean, "this is a test.")

    def test_clean_raw_spacing(self):
        raw = "Line 1\r\n\r\n\r\nLine 2\n\nLine 3"
        cleaned = clean_raw_spacing(raw)
        self.assertEqual(cleaned, "Line 1\n\nLine 2\n\nLine 3")

    def test_make_doc_id(self):
        row = {
            "packet_id": "US-01",
            "layer": "news",
            "source_role": "news_1"
        }
        doc_id = make_doc_id(row)
        self.assertEqual(doc_id, "us-01__news__news_1")

    def test_make_doc_id_with_special_chars(self):
        row = {
            "packet_id": "US-02!",
            "layer": "social",
            "source_role": "social@2"
        }
        doc_id = make_doc_id(row)
        self.assertEqual(doc_id, "us-02-__social__social-2")

if __name__ == '__main__':
    unittest.main()
