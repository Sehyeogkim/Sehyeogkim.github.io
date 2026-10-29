"""Normalize the newer Notion fetch format (HTML-ish tags, blank-line separated blocks)
into the older Notion-markdown format that notion2post.py reads.

usage: notion_html2md.py <in.md> <out.md>
"""
import re, sys

src = open(sys.argv[1]).read()


def inline(s):
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s)
    s = re.sub(r'<s>(.*?)</s>', r'~~\1~~', s)
    return s.replace('<br />', '<br>')


lines = src.split('\n')
out, i = [], 0
in_code = False
container = []          # stack of 'callout' / 'quote' we are inside
while i < len(lines):
    l = lines[i]
    s = l.strip()
    if l.startswith('```'):
        in_code = not in_code
        out.append(('\t' if container else '') + l)
        i += 1
        continue
    if in_code:
        out.append(('\t' if container else '') + l)
        i += 1
        continue
    if not s:
        i += 1
        continue
    pre = '\t' if container else ''
    if s == '<p />':
        if not container:
            out.append('<empty-block/>')
        i += 1
        continue
    if s == '<p>':                      # <p>\ntext\n</p> -> one line
        j = lines.index('</p>', i)
        txt = ' '.join(x.strip() for x in lines[i + 1:j] if x.strip())
        out.append(pre + inline(txt))
        i = j + 1
        continue
    if s.startswith('<callout'):
        out.append(s)
        container.append('callout')
        i += 1
        continue
    if s == '</callout>':
        container.pop()
        out.append('</callout>')
        i += 1
        continue
    if s == '<quote>':
        out.append('>')
        container.append('quote')
        i += 1
        continue
    if s == '</quote>':
        container.pop()
        i += 1
        continue
    if s in ('<ol>', '<ul>'):
        kind = s
        n = 1
        j = i + 1
        while lines[j].strip() != kind.replace('<', '</'):
            if lines[j].strip() == '<li>':
                k = lines.index('</li>', j)
                txt = ' '.join(x.strip() for x in lines[j + 1:k] if x.strip())
                out.append(pre + (f'{n}. ' if kind == '<ol>' else '- ') + inline(txt))
                n += 1
                j = k + 1
            else:
                j += 1
        i = j + 1
        continue
    if s.startswith('|') and s.endswith('|'):
        # Markdown pipe table (rows come blank-line separated) -> <table> block notion2post understands
        rows, j = [], i
        while j < len(lines) and (not lines[j].strip() or (lines[j].strip().startswith('|') and lines[j].strip().endswith('|'))):
            r = lines[j].strip()
            if r and not re.fullmatch(r'\|(\s*:?-+:?\s*\|)+', r):
                rows.append('<tr>' + ''.join('<td>' + inline(c.strip()) + '</td>' for c in r[1:-1].split('|')) + '</tr>')
            j += 1
        out.extend([pre + '<table>'] + [pre + r for r in rows] + [pre + '</table>'])
        i = j
        continue
    if s == '<table-of-contents />':
        out.append('<table_of_contents/>')
        i += 1
        continue
    m = re.match(r'<video source="(https?://[^"]+)"\s*/>', s)
    if m:   # external video -> inline HTML5 player
        out.append(pre + f'<video src="{m.group(1)}" controls muted loop playsinline style="width:100%"></video>')
        i += 1
        continue
    m = re.match(r'<image source="([^"]+)"\s*/>', s)
    if m:
        out.append(pre + f'![]({m.group(1)})')
        i += 1
        continue
    if s.startswith('<table'):
        j = next(k for k in range(i, len(lines)) if lines[k].strip() == '</table>')
        body = '\n'.join(lines[i:j + 1])
        body = re.sub(r'<td>\s*(.*?)\s*</td>', lambda m: '<td>' + inline(' '.join(m.group(1).split())) + '</td>', body, flags=re.S)
        body = re.sub(r'<tr>\s*(.*?)\s*</tr>', lambda m: '<tr>' + re.sub(r'\s*\n\s*', '', m.group(1)) + '</tr>', body, flags=re.S)
        out.extend(pre + x for x in body.split('\n'))
        i = j + 1
        continue
    # list indent: Notion now uses 2 spaces per level, old format used tabs
    m = re.match(r'^((?:  )+)(-( |$)|\d+\. )', l)
    if m:
        l = '\t' * (len(m.group(1)) // 2) + l.lstrip(' ')
    out.append(pre + inline(l))
    i += 1

open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
