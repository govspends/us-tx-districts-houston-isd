"""Crude HTML table -> pipe-delimited text (stdlib only). Usage: html2text.py in.html [start_marker]"""
import re, html, sys
s = open(sys.argv[1], encoding='utf-8', errors='replace').read()
s = re.sub(r'(?is)<script.*?</script>|<style.*?</style>|<select.*?</select>', '', s)
s = re.sub(r'(?i)</t[dh]>', ' | ', s)
s = re.sub(r'(?i)</tr>|<br\s*/?>|</p>|</div>', '\n', s)
s = re.sub(r'<[^>]+>', '', s)
s = html.unescape(s)
lines = [re.sub(r'\s+', ' ', l).strip() for l in s.split('\n')]
out = [l for l in lines if l and l.strip('| ')]
txt = '\n'.join(out)
if len(sys.argv) > 2 and sys.argv[2] in txt:
    txt = txt[txt.find(sys.argv[2]):]
print(txt)
