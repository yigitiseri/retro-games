import sys, os, re

# Paste the Cloudflare Web Analytics token here to switch analytics on for the
# GitHub Pages copies. Empty means no analytics script is emitted at all.
# The Artifact versions never get this: they are private, and counting your own
# play sessions would only pollute the numbers.
ANALYTICS_TOKEN = "aee6e644a3b74cb9bdaf4e1569d570e2"

# Where the built copies are served from. Used for the canonical link and for the
# share card, both of which have to be absolute URLs: a relative one is ignored.
SITE_URL = "https://yigitiseri.github.io/retro-games/"
SITE_NAME = "Retro Games Arcade"

GOOGLE_FONT_LINKS = re.compile(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*">'
)

src_path, out_path, desc = sys.argv[1], sys.argv[2], sys.argv[3]
src = open(src_path, encoding='utf-8').read()

# test hooks belong to the harness, not to the cabinet people play
if not os.environ.get('KEEP_TEST_HOOK'):
    src = re.sub(r'\n?[ \t]*/\* test-hook:start.*?test-hook:end \*/', '', src, flags=re.S)
    assert 'test-hook' not in src, 'unbalanced test-hook markers in %s' % src_path
split = src.index('</style>') + len('</style>')
head, body = src[:split], src[split:].strip('\n')

# fonts are served from this site, not from Google: embedding them from
# fonts.gstatic.com hands every visitor's IP to a third party before they have
# agreed to anything
depth = len(os.path.normpath(out_path).split(os.sep))
rel = ''
m = re.search(r'(^|/)(games/[^/]+)/[^/]+$', out_path.replace(os.sep, '/'))
rel = '../../' if m else ''
# each family the page asks Google for maps to a stylesheet we serve ourselves,
# so a new font can never silently fall back to a system one in the built copy
FAMILY_FILES = {
    'Press Start 2P': ('fonts.css', 'press-start-2p-latin.woff2'),
    'VT323':          ('fonts.css', None),
    'Chakra Petch':   ('chakra-petch.css', 'chakra-petch-700-latin.woff2'),
}

m_fonts = GOOGLE_FONT_LINKS.search(head)
assert m_fonts, 'expected exactly one Google Fonts block in %s' % src_path
families = [f.split(':')[0].replace('+', ' ')
            for f in re.findall(r'family=([^&"]+)', m_fonts.group(0))]
assert families, 'no font families named in the Google Fonts block of %s' % src_path

sheets, preloads = [], []
for fam in families:
    assert fam in FAMILY_FILES, (
        '%s asks for "%s", which is not served from this site yet. Add the woff2 '
        'files and a stylesheet under assets/fonts/ first.' % (src_path, fam))
    sheet, preload = FAMILY_FILES[fam]
    if sheet not in sheets: sheets.append(sheet)
    if preload and preload not in preloads: preloads.append(preload)

links = ''.join(
    '<link rel="preload" href="%sassets/fonts/%s" as="font" type="font/woff2" crossorigin>\n' % (rel, f)
    for f in preloads)
links += '\n'.join('<link rel="stylesheet" href="%sassets/fonts/%s">' % (rel, f) for f in sheets)

head, n = GOOGLE_FONT_LINKS.subn(links.replace('\\', '\\\\'), head)
assert n == 1, 'expected exactly one Google Fonts block, found %d in %s' % (n, src_path)

# the page's own address, derived from where it is being written
page_rel = m.group(2) + '/' if m else ''
page_url = SITE_URL + page_rel

title_m = re.search(r'<title>(.*?)</title>', head, re.S)
assert title_m, 'no <title> in %s' % src_path
game_name = title_m.group(1).strip()
# search results show the title: the cabinet name alone says nothing about what it is
page_title = '%s \u2014 %s' % (game_name, SITE_NAME) if page_rel else game_name
head = head[:title_m.start()] + '<title>%s</title>' % page_title + head[title_m.end():]

social = """
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{root}assets/social-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{root}assets/social-card.png">
""".format(url=page_url, site=SITE_NAME, title=page_title,
           desc=desc.replace('"', '&quot;'), root=SITE_URL)

analytics = ''
if ANALYTICS_TOKEN:
    analytics = (
        '\n<!-- Cloudflare Web Analytics: no cookies, no client-side storage -->\n'
        '<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" '
        'data-cf-beacon=\'{"token": "%s"}\'></script>\n'
        '<!-- End Cloudflare Web Analytics -->\n' % ANALYTICS_TOKEN)

doc = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1">
<meta name="description" content="%s">
<meta name="theme-color" content="#08090e">
<style>
  :root {
    color-scheme: dark;
    padding-top: env(safe-area-inset-top, 0px);
    padding-bottom: env(safe-area-inset-bottom, 0px);
  }
  body { margin: 0; }
  img { max-width: 100%%; }
  [hidden] { display: none !important; }
</style>
''' % desc + head + social + analytics + '''
</head>
<body>
''' + body + '''
</body>
</html>
'''
open(out_path, 'w', encoding='utf-8').write(doc)
