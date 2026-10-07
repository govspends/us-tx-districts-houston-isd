#!/usr/bin/env python3
"""Strip an HTML file to text and print context around $ amounts (or a regex given as argv[2])."""
import re, html, sys
t = open(sys.argv[1], errors='ignore').read()
t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
t = html.unescape(re.sub(r'<[^>]+>', ' ', t)); t = re.sub(r'\s+', ' ', t)
pat = sys.argv[2] if len(sys.argv) > 2 else r'\$[0-9][0-9,\.]*( (million|billion))?'
w = int(sys.argv[3]) if len(sys.argv) > 3 else 200
for m in re.finditer(pat, t):
    print('...', t[max(0, m.start()-w):m.end()+w//2], '...\n')
