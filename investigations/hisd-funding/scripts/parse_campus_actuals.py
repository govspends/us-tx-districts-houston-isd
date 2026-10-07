"""Parse TEA 'PEIMS Actual Financial Data, Organized by Campus' PDFs (pdftotext -layout output)
for HISD into data/hisd_campus_actuals.csv.

Input: sources/tea_peims/campus/allcamp_actual_{2023,2024,2025}_101912.txt
       (TEA program sfadhoc.allcamp_actual_report_YYYY.sas, YYYY = spring year of the school year)
Each campus spans 2 pages; lines look like:
  'Instruction (11,95)          *     2,100,281     66.78         10,397             2,334,494    64.81            11,557'
-> GF amount, GF %, GF per student, AF amount, AF %, AF per student.
"""
import csv, re, sys

SRC = "/git/Texas/HISD/sources/tea_peims/campus/allcamp_actual_{}_101912.txt"
OUT = "/git/Texas/HISD/data/hisd_campus_actuals.csv"
YEARS = {"2023": "2022-23", "2024": "2023-24", "2025": "2024-25"}
NUM = r"(-?[\d,]+(?:\.\d+)?)"
LINE_RE = re.compile(r"^\s*(.+?)\s+\**\s*" + r"\s+".join([NUM] * 6) + r"\s*$")

LABELS = {  # pdf label (normalized: no spaces) -> column key
    "TotalExpenditures": "total_exp_6100_6600",
    "Operating-Payroll": "payroll",
    "OtherOperating": "other_operating",
    "Non-Operating(Equipt/Supplies)": "non_operating",
    "TotalOperatingExpenditures": "total_oper_exp",
    "Instruction(11,95)": "f11_instruction",
    "InstructionalRes/Media(12)": "f12_instr_resources",
    "Curriculum/StaffDevelop(13)": "f13_curriculum",
    "InstructionalLeadership(21)": "f21_instr_leadership",
    "SchoolLeadership(23)": "f23_school_leadership",
    "Guidance/CounselingSvcs(31)": "f31_guidance",
    "SocialWorkServices(32)": "f32_social_work",
    "HealthServices(33)": "f33_health",
    "Transportation(34)": "f34_transportation",
    "Food(35)": "f35_food",
    "Extracurricular(36)": "f36_extracurricular",
    "PlantMaint/Operation(51)": "f51_plant",
    "Security/Monitoring(52)": "f52_security",
    "DataProcessingSvcs(53)": "f53_data_processing",
    "Regular": "pic_regular",
    "Gifted&Talented": "pic_gt",
    "Career&Technical": "pic_cte",
    "StudentswithDisabilities": "pic_swd",
    "StateCompensatoryED": "pic_comp_ed",
    "Bilingual": "pic_bilingual",
    "EarlyEducationAllotment": "pic_early_ed",
    "DyslexiaorRelatedDisorderServ": "pic_dyslexia",
    "CCMR": "pic_ccmr",
    "AthleticProgramming": "pic_athletics",
    "Un-Allocated": "pic_unallocated",
}


def f(x):
    return float(x.replace(",", ""))


def main():
    rows = []
    for yy, sy in YEARS.items():
        cur = None
        seen_total_oper = 0
        for line in open(SRC.format(yy), encoding="utf-8", errors="replace"):
            m = re.search(r"School Campus:(.+?)\s*District:", line)
            if m:
                name = m.group(1).strip()
                continue
            m = re.search(r"Campus Number:(\d{9})\s+Total Membership:\s*([\d,]+)", line)
            if m:
                if cur is None or cur["campus_id"] != m.group(1):
                    cur = {"school_year": sy, "campus_id": m.group(1), "campus_name": name,
                           "membership": int(m.group(2).replace(",", ""))}
                    rows.append(cur)
                    seen_total_oper = 0
                continue
            m = LINE_RE.match(line)
            if m and cur is not None:
                lab = re.sub(r"\s+", "", m.group(1)).rstrip("*")
                key = LABELS.get(lab)
                if key == "total_oper_exp":
                    seen_total_oper += 1
                    if seen_total_oper > 1:   # repeated at top of program section
                        continue
                if key:
                    cur[key + "_gf"] = f(m.group(2)); cur[key + "_gf_ps"] = f(m.group(4))
                    cur[key + "_af"] = f(m.group(5)); cur[key + "_af_ps"] = f(m.group(7))
    keys = ["school_year", "campus_id", "campus_name", "membership"]
    for k in LABELS.values():
        keys += [k + s for s in ("_gf", "_gf_ps", "_af", "_af_ps")]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in keys})
    by = {}
    for r in rows:
        by.setdefault(r["school_year"], []).append(r)
    for sy, rs in by.items():
        miss = [r["campus_id"] for r in rs if "total_oper_exp_af" not in r]
        print(sy, "campuses", len(rs), "membership", sum(r["membership"] for r in rs),
              "AF oper exp", round(sum(r.get("total_oper_exp_af", 0) for r in rs)), "missing", miss[:5], file=sys.stderr)


if __name__ == "__main__":
    main()
