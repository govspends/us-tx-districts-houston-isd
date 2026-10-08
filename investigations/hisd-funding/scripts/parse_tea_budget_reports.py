"""Parse TEA 'Budgeted Financial Data' reports (PEIMS Financial Standard Reports, budget side) for HISD and the
state total into data/tea_peims_budget_long.csv, and check that they reconcile.

Input:  sources/tea_peims/pwr/pwr_budget_{YYYY}_{101912,_STATE}.txt  (pdftotext -layout of the TEA PDFs;
        TEA program sfadhoc.budget_report_YYYY.sas, YYYY = spring year of the school year; 2019-20 .. 2025-26.
        2018-19 is not served by TEA's report server.)
Output: data/tea_peims_budget_long.csv

These are the budgets districts file with TEA in PEIMS (fall submission), i.e. the ADOPTED budget for the
General Fund, Food Service and Debt Service funds only. They are NOT actuals: "All Funds" here means those
adopted funds, not the all-funds totals in TEA's actual reports (which include federal grants).

Each data line carries six values: GF amount, GF %, GF per student, all-funds amount, %, per student, e.g.
  'State Operating Funds    $311,500,000   15.74%   $1,856   $311,991,957   14.67%   $1,859'
The script exits non-zero if a check fails.
"""
import csv, re, sys
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # the investigation folder

SRC = ROOT + "/sources/tea_peims/pwr/pwr_budget_{}_{}.txt"
OUT = ROOT + "/data/tea_peims_budget_long.csv"
YEARS = {"2020": "2019-20", "2021": "2020-21", "2022": "2021-22", "2023": "2022-23", "2024": "2023-24",
         "2025": "2024-25", "2026": "2025-26"}
ENT = {"101912": "Houston ISD", "_STATE": "State total"}
MONEY = r"(-?\$?-?[\d,]+)"
PCT = r"(-?[\d.]+)%"
LINE_RE = re.compile(r"^\s*(\S.*?)\s+" + r"\s+".join([MONEY, PCT, MONEY, MONEY, PCT, MONEY]) + r"\s*$")
SECTIONS = ["Operating Revenue", "Other Revenue", "Recapture Revenue",
            "Debt Service Financing and TRS Estimate Revenue", "Operating Expenditures by Object",
            "Non-Operating Expenditures by Object", "Operating Expenditures by Function",
            "Non-Operating Expenditures by Function", "Operating Expenditures by Program Intent Code",
            "Non-Operating Expenditures by PIC", "Total Disbursements"]

# HISD's own adopted General Fund budget for 2025-26 (S26 = sources/budget/FY26_-_Financial_Schedules_v2.pdf)
S26 = {"revenue": 2_082_033_202, "other_sources": 20_000_000 + 25_000_000,
       "appropriations": 2_121_893_114, "transfers_out": 19_823_927}


def num(x):
    return int(x.replace("$", "").replace(",", ""))


def parse(path):
    sec, rows, mem = "", [], None
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.search(r"Total Enrolled Membership:\s*([\d,]+)", line)
        if m:
            mem = num(m.group(1))
            continue
        s = line.strip()
        for t in SECTIONS:
            if s.startswith(t) and not re.search(r"\d%", s):
                sec = t
        m = LINE_RE.match(line)
        if m:
            lab = re.sub(r"\s+", " ", m.group(1)).strip()
            rows.append({"section": sec, "line": lab, "gf": num(m.group(2)), "gf_ps": num(m.group(4)),
                         "af": num(m.group(5)), "af_ps": num(m.group(7))})
    return rows, mem


def get(rows, sec, prefix, col):
    hits = [r[col] for r in rows if r["section"] == sec and r["line"].startswith(prefix)]
    if len(hits) != 1:
        raise KeyError(f"{sec} / {prefix}: {len(hits)} matches")
    return hits[0]


def main():
    out, ok = [], True

    def check(name, a, b, tol=0):
        nonlocal ok
        good = abs(a - b) <= tol
        ok &= good
        print(("OK       " if good else "MISMATCH ") + f"{name}: {a:,} vs {b:,}" + (f" (tolerance {tol})" if tol else ""))

    for yy, sy in YEARS.items():
        for cdn, ent in ENT.items():
            rows, mem = parse(SRC.format(yy, cdn))
            for r in rows:
                out.append({"cdn": cdn, "entity": ent, "school_year": sy, "basis": "budget filed with TEA (PEIMS)",
                            "enrolled_membership": mem, **r})
            tag = f"{sy} {ent}"
            for col in ("gf", "af"):
                op = "Operating Revenue"
                parts = sum(get(rows, op, p, col) for p in ("Local Property Tax from M&O", "State Operating Funds",
                                                            "Federal Funds", "Other Local"))
                check(f"{tag} {col.upper()} operating revenue = sum of sources", parts,
                      get(rows, op, "Total Operating Revenue", col), tol=4)
                fn = [r[col] for r in rows if r["section"] == "Operating Expenditures by Function"
                      and re.search(r"\(Function", r["line"])]
                check(f"{tag} {col.upper()} operating spending by function = by object", sum(fn),
                      get(rows, "Operating Expenditures by Object", "Total Operating Expenditures by Object", col), tol=4)
            if yy == "2026" and cdn == "101912":
                grand = (get(rows, "Operating Revenue", "Total Operating Revenue", "gf")
                         + get(rows, "Other Revenue", "Total Other Revenue", "gf")
                         + get(rows, "Debt Service Financing and TRS Estimate Revenue", "Estimated State TRS", "gf"))
                check(f"{tag} GF revenue incl. TRS and other receipts = HISD adopted revenue + other sources (S26)",
                      grand, S26["revenue"] + S26["other_sources"])
                check(f"{tag} GF total disbursements = HISD adopted appropriations + transfers out (S26)",
                      get(rows, "Total Disbursements", "Total Disbursements", "gf"),
                      S26["appropriations"] + S26["transfers_out"], tol=250)
    keys = ["cdn", "entity", "school_year", "basis", "enrolled_membership", "section", "line", "gf", "gf_ps", "af", "af_ps"]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(out)
    print(f"wrote {len(out)} rows to {OUT}")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
