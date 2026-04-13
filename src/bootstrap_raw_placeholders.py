from __future__ import annotations

from pathlib import Path

from normalize import active_manifest_rows, load_manifest, make_doc_id


def build_placeholder_text(row: dict[str, str], doc_id: str) -> str:
    header = [
        f"# {row['title_or_label']}",
        "",
        f"- `doc_id`: {doc_id}",
        f"- `packet_id`: {row['packet_id']}",
        f"- `layer`: {row['layer']}",
        f"- `source_role`: {row['source_role']}",
        f"- `source_type`: {row['source_type']}",
        f"- `publisher_org`: {row['publisher_org']}",
        f"- `url`: {row['url']}",
        f"- `pub_date`: {row['pub_date']}",
        f"- `language`: {row['language']}",
        "",
        "## Notes",
        "",
        row["notes"] or "TBD",
        "",
        "## Raw Text",
        "",
        "TBD",
        "",
    ]
    return "\n".join(header)


def create_placeholders(repo_root: str | Path) -> list[Path]:
    repo_root = Path(repo_root)
    manifest_path = repo_root / "manifests" / "source_manifest.csv"
    raw_root = repo_root / "data" / "raw"

    created: list[Path] = []
    rows = active_manifest_rows(load_manifest(manifest_path))
    for row in rows:
        doc_id = make_doc_id(row)
        path = raw_root / row["layer"] / f"{doc_id}.md"
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(build_placeholder_text(row, doc_id), encoding="utf-8")
        created.append(path)
    return created


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    created = create_placeholders(repo_root)
    print(f"created {len(created)} placeholder files")
    for path in created[:10]:
        print(path)
