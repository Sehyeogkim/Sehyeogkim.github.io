---
name: github-data-poster
description: Historical blog_data import reference. The current site is authored and built with Jekyll; do not run the legacy static generator.
---

# GitHub Data Poster Skill

## Current Jekyll workflow (supersedes the historical instructions below)

- Read the root `README.md` for the current front matter and preview instructions.
- Add new posts under `_posts/`; build with `bundle exec jekyll build` and preview with `bundle exec jekyll serve`.
- Preserve the migrated `blog/**/index.html` Jekyll source, existing permalinks, article bodies, and image paths.
- Do not delete/reset `blog/` or regenerate it from `blog_data/`. The legacy `scripts/build_site.py` exits 2 when `_config.yml` exists, including with `--clean`.
- The source metadata and image parsing rules below are retained for reference only. A future import must create or update Jekyll sources without overwriting existing pages; do not restart extraction or publishing unless requested.

## Historical reference — not an executable workflow

## When To Use

- `blog_data/`를 기준으로 GitHub Pages 게시용 `blog/`를 다시 만들 때
- 카테고리 클릭 -> 포스트 리스트 -> 포스트 상세 구조를 보장해야 할 때
- 과거 변환 규칙을 참고할 때 (기존 `blog/` 삭제 금지)

## Inputs

- Source root: `/Users/jeff/blog/Sehyeogkim.github.io/blog_data`
- Target root: `/Users/jeff/blog/Sehyeogkim.github.io/blog`
- Category directories under source
- Per-post `content.txt` and `images/`

## Output

- Rebuilt `blog/` static structure with:
  - Home page
  - Category list/navigation
  - Category post-list pages
  - Post detail pages rendered from `content.txt`
  - Copied image assets used by posts

## Workflow

1. Pre-check
- Confirm source root exists.
- Enumerate categories and posts.
- Validate each post has `content.txt`.

2. Preserve target
- Keep existing Jekyll sources, article URLs, and images under `blog/`.
- Do not reset or recreate the published source tree.

3. Build site map
- Create category metadata from directory names.
- Extract post title/date from metadata header in `content.txt`.
- Sort posts deterministically (date desc, then slug asc if date missing).

4. Render pages
- Home: project intro + category cards/links.
- Category page: post list with links.
- Post page:
  - Render metadata section.
  - Render body blocks in original order.
  - Replace `[IMAGE: images/<file>]` with image references.

5. Copy assets
- Copy per-post `images/*` into published post asset directory.
- Keep filenames stable (`img-001.*`, etc).

6. Validate
- Every category link resolves.
- Every post link resolves.
- Every image marker maps to an existing copied file.

7. Report
- categories processed
- posts processed
- skipped (if resume mode)
- failed items with reason

## Parsing Rules

- `content.txt` header keys to read:
  - `Title:`
  - `URL:`
  - `PageID:` or `PostID:`
  - `Date:`
  - `Category:`
- Body starts after the metadata header block.
- Preserve line order from body exactly.

## Safety

- Never run bulk publish until user explicitly asks.
- Never write credentials to disk or commit history.
- Never delete outside `blog/`.

## Resume Strategy

- Current mode: Jekyll build into `_site/`; preserve all source files under `blog/`.
- Optional mode: resume publish by skipping posts whose output and assets already exist.
- Only use resume mode when user explicitly asks.
