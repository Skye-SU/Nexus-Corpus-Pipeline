# Source Helpers

This directory contains the core reusable helpers for processing the research text dataset.

Available modules:

- `extract.py`: Handles raw text extraction from source files.
- `normalize.py`: Implements text normalization and clean text generation logic.
- `link_documents.py`: Establishes relation links across layers based on packet membership and manual overrides.
- `bootstrap_raw_placeholders.py`: A utility to generate markdown placeholders in `data/raw` from the source manifest.

Rules:
- Keep everything simple and notebook-first.
- Do not turn this into a large framework.
