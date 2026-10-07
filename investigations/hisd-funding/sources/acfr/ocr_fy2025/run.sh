#!/usr/bin/env bash
cd /git/Texas/HISD/sources/acfr/ocr_fy2025
export TESSDATA_PREFIX=/tmp/claude-1000/-git/ef6926c4-5a2f-410b-ad21-44e5116c6cd8/scratchpad/tessdata
for p in $(cat pages.lst); do
  [ -s p$p.txt ] && continue
  pdftoppm -r 300 -gray -f $p -l $p -png ../HISD_ACFR_FY2025.pdf img
  f=$(ls img*.png | head -1)
  /nix/store/bv3yzxlghi529ia2vfnpy2x80yy1qhb2-tesseract-5.5.3/bin/tesseract $f p$p --psm 6 -c preserve_interword_spaces=1 >/dev/null 2>&1
  rm -f img*.png
done
echo DONE > done.flag
