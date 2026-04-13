import sys
import unittest
from pathlib import Path
import tempfile

repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / "src"))

from extract import read_raw_text


class TestReadRawText(unittest.TestCase):
    def _write_temp(self, suffix, content):
        f = tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False, encoding="utf-8")
        f.write(content)
        f.close()
        return Path(f.name)

    def test_md_with_raw_text_marker(self):
        path = self._write_temp(".md", "# Title\n\n## Notes\n\nSome note.\n\n## Raw Text\n\nActual content here.\n")
        result = read_raw_text(path)
        self.assertIn("Actual content here.", result)
        self.assertNotIn("# Title", result)
        self.assertNotIn("Some note", result)

    def test_md_without_raw_text_marker(self):
        path = self._write_temp(".md", "Plain markdown content without marker.\n")
        result = read_raw_text(path)
        self.assertEqual(result, "Plain markdown content without marker.")

    def test_md_with_tbd_placeholder(self):
        path = self._write_temp(".md", "# Title\n\n## Raw Text\n\nTBD\n")
        result = read_raw_text(path)
        self.assertEqual(result.strip(), "")

    def test_html_extraction(self):
        path = self._write_temp(".html", "<html><body><p>Hello world</p><nav>Skip</nav></body></html>")
        result = read_raw_text(path)
        self.assertIn("Hello world", result)


if __name__ == "__main__":
    unittest.main()
