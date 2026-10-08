"""TAPR staff + student profile for HISD, peers and state, from TEA TAPR data-download CSVs.

Inputs: sources/tea_peims/tapr/tapr{2025,2024}_all_d_{STAF,STUD}.csv (+ tapr{YYYY}_all_s_STAF.csv state)
  (TPRS data download: perfrept.perfmast.sas, tapr=all_d / all_s, dsname=STAF / STUD, csv).
  Row 1 = long labels, row 2 = variable codes (DPxxxxx district, SPxxxxx state). TAPR 2025 = SY 2024-25.
Also (history extension 2026-10-07): sources/tea_peims/tapr/tapr{2023,2022,2021,2020,2019}_{D,S}PROF.csv
  = old per-year TAPR "Profile" data download (scripts/fetch_tapr_dd.py); row 1 = variable codes only.
  TAPR 2023 = SY 2022-23 ... TAPR 2019 = SY 2018-19. Rows for these years are appended after the
  2024-25/2023-24 rows; state rows for these years also carry student counts/percentages.
  2018-19/2019-20 files have no 21-30 / 30+ year salary bands (ST21SA/ST30SA): left blank.
  STETLEPC = "English Learners (EL)" (2019-20) / "EB Students/EL" (2021+), same variable.
Output: data/tapr_staff_peer_comparison.csv
"""
import csv, os
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # the investigation folder

SRC = ROOT + "/sources/tea_peims/tapr"
OUT = ROOT + "/data/tapr_staff_peer_comparison.csv"
PEERS = {"101912": "Houston ISD", "057905": "Dallas ISD", "227901": "Austin ISD", "220905": "Fort Worth ISD",
         "015915": "Northside ISD", "101907": "Cypress-Fairbanks ISD", "101914": "Katy ISD", "079907": "Fort Bend ISD"}
STAF = [("teachers_fte", "STTOFC"), ("prof_support_fte", "SUTOFC"), ("campus_admin_fte", "SSTOFC"),
        ("central_admin_fte", "SCTOFC"), ("aides_fte", "SETOFC"), ("auxiliary_fte", "SXTOFC"),
        ("professional_fte", "SPTOFC"), ("all_staff_fte", "SATOFC"), ("contracted_instr_fte", "SOTOFC"),
        ("students_per_teacher", "STKIDR"), ("teacher_avg_salary", "STTOSA"), ("prof_support_avg_salary", "SUTOSA"),
        ("campus_admin_avg_salary", "SSTOSA"), ("central_admin_avg_salary", "SCTOSA"),
        ("beginning_teacher_avg_salary", "ST00SA"), ("teacher_1_5yr_avg_salary", "ST01SA"),
        ("teacher_6_10yr_avg_salary", "ST06SA"), ("teacher_11_20yr_avg_salary", "ST11SA"),
        ("teacher_21_30yr_avg_salary", "ST21SA"), ("teacher_30plus_avg_salary", "ST30SA"),
        ("teacher_avg_years_exp", "STEXPA"), ("teacher_avg_years_with_district", "STTENA"),
        ("principal_avg_years_exp", "SHEXPA"), ("teacher_turnover_rate", "STURNR"),
        ("beginning_teacher_pct", "ST00FP"), ("teacher_no_degree_pct", "STNOFP")]
STUD = [("membership", "ETALLC"), ("econ_disadv", "ETECOC"), ("emergent_bilingual", "ETLEPC"),
        ("special_ed", "ETSPEC"), ("at_risk", "ETRSKC")]


def load(path):
    rows = list(csv.reader(open(path, encoding="latin-1")))
    codes = rows[1]
    return codes, rows[2:]


def load_prof(path):
    rows = list(csv.reader(open(path, encoding="latin-1")))
    return rows[0], rows[1:]


def derive(rec):
    m = rec["membership"]
    for k in ("econ_disadv", "emergent_bilingual", "special_ed", "at_risk"):
        rec[k + "_pct"] = round(100 * rec[k] / m, 1) if isinstance(rec[k], float) and m else ""
    for k in ("central_admin_fte", "campus_admin_fte", "prof_support_fte", "teachers_fte", "all_staff_fte"):
        rec[k + "_per_1000_students"] = round(1000 * rec[k] / m, 2) if isinstance(rec[k], float) and m else ""


def val(codes, row, suffix, prefix):
    code = prefix + suffix
    if code not in codes:
        return ""
    v = row[codes.index(code)].strip()
    try:
        return float(v)
    except ValueError:
        return v


def main():
    out = []
    for yr, sy in (("2025", "2024-25"), ("2024", "2023-24")):
        sc, srows = load(f"{SRC}/tapr{yr}_all_d_STAF.csv")
        uc, urows = load(f"{SRC}/tapr{yr}_all_d_STUD.csv")
        sidx = {r[0].strip().lstrip("'"): r for r in srows}
        uidx = {r[0].strip().lstrip("'"): r for r in urows}
        st_path = f"{SRC}/tapr{yr}_all_s_STAF.csv"
        state = load(st_path) if os.path.exists(st_path) else None
        for cdn, name in PEERS.items():
            rec = {"school_year": sy, "cdn": cdn, "entity": name}
            for k, s in STAF:
                rec[k] = val(sc, sidx[cdn], s, "DP")
            for k, s in STUD:
                rec[k] = val(uc, uidx[cdn], s, "DP")
            derive(rec)
            out.append(rec)
        if state:
            codes, rows = state
            rec = {"school_year": sy, "cdn": "STATE", "entity": "State"}
            for k, s in STAF:
                rec[k] = val(codes, rows[0], s, "SP")
            out.append(rec)
    for yr, sy in (("2023", "2022-23"), ("2022", "2021-22"), ("2021", "2020-21"), ("2020", "2019-20"), ("2019", "2018-19")):
        dc, drows = load_prof(f"{SRC}/tapr{yr}_DPROF.csv")
        didx = {r[dc.index("DISTRICT")].strip().lstrip("'"): r for r in drows}
        for cdn, name in PEERS.items():
            rec = {"school_year": sy, "cdn": cdn, "entity": name}
            for k, s_ in STAF + STUD:
                rec[k] = val(dc, didx[cdn], s_, "DP")
            derive(rec)
            out.append(rec)
        sc, srows = load_prof(f"{SRC}/tapr{yr}_SPROF.csv")
        rec = {"school_year": sy, "cdn": "STATE", "entity": "State"}
        for k, s_ in STAF + STUD:
            rec[k] = val(sc, srows[0], s_, "SP")
        derive(rec)
        out.append(rec)
    cols = []
    for r in out:
        for k in r:
            if k not in cols:
                cols.append(k)
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
    print("wrote", OUT, len(out))


if __name__ == "__main__":
    main()
