from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path
import html

MANIFEST_FIELDS = [
    "packet_id",
    "packet_name",
    "jurisdiction",
    "theme",
    "core_or_adjacent",
    "layer",
    "source_role",
    "source_type",
    "title_or_label",
    "publisher_org",
    "url",
    "pub_date",
    "language",
    "collection_status",
    "retrieval_method",
    "why_selected",
    "notes",
]

DOCUMENT_FIELDS = [
    "doc_id",
    "packet_id",
    "layer",
    "jurisdiction",
    "theme",
    "source_type",
    "source_name",
    "title",
    "url",
    "author_org",
    "pub_date",
    "language",
    "retrieved_at",
    "text_raw",
    "text_clean",
]

ACTIVE_STATUSES = {"shortlist", "candidate", "collected"}


def _clean_value(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def normalize_manifest_row(row: dict[str, str]) -> dict[str, str]:
    normalized = {}
    for field in MANIFEST_FIELDS:
        normalized[field] = _clean_value(row.get(field, ""))
    return normalized


def load_manifest(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return [normalize_manifest_row(row) for row in csv.DictReader(handle)]


def active_manifest_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if row["collection_status"] in ACTIVE_STATUSES]


def make_doc_id(row: dict[str, str]) -> str:
    parts = [row["packet_id"], row["layer"], row["source_role"]]
    slug = "__".join(parts).lower()
    return re.sub(r"[^a-z0-9_]+", "-", slug)


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

def clean_raw_spacing(text: str) -> str:
    # Only remove carriage returns, keep basic structure but no excessive blank lines
    text = text.replace('\r', '')
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def manifest_to_documents(
    rows: list[dict[str, str]], retrieved_at: str | None = None
) -> list[dict[str, str]]:
    timestamp = retrieved_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    documents = []
    for row in rows:
        documents.append(
            {
                "doc_id": make_doc_id(row),
                "packet_id": row["packet_id"],
                "layer": row["layer"],
                "jurisdiction": row["jurisdiction"],
                "theme": row["theme"],
                "source_type": row["source_type"],
                "source_name": row["publisher_org"],
                "title": row["title_or_label"],
                "url": row["url"],
                "author_org": row["publisher_org"],
                "pub_date": row["pub_date"],
                "language": row["language"],
                "retrieved_at": timestamp,
                "text_raw": "",
                "text_clean": "",
            }
        )
    return documents


def write_csv(path: str | Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
