# HISD (101912) — TEA / State of Texas data: actual spending, staffing, FIRST, peers

Retrieved 2026-10-06. Every figure below is from a PRIMARY TEA or Comptroller file in
`sources/tea_peims/` (see `sources/tea_peims/SOURCES.md`); computed tables are in `data/`, built by the
scripts in `scripts/` (stdlib Python only; `xlsx_lite.py` replaces openpyxl, which is not installed).

Reproduce:
```
python3 scripts/build_peer_comparison.py   # -> data/peer_comparison.csv, hisd_peims_trend.csv, tea_peims_actuals_long.csv
python3 scripts/build_tapr_peers.py        # -> data/tapr_staff_peer_comparison.csv
python3 scripts/fetch_first.py             # -> data/first_ratings.csv (re-uses saved pages)
python3 scripts/parse_campus_actuals.py    # -> data/hisd_campus_actuals.csv
python3 scripts/analyze_campus_nes.py      # -> data/hisd_campus_nes_summary.csv (needs data/hisd_nes_campuses.csv)
```

**Definitions that matter.** TEA's PEIMS "PWR" reports divide by *Total Enrolled Membership* (HISD 2024-25:
176,039), not ADA/WADA, so these per-student numbers are not comparable to the FSP per-ADA figures in
`data/hisd_sof_trend.md`. "AF" = all funds (general + special revenue + debt service + capital projects + food
service); "GF" = general fund. "Operating" = objects 61xx-64xx (excludes debt service 65xx and capital 66xx).
PEIMS data is the district's own coding submitted to TEA; FIRST indicator 16 checks it against the audited AFR
within 3% (HISD passed in all five rating years checked). My script reproduces TEA's own PWR per-student numbers exactly
(e.g. HISD 2024-25 AF operating revenue $12,666, GF instruction $7,092; state AF operating expenditure $12,951).

---

## 1. HISD actual revenue and spending, 2020-21 → 2024-25 (PEIMS actuals)

Source: `data/hisd_peims_trend.csv` (from the five statewide xlsx dumps); spot-checked against
`sources/tea_peims/pwr/pwr_actual_{2023,2024,2025}_101912.txt` (TEA PWR PDFs).

| HISD | 2020-21 | 2021-22 | 2022-23 | 2023-24 | 2024-25 |
|---|---|---|---|---|---|
| Enrolled membership | 196,550 | 193,727 | 189,290 | 183,603 | 176,039 |
| **AF operating revenue / student** | 11,262 | 13,087 | 13,764 | 14,452 | **12,666** |
| — local M&O tax (excl. recapture) | 8,159 | 8,313 | 8,099 | 8,207 | 8,329 |
| — state operating | 1,171 | 836 | 767 | 1,399 | 1,221 |
| — federal | 1,735 | 3,609 | 4,313 | 4,247 | 2,275 |
| — other local | 196 | 329 | 587 | 599 | 842 |
| Recapture paid (PEIMS, $M) | 197.8 | 184.5 | 276.4 | **0** | 56.9 |
| **AF operating expenditure / student** | 10,524 | 11,772 | 12,998 | 14,337 | **14,147** |
| AF total expenditure incl. debt+capital / student | 13,516 | 14,985 | 16,350 | 18,150 | 17,026 |
| **GF operating expenditure / student** | 9,037 | 8,511 | 9,254 | 10,629 | **11,825** |
| GF payroll (61xx), $M | 1,425.9 | 1,311.1 | 1,418.2 | 1,664.5 | 1,741.7 |
| AF federal revenue, $M | 341.0 | 699.1 | 816.3 | 779.8 | 400.5 |
| GF total fund balance (end of year), $M | 996.6 | 1,126.9 | 1,127.1 | 1,047.2 | **not reported (shows $0)** |

Key observations:

- **Federal (ESSER) cliff, and payroll shifted onto the general fund.** All-funds federal revenue fell from
  $816.3M (2022-23, `pwr_actual_2023_101912.txt` line 14) to $400.5M (2024-25, `pwr_actual_2025_101912.txt`
  line 14). Over the same two years GF payroll rose from $1,418.2M (2023 txt line 54) to $1,741.7M (2025 txt
  line 54) while enrollment fell 7.0%: GF payroll per student $7,492 → $9,894 (+32%). Total all-funds operating
  spending per student stayed roughly flat ($14,337 → $14,147), so the general fund absorbed costs previously
  carried by federal relief money.
- **The general fund is running deficits.** 2023-24 GF "Excess (Deficiency) Operating Expenditures" =
  **−$166.6M** (`pwr_actual_2024_101912.txt` line 198; 2022-23 was −$20.2M, 2023 txt line 197). In 2024-25 GF
  grand-total revenue (operating + other + TRS on-behalf, excluding recapture) was $1,911.2M (2025 txt line 35)
  against GF total disbursements of $2,267.2M (2025 txt line 162) — a ~$356M gap (simple difference; the
  official fund-balance reconciliation is missing for 2024-25, see below).
- **HISD's 2024-25 fund balance is missing from PEIMS.** The 2024-25 PWR shows GF and AF fund balance = $0, with
  an "Uncommon Items" line of −$1,047,196,700 that zeroes out the prior-year balance (2025 txt lines 194-203).
  That is a data gap at TEA, not a real $0 balance; use the ACFR (other agent) for the June-30-2025 balance.
  Also note the 2022-23 and 2023-24 GF *unassigned* balances are identical to the dollar ($590,067,862; 2023 txt
  line 193, 2024 txt line 194) — likely a reporting carry-forward; treat with caution.
- **Recapture in PEIMS ≠ SOF.** PEIMS records recapture of $56.9M in 2024-25 (2025 txt line 25) vs. $49.1M in
  TEA's SOF for SY2024-25, and **$0 in 2023-24** (2024 txt line 25) vs. $276.4M in 2022-23 (2023 txt line 25).
  PEIMS books cash/accrual by fiscal year (HISD FY ends June 30), SOF is the FSP entitlement year; the 2023-24 $0
  needs reconciliation against the ACFR (could be a timing/accrual reversal).
- **Local property tax is ~83% of HISD's GF operating revenue** (2024-25: $1,466.2M of $1,769.8M, 2025 txt
  lines 12, 16); state operating funds are only 9.0% of GF operating revenue vs. 44.5% statewide (AF basis:
  HISD 9.6% vs. state 44.5%).
