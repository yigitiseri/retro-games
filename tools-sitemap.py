"""Rebuild sitemap.xml from what is actually on disk.

Hand-maintained lists go stale: the homepage description claimed seven
cabinets when there were fourteen. This reads the games directory instead,
so a new cabinet cannot be left out of the sitemap by forgetting a line.
"""
import os, re, datetime, sys

SITE = "https://yigitiseri.github.io/retro-games/"
root = os.path.dirname(os.path.abspath(__file__))

games = sorted(d for d in os.listdir(os.path.join(root, 'games'))
               if os.path.isfile(os.path.join(root, 'games', d, 'index.html')))
pages = [('', '1.0')] + [('games/%s/' % g, '0.8') for g in games] \
      + [(p, '0.2') for p in ('privacy.html', 'datenschutz.html')
         if os.path.isfile(os.path.join(root, p))]

today = datetime.date.today().isoformat()
out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, pri in pages:
    out += ['  <url>', '    <loc>%s%s</loc>' % (SITE, path),
            '    <lastmod>%s</lastmod>' % today,
            '    <priority>%s</priority>' % pri, '  </url>']
out.append('</urlset>')
open(os.path.join(root, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# the homepage says how many cabinets there are; keep that honest too
idx = os.path.join(root, 'index.html')
html = open(idx, encoding='utf-8').read()
cards = len(re.findall(r'<a class="cab ', html))
assert cards == len(games), 'menu lists %d cabinets but games/ holds %d' % (cards, len(games))
print('sitemap.xml: %d urls, %d cabinets' % (len(pages), len(games)))

# The root README drifted for twelve cabinets before anyone noticed, so it is
# checked here against the same source of truth as the sitemap: the menu.
def check_readme(n):

    md = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    rows = re.findall(r"^\| \[\*\*", md, re.M)
    assert len(rows) == n, (
        "README lists %d cabinets, the menu has %d" % (len(rows), n))
    words = {13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
             17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
             21: "Twenty-one", 22: "Twenty-two", 23: "Twenty-three",
             24: "Twenty-four", 25: "Twenty-five", 26: "Twenty-six",
             27: "Twenty-seven", 28: "Twenty-eight"}
    want = words.get(n)
    if want:
        assert md.startswith("# Retro Games\n\n%s arcade cabinets," % want), (
            "README opening line does not say %r" % want)
    print("README.md: %d cabinets, opening line agrees" % len(rows))


check_readme(cards)
