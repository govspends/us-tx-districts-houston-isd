#!/usr/bin/env python3
"""Extract key HISD figures from TEA Summary of Finances text (pdftotext -layout) into a CSV.

Uses the right-hand column of each SOF (Final / Near-Final / Preliminary LPE).
SY2018-19 predates HB3 (2019): it reports a cost-adjusted "Adjusted Allotment" instead of the Basic
Allotment, labels the tiers "Tier I/II", and carries no recapture line (recapture comes from TEA's
separate Cost of Recapture report). Recapture for every year is therefore also taken from
data/sof_run_history.csv (TEA's dashboard run table), matched on the report's own Run ID.
Regenerate the text with:
  pdftotext -layout sources/<sof>.pdf data/sof_text/<name>.txt
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = [
    ("SY2018-19 Final", ROOT / "data/sof_text/sof_2018-19_final.txt"),
    ("SY2019-20 Final", ROOT / "data/sof_text/sof_2019-20_final.txt"),
    ("SY2020-21 Final", ROOT / "data/sof_text/sof_2020-21_final.txt"),
    ("SY2021-22 Final", ROOT / "data/sof_text/sof_2021-22_final.txt"),
    ("SY2022-23 Final", ROOT / "data/sof_text/sof_2022-23_final.txt"),
    ("SY2023-24 Final", ROOT / "data/sof_text/sof_2023-24_final.txt"),
    ("SY2024-25 Final", ROOT / "data/sof_text/sof_2024-25_final.txt"),
    ("SY2025-26 Near-Final", ROOT / "data/sof_text/sof_2025-26_nearfinal.txt"),
    ("SY2026-27 Preliminary", ROOT / "data/sof_text/sof_2026-27_preliminary_run47318.txt"),
]

NUM = re.compile(r"\(?\$?-?[\d,]+(?:\.\d+)?\)?")

# (row name, section, label regex). section: "summary" = page 1-2 summary,
# "other" = Other Programs Detail Report. Missing rows are recorded as blank.
ROWS = [
    ("Refined ADA", "summary", r"Refined Average Daily Attendance"),
    ("WADA", "summary", r"Weighted ADA \(WADA\)"),
    ("PEIMS enrollment", "summary", r"PEIMS Enrollment"),
    ("Basic Allotment (SY2018-19: cost-adjusted allotment)", "summary",
     r"District Basic Allotment|^\s*\d+\.\s+Adjusted Allotment\s"),
    ("M&O tax rate", "summary", r"current tax year\) M&O Tax Rate|M&O Tax Rate \(current tax year\)"),
    ("Tier One M&O tax rate", "summary", r"current tax year\) (Tier one|Compressed) M&O Tax Rate"),
    ("M&O tax collections", "summary", r"\d{4}-\d{4} (\(current school year\) )?M&O Tax Collections"),
    ("I&S tax collections", "summary", r"\d{4}-\d{4} (\(current school year\) )?I&S Tax Collections"),
    ("Regular Program Allotment", "summary", r"11-Regular Program Allotment|Regular Program Allotment 48\.051"),
    ("Special Education Allotment", "summary", r"Special Education Adjusted Allotment"),
    ("Dyslexia Allotment", "summary", r"Dyslexia Allotment"),
    ("Compensatory Education Allotment", "summary", r"Compensatory Education Allotment"),
    ("Bilingual Education Allotment", "summary", r"Bilingual Education Allotment"),
    ("Career & Technology Allotment", "summary", r"Career and Technology Allotment"),
    ("Early Education Allotment", "summary", r"36-Early Education Allotment"),
    ("Full-Day Pre-K Distribution", "summary", r"36-Full-Day Pre-K Distribution"),
    ("Gifted & Talented Allotment", "summary", r"Gifted & Talented Adjusted Allotment"),
    ("CCMR Outcomes Bonus", "summary", r"CCMR Outcomes Bonus"),
    ("Teacher Incentive Allotment", "summary", r"Teacher Incentive Allotment 48\.112"),
    ("Teacher Retention Allotment", "summary", r"Teacher Retention Allotment 48\.158"),
    ("Support Staff Retention Allotment", "summary", r"Support Staff Retention Allotment"),
    ("School Safety Allotment", "summary", r"School Safety Allotment 48\.1(15|60)"),
    ("Allotment for Basic Costs", "summary", r"Allotment for Basic Costs"),
    ("Special Ed FIIE Allotment", "summary", r"Full Individual and Initial Evaluation"),
    ("Transportation Allotment", "summary", r"99-Transportation Allotment"),
    ("Dropout Recovery/Residential Allotment", "summary", r"Dropout Recovery and Residential"),
    ("College Prep Assessment Reimbursement", "summary", r"College Prep"),
    ("Certification Exam Reimbursement", "summary", r"Certification Examination Reimbursement"),
    ("Total Cost of Tier One", "summary", r"Total Cost of Tier (One|I)\s"),
    ("Local Fund Assignment", "summary", r"Local Fund Assignment"),
    ("ASF per-capita distribution", "summary", r"Per Capita Distribution from Available School Fund"),
    ("Tier Two", "summary", r"^\s*\d+\.?\s+Tier (Two|II)\s"),
    ("Other Programs", "summary", r"^\s*\d+\.?\s+Other Programs\s"),
    ("Foundation School Fund (199/5812)", "summary", r"199/5812"),
    ("Available School Fund (199/5811)", "summary", r"199/5811"),
    ("Instructional Materials & Tech Fund (410/5829)", "summary", r"410/5829"),
    ("ASAHE for facilities (I&S)", "summary", r"Additional State Aid for Homestead"),
    ("TOTAL FSP/ASF STATE AID", "summary", r"TOTAL FSP/ASF STATE AID"),
    ("Recapture (local revenue in excess of entitlement)", "summary",
     r"^\s*\d+\.?\s+Local Revenue in Excess of Entitlement"),
    ("OP: Supplemental TIF/TIRZ payment 48.253", "other", r"Supplemental Tax Increment Fund"),
    ("OP: Ad valorem tax refunds 48.2541", "other", r"Certain Ad Valorem Tax Refunds"),
    ("OP: Elderly/disabled homestead limitation 48.2542", "other",
     r"Limitation( on)?$|Limitation on Tax Increases|on Tax Increases on Homestead"),
    ("OP: Districts impacted by compression 48.283", "other", r"Impacted( by Compression)?"),
    ("OP: No longer subject to recapture 48.257(b-1)", "other", r"Districts No\b|No Longer Subject to Recapture"),
    ("OP: State-approved instructional materials 48.307", "other", r"State-Approved Instructional"),
    ("OP: OER instructional materials 48.308", "other", r"Open Education Resource|Materials \(48\.308\)"),
    ("OP: TSBVI", "other", r"School for the Blind and Visually Impaired( \(TSBVI\))?\s*(\(|\$|$)"),
    ("OP: TSD", "other", r"Texas School for the Deaf( \(TSD\))?\s*(\(|\$|$)"),
]


def parse_num(tok):
    neg = tok.startswith("(") and tok.endswith(")")
    v = tok.strip("()$").replace(",", "")
    try:
        x = float(v)
    except ValueError:
        return None
    return -x if neg else x


def amounts(line):
    # Only take tokens that look like money/quantities after the label text.
    toks = re.findall(r"\(?\$[\d,]+(?:\.\d+)?\)?|\(?\$\-?[\d,]+\)?|(?<![\w.§])[\d]{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.§])\d+\.\d{3,}", line)
    return [n for n in (parse_num(t) for t in toks) if n is not None]


def section_lines(lines, section):
    if section == "summary":
        return lines[:240]
    start = next((i for i, l in enumerate(lines) if "Other Programs Detail" in l), None)
    if start is None:
        return []
    end = next((i for i in range(start + 5, len(lines)) if "Total Other Programs" in lines[i]), start + 140)
    return lines[start:end + 1]


def find(lines, pattern):
    rx = re.compile(pattern)
    for i, line in enumerate(lines):
        if rx.search(line):
            for j in [i, i + 1, i - 1, i + 2, i + 3]:
                if 0 <= j < len(lines):
                    a = amounts(lines[j])
                    if a:
                        return a[-1]
            return None
    return None


def fmt(v):
    if v is None:
        return ""
    if v == int(v):
        return str(int(v))
    return f"{v:.4f}".rstrip("0").rstrip(".")


RUN_TABLE_RECAPTURE = "Recapture (TEA dashboard run table, same run)"
RUN_ID = "SOF run ID"


def run_table():
    path = ROOT / "data/sof_run_history.csv"
    if not path.exists():
        return {}
    return {r["run_id"]: r for r in csv.DictReader(path.open())}


def main():
    data = {}
    runs = run_table()
    for year, path in YEARS:
        text = path.read_text()
        lines = text.splitlines()
        data[year] = {name: find(section_lines(lines, sec), pat) for name, sec, pat in ROWS}
        m = re.search(r"Run I[dD]:\s*(\d+)", text)
        run = m.group(1) if m else None
        data[year][RUN_ID] = float(run) if run else None
        r = runs.get(run)
        data[year][RUN_TABLE_RECAPTURE] = -float(r["recapture_amount"]) if r else None
    names = [RUN_ID] + [n for n, _, _ in ROWS] + [RUN_TABLE_RECAPTURE]
    out = ROOT / "data/sof_key_figures.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item"] + [y for y, _ in YEARS])
        for name in names:
            w.writerow([name] + [fmt(data[y][name]) for y, _ in YEARS])
    print(f"wrote {out}", file=sys.stderr)
    ok = reconcile(data)
    sys.exit(0 if ok else 1)


def reconcile(data):
    ok = True
    for year, d in data.items():
        g = lambda k: d.get(k) or 0
        checks = {
            "state aid = FSF + ASF + IMTF + ASAHE": (
                g("TOTAL FSP/ASF STATE AID"),
                g("Foundation School Fund (199/5812)") + g("Available School Fund (199/5811)")
                + g("Instructional Materials & Tech Fund (410/5829)") + g("ASAHE for facilities (I&S)")),
            "ASF = per-capita distribution": (
                g("Available School Fund (199/5811)"), abs(g("ASF per-capita distribution"))),
        }
        pdf_recapture = d.get("Recapture (local revenue in excess of entitlement)")
        if pdf_recapture is not None and d.get(RUN_TABLE_RECAPTURE) is not None:
            checks["recapture in report = dashboard run table"] = (pdf_recapture, d[RUN_TABLE_RECAPTURE])
        for label, (a, b) in checks.items():
            good = abs(a - b) < 1
            ok &= good
            print(f"{year}: {label}: {'OK' if good else f'MISMATCH {a:,.0f} vs {b:,.0f}'}", file=sys.stderr)
    return ok


if __name__ == "__main__":
    main()