- Ten-year view (`pwr/longitudinal_10yr_101912.txt`): AF expenditures per student 2015-16 $13,573 → 2019-20
  $13,871 → 2023-24 $18,150 → 2024-25 $17,026; enrollment 214,891 → 176,039 (−18%).

## 2. Spending by function per student — HISD vs. state, 2024-25

From `pwr_actual_2025_101912.txt` lines 71-90 (all funds, operating) and `data/peer_comparison.csv`.

| Function (AF, per enrolled student) | HISD | State | HISD 2022-23 |
|---|---|---|---|
| Instruction (11, 95) | 7,996 | 7,064 | 7,291 |
| Instructional resources/media (12) | 41 | 114 | 98 |
| Curriculum & staff development (13) | 220 | 296 | 391 |
| Instructional leadership (21) | **474** | 227 | 217 |
| School leadership (23) | **1,369** | 752 | 886 |
| Guidance & counseling (31) | 466 | 537 | 540 |
| Social work (32) | 49 | 40 | 196 |
| Health (33) | 161 | 132 | 160 |
| Transportation (34) | 305 | 395 | 300 |
| Food service (35) | 801 | 690 | 705 |
| Extracurricular (36) | 216 | 406 | 196 |
| General administration (41, 92) | 336 | 424 | 306 |
| Plant maintenance & operations (51) | 1,193 | 1,327 | 1,158 |
| Security (52) | 191 | 238 | 176 |
| Data processing (53) | 262 | 239 | 301 |
| **Total operating** | **14,147** | **12,951** | 12,998 |

- **School leadership (principals/APs/campus admin) is 1.8× the state rate per student** and grew 55% per
  student in two years ($886 → $1,369); **instructional leadership** (function 21, typically central/regional
  academic leadership and coaches) more than doubled ($217 → $474; GF $117 → $387). These two functions are where
  HISD most diverges from peers (see §4). This is consistent with the NES staffing model but the PEIMS data does
  not by itself attribute the cause.
- Curriculum/staff development (13), instructional resources (12), social work (32) and extracurricular (36)
  are well below state rates and (except 36) fell sharply since 2022-23.
- **Contracted services (object 62xx) are high: $1,893/student AF (13.4% of operating) vs. state $1,321
  (10.2%)**; GF $1,513 vs. state $1,073 (`pwr_actual_2025_101912.txt` line 55).
- By program intent (AF): special education $2,054/student (state $1,820), up from $1,406 in 2022-23; state
  compensatory education $1,304 (state $1,067), down from $1,721 in 2023-24; bilingual $217 (state $147) even
  though HISD's EB share is 39% vs. 24% statewide.

## 3. Revenue per student by source — peers, 2024-25 (all funds, operating)

From `data/peer_comparison.csv` (rows `2024-25,AF,rev_*`). Recapture is paid *out* of local M&O.

| District | Enrolled | Local M&O | State oper. | Federal | Other local | **Total oper. rev.** | Recapture paid |
|---|---|---|---|---|---|---|---|
| Houston ISD | 176,039 | 8,329 | 1,221 | 2,275 | 842 | **12,666** | 323 |
| Dallas ISD | 139,776 | 9,466 | 1,489 | 2,039 | 536 | 13,530 | 376 |
| Austin ISD | 72,175 | 10,242 | 650 | 1,555 | 861 | 13,308 | 10,691 |
| Fort Worth ISD | 70,184 | 5,808 | 5,043 | 1,271 | 466 | 12,589 | 74 |
| Northside ISD | 99,729 | 5,032 | 4,243 | 1,273 | 710 | 11,259 | 0 |
| Cypress-Fairbanks ISD | 117,658 | 4,044 | 4,763 | 1,192 | 732 | 10,731 | 0 |
| Katy ISD | 95,919 | 4,350 | 6,080 | 769 | 796 | 11,994 | 0 |
| Fort Bend ISD | 79,513 | 5,078 | 4,780 | 1,223 | 487 | 11,568 | 0 |
| State (all LEAs) | 5,528,915 | 4,776 | 5,637 | 1,471 | 783 | 12,666 | 533 |

HISD's operating revenue per student equals the state average exactly ($12,666) and is below Dallas
and Austin. That figure is already net of recapture: TEA's line is "Local Property Tax from M&O (excluding
recapture)" (FY2025 PWR p.1). *(Corrected 2026-10-08: an earlier version subtracted recapture again to get
$12,343.)* Austin's recapture ($10,691/student) is on top of the $10,242 of M&O tax it keeps, so it sends a
little over half its M&O tax to the state. From unrounded dollars, HISD's M&O tax + state operating funds =
$9,550 per student, and adding other local revenue gives $10,391 of nonfederal operating revenue.

## 4. Spending per student — peers, 2024-25 (all funds, operating, per enrolled student)

| District | Total oper. | Instruction (11) | Instr. leadership (21) | School leadership (23) | Gen. admin (41) | Contracted svcs (62xx) | Admin-cost PROXY* |
|---|---|---|---|---|---|---|---|
| Houston ISD | **14,147** | **7,996** | **474** | **1,369** | 336 | **1,893** | 0.093 |
| Dallas ISD | 14,210 | 7,206 | 374 | 850 | 439 | 1,067 | 0.095 |
| Austin ISD | 14,703 | 8,035 | 298 | 895 | 377 | 1,243 | 0.072 |
| Fort Worth ISD | 13,908 | 7,463 | 245 | 781 | 332 | 1,432 | 0.065 |
| Northside ISD | 12,278 | 7,125 | 209 | 638 | 180 | 732 | 0.049 |
| Cypress-Fairbanks ISD | 11,194 | 6,934 | 119 | 572 | 155 | 593 | 0.036 |
| Katy ISD | 12,333 | 7,731 | 102 | 641 | 213 | 501 | 0.036 |
| Fort Bend ISD | 11,651 | 6,526 | 256 | 648 | 263 | 835 | 0.068 |
| State (all LEAs) | 12,951 | 7,064 | 227 | 752 | 424 | 1,321 | 0.081 |

\*PROXY = (functions 21 + 41/92) ÷ (11 + 12 + 13 + 31), AF operating, from PWR totals. It mimics the old FIRST
administrative-cost-ratio formula but is **not** TEA's official ratio (TEA's uses specific fund/function/object
filters). Official ratios are not published in any downloadable TEA file I found; FIRST only shows points.

- HISD's operating spending per student is in line with Dallas/Austin and ~9% above the state average; it is
  21-26% above the suburban Houston-area peers (Fort Bend +21%, Cy-Fair +26%) — which have far fewer economically
  disadvantaged / EB students (§5).
