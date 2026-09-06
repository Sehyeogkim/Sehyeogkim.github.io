# Personal Blog — Sehyeog Kim

Technical notes, essays, and leisure stories at https://sehyeogkim.github.io.

Uses [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), pinned to **7.6.0**, with its sidebar, article cards, search, and reading layout. The sidebar includes GitHub, LinkedIn, X, and Instagram.

## Write a new post

Create `_posts/YYYY-MM-DD-your-title.md`:

```yaml
---
layout: post
title: "Your title"
date: 2026-09-06 12:00:00 +0900
categories: [Study, AI]
section: Study
study_area: AI
topic: "Machine Learning"
tags: [machine-learning]
description: "A short introduction."
image:
  path: /assets/images/your-cover.jpg
  alt: "A description of the cover image"
math: true
---

Your article here.
```

Use `categories: [Study, AI]`, `[Study, Mechanical]`, or `[Study, CS]` for study notes. Use `[Essay]` or `[Leisure]` for other writing. Categories are ordered from the broad section to the study area. A cover image is optional. Set `math: true` when the article needs mathematical notation.

The Study explorer groups notes by `study_area` and `topic`. Match `topic` to an entry in `_data/study_topics.yml`; add a topic entry and its archive page when introducing a new topic. Set `section: Essay` or `section: Leisure` for non-study posts and omit `study_area` and `topic` there. The explorer appears on Study lists, topic pages, and Study articles; folder state is saved in the browser. Essay and Leisure have their own explorers, grouped by year. Click an explorer heading to collapse or expand it; each section remembers its own state. The home page has no right-hand discovery panel.

## Existing articles

The 230 archived HTML articles live under `_posts/`, named `YYYY-MM-DD-slug-hash.html`. Their explicit `permalink` values preserve the original `/blog/.../` URLs. Their original HTML bodies and image paths remain unchanged. Topic archive URLs also remain available.

Find an archived article by its title or `permalink` in `_posts/`; edit that source file, not generated HTML in `_site/`. Imported front matter may contain compatibility metadata in addition to the native Chirpy fields. Retain it unless a migration explicitly replaces it. Do not interpret a filename date assigned during migration as verified evidence of the original publication date.

## Development and deployment

Use Ruby **3.4** with Bundler:

```sh
bundle install
bundle exec jekyll serve
```

For a production build and preservation check:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/verify_site.py _site
```

GitHub Actions builds and deploys the site to GitHub Pages. Keep the Pages source set to **GitHub Actions**. The theme is installed through the Gemfile; the old GitHub Pages remote-theme build is no longer the deployment path.

Site identity and theme settings are in `_config.yml`. Sidebar social links are configured in `_data/contact.yml`; section pages live under `_tabs/`. Theme overrides in `_layouts`, `_includes`, and `assets` should remain as small as possible.

The existing data extraction pipelines are separate from this presentation layer; see their own instructions before running them. Never run the legacy static site generator over the Jekyll source tree.

## Migration checks

`python3 scripts/verify_site.py _site` checks the archived article bodies and preserved URLs against `_data/migration.json`, plus the generated navigation and topic archive pages. Run it after a build whenever moving archived sources or changing layouts. New writing does not need to be added to the migration manifest. When intentionally rewriting an archived article, update its manifest hash only for the approved content change.
