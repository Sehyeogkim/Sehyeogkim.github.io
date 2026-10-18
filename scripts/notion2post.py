"""Convert a Notion fetch (<content>…</content>) into Jekyll post body, keeping the author's spacing.

usage: notion2post.py <notion.md> <frontmatter.yml> <out.md> [--ref "note under the reference link"] [--shift-headings]

Spacing rules (see writing_style.md "Notion → 블로그 변환 규칙"):
  - a run of N <empty-block/> (or a standalone <br>) -> <div class="notion-gap" style="--gap: N"></div>
  - <br> inside a line is kept as an inline line break
  - every other Notion block becomes its own Markdown block (one Enter = one paragraph break)
"""
import re, sys

src_path, fm_path, out_path = sys.argv[1:4]
ref_note = sys.argv[sys.argv.index('--ref') + 1] if '--ref' in sys.argv else ''

lines = open(src_path).read().replace('<content>', '').replace('</content>', '').strip('\n').split('\n')
img_no = 0


def flatten_columns(src):
    # Notion side-by-side columns -> blocks one after another (blog is single-column)
    out, depth = [], 0
    for ln in src:
        s = ln.strip()
        if s == '<columns>' or s.startswith('<column ') or s == '<column>':
            depth += 1
            continue
        if s in ('</column>', '</columns>'):
            depth -= 1
            continue
        out.append(ln[2:] if depth and ln.startswith('\t\t') else ln)
    return out


lines = flatten_columns(lines)
# blocks the Notion API can't export (video / embed placeholders) have nothing to show on the blog
lines = [ln for ln in lines if not ln.lstrip().startswith('<unknown ')]