- HISD has the highest instruction spending per student among the urban peers except Austin, and the highest
  school-leadership and instructional-leadership spending of the group by a wide margin.
- Share of AF operating spending on instruction: HISD 56.5%, state 54.5%, Katy 62.7%, Cy-Fair 62.0%, Dallas 50.7%.
- GF per student 2024-25 (operating): HISD $11,825; Dallas 12,236; Austin 12,924; Fort Worth 11,777; Northside
  10,704; Cy-Fair 9,638; Katy 11,116; Fort Bend 10,390; state 11,227.

## 5. Staffing and students (TAPR)

District TAPR PDFs: `tapr/tapr_{2023,2024,2025}_101912.txt` (staff section ~lines 1185-1260 / 1243-1315 /
1285-1365). Peer table: `data/tapr_staff_peer_comparison.csv` (from TAPR data-download CSVs).

HISD trend (FTE, TAPR; 2025 = SY2024-25):

| | 2022-23 | 2023-24 | 2024-25 | State 2024-25 |
|---|---|---|---|---|
| Total staff FTE | 24,451.4 | 25,558.2 | 23,524.0 | 764,857.7 |
| Teachers | 10,543.4 | 11,378.4 | 10,589.9 | 369,689.2 |
| Professional support | 3,616.5 | 4,616.5 | 3,849.1 | 82,751.4 |
| Campus administration | 580.9 | 851.6 | 898.7 | 25,687.5 |
| Central administration | 118.0 | 104.0 | 71.0 | 9,554.2 |
| Educational aides | 1,373.2 | 1,317.0 | 1,451.1 | 81,972.7 |
| Auxiliary | 8,219.5 | 7,290.7 | 6,664.2 | 195,202.8 |
| Students per teacher | 18.0 | 16.1 | 16.6 | 15.0 |
| Avg teacher salary | $64,954 | $67,073 | $73,604 | $63,751 |
| Avg campus-admin salary | $100,128 | $97,656 | $117,069 | $88,786 |
| Avg central-admin salary | $120,940 | $116,344 | $122,897 | $118,447 |
| Beginning teachers (% of teachers) | 7.2% | 10.6% | 12.1% | 7.3% |
| Teacher turnover rate | 22.3% | 19.7% | **32.2%** | 18.8% |
| Teachers with no degree | 6.8% (716.6) | 8.1% (916.7) | 7.0% (739.6) | 2.4% |
| Principals' avg years experience | 5.8 | 4.8 | 4.1 | 6.0 |
| Contracted instructional staff (excluded) | 437.0 | 415.0 | 403.0 | 1,637.7 |

(TAPR 2025 lines 1290-1297, 1316, 1321-1327, 1336-1362; TAPR 2024 lines 1243-1315; TAPR 2023 lines 1185-1257.)
Turnover definition (TAPR glossary `tapr/tapr_2024-25_glossary.txt` line 1800): share of fall-2023-24 teacher FTE
not employed *as teachers* in the district in fall 2024-25 — so 32.2% is the 2023-24 → 2024-25 transition.

- Campus administration FTE rose 55% (580.9 → 898.7) while enrollment fell 7%; per 1,000 students: HISD 5.11
  vs. state 4.64. Professional support per 1,000 students: HISD 21.9 vs. state 15.0 (highest of all peers).
- Central administration FTE (71.0, 0.40 per 1,000 students vs. state 1.73) is the *lowest* of the peers — but
  PEIMS "central administration" is a narrow role-ID category (superintendents, CFO-type administrators with a
  central-office ID); HISD's spending on instructional leadership (function 21) and general administration
  (function 41) per student is not low (§2/§4). Treat the FTE count as a coding artifact, not proof of a lean
  central office.
- HISD teacher pay is the highest of the peer group for beginning through 11-20-year teachers (beginning
  $66,987 vs. Dallas $60,406, state $55,689) and overall average ($73,604), but not for 21+ years (Fort Bend
  $79,627 and Fort Worth $87,127 pay more at 21-30 / 30+ years).
- Students (TAPR 2025 lines 1151-1209): econ. disadvantaged 77.8% (state 60.5%); emergent bilingual 39.2%
  (24.3%); special education 11.5% (15.3%); at-risk 67.7% (53.5%); immigrant 10.0% (3.5%); Title I 91.0%.
  Peer econ.-disadv.: Dallas 89.3%, Fort Worth 83.1%, Cy-Fair 58.9%, Austin 51.1%, Northside 49.9%, Fort Bend
  47.5%, Katy 42.7%.

Peer staffing per 1,000 students, 2024-25 (TAPR): teachers — HISD 60.2, Dallas 67.1, Austin 71.7, Fort Worth
67.3, Northside 70.9, Cy-Fair 65.1, Katy 72.1, Fort Bend 62.4, state 66.8. HISD has the fewest teachers per
student in the group and the highest students-per-teacher ratio (16.6).

## 6. School FIRST ratings (financial integrity)

`data/first_ratings.csv`, pages in `sources/tea_peims/first/`. Rating year Y is based on the prior school year's
audited data.

| Rating year (data year) | HISD | Dallas | Austin | Fort Worth | Northside | Cy-Fair | Katy | Fort Bend |
|---|---|---|---|---|---|---|---|---|
| 2025-26 (2024-25) | **A 94** | A 98 | B 88 | A 100 | A 98 | A 98 | A 98 | A 94 |
| 2024-25 (2023-24) | A 96 | A 96 | A 95 | B 85 | A 98 | A 98 | A 98 | A 98 |
| 2023-24 (2022-23) | A 96 | A 98 | A 94 | A 100 | A 98 | A 98 | A 96 | A 95 |
| 2022-23 (2021-22) | A 98 | A 95 | A 94 | A 98 | A 98 | A 92 | A 98 | A 96 |
| 2021-22 (2020-21) | **C 79** | A 96 | A 90 | A 94 | A 96 | A 92 | A 98 | A 92 |

- HISD 2025-26 (published 8/7/2026): A, 94/100. Points lost on indicator 8 (current assets ÷ current
  liabilities: 4 of 10 — down from 8 the year before and 6 in 2023-24), indicator 15 (ADA vs. projection: 5 of
  10, every year) and indicator 19 (website posting: 5 of 10). Days-cash-on-hand (7) and GF revenue ≥
  expenditures-or-60-days-cash (9) scored 10/10, but the pages show points only, not the underlying values.
