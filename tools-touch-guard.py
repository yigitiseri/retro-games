#!/usr/bin/env python3
"""Put tools-build.py's TOUCH_GUARD into every page already built.

Idempotent: a page that already carries the block has it replaced with the
current one, so this is safe to run again whenever the guard changes.
"""
import io, os, re, glob

root = os.path.dirname(os.path.abspath(__file__))
build = io.open(os.path.join(root, 'tools-build.py'), encoding='utf-8').read()
m = re.search(r'TOUCH_GUARD = """(.*?)"""', build, re.S)
assert m, 'TOUCH_GUARD not found in tools-build.py'
guard = m.group(1)
block = re.compile(r'<!-- touch-guard:start -->.*?<!-- touch-guard:end -->\n?', re.S)

n = 0
for path in sorted(glob.glob(os.path.join(root, 'games', '*', 'index.html'))):
    src = io.open(path, encoding='utf-8').read()
    src = block.sub('', src)
    assert src.count('</head>') == 1, 'expected one </head> in %s' % path
    src = src.replace('</head>', guard + '</head>')
    io.open(path, 'w', encoding='utf-8').write(src)
    n += 1
print('touch guard in %d cabinets' % n)
