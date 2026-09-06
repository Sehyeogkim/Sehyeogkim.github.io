#!/usr/bin/env python3
"""Verify original article bytes, permalinks, and rendered content after migration.

Run: python3 scripts/verify_site.py [path/to/built/site]
Source bodies must remain byte-identical. Theme-generated markup may change, so
built pages are checked for ordered source text and original image references.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / '_data/migration.json').read_text(encoding='utf-8'))
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
errors = []
routes = {}

class Content(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.words = []
        self.images = []
        self.hidden = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'img':
            attrs = dict(attrs)
            if attrs.get('src'):
                self.images.append(attrs['src'])
    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.hidden:
            self.hidden -= 1
    def handle_data(self, data):
        if not self.hidden:
            self.words.extend(data.split())

def ordered_in(expected, actual):
    actual = iter(actual)
    return all(any(word == value for value in actual) for word in expected)

def image_key(src, page_url):
    url = urlsplit(urljoin('https://sehyeogkim.github.io' + page_url, src))
    return (url.netloc.lower(), unquote(url.path), url.query)

for post in manifest['posts']:
    path = ROOT / post['path']
    if not path.is_file():
        errors.append(f"Missing archived article: {post['path']}")
        continue
    source = path.read_bytes()
    body = re.search(rb'{% raw %}(.*){% endraw %}', source, re.S)
    if not body or hashlib.sha256(body.group(1)).hexdigest() != post['body_sha256']:
        errors.append(f"Archived body changed: {post['path']}")
    try:
        # Migrated front matter is JSON, which is also valid YAML.
        metadata = json.loads(source.split(b'---', 2)[1])
        if metadata.get('permalink') != post['url']:
            errors.append(f"Archived URL changed: {post['path']}")
        if metadata.get('date') != post['date']:
            errors.append(f"Archived date changed: {post['path']}")
        if metadata.get('layout') != 'post' or not post['path'].startswith('_posts/'):
            errors.append(f"Not a native post: {post['path']}")
        route = metadata.get('permalink')
        if route in routes:
            errors.append(f"Duplicate article URL: {route}")
        routes[route] = post['path']
    except (IndexError, ValueError):
        errors.append(f"Cannot read migrated metadata: {post['path']}")
    old_path = post.get('original_path')
    if old_path and (ROOT / old_path).exists():
        errors.append(f"Duplicate legacy article route: {old_path}")
    if output:
        built = output / post['url'].lstrip('/') / 'index.html'
        if not built.is_file():
            errors.append(f"Not generated: {post['url']}")
        elif body:
            original_content = Content()
            original_content.feed(body.group(1).decode('utf-8'))
            rendered_content = Content()
            rendered_content.feed(built.read_text(encoding='utf-8'))
            if not ordered_in(original_content.words, rendered_content.words):
                errors.append(f"Original text missing or reordered: {post['url']}")
            built_images = {image_key(src, post['url']) for src in rendered_content.images}
            for src in original_content.images:
                if image_key(src, post['url']) not in built_images:
                    errors.append(f"Original image reference missing: {post['url']} -> {src}")

for url in manifest['archive_urls']:
    if url in routes:
        errors.append(f'Duplicate topic/article URL: {url}')
    if not (ROOT / url.lstrip('/') / 'index.html').is_file():
        errors.append(f'Missing original topic page: {url}')
if output:
    for url in ['/', '/study/', '/study/ai/', '/study/mechanical/', '/study/cs/', '/essay/', '/leisure/', '/about/'] + manifest['archive_urls']:
        if not (output / url.lstrip('/') / 'index.html').is_file():
            errors.append(f'Missing generated navigation page: {url}')

print(f"Checked {len(manifest['posts'])} archived articles and {len(manifest['archive_urls'])} topic pages.")
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Archived body bytes, dates, and URLs are preserved; no duplicate article routes.'
      + (' Rendered text and image references verified.' if output else ''))
