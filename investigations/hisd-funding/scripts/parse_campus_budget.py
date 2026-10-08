"""Parse TEA's '2025-2026 PEIMS Budget Financial Data, Organized by Campus' for HISD and summarize NES vs non-NES.

Input:  sources/tea_peims/campus/allcamp_budget_2026_101912.txt
        (pdftotext -layout of TEA program sfadhoc.allcamp_budget_report_2026.sas, who_box=101912; same layout as
         the campus ACTUAL reports parsed by parse_campus_actuals.py, whose line pattern and labels are reused)
        data/hisd_nes_campuses.csv (column nes_2025_26)
Output: data/hisd_campus_budget_2025_26.csv   (one row per campus, BUDGETED, as filed by HISD with TEA)
        data/hisd_campus_nes_budget_summary.csv (membership-weighted per-student budget by NES status)

These are budgets, not actuals. Campus budgets cover the adopted funds only (in practice the General Fund), so
compare them with the General Fund (gf) columns of the actuals, not the all-funds columns. Membership is TEA's
fall 2025 count. Exclusions follow analyze_campus_nes.py (membership < 100; DAEP/JJAEP/program sites).
"""
import csv, re, sys
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from parse_campus_actuals import LABELS, LINE_RE, f   # same report layout
from analyze_campus_nes import EXCL, level

ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
SRC = ROOT + "/sources/tea_peims/campus/allcamp_budget_2026_101912.txt"
OUT = ROOT + "/data/hisd_campus_budget_2025_26.csv"
SUM = ROOT + "/data/hisd_campus_nes_budget_summary.csv"
DISTRICT_GF_OPER_2026 = 2_038_813_425   # TEA district budget report 2025-26, GF total operating expenditures


def main():
    rows, cur, name, seen = [], None, "", 0
    for line in open(SRC, encoding="utf-8", errors="replace"):
        m = re.search(r"School Campus:(.+?)\s*District:", line)
        if m:
            name = m.group(1).strip()
            continue
        m = re.search(r"Campus Number:(\d{9})\s+Total Membership:\s*([\d,]+)", line)
        if m:
            if cur is None or cur["campus_id"] != m.group(1):
                cur = {"school_year": "2025-26", "basis": "budget filed with TEA (PEIMS)", "campus_id": m.group(1),
                       "campus_name": name, "membership": int(m.group(2).replace(",", ""))}
                rows.append(cur)
                seen = 0
            continue
        if not line.rstrip()[-1:].isdigit():
            continue
        m = LINE_RE.match(line)
        if m and cur is not None:
            key = LABELS.get(re.sub(r"\s+", "", m.group(1)).rstrip("*"))
            if key == "total_oper_exp":
                seen += 1
                if seen > 1:
                    continue
            if key:
                cur[key + "_gf"] = f(m.group(2)); cur[key + "_gf_ps"] = f(m.group(4))
                cur[key + "_af"] = f(m.group(5)); cur[key + "_af_ps"] = f(m.group(7))
    keys = ["school_year", "basis", "campus_id", "campus_name", "membership"]
    for k in LABELS.values():
        if any(k + "_gf" in r for r in rows):
            keys += [k + s for s in ("_gf", "_gf_ps", "_af", "_af_ps")]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in keys})

    nes = {r["campus_id"]: r.get("nes_2025_26", "").strip() for r in csv.DictReader(open(ROOT + "/data/hisd_nes_campuses.csv"))}
    groups = {}
    for r in rows:
        if r["membership"] < 100 or EXCL.search(r["campus_name"]):
            continue
        st = "NES" if nes.get(r["campus_id"], "").upper().startswith("NES") else "non-NES"
        for lv in ("ALL", level(r["campus_name"])):
            groups.setdefault((st, lv), []).append(r)
    out = []
    for (st, lv), rs in sorted(groups.items()):
        mem = sum(r["membership"] for r in rs)
        rec = {"school_year": "2025-26", "basis": "budget filed with TEA (PEIMS)", "nes_status": st, "level": lv,
               "campuses": len(rs), "membership": mem}
        for k in ("total_oper_exp", "payroll", "f11_instruction", "f23_school_leadership", "f21_instr_leadership"):
            rec[f"{k}_gf_per_student"] = round(sum(r.get(k + "_gf", 0) for r in rs) / mem)
        out.append(rec)
    with open(SUM, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

    tot = sum(r.get("total_oper_exp_gf", 0) for r in rows)
    print(f"campuses {len(rows)}, membership {sum(r['membership'] for r in rows):,}, "
          f"campus-coded GF operating budget {tot:,.0f} = {tot / DISTRICT_GF_OPER_2026:.1%} of the district GF operating budget")
    missing = [r["campus_id"] for r in rows if "total_oper_exp_gf" not in r]
    for r in out:
        print(r["nes_status"].ljust(8), r["level"].ljust(15), str(r["campuses"]).rjust(4), str(r["membership"]).rjust(7),
              "GF oper/student", r["total_oper_exp_gf_per_student"])
    if missing:
        print("MISSING totals for", missing[:10]); sys.exit(1)


if __name__ == "__main__":
    main()
