"""HISD General Fund, FY2019-FY2027, every figure labeled with its basis (audited, adopted budget, amended budget,
HISD forecast). Audited figures are used wherever they exist; budgets fill FY2026 and FY2027, which have no audit yet.

Inputs:  data/hisd_history_gf_fy2019_2025.csv (audited; built from the ACFRs, see notes/acfr.md)
         data/tea_peims_budget_long.csv       (parse_tea_budget_reports.py; TEA enrollment count for 2025-26)
         figures below, copied from HISD's budget documents (cited per row; see notes/budget.md)
Outputs: data/hisd_gf_fy2019_2027_by_basis.csv   one row per fiscal year and basis
         data/hisd_gf_function_fy2019_2027.csv   General Fund spending by function: audited FY2019-FY2025,
                                                 amended budget FY2026, adopted budget FY2027
Checks (exit non-zero on failure): for every budget row, revenue - appropriations + other sources = net change,
and beginning + net change = ending fund balance; function lines sum to the stated totals.
"""
import csv, sys
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
D = ROOT + "/data"

# ---- HISD budget documents (abbreviations as in notes/budget.md) ----------------------------------------------
# fy: (revenue, appropriations, other sources net, net change, beginning FB, ending FB, recapture, source)
ADOPTED = {
    "FY2019": (1977345003, 1996983851, -15961773, -35600621, 612678670, 577078049, 272407268, "B19 p24 (adopted Jun 28 2018)"),
    "FY2020": (1903085694, 1923742406, -2544977, -23201689, 582138621, 558936932, 0, "S20 (adopted Jun 27 2019)"),
    "FY2021": (1972054361, 1991093833, -14949140, -33988612, 878463630, 844475018, 12083891, "S21 (adopted Jun 11 2020)"),
    "FY2022": (2081127566, 2186550176, 23346295, -82076315, 769293013, 687216698, 213265281, "S22 (adopted Jun 2021)"),
    # FY2023/FY2024 beginning balances include $70.0M of 'anticipated unspent' appropriations (S23, S24)
    "FY2023": (2163294662, 2267677919, 3613800, -100769457, 852224713 + 70000000, 821455256, 247439733, "S23 (adopted Jun 9 2022)"),
    "FY2024": (2194824843, 2377150619, 13786350, -168539426, 1120551047 + 70000000, 1022011621, 326539245, "S24 (adopted Jun 22 2023)"),
    "FY2025": (1888577811, 2100290919, 80594726, -131118382, 932687809, 801569427, 0, "S25 (adopted Jun 13 2024)"),
    "FY2026": (2082033202, 2121893114, 25176073, -14683839, 799864486, 785180647, 0, "S26 (adopted Jun 12 2025)"),
    "FY2027": (1990447057, 2015007011, 23769073, -790881, 730042378, 729251497, 0, "S27 (adopted Jun 25 2026)"),
}
# Last amendment of the year. FY2019-FY2024: ACFR RSI final-budget column (revenue not carried in the notes).
AMENDED = {
    "FY2019": (None, 2167653402, None, -86736798, None, None, 274.8e6, "FY19 ACFR RSI p.106"),
    "FY2020": (None, 2051838084, None, -89739826, None, None, 75.4e6, "FY20 ACFR RSI p.101"),
    "FY2021": (None, 2330879400, None, -206965474, None, None, 136.6e6, "FY21 ACFR RSI p.92"),
    "FY2022": (None, 2209721030, None, -144400998, None, None, 178.8e6, "FY22 ACFR RSI p.91"),
    "FY2023": (None, 2359123684, None, -164930325, None, None, 283.8e6, "FY23 ACFR RSI p.95"),
    "FY2024": (None, 2227255442, None, -194381109, None, None, 0, "FY24 ACFR RSI p.91"),
    "FY2025": (1906604750, 2176231690, 22294726, -247332214, 1047196700, 799864486, 44468370, "A25-Jun (Jun 12 2025)"),
    "FY2026": (2053847057, 2109408270, 37515277, -18045936, 748088314, 730042378, 0, "A26-2 (Jun 11 2026)"),
}
# HISD's own in-year forecasts of the ending fund balance
FORECAST = {
    "FY2026": [("Apr 2026", 751966507, "WS-Apr26 slide 36 (actuals to Mar 31 2026; equals the Feb 2026 amended budget)"),
               ("May 2026", 730042378, "WS-May26 slide 14 'Forecasted FY 2026 Fund Balance' (= A26-2)")],
}
# Revenue by source in budgets: (local, state, federal)
BUDGET_SOURCES = {
    "FY2026 amended": (1654861362, 377325695, 21660000, "A26-2"),
    "FY2026 adopted": (1645873202, 414500000, 21660000, "S26"),
    "FY2027 adopted": (1604861362, 364725695, 20860000, "S27"),
}
ENROLL_PROJ_FY2027 = (164812, "HISD projection (WS-May26 slide 8)")

