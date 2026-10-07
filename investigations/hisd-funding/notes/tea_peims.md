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

HISD's gross operating revenue per student equals the state average exactly ($12,666) and is below Dallas
and Austin; net of recapture it is $12,343. Austin's local revenue is mostly recaptured ($10,691/student).

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
