#!/usr/bin/env python3
"""Parse a Playwright accessibility snapshot of TEA's SOF dashboard run table into CSV rows.

Usage: sof_runs_from_snapshot.py <school_year> <snapshot.yml> >> data/sof_run_history.csv
Columns: school_year, run_id, run_date, payment_cycle, foundation_allotment, recapture_amount
"""
import re, sys

sy, path = sys.argv[1], sys.argv[2]
cells = re.findall(r'gridcell "([^"]*)"', open(path).read())
header = ["Payment Cycle", "Foundation Allotment", "Recapture Amount", "SOF"]
start = next(i for i in range(len(cells)) if cells[i:i+4] == header) + 4
rows = cells[start:]
for i in range(0, len(rows) - 4, 5):
    run, date, cycle, fa, rc = rows[i:i+5]
    if not run.isdigit():
        break
    num = lambda s: s.replace("$", "").replace(",", "").replace("(", "-").replace(")", "")
    print(f'{sy},{run},"{date}",{cycle},{num(fa)},{num(rc)}')
