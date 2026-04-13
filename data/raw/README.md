# Raw Text Conventions

Store local raw text files by layer:

- `official/`
- `news/`
- `social/`

Use the generated `doc_id` as the filename stem.

Examples:

- `us-03__official__anchor.md`
- `us-03__news__news_1.md`
- `cn-04__social__social_2.md`

Allowed extensions right now:

- `.txt`
- `.md`
- `.html`

The current helper loader will:

- match files by `doc_id`
- read plain text or markdown directly
- strip HTML to text in a lightweight way

The pipeline currently uses `.md` for all raw files.
