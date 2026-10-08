#!/usr/bin/env bash
# Decode a base64 SOF download (saved by the browser tool as a JSON string) into <name>.pdf + <name>.txt.
# Usage: sof_b64_to_pdf.sh <in.b64> <out_basename>
set -e
in="$1"; out="$2"
head -c 7 "$in" | grep -q FAILED && { echo "download failed: $in" >&2; exit 1; }
tr -d '"\n ' < "$in" | base64 -d > "$out.pdf"
[ "$(head -c 5 "$out.pdf")" = "%PDF-" ] || { echo "not a PDF: $out.pdf" >&2; exit 1; }
rm -f "$in"
nix-shell -p poppler-utils --run "pdftotext -layout '$out.pdf' '$out.txt'; pdfinfo '$out.pdf' | grep Pages" 2>&1 | grep -v "search path"
sed -n '1,8p' "$out.txt" | grep -E "Summary of Finances|Last Update|Run Id" | sed 's/^ *//'
