import sys, os, re

# Paste the Cloudflare Web Analytics token here to switch analytics on for the
# GitHub Pages copies. Empty means no analytics script is emitted at all.
# The Artifact versions never get this: they are private, and counting your own
# play sessions would only pollute the numbers.
ANALYTICS_TOKEN = "aee6e644a3b74cb9bdaf4e1569d570e2"

GOOGLE_FONT_LINKS = re.compile(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*">'
)

src_path, out_path, desc = sys.argv[1], sys.argv[2], sys.argv[3]
src = open(src_path, encoding='utf-8').read()
split = src.index('</style>') + len('</style>')
head, body = src[:split], src[split:].strip('\n')

# fonts are served from this site, not from Google: embedding them from
# fonts.gstatic.com hands every visitor's IP to a third party before they have
# agreed to anything
depth = len(os.path.normpath(out_path).split(os.sep))
rel = ''
m = re.search(r'(^|/)(games/[^/]+)/[^/]+$', out_path.replace(os.sep, '/'))
rel = '../../' if m else ''
head, n = GOOGLE_FONT_LINKS.subn(
    '<link rel="preload" href="%sassets/fonts/press-start-2p-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<link rel="stylesheet" href="%sassets/fonts/fonts.css">' % (rel, rel), head)
assert n == 1, 'expected exactly one Google Fonts block, found %d in %s' % (n, src_path)

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
''' % desc + head + analytics + '''
</head>
<body>
''' + body + '''
</body>
</html>
'''
open(out_path, 'w', encoding='utf-8').write(doc)