- HISD 2021-22 C (79): ceiling indicator 17 failed — the auditor reported a material weakness in internal
  controls for FY2020-21, capping the rating at 79 (`first_District_2020_101912.html`).
- Administrative cost ratio (old indicator 13): HISD scored 8/10 in 2024-25 (2023-24 data), 10/10 in prior
  years; the indicator was dropped ("not being evaluated") in 2025-26. Dallas and Austin also scored 8.
  The underlying ratio values are not on the public FIRST pages.

## 7. Campus-level spending and NES vs. non-NES

Data: TEA "PEIMS Actual Financial Data, Organized by Campus" for all 272 HISD campuses, 2022-23..2024-25
(`sources/tea_peims/campus/allcamp_actual_{2023,2024,2025}_101912.pdf/.txt`) parsed to
`data/hisd_campus_actuals.csv`; NES status by year in `data/hisd_nes_campuses.csv` (130 campuses, all matched to
TEA campus IDs; main source an HISD ArcGIS school layer + HISD press packets, news lists as secondary — see the
NES section of `sources/tea_peims/SOURCES.md`). Summary: `data/hisd_campus_nes_summary.csv`
(`scripts/analyze_campus_nes.py`; membership-weighted; campuses <100 students and DAEP/JJAEP/program sites
excluded).

Caveats: campus reports cover only campus-coded spending — $1,989.4M of HISD's $2,490.5M AF operating spending in
2024-25 (~80%); central costs (much of functions 34-99, central instructional leadership) are mostly not
attributed. TEA itself warns (footnote on every campus page) that district-level data should be used for
comparisons of costs. NES campuses also serve more disadvantaged students, so part of the gap predates NES.

Operating spending per student (objects 61xx-64xx), all funds:

| Group | 2022-23 (pre-NES) | 2023-24 | 2024-25 |
|---|---|---|---|
| Campuses that are NES by 2024-25 (129 in sample) | 10,125 | — | **14,288** |
| — of which original 28 NES | — | 16,958 | — |
| — of which 57 NES-aligned | — | 13,718 | — |
| — of which 45 joining in 2024-25 | — | 10,388 | — |
| Never-NES campuses (134-135) | 8,421 | 8,776 | **9,193** |
| NES minus non-NES gap | +1,704 (+20%) | | **+5,095 (+55%)** |

- General fund only, 2024-25: NES $12,460 vs. non-NES $8,437 per student (+$4,023).
- Instruction (function 11) 2024-25: NES $9,921 vs. non-NES $6,220; school leadership (23): $1,751 vs. $1,077;
  payroll: $12,184 vs. $7,221.
- Same pattern within each level (2024-25 AF): elementary NES $13,747 vs. $9,499; middle $15,770 vs. $9,203;
  high $14,590 vs. $9,159.
- Change 2022-23 → 2024-25: NES cohort +$4,163/student (+41%); never-NES +$772/student (+9%). In dollars
  (all campuses, unfiltered), campus-coded operating spending at the 130 NES campuses rose from $810.1M to
  $996.1M (+$186M) while non-NES campuses rose $935.1M → $993.3M (+$58M).
- Enrollment (TEA membership, all campuses) 2022-23 → 2024-25: original 28 NES 14,447 → 12,871 (−10.9%);
  57 NES-aligned 37,204 → 31,969 (−14.1%); 2024-25 joiners 28,440 → 24,860 (−12.6%); non-NES 109,086 →
  106,225 (−2.6%). This matches the Texas Tribune's reported NES-vs-non-NES enrollment divergence, now from
  TEA's own membership counts.
- The ~$5,100 all-funds / ~$4,000 GF per-student NES gap in TEA actuals is larger than the ~$2,500 budget-
  formula gap reported in the press (README §5) — the press figure is HISD's per-pupil *allocation* formula;
  the TEA figure is total campus-coded actual spending, including federal/special-revenue funds and the
  pre-existing compensatory-ed differential (~$1,700 in 2022-23).

## 8. Comptroller property value study (HISD 101-912)

`sources/tea_peims/comptroller/pvs_*.txt`: total taxable value (T2, M&O, after state homestead exemption):
2023 final $232.70B; 2024 final $236.92B (`pvs_2024F.txt` lines 351-377: category subtotal $289.53B less
$52.61B deductions = $236.92B; T2 line 377); 2025 preliminary $236.18B. In every year the value assigned is the
local appraisal-roll value (2023: Comptroller estimate $240.57B, but local value used). Property wealth is flat, consistent with the README's "+0.24%" note.

## 9. What I could not get

- **2024-25 HISD fund balance** — missing from PEIMS (shows $0 with an offsetting "uncommon items" entry).
- **Official FIRST indicator values** (days cash on hand, current ratio, admin cost ratio) — FIRST public pages
  show only points; values are in each district's own annual FIRST report/hearing materials.
- **Official TEA administrative cost ratio** — no downloadable TEA file found; I report a labelled proxy.
- **Account-level PEIMS detail** (fund × function × object × organization; `actget2024.zip`, 27 MB) — not
  downloaded; would allow exact admin-cost-ratio replication and campus-vs-central splits. No 2024-25 file
  posted yet.
- **TAPR financial section** — TAPR no longer includes district finance; the PWR reports above replace it.
- **Comptroller FAST** — last published for ~2014-era data; not current, not used.
- PEIMS 2024-25 is the latest actual year; 2025-26 actuals are not yet published (only budgets).

---

## 2018-19 to 2021-22 (history extension, 2026-10-07)

All sources below are PRIMARY TEA/Comptroller files retrieved 2026-10-07 (catalogued in
`sources/tea_peims/SOURCES.md`, "History extension" section). Tables are rebuilt by the same scripts, which now
also read the older years:

```
python3 scripts/build_peer_comparison.py   # now 7 dumps 2018-19..2024-25; adds data/peer_comparison_2019_2025.csv
python3 scripts/parse_campus_actuals.py    # now 2018-19..2024-25
python3 scripts/analyze_campus_nes.py      # pre-NES baseline now 2018-19..2022-23, split by NES entry wave
python3 scripts/fetch_tapr_dd.py           # NEW: downloads old-format TAPR Profile CSVs (2019..2023)
python3 scripts/build_tapr_peers.py        # appends 2018-19..2022-23 rows (HISD, 7 peers, state)
python3 scripts/fetch_first.py             # app years 2019 and 2018 added
python3 scripts/fac_summary.py > sources/federal_debt/fac_sefa_summary_FY2018-2025.txt
```

