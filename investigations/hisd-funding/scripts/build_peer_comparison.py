"""Build HISD + peer + state PEIMS actual-financial tables from TEA's statewide PWR data-dump xlsx files.

Inputs (TEA "PEIMS Financial Standard Reports" -> Financial Actual Reports data download, one per year):
  sources/tea_peims/{actual2025-info-gen-all, actual2024-info-gen-all-w-fb, 2023-actual-pwr,
                     2022-actual-pwr-0, 2021-actual-pwr}.xlsx
Per-student = amount / Total Enrolled Membership (the denominator TEA's PWR report uses).
"State" = sum of every row in the dump (all ISDs + charters), which is what TEA's PWR
"State Total (All Districts)" shows; ISD-only state totals are also emitted as STATE_ISD.

Outputs:
  data/tea_peims_actuals_long.csv   one row per (entity, year, fund, line): amount, per_student
  data/peer_comparison.csv          wide, latest year (2024-25), per student, AF and GF
  data/hisd_peims_trend.csv         HISD 2020-21..2024-25, per student, AF and GF
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from xlsx_lite import read_xlsx

SRC = "/git/Texas/HISD/sources/tea_peims"
DATA = "/git/Texas/HISD/data"
FILES = {"2024-25": "actual2025-info-gen-all.xlsx", "2023-24": "actual2024-info-gen-all-w-fb.xlsx",
         "2022-23": "2023-actual-pwr.xlsx", "2021-22": "2022-actual-pwr-0.xlsx", "2020-21": "2021-actual-pwr.xlsx"}
PEERS = {"101912": "Houston ISD", "057905": "Dallas ISD", "227901": "Austin ISD", "220905": "Fort Worth ISD",
         "015915": "Northside ISD", "101907": "Cypress-Fairbanks ISD", "101914": "Katy ISD", "079907": "Fort Bend ISD"}

# canonical key -> header text after the "GF "/"AF " prefix (first occurrence wins)
LINES = [
    ("rev_local_mo", "Local Property Tax from M&O (excluding recapture)"),
    ("rev_state_oper", "State Operating Funds"),
    ("rev_federal", "Federal Funds"),
    ("rev_other_local", "Other Local"),
    ("rev_total_oper", "Total Operating Revenue"),
    ("rev_local_is", "Local Property Tax from I&S"),
    ("rev_state_debt", "State Assistance for Debt Service"),
    ("rev_total_other", "Total Other Revenue"),
    ("recapture_rev", "Local Property Tax Recaptured"),
    ("rev_trs_onbehalf", "Estimated State TRS Contributions"),
    ("rev_debt_fin", "Debt Service Financing Related Revenue"),
    ("exp_payroll_61", "Payroll Expenditures (Object 61xx)"),
    ("exp_contracted_62", "Professional & Contracted Services (Object 62xx)"),
    ("exp_supplies_63", "Supplies & Materials (Object 63xx)"),
    ("exp_otherop_64", "Other Operating Expenditures (Object 64xx)"),
    ("exp_total_oper", "Total Operating Expenditures by Object"),
    ("exp_debt_65", "Debt Services (Object 65xx)"),
    ("exp_capital_66", "Capital Outlay (Object 66xx)"),
    ("exp_grand_total", "Grand Total: Operating and Non-Operating Expenditures by Object"),
    ("f11_instruction", "Instruction (Function 11,95)"),
    ("f12_instr_resources", "Instructional Resources & Media Services (Function 12)"),
    ("f13_curriculum_staffdev", "Curriculum & Staff Development (Function 13)"),
    ("f21_instr_leadership", "Instructional Leadership (Function 21)"),
    ("f23_school_leadership", "School Leadership (Function 23)"),
    ("f31_guidance", "Guidance Counseling Services (Function 31)"),
    ("f32_social_work", "Social Work Services (Function 32)"),
    ("f33_health", "Health Services (Function 33)"),
    ("f34_transportation", "Transportation (Function 34)"),
    ("f35_food", "Food Services (Function 35)"),
    ("f36_extracurricular", "Extracurricular (Function 36)"),
    ("f41_general_admin", "General Administration (Function 41,92)"),
    ("f51_plant_maint", "Facilities Maintenance & Operations (Function 51)"),
    ("f52_security", "Security & Monitoring Services (Function 52)"),
    ("f53_data_processing", "Data Processing Services (Function 53)"),
    ("f61_community", "Community Services (Function 61)"),
    ("pic11_basic", "Basic Educational Services (PIC 11)"),
    ("pic21_gt", "Gifted and Talented (PIC 21)"),
    ("pic22_cte", "Career and Technical (PIC 22)"),
    ("pic23_swd", "Students with Disabilities (PICs 23,33,43)"),
    ("pic24_comp_ed", "State Compensatory Education (PICs 24,26,28,29,30"),   # prefix match (GF/AF differ)
    ("pic25_bilingual", "Bilingual (PICs 25"),                                 # prefix match
    ("pic91_athletics", "Athletics/Related Activities (PIC 91)"),
    ("pic99_unallocated", "Un-Allocated (PIC 99)"),
    ("disb_recapture", "Recapture"),
    ("disb_total", "Total Disbursements"),
]
FB = [("fb_unassigned", "Unassigned Fund Balance"), ("fb_total", "Total Fund Balance")]


def sheet(d, suffix, exclude=("Equity",)):
    for k in d:
        if k.endswith(suffix) and not any(e in k for e in exclude):
            return d[k]
    raise KeyError(suffix)


def colmap(header, prefix, lines):
    out = {}
    for key, txt in lines:
        for i, h in enumerate(header):
            if not isinstance(h, str):
                continue
            h2 = h.replace("\xa0", " ").strip()
            if h2.startswith(prefix + " "):
                body = h2[len(prefix) + 1:]
                if body == txt or (txt.endswith((",30", "25")) and body.startswith(txt)):
                    out[key] = i
                    break
    missing = [k for k, _ in lines if k not in out]
    if missing:
        print("WARN missing", prefix, missing, file=sys.stderr)
    return out


def num(v):
    return float(v) if isinstance(v, (int, float)) else 0.0


def main():
    long_rows = []
    for year, fn in FILES.items():
        d = read_xlsx(os.path.join(SRC, fn))
        enr = sheet(d, "Enroll Act")
        enroll = {r[2]: num(r[6]) for r in enr[1:] if len(r) > 6 and r[2]}
        dtype = {r[2]: r[4] for r in enr[1:] if len(r) > 6 and r[2]}
        tables = {"GF": sheet(d, "GF Act", ("Equity",)), "AF": sheet(d, "AF Act", ("Equity", "GF AF"))}
        eq = sheet(d, "Equity GF AF Act", ())
        # state aggregates
        agg = {"STATE": lambda c: True, "STATE_ISD": lambda c: str(dtype.get(c, "")).upper().startswith("INDEP")}
        for fund, t in tables.items():
            cm = colmap(t[0], fund, LINES)
            rows = {r[2]: r for r in t[1:] if len(r) > 2 and r[2]}
            ents = {c: PEERS[c] for c in PEERS}
            for c, name in ents.items():
                r = rows[c]
                for key, i in cm.items():
                    amt = num(r[i]) if i < len(r) else 0.0
                    long_rows.append([c, name, year, fund, key, round(amt), enroll[c], round(amt / enroll[c], 2)])
            for an, pred in agg.items():
                members = [c for c in rows if pred(c)]
                en = sum(enroll.get(c, 0) for c in members)
                for key, i in cm.items():
                    amt = sum(num(rows[c][i]) for c in members if i < len(rows[c]))
                    long_rows.append([an, "State total (all districts+charters)" if an == "STATE" else "State total (ISDs only)",
                                      year, fund, key, round(amt), en, round(amt / en, 2)])
        # fund balance (GF and AF) from Equity sheet
        hdr = eq[0]
        # NOTE: in the dump the "AF ... Fund Balance" columns hold PER-STUDENT values, not dollars
        # (e.g. Dallas 2024-25 AF Total = 6950), so only the GF dollar columns are used.
        for fund in ("GF",):
            cm = colmap(hdr, fund, FB)
            rows = {r[2]: r for r in eq[1:] if len(r) > 2 and r[2]}
            for c, name in PEERS.items():
                for key, i in cm.items():
                    amt = num(rows[c][i])
                    long_rows.append([c, name, year, fund, key, round(amt), enroll[c], round(amt / enroll[c], 2)])
    os.makedirs(DATA, exist_ok=True)
    with open(f"{DATA}/tea_peims_actuals_long.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cdn", "entity", "school_year", "fund", "line", "amount", "enrolled_membership", "per_student"])
        w.writerows(long_rows)

    idx = {(r[0], r[2], r[3], r[4]): r for r in long_rows}
    keys = [k for k, _ in LINES] + [k for k, _ in FB]
    ents = list(PEERS) + ["STATE", "STATE_ISD"]
    names = {**PEERS, "STATE": "State (all LEAs)", "STATE_ISD": "State (ISDs only)"}

    # peer comparison, latest year, per student
    with open(f"{DATA}/peer_comparison.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["school_year", "fund", "line"] + [names[e] for e in ents])
        for yr in ("2024-25", "2023-24"):
            w.writerow([yr, "", "enrolled_membership"] + [int(idx[(e, yr, "AF", "rev_local_mo")][6]) for e in ents])
            for fund in ("AF", "GF"):
                for k in keys:
                    vals = [idx.get((e, yr, fund, k)) for e in ents]
                    if all(v is None for v in vals):
                        continue
                    w.writerow([yr, fund, k + "_per_student"] + ["" if v is None else round(v[7]) for v in vals])
        # derived ratios
        yr = "2024-25"
        for fund in ("AF", "GF"):
            def g(e, k):
                v = idx.get((e, yr, fund, k)); return v[5] if v else 0
            w.writerow([yr, fund, "instruction_share_of_oper_exp_pct"] + [round(100 * g(e, "f11_instruction") / g(e, "exp_total_oper"), 2) for e in ents])
            w.writerow([yr, fund, "school_leadership_share_pct"] + [round(100 * g(e, "f23_school_leadership") / g(e, "exp_total_oper"), 2) for e in ents])
            w.writerow([yr, fund, "general_admin_share_pct"] + [round(100 * g(e, "f41_general_admin") / g(e, "exp_total_oper"), 2) for e in ents])
            w.writerow([yr, fund, "contracted_services_share_pct"] + [round(100 * g(e, "exp_contracted_62") / g(e, "exp_total_oper"), 2) for e in ents])
            # Proxy of FIRST admin cost ratio: (F21 + F41) / (F11 + F12 + F13 + F31). PROXY ONLY: TEA's official
            # ratio uses specific fund groups / function 41 excluding 92 (see notes); this uses PWR totals.
            w.writerow([yr, fund, "admin_cost_ratio_PROXY_(21+41)/(11+12+13+31)"] + [
                round((g(e, "f21_instr_leadership") + g(e, "f41_general_admin")) /
                      (g(e, "f11_instruction") + g(e, "f12_instr_resources") + g(e, "f13_curriculum_staffdev") + g(e, "f31_guidance")), 4)
                for e in ents])
            w.writerow([yr, fund, "state_oper_share_of_oper_rev_pct"] + [round(100 * g(e, "rev_state_oper") / g(e, "rev_total_oper"), 2) for e in ents])
            w.writerow([yr, fund, "local_mo_share_of_oper_rev_pct"] + [round(100 * g(e, "rev_local_mo") / g(e, "rev_total_oper"), 2) for e in ents])
            w.writerow([yr, fund, "federal_share_of_oper_rev_pct"] + [round(100 * g(e, "rev_federal") / g(e, "rev_total_oper"), 2) for e in ents])

    # HISD trend
    yrs = list(FILES)[::-1]
    with open(f"{DATA}/hisd_peims_trend.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["fund", "line", "measure"] + yrs)
        w.writerow(["", "enrolled_membership", "count"] + [int(idx[("101912", y, "AF", "rev_local_mo")][6]) for y in yrs])
        for fund in ("AF", "GF"):
            for k in keys:
                if not all(idx.get(("101912", y, fund, k)) for y in yrs):
                    continue
                w.writerow([fund, k, "amount"] + [idx[("101912", y, fund, k)][5] for y in yrs])
                w.writerow([fund, k, "per_student"] + [round(idx[("101912", y, fund, k)][7]) for y in yrs])
                w.writerow([fund, k, "state_per_student"] + [round(idx[("STATE", y, fund, k)][7]) if idx.get(("STATE", y, fund, k)) else "" for y in yrs])
    print("rows", len(long_rows))


if __name__ == "__main__":
    main()
