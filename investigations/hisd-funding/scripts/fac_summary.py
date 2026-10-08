#!/usr/bin/env python3
"""Summarize HISD Federal Audit Clearinghouse (FAC) SEFA data by ALN, one column per audit year found (FY2018-FY2025 as of 2026-10-07).
Input: sources/federal_debt/fac_awards_<report_id>.json (api.fac.gov federal_awards)."""
import json, glob, collections, os
base = os.path.join(os.path.dirname(__file__), '..', 'sources', 'federal_debt')
years = {}
for f in sorted(glob.glob(os.path.join(base, 'fac_awards_*.json'))):
    d = json.load(open(f))
    y = d[0]['audit_year']
    agg = collections.OrderedDict()
    for r in d:
        aln = f"{r['federal_agency_prefix']}.{r['federal_award_extension']}"
        key = (aln, r['federal_program_name'][:70])
        agg[key] = agg.get(key, 0) + r['amount_expended']
    years[y] = agg
alns = collections.OrderedDict()
for y in sorted(years):
    for k in years[y]:
        alns.setdefault(k[0], k[1])
ys = sorted(years)
print('ALN'.ljust(9), 'Program'.ljust(60), *[y.rjust(13) for y in ys])
for aln, name in sorted(alns.items()):
    vals = []
    for y in ys:
        v = sum(a for (k, n), a in years[y].items() if k == aln)
        vals.append(f"{v:13,}" if v else ' ' * 12 + '-')
    print(aln.ljust(9), name[:60].ljust(60), *vals)
print('TOTAL'.ljust(70), *[f"{sum(years[y].values()):13,}" for y in ys])
