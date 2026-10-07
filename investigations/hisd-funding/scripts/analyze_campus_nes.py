"""NES vs non-NES campus spending from TEA campus-level PEIMS actuals.

Inputs:  data/hisd_campus_actuals.csv  (parse_campus_actuals.py; TEA campus actual reports)
         data/hisd_nes_campuses.csv    (NES status by year; compiled from HISD/news sources - see SOURCES.md)
Output:  data/hisd_campus_nes_summary.csv

Per-student figures are membership-weighted (sum of dollars / sum of TEA 'Total Membership').
Campus-level PEIMS data covers only campus-coded spending (~80% of HISD AF operating spending in 2024-25);
central costs (function 34-99 especially) are mostly not attributed to campuses.
Campuses with membership < 100 and alternative/DAEP/JJAEP/program sites are excluded.
"""
import csv, re, statistics

D = "/git/Texas/HISD/data"
EXCL = re.compile(r"daep|j j a e p|jjaep|chrysalis|life skills|community services|ahead academy|program", re.I)


def level(name):
    n = name.replace("El", " El").replace("Middle", " Middle")
    if re.search(r"Early Childhood|\bEcc\b|Ctr$", n) and "Early" in n or re.search(r"\bEcc\b", n):
        return "ECC"
    if re.search(r"\bEl\b", n):
        return "Elementary"
    if re.search(r"\bMiddle\b|\bM S\b", n):
        return "Middle"
    if re.search(r"\bH S\b|High", n):
        return "High"
    return "Other/Combined"


def main():
    camp = list(csv.DictReader(open(f"{D}/hisd_campus_actuals.csv")))
    nes = {r["campus_id"]: r for r in csv.DictReader(open(f"{D}/hisd_nes_campuses.csv"))}
    col = {"2023-24": "nes_2023_24", "2024-25": "nes_2024_25"}
    nes_2425 = {cid for cid, r in nes.items() if r.get("nes_2024_25", "").strip().upper().startswith("NES")}

    def status(cid, sy):
        if sy == "2022-23":   # NES started Aug 2023; classify by 2024-25 cohort for before/after comparisons
            return "NES-cohort-2024-25 (pre-NES year)" if cid in nes_2425 else "never-NES-by-2024-25"
        v = nes.get(cid, {}).get(col[sy], "").strip()
        if not v and sy == "2023-24" and cid in nes_2425:
            return "non-NES (joins NES 2024-25)"
        return v if v else "non-NES"

    groups = {}
    for r in camp:
        m = int(r["membership"])
        if m < 100 or EXCL.search(r["campus_name"]):
            continue
        for lv in ("ALL", level(r["campus_name"])):
            key = (r["school_year"], status(r["campus_id"], r["school_year"]), lv)
            groups.setdefault(key, []).append(r)
    out = []
    for (sy, st, lv), rs in sorted(groups.items()):
        mem = sum(int(r["membership"]) for r in rs)
        rec = {"school_year": sy, "nes_status": st, "level": lv, "campuses": len(rs), "membership": mem}
        for k in ("total_oper_exp", "payroll", "f11_instruction", "f23_school_leadership", "f21_instr_leadership",
                  "f31_guidance", "pic_comp_ed", "pic_swd"):
            for fund in ("af", "gf"):
                tot = sum(float(r.get(f"{k}_{fund}") or 0) for r in rs)
                rec[f"{k}_{fund}_per_student"] = round(tot / mem) if mem else ""
        rec["median_campus_total_oper_af_ps"] = round(statistics.median(float(r["total_oper_exp_af_ps"]) for r in rs))
        out.append(rec)
    with open(f"{D}/hisd_campus_nes_summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    for r in out:
        if r["level"] in ("ALL", "Elementary", "Middle", "High"):
            print(r["school_year"], r["nes_status"][:34].ljust(34), r["level"].ljust(10), str(r["campuses"]).rjust(4),
                  str(r["membership"]).rjust(7), "AF oper/stu", r["total_oper_exp_af_per_student"],
                  "GF", r["total_oper_exp_gf_per_student"], "instr AF", r["f11_instruction_af_per_student"],
                  "schl-lead AF", r["f23_school_leadership_af_per_student"], "payroll AF", r["payroll_af_per_student"])


if __name__ == "__main__":
    main()
