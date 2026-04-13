from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

from normalize import normalize_text, clean_raw_spacing

RAW_EXTENSIONS = (".txt", ".md", ".html")


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data)

    def get_text(self) -> str:
        return " ".join(self.parts)


def find_raw_text_path(raw_root: str | Path, layer: str, doc_id: str) -> Path | None:
    raw_root = Path(raw_root)
    for ext in RAW_EXTENSIONS:
        candidate = raw_root / layer / f"{doc_id}{ext}"
        if candidate.exists():
            return candidate
    return None


def read_raw_text(path: str | Path) -> str:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".html":
        parser = _HTMLTextExtractor()
        parser.feed(text)
        return clean_raw_spacing(parser.get_text())
    if path.suffix.lower() == ".md":
        marker = "## Raw Text"
        if marker in text:
            _, _, tail = text.partition(marker)
            return clean_raw_spacing(tail.replace("TBD", "", 1))
    return clean_raw_spacing(text)


def attach_raw_text(
    documents: list[dict[str, str]], raw_root: str | Path
) -> list[dict[str, str]]:
    attached = []
    for document in documents:
        updated = dict(document)
        raw_path = find_raw_text_path(raw_root, updated["layer"], updated["doc_id"])
        if raw_path is not None:
            text = read_raw_text(raw_path)
            updated["text_raw"] = text
            updated["text_clean"] = normalize_text(text)
        attached.append(updated)
    return attached
