#!/usr/bin/env bash
# Run a govspends tool from the hub repository against this repository, e.g.
#   ./tools.sh run_checks            re-run the parsers and fail if the data tables change
#   ./tools.sh build_tables          refresh the generated tables and chart images in the pages
#   ./tools.sh sync_docs             refresh references, audit summary, notes, review and the Sources page
#   ./tools.sh build_site            refresh the generated block of docs/index.md
#   ./tools.sh build_pdf             build the PDF from the pages (needs weasyprint)
# The hub is cloned into .hub/ on first use (set GOVSPENDS_HUB to use an existing checkout).
# When this repository is cloned inside the hub folder (govspends/us-tx-counties-harris), the hub's tools are used directly.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
HUB="${GOVSPENDS_HUB:-}"
if [ -z "$HUB" ]; then
  if [ -f "$HERE/../tools/registry.py" ]; then HUB="$HERE/.."; else HUB="$HERE/.hub"; fi
fi
[ -d "$HUB" ] || git clone -q --depth 1 https://github.com/govspends/govspends "$HUB"
cd "$HERE" && exec python3 "$HUB/tools/$1.py" "${@:2}"