# GF appropriations by TEA function, budgets (A26-2 for FY2026, S27 for FY2027). The A26-2 function lines sum to
# $2,109,408,271, $1 more than the amendment's stated total of $2,109,408,270 (source rounding); the checks allow $1,
# and every summary figure uses the stated total.
FN_BUDGET = {
    "FY2026": {"11": 1242265908, "12": 5184480, "13": 12713049, "21": 77074342, "23": 217307577, "31": 58785248,
               "32": 2228592, "33": 23173706, "34": 52799353, "35": 181891, "36": 23611966, "41": 51702667,
               "51": 181175146, "52": 33419485, "53": 42125123, "61": 5692561, "71": 1020000, "81": 3993633,
               "91": 0, "95": 792000, "97": 54247082, "99": 19914462},
    "FY2027": {"11": 1148040067, "12": 5059621, "13": 10669615, "21": 79557300, "23": 215400326, "31": 56597969,
               "32": 2546968, "33": 24494267, "34": 50424755, "35": 68900, "36": 22567751, "41": 52226155,
               "51": 196948263, "52": 35579566, "53": 42549020, "61": 6839219, "71": 0, "81": 33011,
               "91": 0, "95": 792000, "97": 44698594, "99": 19913644},
}
# Audited GF expenditures by function (ACFR; notes/acfr.md H4 and 2d), in the ACFR's own line order
FN_ACTUAL = {  # instr, media, staffdev, instrlead, schoollead, guid, socwork, health, transp, food, extra, genadm, plant, security, dp, community, jjaep, tirz, appraisal, recapture, debt, capital
    "FY2019": [970793048, 9822477, 29267000, 20820355, 142326291, 50299761, 8429482, 19312797, 59243844, 0, 15549148, 41097974, 195853168, 22606971, 54951868, 2135207, 792000, 58465450, 14990752, 265231840, 8946862, 269834],
    "FY2020": [996399361, 7798643, 29215532, 20983417, 149489190, 60053228, 12142590, 21317891, 53629143, 234114, 16107773, 32135554, 192496074, 24179218, 62025501, 3828274, 792000, 61321789, 14980471, 80843995, 14995323, 8635291],
    "FY2021": [1081410519, 9071254, 33204034, 23904023, 146408036, 63467347, 16938834, 48100766, 46389028, 2741097, 14536297, 32663797, 211943777, 27507090, 65812348, 2631134, 792000, 61491720, 15517042, 197810414, 14818736, 1340201],
    "FY2022": [980058268, 6732685, 31637515, 24155192, 146733334, 59348406, 17955510, 31234756, 51909647, 50603, 16464559, 37490457, 218863332, 30024646, 58213621, 1948276, 724500, 65956709, 15553451, 184470759, 10250591, 3080548],
    "FY2023": [1037292731, 18410029, 29076351, 22530676, 162215725, 65086596, 8351000, 26671528, 52317948, 86050, 21005560, 41114014, 227609507, 31396069, 51198314, 1909451, 579600, 72368633, 15767806, 276396220, 12901379, 715613],
    "FY2024": [1150954093, 13830385, 25815707, 63063461, 215392395, 64717439, 4712785, 24201089, 57023753, 71239, 25280790, 53050919, 235307348, 32091167, 58440335, 7050496, 583200, 75544048, 16453702, 0, 18998183, 6632145],
    "FY2025": [1261908377, 6952956, 14265492, 68430832, 234320097, 67564581, 8418802, 26031897, 52179127, 118309, 25759045, 51233688, 215104150, 30520778, 44249043, 5148816, 583200, 56066884, 14172784, 56900029, 10163192, 872408],
}
# Audited GF revenue by source (ACFR; notes/acfr.md H3 and 2c): property tax, investment earnings, misc. local, state, federal
SRC_ACTUAL = {
    "FY2019": (1747189582, 19083204, 15082252, 399872504, 19372818),
    "FY2020": (1715002326, 14027724, 9972928, 218933263, 23877840),
    "FY2021": (1801428452, 2342077, 12241775, 295665220, 27712808),
    "FY2022": (1794873129, 3341346, 19373978, 228667029, 61236580),
    "FY2023": (1809366483, 50872795, 9603175, 214953566, 69955765),
    "FY2024": (1506848009, 72775580, 5347301, 319532249, 78105613),
    "FY2025": (1523111132, 52185094, 67369842, 272139946, 25580042),
}
ACT_KEYS = ["11", "12", "13", "21", "23", "31", "32", "33", "34", "35", "36", "41", "51", "52", "53", "61", "95", "97", "99", "91", "71", "81"]
ROWS = [  # (label, function codes)
    ("Instruction", ["11"]), ("School leadership", ["23"]), ("Instructional leadership", ["21"]),
    ("Plant maintenance & operations", ["51"]), ("Guidance & counseling", ["31"]), ("Transportation", ["34"]),
    ("General administration", ["41"]), ("Data processing", ["53"]), ("Security", ["52"]), ("Health", ["33"]),
    ("Extracurricular", ["36"]), ("Instructional staff development", ["13"]), ("Recapture (payments to the state)", ["91"]),
    ("Payments into city tax-increment zones (TIRZ)", ["97"]),
    ("Other (social work, media, food service, community services, appraisal fees, debt, capital, juvenile justice AEP)",
     ["32", "12", "35", "61", "99", "71", "81", "95"]),
]