**Regression check (2026-10-08).** Every row/cell that existed before this extension is unchanged
(compared against git HEAD): `tea_peims_actuals_long.csv` (4,580 old rows, 0 changed), `hisd_peims_trend.csv`
(0 changed cells in the 2020-21..2024-25 columns), `peer_comparison.csv` (byte-identical),
`hisd_campus_actuals.csv` (816 old rows, 0 changed; new PIC columns appended at the end),
`hisd_campus_nes_summary.csv` (43 old rows, 0 changed), `tapr_staff_peer_comparison.csv` (18 old rows, 0 changed),
`first_ratings.csv` (40 old rows, 0 changed). Headline figures still reproduce: 2024-25 NES $14,288 vs non-NES
$9,193 per student; HISD 2024-25 AF operating spending $14,147 and revenue $12,666 per student.

### H1. PEIMS actuals — HISD vs. state, 2018-19 → 2021-22

Source: `data/hisd_peims_trend.csv` (now 2018-19..2024-25), built from the statewide dumps
`2019-actual-pwr-1.xlsx` and `2020-actual-pwr-0.xlsx` (plus the three already held). The 2018-19 and 2019-20
values reproduce TEA's own PWR PDFs exactly (`pwr/pwr_actual_2019_101912.txt` lines 16, 56;
`pwr/pwr_actual_2020_101912.txt` lines 16, 56). PWR PDFs for 2020-21 and 2021-22 were also downloaded
(`pwr_actual_{2021,2022}_101912.txt`, `pwr_actual_{2019..2022}__STATE.txt`).

| Per enrolled student (trend csv line) | 2018-19 | 2019-20 | 2020-21 | 2021-22 | 2022-23 |
|---|---|---|---|---|---|
| Enrolled membership (l.2) | 209,040 | 209,309 | 196,550 | 193,727 | 189,290 |
| AF operating revenue (l.16) | 10,723 | 10,497 | 11,262 | 13,087 | 13,764 |
| — state AF operating revenue (l.17) | 10,470 | 10,811 | 11,505 | 12,502 | 12,822 |
| — HISD local M&O (l.4) | 7,089 | 7,807 | 8,159 | 8,313 | 8,099 |
| — HISD state operating funds (l.7) | 1,722 | 767 | 1,171 | 836 | 767 |
| — HISD federal (l.10) | 1,585 | 1,683 | 1,735 | 3,609 | 4,313 |
| AF operating expenditure (l.49) | **9,380** | 9,719 | 10,524 | 11,772 | 12,998 |
| — state (l.50) | 9,913 | 10,406 | 11,106 | 11,941 | 12,389 |
| GF operating expenditure (l.184) | 7,758 | 7,753 | 9,037 | 8,511 | 9,254 |
| — state (l.185) | 8,618 | 8,993 | 9,539 | 9,655 | 10,032 |
| Instruction, AF (l.61) | 5,191 | 5,518 | 5,989 | 6,497 | 7,291 |
| School leadership f23, AF (l.73) | 697 | 720 | 749 | 779 | 886 |
| Instructional leadership f21, AF (l.70) | 153 | 155 | 185 | 200 | 217 |
| Contracted services 62xx, AF (l.40) | 1,410 | 1,350 | 1,623 | 1,972 | 1,956 |
| Recapture paid, $M (l.27) | 265.2 | 80.8 | 197.8 | 184.5 | 276.4 |
| AF federal revenue, $M (l.9) | 331.4 | 352.2 | 341.0 | 699.1 | 816.3 |
| GF total fund balance, $M (l.276) | 819.0 | 967.9 | 996.6 | 1,126.9 | 1,127.1 |

- **Before ESSER, HISD spent less per student than the state average.** AF operating spending was $9,380 vs.
  $9,913 statewide in 2018-19 (−5%) and $9,719 vs. $10,406 in 2019-20 (−7%); GF operating spending was 10-14%
  below the state. HISD crossed above the state average only in 2022-23 ($12,998 vs. $12,389). Over 2018-19 →
  2024-25 HISD AF operating spending per student rose 51% ($9,380 → $14,147) vs. 31% statewide ($9,913 → $12,951)
  — in dollars only +27% ($1,960.7M → $2,490.5M, `tea_peims_actuals_long.csv`), because enrollment fell 16%.
- **School leadership was already above the state rate pre-NES** ($697 vs. $589, +18% in 2018-19; trend l.73-74)
  but the gap widened to +82% by 2024-25. Instructional leadership (f21) was *below* the state in 2018-19 ($153
  vs. $162) and 2.1× the state by 2024-25 ($474 vs. $227). Contracted services were 51% above the state rate
  already in 2018-19 ($1,410 vs. $933; l.40-41).
- **GF ran surpluses pre-takeover.** GF "Excess (Deficiency) Operating Expenditures": +$209.4M in 2018-19
  (`pwr_actual_2019_101912.txt` line 170), +$118.2M in 2019-20 (`pwr_actual_2020_101912.txt` line 175), +$20.9M
  in 2020-21 (`pwr_actual_2021_101912.txt` line 193). The 2021-22 line shows $0 for HISD (and $0 AF;
  `pwr_actual_2022_101912.txt` line 198) although the balance rose $130.3M (lines 195, 197) — the
  reconciliation line is blank/zeroed in TEA's PWR, like the 2024-25 gap noted in §9. GF total fund balance grew
  $819.0M → $1,126.9M (2018-19 → 2021-22), peaked at $1,127.1M in 2022-23.
- **State aid share collapsed with HB 3 (2019).** HISD's state operating revenue fell from $1,722/student
  (2018-19) to $767 (2019-20) while local M&O rose $7,089 → $7,807 and recapture fell $265.2M → $80.8M (HB 3
  compressed tax rates and changed recapture). State AF operating revenue was 16.1% of HISD's in 2018-19
  (`pwr_actual_2019_101912.txt` line 13) vs. 7.3% in 2019-20 (`pwr_actual_2020_101912.txt` line 13).
- **FLAG — 2018-19 recapture:** PEIMS records $265,231,840 (`pwr_actual_2019_101912.txt` line 24) but the
  ACFR25 statistical table (cited in `notes/federal_debt.md` §5) gives $185.1M for FY2019. 2019-20 ($80.8M vs.
  $74.9M) and 2020-21 ($197.8M vs. $198.1M) are close. Probably a prior-year settlement booked in 2018-19;
  unreconciled.
