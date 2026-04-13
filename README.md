# GenAI Copyright Text Infrastructure

A notebook-first research text infrastructure for cross-jurisdictional analysis of generative AI copyright law.

This repository organizes scattered primary sources, news coverage, and social discourse into reusable, linked data packets covering:

- Generative AI copyright and authorship doctrine
- Originality requirements for AI-generated and AI-assisted works
- AI-related copyright regulation and public discourse

## Purpose

Researchers studying AI copyright often recollect official texts, media reports, and public commentary from scratch for each project. This repository provides a reproducible pipeline that keeps these materials linked in a consistent packet structure, supporting:

- Data collection and cleaning demonstrations
- Cross-layer text comparison and similarity analysis
- Semantic analysis of discourse transformation across layers
- Reusable notebook examples from a documented source base

## Repository Contents

- `manifests/source_manifest.csv` — Source packet registry
- `data/processed/documents.csv` — Normalized document table
- `data/processed/links.csv` — Cross-layer links
- `notebooks/01_build_dataset.ipynb` — Dataset build notebook
- `notebooks/02_compare_layers.ipynb` — Layer comparison notebook
- `docs/overview.md` — Project overview
- `docs/schema.md` — Schema documentation

### Current Scope

| Dimension | Value |
|-----------|-------|
| Jurisdictions | United States, China |
| Packets | US-01, US-02, US-03, CN-02, CN-04 |
| Documents | 29 |
| Cross-layer links | 24 |

## How to Review

1. Start with [`docs/overview.md`](docs/overview.md)
2. Open [`notebooks/02_compare_layers.ipynb`](notebooks/02_compare_layers.ipynb)
3. Browse the repository for implementation details as needed

No installation is required for a document-level review on GitHub.

## Scope Limitations

This is not a chatbot, frontend application, or broad AI governance platform. The value lies in the packet structure, source provenance, and reproducible data pipeline.

## Reproducibility

```bash
pip install -r requirements.txt
make build    # builds documents.csv and links.csv, executes notebooks
make test     # runs the test suite
```

## Documentation

- [`docs/overview.md`](docs/overview.md) — Project overview and analytical observations
- [`docs/schema.md`](docs/schema.md) — Manifest and output table schemas
