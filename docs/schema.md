# Schema Notes

Last updated: 2026-04-11

## Manifest

Current working manifest file:

- `manifests/source_manifest.csv`

Minimum working fields:

- `packet_id`
- `packet_name`
- `jurisdiction`
- `theme`
- `core_or_adjacent`
- `layer`
- `source_role`
- `source_type`
- `title_or_label`
- `publisher_org`
- `url`
- `pub_date`
- `language`
- `collection_status`
- `retrieval_method`
- `why_selected`
- `notes`

Working `collection_status` vocabulary in the MVP:

- `reserve`: tracked but not included in the active build
- `shortlist`: actively retained anchor or packet row
- `candidate`: active row not yet fully captured
- `collected`: active row with working text captured locally

## Planned Output Tables

### documents.csv

- `doc_id`
- `packet_id`
- `layer`
- `jurisdiction`
- `theme`
- `source_type`
- `source_name`
- `title`
- `url`
- `author_org`
- `pub_date`
- `language`
- `retrieved_at`
- `text_raw`
- `text_clean`

### links.csv

- `link_id`
- `from_doc_id`
- `to_doc_id`
- `relation_type`
- `evidence`
- `confidence`
- `notes`

Allowed relation types in the MVP:

- `reports_on`
- `references`
- `reposts_or_discusses`

## Processing Notes

### `text_clean` derivation

The `text_clean` field is derived from `text_raw` via `normalize_text()` in `src/normalize.py`:

1. HTML entity decoding (`html.unescape()`)
2. Markdown link syntax removal (`[text](url)` → `text`)
3. Whitespace collapsing and trimming
4. Lowercasing

### `text_raw` extraction

Raw text is extracted from files in `data/raw/` via `read_raw_text()` in `src/extract.py`:

- For `.md` files with a `## Raw Text` marker: text after the marker is used
- For `.md` files without the marker: the entire file content is used
- For `.html` files: HTML tags are stripped to plain text
- `TBD` placeholders are removed