- 10-year longitudinal report (`pwr/longitudinal_10yr_101912.txt`) gives AF total expenditure per student
  $13,643 (2018-19) / $13,871 (2019-20), matching trend l.58 exactly.

**Peers, 2018-19 vs. 2021-22** (`data/peer_comparison_2019_2025.csv`; AF operating, per enrolled student;
2018-19 lines 560-591, 2021-22 lines 281-312):

| District | Oper. revenue 18-19 | Oper. spend 18-19 | School lead. 18-19 | Oper. revenue 21-22 | Oper. spend 21-22 |
|---|---|---|---|---|---|
| Houston ISD | 10,723 | **9,380** | 697 | 13,087 | **11,772** |
| Dallas ISD | 11,742 | 10,252 | 631 | 13,293 | 12,991 |
| Austin ISD | 10,799 | 10,855 | 689 | 13,556 | 13,299 |
| Fort Worth ISD | 9,520 | 10,544 | 590 | 13,286 | 13,283 |
| Northside ISD | 9,342 | 9,367 | 501 | 11,211 | 11,042 |
| Cypress-Fairbanks ISD | 9,265 | 8,922 | 422 | 10,249 | 10,444 |
| Katy ISD | 10,174 | 9,607 | 521 | 11,312 | 11,222 |
| Fort Bend ISD | 9,638 | 9,550 | 602 | 10,829 | 11,170 |
| State (all LEAs) | 10,470 | 9,913 | 589 | 12,502 | 11,941 |

In 2018-19 HISD's operating spending per student was the lowest of the four urban districts and below Katy;
by 2024-25 it was 3rd-highest of the eight, behind Austin and Dallas (§4). HISD's admin-cost PROXY was 0.0629 in 2018-19 and 0.051-0.057
in 2019-20..2021-22 (state 0.076-0.079; csv lines 753, 737, 721, 705) vs. 0.093 in 2024-25.

### H2. Campus actuals and the longer pre-NES baseline

`data/hisd_campus_actuals.csv` now covers 2018-19 (279 campuses, membership 209,023), 2019-20 (278), 2020-21
(274), 2021-22 (272), from `campus/allcamp_actual_{2019,2020,2021,2022}_101912.txt` (TEA program name for 2019-20 is
`allcamp_actual_report_1920.sas`). The pre-2021-22 reports have no Transportation (34) line and itemize State
Comp Ed by PIC (24/26/28/29/30); `pic_comp_ed` is their sum for those years. Campus-coded AF operating spending
was $1,461.4M of $1,960.7M district-wide in 2018-19 (74.5%) vs. ~80% in 2024-25.

AF operating spending per student, membership-weighted, by 2024-25 NES status (`data/hisd_campus_nes_summary.csv`):

| Year (csv lines) | NES cohort (129) | never-NES | Gap | Original 28 | 57 aligned* | 45 joiners |
|---|---|---|---|---|---|---|
| 2018-19 (2, 7, 13-15) | 7,381 | 6,561 | +820 (+12.5%) | 7,620 | 7,376 | 7,263 |
| 2019-20 (16, 21, 27-29) | 7,616 | 6,758 | +858 (+12.7%) | 8,229 | 7,560 | 7,367 |
| 2020-21 (30, 35, 41-43) | 8,263 | 7,311 | +952 (+13.0%) | 8,659 | 8,241 | 8,082 |
| 2021-22 (44, 49, 55-57) | 8,834 | 7,713 | +1,121 (+14.5%) | 9,438 | 8,721 | 8,669 |
| 2022-23 (58, 63, 69-71) | 10,125 | 8,421 | +1,704 (+20.2%) | 11,272 | 9,953 | 9,766 |
| 2024-25 (existing) | 14,288 | 9,193 | +5,095 (+55.4%) | — | — | — |

\*56 in sample (one excluded by the <100-student / program-site filter).

- The campuses that became NES were already ~12-13% more expensive per student in 2018-20 (higher comp-ed /
  Title I intensity). The gap widened gradually to +20% by 2022-23 (ESSER years), then to +55% under NES. So the
  NES-attributable increase is roughly +$3,400-4,300/student on top of a pre-existing ~$800-1,700 differential.
- Over 2018-19 → 2022-23 (pre-NES, 4 years) the NES cohort rose +$2,744 (+37%) and never-NES +$1,860 (+28%);
  2022-23 → 2024-25 (2 years) +$4,163 (+41%) vs. +$772 (+9%).
- GF only: the cohort was +$600/student above never-NES in 2018-19 ($6,827 vs. $6,227, lines 2/7) vs. +$4,023
  in 2024-25.
- Enrollment: the NES cohort lost 24% of membership 2018-19 → 2024-25 (91,708 → 69,459) vs. 9% for never-NES
  (116,466 → 105,714; the never-NES set also shrinks from 141 to 134 campuses through closures). The original 28
  lost 26% (17,322 → 12,871).

### H3. TAPR staffing and students, 2018-19 → 2021-22

Source: `data/tapr_staff_peer_comparison.csv` rows for 2018-19 (csv lines 56-64), 2019-20 (47-55), 2020-21
(38-46), 2021-22 (29-37), 2022-23 (20-28), built from `tapr/tapr{2019..2023}_{D,S}PROF.csv`; HISD values
cross-check against the district TAPR PDFs `tapr/tapr_{2019,2020,2021,2022}_101912.txt` (staff sections at lines
1058-1139 / 1180-1259 / 1270-1342 / 1183-1255).

| HISD (State) | 2018-19 | 2019-20 | 2020-21 | 2021-22 |
|---|---|---|---|---|
| Total staff FTE | 24,676.3 | 24,328.2 | 24,419.6 | 23,716.2 |
| Teachers FTE | 11,464.7 | 11,283.1 | 11,254.4 | 10,619.5 |
| Professional support | 2,926.5 | 2,978.5 | 3,334.6 | 3,437.0 |
| Campus administration | 586.4 | 570.8 | 553.1 | 530.0 |
| Central administration | 138.0 | 137.1 | 153.0 | 152.2 |
| Students per teacher | 18.2 (15.1) | 18.6 (15.1) | 17.5 (14.5) | 18.2 (14.6) |
| Avg teacher salary | $54,125 ($54,122) | $56,340 ($57,091) | $56,664 ($57,641) | $59,161 ($58,887) |
| Avg campus-admin salary | $84,319 | $84,846 | $84,936 | $87,547 |
| Teacher turnover | 19.1% (16.5%) | 20.3% (16.8%) | 18.8% (14.3%) | 22.4% (17.7%) |
| Beginning teachers | 8.1% | 8.6% | 9.3% | 7.4% |
| Teachers with no degree | 4.6% | 5.9% | 8.2% | 1.2% |
| Econ. disadvantaged | 79.9% (60.6%) | 79.3% (60.3%) | 78.5% (60.3%) | 79.2% (60.7%) |
| Emergent bilingual / EL | 31.8% (19.5%) | 34.0% (20.3%) | 33.4% (20.7%) | 35.1% (21.7%) |

