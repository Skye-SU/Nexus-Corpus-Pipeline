import sys
import unittest
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / "src"))

from link_documents import build_link_scaffold


class TestBuildLinkScaffold(unittest.TestCase):
    def test_basic_scaffold(self):
        docs = [
            {"doc_id": "test__official__anchor", "packet_id": "TEST", "layer": "official"},
            {"doc_id": "test__news__news_1", "packet_id": "TEST", "layer": "news"},
            {"doc_id": "test__social__social_1", "packet_id": "TEST", "layer": "social"},
        ]
        links = build_link_scaffold(docs)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0]["from_doc_id"], "test__news__news_1")
        self.assertEqual(links[0]["to_doc_id"], "test__official__anchor")
        self.assertEqual(links[0]["relation_type"], "reports_on")
        self.assertEqual(links[1]["relation_type"], "reposts_or_discusses")

    def test_no_anchor_produces_no_links(self):
        docs = [
            {"doc_id": "test__news__news_1", "packet_id": "TEST", "layer": "news"},
        ]
        links = build_link_scaffold(docs)
        self.assertEqual(len(links), 0)

    def test_override_applied(self):
        docs = [
            {"doc_id": "us-01__official__anchor", "packet_id": "US-01", "layer": "official"},
            {"doc_id": "us-01__news__news_1", "packet_id": "US-01", "layer": "news"},
        ]
        links = build_link_scaffold(docs)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["confidence"], "0.95")


if __name__ == "__main__":
    unittest.main()
