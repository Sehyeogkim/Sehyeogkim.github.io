#!/usr/bin/env python3
"""Verify that the theme migration has not changed archived article bodies or URLs.

Run: python3 scripts/verify_site.py [path/to/built/site]
The manifest records SHA-256 hashes of the original, pre-theme article HTML.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / '_data/migration.json').read_text(encoding='utf-8'))
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
errors = []
for post in manifest['posts']:
    path = ROOT / post['path']
    if not path.is_file():
        errors.append(f"Missing archived article: {post['path']}")
        continue
    source = path.read_text(encoding='utf-8')
    body = re.search(r'{% raw %}(.*){% endraw %}', source, re.S)
    if not body or hashlib.sha256(body.group(1).encode()).hexdigest() != post['body_sha256']:
        errors.append(f"Archived body changed: {post['path']}")
    try:
        # Migrated front matter is JSON, which is also valid YAML.
        metadata = json.loads(source.split('---', 2)[1])
        if metadata.get('permalink') != post['url']:
            errors.append(f"Archived URL changed: {post['path']}")
    except (IndexError, ValueError):
        errors.append(f"Cannot read migrated metadata: {post['path']}")
    if output:
        built = output / post['path']
        if not built.is_file():
            errors.append(f"Not generated: {post['url']}")
        elif body and body.group(1) not in built.read_text(encoding='utf-8'):
            errors.append(f"Archived body missing from generated page: {post['url']}")

for url in manifest['archive_urls']:
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
print('Archived bodies and URLs are preserved.' + (' Generated pages verified.' if output else ''))