(TAPR 2019 lines 1058-1066, 1091, 1097, 1103, 1132-1135, 1139, 972-975; TAPR 2020 lines 1180-1188, 1213, 1219,
1225, 1252-1255, 1259, 1070-1073; TAPR 2021 lines 1270-1277, 1296, 1301, 1307, 1330-1333, 1342, 1164, 1167;
TAPR 2022 lines 1183-1190, 1209, 1214, 1220, 1243-1246, 1255, 1075, 1078.)

- **Campus administration FTE was flat-to-falling pre-takeover** (586 → 530, 2018-19 → 2021-22; 2.8 per 1,000
  students vs. state ~4.0) and then rose to 898.7 by 2024-25 (5.1 per 1,000). Professional support rose
  steadily from 2,927 (14.0 per 1,000) to 3,849 in 2024-25 (21.9).
- **HISD always had the highest students-per-teacher ratio of the peer group** (18.2 in 2018-19 vs. 14.4-16.3 for
  the 7 peers; csv lines 56-63); its lowest values are the post-takeover 16.1 (2023-24) and 16.6 (2024-25).
- **Teacher pay matched the state average pre-takeover** ($54,125 vs. $54,122 in 2018-19; below the state in
  2019-20 and 2020-21) and was below every peer except Austin in 2018-19 (Dallas $58,012, Cy-Fair $60,258); by
  2024-25 it was the highest ($73,604, +36% over 2018-19 vs. +18% statewide).
- Turnover was 2.6-4.7 points above the state in each year 2018-19..2021-22 (0.6-0.9 points in 2022-23/2023-24);
  the 2024-25 32.2% is ~10 points above any earlier year.
- The 2018-19/2019-20 profile files have no 21-30 / 30+ year salary bands (blank in the csv). At-risk % is not
  comparable across years (HISD 65.3% → 71.0% → 52.7% → 61.5%; definition/coding changes) — not used.

### H4. FIRST, rating years 2019-20 and 2020-21

`data/first_ratings.csv` (app years 2019, 2018 added), pages `first/first_District_{2019,2018}_*.html`.

| Rating year (data year) | HISD | Dallas | Austin | Fort Worth | Northside | Cy-Fair | Katy | Fort Bend |
|---|---|---|---|---|---|---|---|---|
| 2020-21 (2019-20) | **C 79** | A 96 | A 92 | A 96 | A 96 | A 92 | A 98 | A 90 |
| 2019-20 (2018-19) | A 100 | A 98 | A 98 | A 96 | A 96 | A 94 | A 100 | A 92 |

- 2020-21 (FY2020 data): HISD scored 98 weighted points but was capped at 79 by ceiling indicator 17 —
  the auditor reported a material weakness in internal control (`first_District_2019_101912.html` line 1334,
  "Ceiling Failed"). With 2021-22 (FY2021 data, already in §6) that makes **two consecutive C ratings** for the
  same reason.