def inline(s):
    # kramdown does not parse ** inside inline HTML, so bold inside an underline becomes <strong>
    s = re.sub(r'<span underline="true">(.*?)</span>', lambda m: '<u>' + re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', m.group(1)) + '</u>', s)
    s = re.sub(r'<span color="[^"]*">(.*?)</span>', r'\1', s)
    s = s.replace('****', '')
    # Notion leaves a space before the closing **: "**처음부터 **" -> "**처음부터** " (kramdown would print the ** literally)
    s = re.sub(r'(?<!\S)\*\*(\S[^*\n]*?\S|\S)\s+\*\*(?![*$])', r'**\1** ', s)
    s = s.replace('\\~', '~')
    # Notion inline math $`x`$ -> $x$, with _ escaped so kramdown does not turn it into <em>,
    # and \{ \} doubled so kramdown keeps the backslash for MathJax
    s = re.sub(r'\$`([^`]*)`\$', lambda m: '$' + m.group(1).replace('_', '\\_').replace('\\{', '\\\\{').replace('\\}', '\\\\}') + '$', s)
    # Notion splits bold around inline math: **A **$m$** B** -> **A $m$ B**
    s = re.sub(r'\*\*(\$[^$]+\$)\*\*', r'\1', s)
    # **A **$m$ (Notion closes bold right before math) -> **A $m$**
    s = re.sub(r'\*\*([^*\n]+?)\s+\*\*(\$[^$\n]+\$)', r'**\1 \2**', s)
    return s


def is_list(l):
    return bool(re.match(r'^\t*(-( |$)|\d+\. )', l)) or l.startswith('\t')


def gap(n):
    return f'<div class="notion-gap" style="--gap: {n}"></div>'


def img_md(item):
    global img_no
    img_no += 1
    nm = re.search(r'name=([^)&]+)', item)
    ext = nm.group(1).rsplit('.', 1)[-1].lower() if nm else 'png'
    return f'![](images/img-{img_no:03d}.' + ('jpg' if ext in ('jpg', 'jpeg') else 'png') + ')'


blocks = []          # list of (kind, text)
num_next = 1         # running number for numbered items split by other blocks
i = 0
while i < len(lines):
    l = lines[i]
    if l in ('<empty-block/>', '<br>') or not l.strip():
        n = 0
        while i < len(lines) and (lines[i] in ('<empty-block/>', '<br>') or not lines[i].strip()):
            n += 1 if lines[i].strip() else 0
            i += 1
        if n:
            blocks.append(('gap', n))
        continue
    if l.strip() == '<table_of_contents/>':
        # Notion TOC block -> list of the page's top-level (#) headings
        tops = [h[2:].strip() for h in lines if h.startswith('# ') and h[2:].strip() not in ('Contents', 'Table of Contents')]
        blocks.append(('p', '\n'.join('- ' + re.sub(r'^(\d+)\. ', r'\1\\. ', t) for t in tops)))
        i += 1
        continue
    if l.startswith('#'):
        num_next = 1
        blocks.append(('h', ('#' + l) if '--shift-headings' in sys.argv else l))
        i += 1
        continue
    if l.strip() == '>':
        # Notion quote block whose lines are tab-indented children -> one blockquote, one line per Notion line
        body = []
        i += 1
        while i < len(lines) and lines[i].startswith('\t'):
            body.append(inline(lines[i].lstrip('\t')))
            i += 1
        blocks.append(('p', '\n>\n'.join('> ' + b for b in body)))
        continue
    if l.startswith('<callout'):
        body = []
        i += 1
        while not lines[i].startswith('</callout>'):
            ln = lines[i][1:] if lines[i].startswith('\t') else lines[i]
            depth = len(ln) - len(ln.lstrip('\t'))  # nested list inside a callout keeps its indent
            body.append('  ' * depth + inline(ln.lstrip('\t')))
            i += 1
        i += 1
        # one Notion line inside a callout = one line in the blog (list items stay together)
        q = []
        for k, b in enumerate(body):
            if k and not (is_list(b.lstrip()) and is_list(body[k - 1].lstrip())):
                q.append('>')
            q.append('> ' + b)
        kind = 'prompt-tip' if 'green' in l else 'prompt-info'  # 🔑 green callout = tip (writing_style.md)
        blocks.append(('p', '\n'.join(q) + '\n{: .' + kind + ' }'))
        continue
    if l.startswith('<table'):
        j = next(k for k in range(i, len(lines)) if lines[k].startswith('</table>'))
        body = '\n'.join(lines[i:j + 1])
        rows = [re.findall(r'<td>(.*?)</td>', r, re.S) for r in re.findall(r'<tr>(.*?)</tr>', body, re.S)]
        md = ['| ' + ' | '.join(inline(c) for c in rows[0]) + ' |', '|' + '---|' * len(rows[0])]
        md += ['| ' + ' | '.join(inline(c) for c in r) + ' |' for r in rows[1:]]
        blocks.append(('p', '\n'.join(md)))
        i = j + 1
        continue
    if l.startswith('```'):
        j = next(k for k in range(i + 1, len(lines)) if lines[k].startswith('```'))
        lang = l[3:].strip()
        lang = 'text' if lang in ('', 'plain text', 'fortran') else lang  # he uses fortran blocks for plain prose
        blocks.append(('p', '```' + lang + '\n' + '\n'.join(lines[i + 1:j]) + '\n```'))
        i = j + 1
        continue
    if l == '$$':
        j = lines.index('$$', i + 1)
        blocks.append(('p', '\n'.join(lines[i:j + 1])))
        i = j + 1
        continue
    if l.startswith('!['):
        b = img_md(l)
        if i + 1 < len(lines) and re.match(r'^\(.*\)$', lines[i + 1]):
            b += '\n_' + lines[i + 1][1:-1] + '_'
            i += 1
        blocks.append(('p', b))
        i += 1
        continue
    if is_list(l):
        grp = []
        numbered = bool(re.match(r'^\d+\. ', l))
        kind = re.match(r'^(\d+\. |- )', l)
        while i < len(lines) and is_list(lines[i]):
            top_kind = re.match(r'^(\d+\. |- )', lines[i])
            # an ordered item right after bullets (or vice versa) starts a new block
            if grp and top_kind and kind and (top_kind.group(1) == '- ') != (kind.group(1) == '- '):
                break
            m = re.match(r'^(\t*)(.*)', lines[i])
            item = m.group(2)
            item = img_md(item) if item.startswith('![') else inline(item)  # image nested inside a list item
            if m.group(1) and not re.match(r'^(-( |$)|\d+\. )', m.group(2)):
                grp.append('')  # a plain child line under a bullet is its own line in Notion -> its own paragraph
            grp.append('  ' * len(m.group(1)) + item)
            i += 1
        text = '\n'.join(grp)
        if numbered:
            top = [g for g in grp if re.match(r'^\d+\. ', g)]
            if num_next > 1:
                text += '\n{: start="%d"}' % num_next
            num_next += len(top)
        blocks.append(('p', text))
        continue
    blocks.append(('p', inline(l)))
    i += 1

# drop leading / trailing gaps
while blocks and blocks[0][0] == 'gap':
    blocks.pop(0)
while blocks and blocks[-1][0] == 'gap':
    blocks.pop()

out = []
for kind, t in blocks:
    out.append(gap(t) if kind == 'gap' else t)
body = '\n\n'.join(out)

# first line of the Notion page is the source link -> Reference section
first = out[0]
if first.startswith('[') and '](http' in first:
    ref = '## Reference\n\n---\n\n' + first + ('\n\n' + ref_note if ref_note else '') + '\n\n## Overview\n\n---'
    body = body.replace(first, ref, 1)

open(out_path, 'w').write(open(fm_path).read().rstrip('\n') + '\n\n' + body + '\n')
print(f'{img_no} images, {sum(1 for k, _ in blocks if k == "gap")} gaps')
