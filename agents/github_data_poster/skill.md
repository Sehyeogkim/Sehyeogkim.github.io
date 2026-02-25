---
name: github-data-poster
description: Publish local `blog_data` into GitHub Pages-ready `blog` by rebuilding category navigation (Home -> Category -> Post), rendering content.txt with inline image markers, and copying mapped images.
---

# GitHub Data Poster Skill

## When To Use

- `blog_data/`를 기준으로 GitHub Pages 게시용 `blog/`를 다시 만들 때
- 카테고리 클릭 -> 포스트 리스트 -> 포스트 상세 구조를 보장해야 할 때
- 기존 `blog/` 데이터를 비우고 새 데이터로 재배포할 때

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

2. Reset target
- Remove existing contents under `blog/`.
- Recreate target skeleton directories.
- Keep operation scoped to `blog/` only.

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

- Default mode: full rebuild (clean `blog/` then republish all).
- Optional mode: resume publish by skipping posts whose output and assets already exist.
- Only use resume mode when user explicitly asks.