- 2019-20 (FY2019 data, old 15-indicator framework): A, 100 points, but indicator 2.B ("free of any material
  weaknesses") was answered **No** (`first_District_2018_101912.html` line ~1264) — under that framework 2.B did
  not cap the score. So material-weakness findings appear in three consecutive audits (FY2019-FY2021).
  CAUTION: app-year-2018 indicator numbers differ from 2019+; the `ind*` columns for that year are not comparable.
- Cross-check: FAC `general` records for FY2019-FY2021 flag `is_internal_control_deficiency_disclosed = Yes`
  but material weakness = No (`sources/federal_debt/fac_general_hisd.json`); FAC's flags cover the federal-program
  (Uniform Guidance) section, so the FIRST weakness was presumably in financial-statement controls. Not verified
  against the FY2019-FY2021 ACFRs.

### H5. Comptroller Property Value Study, 2019-2022 (final)

`comptroller/pvs_{2019,2020,2021,2022}F.txt` (from the `.html` pages via `scripts/html2text.py`).

| Tax year | Local roll total taxable value | Comptroller PTAD estimate | Value assigned | T2 (M&O, after state homestead) | Line |
|---|---|---|---|---|---|
| 2019 | $187.34B | $195.48B | local | $187.34B | 359-363, 376 |
| 2020 | $200.16B | $200.16B | local | $200.16B | 359-363 |
| 2021 | $203.49B | $210.46B | local | $203.49B | 361-365, 378 |
| 2022 | $222.77B | $222.77B | local | $222.77B | 361-365, 378 |

Each year states "...FOUND YOUR LOCAL VALUE TO BE VALID, AND LOCAL VALUE WAS CERTIFIED" (2019/2020 line 408,
2021 line 408, 2022 line 417). Taxable value grew 24% 2019 → 2023 ($187.3B → $232.7B) and has been flat since
(2024 $236.9B), consistent with §8.

### H6. Could not get / caveats (history extension)

- **TAPR new-style data download** (`dd_tapr_step_7.sas`) returns "This request completed with errors" for
  2019-2022 (it still works for 2024/2025); older years were taken from the per-year "Profile" download
  (`prgopt=<YYYY>/tapr/tapr_download.sas`, see `scripts/fetch_tapr_dd.py`), which covers the same variables.
- The 2019 district TAPR PDF only renders with `prgopt=2019/tapr/paper_tapr.sas` plus `level=district` and
  `district=101912`; the generic URL returns an all-"no data" shell.
- No account-level PEIMS (actget) files were downloaded for the older years either.
- FIRST underlying ratios (days cash, admin-cost ratio) remain unavailable for all years.
- The 2018-19 recapture and 2021-22 zero fund-balance reconciliation flags above are unresolved.

---

## Budgeted data as filed with TEA, 2019-20 to 2025-26 (update, 2026-10-08)

Source: TEA "Budgeted Financial Data" reports, Houston ISD and State Total, `sources/tea_peims/pwr/pwr_budget_{2020..2026}_{101912,_STATE}.pdf`, parsed by `scripts/parse_tea_budget_reports.py` into `data/tea_peims_budget_long.csv`. Fifty-eight checks pass. Revenue sources sum to total operating revenue, and spending by function sums to spending by object, for HISD and the state, General Fund and adopted-funds totals, every year. HISD's 2025-26 filing also ties to its own adopted budget (see `notes/budget.md` U3).

**What these are.** The adopted budget of the General Fund, Food Service and Debt Service funds, as the district filed it with TEA. They are not actuals. Their "All Funds" columns cover only those three funds: they exclude the special-revenue grant funds but still include federal revenue in those funds ($158.7M for HISD in 2025-26, mostly child nutrition). Compare them only with General Fund actuals. Per-student figures use TEA's fall enrolled membership for the year, the same count as in the actual reports. TEA's report server does not serve 2018-19 (it returns an HTML error page).

### B1. General Fund operating spending per student: budgeted vs actual

| School year | HISD budgeted | HISD actual | HISD actual vs budget [calc] | State budgeted | State actual | State actual vs budget [calc] |
|---|---:|---:|---:|---:|---:|---:|
| 2019-20 | 8,618 | 7,753 | −10.0% | 9,368 | 8,993 | −4.0% |
| 2020-21 | 10,008 | 9,037 | −9.7% | 10,102 | 9,539 | −5.6% |
| 2021-22 | 10,186 | 8,511 | −16.4% | 10,235 | 9,655 | −5.7% |
| 2022-23 | 10,360 | 9,254 | −10.7% | 10,379 | 10,032 | −3.3% |
| 2023-24 | 10,859 | 10,629 | −2.1% | 10,901 | 10,755 | −1.3% |
| 2024-25 | 11,489 | 11,825 | **+2.9%** | 11,240 | 11,227 | −0.1% |
| 2025-26 | **12,151** | – | – | **12,057** | – | – |

Actuals are TEA PEIMS General Fund "Total Operating Expenditures" per enrolled student (`data/tea_peims_actuals_long.csv`, `STATE` = all districts and charters). The state budget total's 2025-26 membership is 5,454,100.

### B2. 2025-26 General Fund, per student (budgeted)

| | HISD | State total | HISD 2024-25 actual |
|---|---:|---:|---:|
| Local property tax (M&O) | 9,314 | 4,938 | |
| State operating funds | 1,856 | 6,039 | |
| Federal | 129 | 202 | |
| Other local | 494 | 377 | |
| **Total operating revenue** | **11,794** | **11,556** | |
| Instruction (11,95) | 7,356 | 6,972 | 7,092 |
| Instructional leadership (21) | 475 | 205 | 387 |
| School leadership (23) | 1,307 | 756 | 1,324 |
| General administration (41,92) | 354 | 449 | 292 |
| **Total operating expenditures** | **12,151** | **12,057** | **11,825** |

HISD's budgeted state share of General Fund operating revenue is 6.8% in 2024-25 (689 of 10,143) and 15.7% in 2025-26 (1,856 of 11,794) [calc]. The shift mostly reflects tax-relief aid, plus new allotments such as the Teacher Retention Allotment (see `data/hisd_sof_trend.md`); this table alone does not isolate the causes. HISD's 2025-26 filing budgets $0 of recapture, and so did its 2019-20 filing (the FY2020 adopted budget had $0).

### B3. Campus budgets 2025-26 and NES

Source: TEA "2025-2026 PEIMS Budget Financial Data, Organized by Campus," HISD (`sources/tea_peims/campus/allcamp_budget_2026_101912.pdf`), parsed by `scripts/parse_campus_budget.py` with the same line pattern and exclusions as the actuals (membership < 100 and alternative or program sites excluded). NES status for 2025-26 is from `data/hisd_nes_campuses.csv` (130 NES campuses; 128 pass the exclusions). Campus budgets cover the General Fund only.

- 271 campuses, membership 167,786; campus-coded General Fund operating budget $1,715,040,903, which is 84.1% of the district's $2,038,813,425 General Fund operating budget.

| 2025-26, General Fund operating budget per student | Campuses | Membership | Per student |
|---|---:|---:|---:|
| NES, all | 128 | 62,616 | **12,944** |
| NES elementary / middle / high | 86 / 21 / 15 | 33,942 / 9,680 / 14,299 | 11,968 / 14,172 / 14,567 |
| Non-NES, all | 133 | 104,313 | **8,409** |
| Non-NES elementary / middle / high | 70 / 14 / 17 | 40,476 / 13,026 / 20,964 | 8,909 / 8,618 / 8,521 |

The budgeted gap is **$4,535** per student (+53.9%), against $4,023 (+47.7%) in 2024-25 General Fund actuals ($12,460 vs $8,437) [calc].

**Enrollment, same eligible campuses, TEA fall counts 2024-25 → 2025-26** (campus membership in the 2024-25 actual report vs the 2025-26 budget report; 2025-26 NES status). Eligible = at least 100 members in *both* years and not an alternative/program site, so the two campuses that closed after 2024-25 are listed separately. Texas Connections Academy, the online school, is shown on its own. *(Corrected 2026-10-08 after independent review: the earlier table kept Las Americas, which had 0 members in 2025-26, and counted the online school with the non-NES campuses, giving −10.9% for NES-A and −1.1% for non-NES.)*

| Group | Campuses | 2024-25 | 2025-26 | Change |
|---|---:|---:|---:|---:|
| NES 2023 (original 28) | 28 | 12,871 | 11,982 | −6.9% |
| NES-A 2023 (aligned) | 55 | 31,617 | 28,270 | −10.6% |
| NES 2024 (joined 2024-25) | 45 | 24,860 | 22,364 | −10.0% |
| **NES, all** | 128 | 69,348 | 62,616 | **−9.7%** |
| **Non-NES brick-and-mortar** | 132 | 96,879 | 92,997 | **−4.0%** |
| Texas Connections Academy (online) | 1 | 8,641 | 11,316 | +31.0% |
| Closed: Las Americas (NES-A), Mount Carmel Academy (non-NES) | 2 | 305 | 0 | |

Including the online school with the non-NES group gives −1.1%. Budgeted 2025-26 General Fund per student excluding the online school: NES $12,944, non-NES $8,799 (gap $4,145); 2024-25 actual on the same 260 campuses: $12,443 vs $8,613. These match the independent review's working papers (`review/data/new_budget_nes_sensitivity.csv`).
