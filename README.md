# Sehyeog Kim — personal blog

Technical notes, essays, and leisure stories at https://sehyeogkim.github.io.

Uses the actual [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme pinned to **4.28.1**. The homepage and section pages use the portfolio-style image grid, with the native author sidebar and article typography.

## Write a new post

Create `_posts/YYYY-MM-DD-your-title.md`:

```yaml
---
title: "Your title"
date: YYYY-MM-DD
section: Study
study_area: AI
topic: "Your topic"
excerpt: "A short introduction."
header:
  teaser: /assets/images/your-cover.jpg
---

Your article here.
```

Use `section: Study`, `Essay`, or `Leisure`. Study areas are `AI`, `Mechanical`, or `CS`; omit `study_area` for other sections. The default post layout is `note`. A cover is optional; posts without one use a simple category graphic. `math: true` enables MathJax for other custom page layouts; note pages support mathematics by default.

## Existing articles

Existing articles remain at their original `/blog/.../` URLs, with their original body content. Their YAML front matter adds titles, section metadata, and optional existing teaser images. Directory indexes now show the same image grid. Missing publication dates are left unspecified; dated articles appear newest first, followed by undated articles alphabetically.

## Development

```sh
bundle install
bundle exec jekyll serve
```

GitHub Pages builds the remote theme with `jekyll-include-cache`. Navigation is in `_data/navigation.yml`; profile and site settings are in `_config.yml`. The custom grid and reading layouts live in `_layouts`, and the small CSS and search enhancement are in `assets`. Without JavaScript, all article cards remain visible.

The existing data extraction pipelines are separate from this presentation layer; see their own instructions before running them.

## Migration checks

Run `python3 scripts/verify_site.py _site` after building to check the 230 archived bodies and URLs against their migration manifest. New articles use `_posts`; existing articles can be edited in their original `blog/.../index.html` files. When intentionally rewriting an archived article, update its manifest hash to match the approved content change.
