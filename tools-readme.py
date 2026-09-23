#!/usr/bin/env python3
"""Regenerate the README's cabinet table, count and layout tree from the menu.

The README drifted for twelve cabinets before anyone noticed, and
tools-sitemap.py now refuses to run when it does. Rather than fix it by hand
each time, generate it: index.html is the single source of truth for what the
arcade contains, and games/ for what is on disk.
"""
import io, os, re, html

root = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(root, 'index.html'), encoding='utf-8').read()

cards = re.findall(
    r'<a class="cab [^"]*" href="(games/[^/]+/)">.*?<span class="no">([^<]*)</span>\s*'
    r'<h2>([^<]*)</h2>\s*<p>(.*?)</p>', src, re.S)
assert cards, 'no cabinets found in index.html'

# Spelled out rather than tabulated: the table ran out at thirty and stopped
# the build on the cabinet that followed.
ONES = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
        'Eighty', 'Ninety']

def word(n):
    assert 0 < n < 100, 'cabinet count out of range: %d' % n
    if n < 20:
        return ONES[n]
    return TENS[n // 10] + ('-' + ONES[n % 10].lower() if n % 10 else '')

n = len(cards)

def clean(t):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t))).strip()

rows, slugs = [], []
for href, _no, name, desc in cards:
    nm = html.unescape(name).strip()
    slugs.append(href.strip('/').split('/')[-1])
    rows.append('| [**%s**](%s) | %s | [`%sindex.html`](%sindex.html) |'
                % (nm, href, clean(desc), href, href))

have = [s for s in slugs if os.path.isfile(os.path.join(root, 'games', s, 'README.md'))]
tree = '\n'.join('  %s/%s index.html%s'
                 % (s, ' ' * max(1, 9 - len(s)), '  README.md' if s in have else '')
                 for s in slugs)

p = os.path.join(root, 'README.md')
md = io.open(p, encoding='utf-8').read()

md = re.sub(r'^\w[\w-]* arcade cabinets,', '%s arcade cabinets,' % word(n), md, count=1, flags=re.M)

a = md.index('| Game | | Play |')
b = md.index('\n\n', md.index('|', a + 40))
md = md[:a] + '| Game | | Play |\n| --- | --- | --- |\n' + '\n'.join(rows) + md[b:]

a = md.index('```\nindex.html       the arcade menu')
b = md.index('```', a + 5) + 3
md = md[:a] + '```\nindex.html       the arcade menu\ngames/\n' + tree + '\n```' + md[b:]

md = re.sub(r'^\d+ of the cabinets have their own README',
            '%d of the cabinets have their own README' % len(have), md, count=1, flags=re.M)

io.open(p, 'w', encoding='utf-8').write(md)
print('README.md: %d cabinets, %d with their own README' % (n, len(have)))
