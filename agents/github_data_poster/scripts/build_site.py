#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SOURCE_ROOT = REPO_ROOT / "blog_data"
TARGET_ROOT = REPO_ROOT / "blog"
DATA_ROOT = REPO_ROOT / "_data"
MAP_FILE = DATA_ROOT / "knowledge_map.yml"
INDEX_FILE = REPO_ROOT / "index.md"

HEADER_KEYS = {"Title", "URL", "PageID", "PostID", "Date", "Category"}
IMAGE_MARKER_RE = re.compile(r"^\[IMAGE:\s*images/([^\]]+)\]\s*$")
LIQUID_URL_RE = re.compile(r"\{\{\s*(https?://[^}\s]+)\s*\}\}")


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def parse_content(path: Path) -> tuple[dict[str, str], list[str]]:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    meta: dict[str, str] = {}
    body_start = 0

    for i, line in enumerate(lines):
        if not line.strip() and meta:
            body_start = i + 1
            break
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*):\s*(.*)$", line)
        if not m:
            break
        key, value = m.group(1), m.group(2)
        if key not in HEADER_KEYS:
            break
        meta[key] = value.strip()
        body_start = i + 1

    body_lines = lines[body_start:]
    return meta, body_lines


def render_body(body_lines: list[str], title: str) -> list[str]:
    rendered: list[str] = []
    for line in body_lines:
        m = IMAGE_MARKER_RE.match(line.strip())
        if m:
            image_name = m.group(1).strip()
            rendered.append(f"![{title}](./images/{image_name})")
        else:
            # Notion-origin text may include {{https://...}} which Jekyll treats as Liquid.
            normalized = LIQUID_URL_RE.sub(r"<\1>", line)
            # Escape any leftover Liquid delimiters so content renders as plain text.
            normalized = normalized.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")
            rendered.append(normalized)
    return rendered


def copy_images(src_images: Path, dst_images: Path) -> int:
    dst_images.mkdir(parents=True, exist_ok=True)
    count = 0
    if src_images.exists():
        for f in sorted(src_images.iterdir()):
            if f.is_file():
                shutil.copy2(f, dst_images / f.name)
                count += 1
    return count


def front_matter(title: str, extra: dict[str, str]) -> str:
    safe_title = title.replace("\"", "\\\"")
    lines = ["---", f'title: "{safe_title}"', "layout: knowledge-home"]
    for key, value in extra.items():
        safe = value.replace('"', '\\"')
        lines.append(f'{key}: "{safe}"')
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def write_home(categories: list[dict[str, str]]) -> None:
    lines = [
        "---",
        "layout: knowledge-home",
        "title: Home",
        "---",
        "",
        "## Knowledge Base",
        "This site is generated from local `blog_data` sources.",
        "",
        "### Categories",
    ]
    if categories:
        for c in categories:
            lines.append(f"- [{c['name']}]({c['url']}) ({c['post_count']} posts)")
    else:
        lines.append("- No categories found")
    lines.append("")
    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")


def write_knowledge_map(categories: list[dict[str, str]]) -> None:
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "generated_at: '{}'".format(dt.datetime.now(dt.timezone.utc).isoformat()),
        "categories:",
    ]
    if not categories:
        lines.append("  - name: No Category")
        lines.append("    slug: no-category")
        lines.append("    url: /")
        lines.append("    post_count: 0")
    else:
        for c in categories:
            safe_name = c["name"].replace("'", "''")
            lines.append(f"  - name: '{safe_name}'")
            lines.append(f"    slug: '{c['slug']}'")
            lines.append(f"    url: '{c['url']}'")
            lines.append(f"    post_count: {c['post_count']}")
    MAP_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not SOURCE_ROOT.exists():
        print(f"ERROR: source root not found: {SOURCE_ROOT}")
        return 1

    # Full rebuild as requested: remove current blog data before publishing.
    if TARGET_ROOT.exists():
        shutil.rmtree(TARGET_ROOT)
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)

    categories = []
    processed_posts = 0
    failed_posts: list[str] = []

    for category_dir in sorted([p for p in SOURCE_ROOT.iterdir() if p.is_dir()]):
        category_name = category_dir.name
        category_slug = slugify(category_name)
        out_category_dir = TARGET_ROOT / category_slug
        out_category_dir.mkdir(parents=True, exist_ok=True)

        post_items = []
        post_dirs = sorted([p for p in category_dir.iterdir() if p.is_dir()])

        for post_dir in post_dirs:
            content_file = post_dir / "content.txt"
            if not content_file.exists():
                failed_posts.append(f"{category_name}/{post_dir.name} (missing content.txt)")
                continue

            try:
                meta, body_lines = parse_content(content_file)
                post_title = meta.get("Title") or post_dir.name
                post_slug = slugify(post_dir.name)
                post_out_dir = out_category_dir / post_slug
                post_out_dir.mkdir(parents=True, exist_ok=True)

                rendered_body = render_body(body_lines, post_title)

                src_url = meta.get("URL", "")
                src_id = meta.get("PageID") or meta.get("PostID", "")
                date = meta.get("Date", "")

                fm = front_matter(
                    post_title,
                    {
                        "source_url": src_url,
                        "source_id": src_id,
                        "date": date,
                        "category": category_name,
                    },
                )
                page_lines = [fm]
                if src_url:
                    page_lines.append(f"Source: [{src_url}]({src_url})")
                    page_lines.append("")
                page_lines.extend(rendered_body)
                (post_out_dir / "index.md").write_text("\n".join(page_lines).rstrip() + "\n", encoding="utf-8")

                image_count = copy_images(post_dir / "images", post_out_dir / "images")
                post_items.append(
                    {
                        "title": post_title,
                        "slug": post_slug,
                        "url": f"/blog/{category_slug}/{post_slug}/",
                        "date": date,
                        "images": image_count,
                    }
                )
                processed_posts += 1
            except Exception as exc:
                failed_posts.append(f"{category_name}/{post_dir.name} ({exc})")

        post_items.sort(key=lambda x: ((x["date"] or ""), x["slug"]), reverse=True)

        category_front = front_matter(category_name, {"category": category_name})
        lines = [category_front, "## Posts", ""]
        if post_items:
            for post in post_items:
                lines.append(f"- [{post['title']}]({post['url']})")
        else:
            lines.append("- No posts yet")
        lines.append("")
        (out_category_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

        categories.append(
            {
                "name": category_name,
                "slug": category_slug,
                "url": f"/blog/{category_slug}/",
                "post_count": len(post_items),
            }
        )

    categories.sort(key=lambda c: c["name"].lower())
    write_home(categories)
    write_knowledge_map(categories)

    print(f"categories processed: {len(categories)}")
    print(f"posts processed: {processed_posts}")
    print(f"posts failed: {len(failed_posts)}")
    if failed_posts:
        print("failed items:")
        for item in failed_posts:
            print(f"- {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