def main():
    ok = True

    def check(name, a, b, tol=1):
        nonlocal ok
        good = abs(a - b) <= tol
        ok &= good
        if not good:
            print(f"MISMATCH {name}: {a:,} vs {b:,}")

    aud = {r["fy"]: r for r in csv.DictReader(open(f"{D}/hisd_history_gf_fy2019_2025.csv"))}
    bud = list(csv.DictReader(open(f"{D}/tea_peims_budget_long.csv")))
    tea_mem = {r["school_year"]: int(r["enrolled_membership"]) for r in bud if r["cdn"] == "101912"}

    out = []
    prev_fb = 612678670   # audited GF fund balance 6/30/2018 (FY25 ACFR p.128)
    for fy in [f"FY{y}" for y in range(2019, 2028)]:
        sy = f"{int(fy[2:]) - 1}-{fy[4:]}"
        mem_tea = tea_mem.get(sy)
        if fy in aud:
            a = aud[fy]
            rev, exp, fb = int(a["gf_revenue"]), int(a["gf_expenditures"]), int(a["gf_fund_balance_end"])
            rec = int(a["recapture_expense"])
            out.append({"fy": fy, "basis": "audited", "label": "Audited (ACFR)", "revenue": rev, "expenditures": exp,
                        "rev_minus_exp": rev - exp, "other_sources_net": fb - prev_fb - (rev - exp),
                        "net_change_fb": fb - prev_fb, "fb_begin": prev_fb, "fb_end": fb, "recapture": rec,
                        "enrollment": int(a["enrollment"]), "enrollment_basis": "HISD enrollment (ACFR statistical section)",
                        "exp_per_student_excl_recapture": round((exp - rec) / int(a["enrollment"])),
                        "source": a["source_note"]})
            prev_fb = fb
        for basis, label, tbl in (("final amended budget", "Final amended budget", AMENDED), ("adopted budget", "Adopted budget", ADOPTED)):
            if fy not in tbl:
                continue
            rev, exp, oth, net, beg, end, rec, src = tbl[fy]
            if rev is not None:
                check(f"{fy} {basis}: rev - exp + other = net change", rev - exp + oth, net)
                check(f"{fy} {basis}: begin + net = end", beg + net, end)
            if fy == "FY2027":
                mem, mb = ENROLL_PROJ_FY2027
            elif fy == "FY2026":
                mem, mb = mem_tea, "TEA enrolled membership, fall 2025 (TEA budget report 2025-26)"
            else:
                mem, mb = None, ""
            out.append({"fy": fy, "basis": basis, "label": label, "revenue": rev, "expenditures": exp,
                        "rev_minus_exp": (rev - exp) if rev is not None else None, "other_sources_net": oth,
                        "net_change_fb": net, "fb_begin": beg, "fb_end": end, "recapture": rec, "enrollment": mem,
                        "enrollment_basis": mb,
                        "exp_per_student_excl_recapture": round((exp - rec) / mem) if mem else None, "source": src})
        for when, fb, src in FORECAST.get(fy, []):
            out.append({"fy": fy, "basis": "HISD forecast", "label": f"HISD forecast ({when})", "fb_end": fb, "source": src})
    keys = ["fy", "basis", "label", "revenue", "expenditures", "rev_minus_exp", "other_sources_net", "net_change_fb",
            "fb_begin", "fb_end", "recapture", "enrollment", "enrollment_basis", "exp_per_student_excl_recapture", "source"]
    with open(f"{D}/hisd_gf_fy2019_2027_by_basis.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader()
        for r in out:
            w.writerow({k: r.get(k, "") if r.get(k) is not None else "" for k in keys})

    # ---- functions --------------------------------------------------------------------------------------------
    fn = {}
    for fy, vals in FN_ACTUAL.items():
        d = dict(zip(ACT_KEYS, vals))
        check(f"{fy} audited functions sum to total", sum(vals), int(aud[fy]["gf_expenditures"]))
        fn[fy] = ("audited", d)
    for fy, d in FN_BUDGET.items():
        tot = ADOPTED["FY2027"][1] if fy == "FY2027" else AMENDED["FY2026"][1]
        check(f"{fy} budget functions sum to total", sum(d.values()), tot)
        fn[fy] = ("final amended budget (A26-2)" if fy == "FY2026" else "adopted budget (S27)", d)
    with open(f"{D}/hisd_gf_function_fy2019_2027.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["line", "functions"] + [f"{fy} ({fn[fy][0]})" for fy in fn])
        for lab, codes in ROWS + [("Total General Fund", None)]:
            w.writerow([lab, "+".join(codes) if codes else "all"] +
                       [sum(v for k, v in fn[fy][1].items() if codes is None or k in codes) for fy in fn])

    # ---- revenue by source ---------------------------------------------------------------------------------------
    srcs = {}
    for fy, (pt, inv, misc, st, fed) in SRC_ACTUAL.items():
        check(f"{fy} audited revenue sources sum to total", pt + inv + misc + st + fed, int(aud[fy]["gf_revenue"]))
        srcs[fy] = ("audited", pt + inv + misc, st, fed)
    for key, fy, basis in (("FY2026 amended", "FY2026", "final amended budget (A26-2)"), ("FY2027 adopted", "FY2027", "adopted budget (S27)")):
        loc, st, fed, _ = BUDGET_SOURCES[key]
        tot = AMENDED[fy][0] if fy == "FY2026" else ADOPTED[fy][0]
        check(f"{key} revenue sources sum to total", loc + st + fed, tot)
        srcs[fy] = (basis, loc, st, fed)
    with open(f"{D}/hisd_gf_revenue_source_fy2019_2027.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["fy", "basis", "local", "state", "federal", "total"])
        for fy, (basis, loc, st, fed) in srcs.items():
            w.writerow([fy, basis, loc, st, fed, loc + st + fed])

    # ---- print markdown for the report pages -------------------------------------------------------------------
    M = lambda x: "" if x in (None, "") else (f"−${abs(x) / 1e6:,.1f}M" if x < 0 else f"${x / 1e6:,.1f}M")
    print("\nGF revenue by source (FY2019-FY2027):")
    for i, lab in ((1, "Local (mostly property tax)"), (2, "State"), (3, "Federal")):
        print("| " + lab + " | " + " | ".join(M(v[i]) for v in srcs.values()) + " |")
    print("| **Total** | " + " | ".join(f"**{M(v[1] + v[2] + v[3])}**" for v in srcs.values()) + " |")
    print("| Mix (local / state / federal) | " + " | ".join(
        " / ".join(f"{100 * x / (v[1] + v[2] + v[3]):.0f}" for x in v[1:]) + " %" for v in srcs.values()) + " |")
    print("\nFunction table (FY2023-FY2027):")
    yrs = ["FY2023", "FY2024", "FY2025", "FY2026", "FY2027"]
    for lab, codes in ROWS + [("**Total General Fund**", None)]:
        print("| " + lab + " | " + " | ".join(M(sum(v for k, v in fn[fy][1].items() if codes is None or k in codes)) for fy in yrs) + " |")
    mem = {"FY2023": int(aud["FY2023"]["enrollment"]), "FY2024": int(aud["FY2024"]["enrollment"]),
           "FY2025": int(aud["FY2025"]["enrollment"]), "FY2026": tea_mem["2025-26"], "FY2027": ENROLL_PROJ_FY2027[0]}
    print("| Excluding recapture and TIRZ, per enrolled student | " + " | ".join(
        f"${(sum(fn[fy][1].values()) - fn[fy][1]['91'] - fn[fy][1]['97']) / mem[fy]:,.0f}" for fy in yrs) + " |")
    print("\nBy basis:")
    for r in out:
        print(r["fy"], r["label"].ljust(28), *(f"{k}={M(r.get(k))}" for k in ("revenue", "expenditures", "rev_minus_exp",
              "other_sources_net", "net_change_fb", "fb_end")), r.get("enrollment"), r.get("exp_per_student_excl_recapture"))
    print("checks:", "all OK" if ok else "FAILED")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
