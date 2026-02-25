---
name: tistory-post-exporter
description: "Export Tistory posts into static-friendly files for publishing workflows. Use when the user asks to extract one or many Tistory posts and save each post as its own directory with content.txt, downloaded images/, and inline image markers like [IMAGE: images/img-001.png]."
---

# Tistory Post Exporter

## Overview

Extract Tistory post text and images into a deterministic directory layout. Keep article order and insert image location markers directly in `content.txt` so downstream static publishing (for example GitHub Pages) is easy.

## Output Contract

- One post per directory:
  - `post-{id}-{slug}/content.txt`
  - `post-{id}-{slug}/images/img-001.<ext>`, `img-002.<ext>`, ...
- `content.txt` must include metadata header:
  - `Title: ...`
  - `URL: ...`
  - `PostID: ...`
  - `Date: ...`
- Image positions must be inline:
  - `[IMAGE: images/img-00X.ext]`

## Script

Use:
- `scripts/export_tistory_posts.py`

### Single Post

```bash
python3 skills/tistory-post-exporter/scripts/export_tistory_posts.py \
  --post-url https://jeffdissel.tistory.com/245 \
  --out-root ./export \
  --resume
```

### All Posts From One Blog

```bash
python3 skills/tistory-post-exporter/scripts/export_tistory_posts.py \
  --blog-url https://jeffdissel.tistory.com \
  --all-posts \
  --out-root ./export \
  --resume
```

Optional flags:
- `--limit N`: export only first N discovered posts
- `--overwrite`: overwrite existing post output
- `--report-file ./export/report.json`: save structured summary

## Workflow

1. Confirm scope
- Export one URL or all posts.
- Confirm output root path.

2. Run exporter script
- Prefer `--resume` for long jobs and reruns.
- Use `--overwrite` only when user requests re-extraction.

3. Validate result quickly
- Check each exported post has `content.txt` and `images/`.
- Verify image markers exist and point to files under the same post folder.

4. Report to user
- Number of processed/skipped/failed posts.
- Failed URLs with error reasons.

## Notes

- This skill does not store credentials in files.
- For login-only posts, use a browser-authenticated workflow separately, then extend the script if needed.
