# References

Houston Independent School District (HISD), TEA district 101912. All retrieval dates are 2026-10-06 unless noted; the FY2027 budget notice and analysis were finished 2026-10-07, and the history extension back to FY2019 (second edition) was retrieved 2026-10-07. "PRIMARY" means an official document from HISD, TEA, the Texas Comptroller, an auditor or a bond issuer (ACFR, single audit, official statement, government dataset). "SECONDARY" means press, advocacy, or an aggregator.

Full source catalogs, with every file and its exact URL, are kept per track in the repository: `sources/acfr/SOURCES.md`, `sources/budget/SOURCES.md`, `sources/federal_debt/SOURCES.md`, `sources/tea_peims/SOURCES.md`. This page summarizes them.

## State formula funding (TEA Summary of Finances)

TEA "Summary of Finances" (SOF) reports for HISD for every school year from 2018-19 through 2026-27. The first edition used three reports downloaded by hand from TEA's public report dashboard (https://tealprod.tea.state.tx.us/Tea.FspReports.Web/dashboard?rpt=SummaryOfFinance&cat=SummaryOfFinance, a JavaScript application with no plain data export):

| File | Title | Payment cycle | Run ID |
|---|---|---|---|
| `2025report.pdf` | SY2024-25 Summary of Finances | Final | 46849 |
| `2026report.pdf` | SY2025-26 Summary of Finances | Near-Final | 47299 |
| `Report_6_47240_2026-10-06T214926.pdf` | SY2026-27 Summary of Finances (superseded by run 47318 below) | Preliminary | 47240 |

The second edition retrieved the rest from the same dashboard with a browser restricted to that site (`sources/sof_history/`, PDF plus text extraction; method in `notes/sof_history.md`). Each is the latest run of its year as of 2026-10-07:

| File | School year | Payment cycle | Run ID | Last updated |
|---|---|---|---|---|
| `sources/sof_history/sof_2018-19_final_run36031.pdf` | 2018-19 | Final | 36031 | May 27, 2022 |
| `sources/sof_history/sof_2019-20_final_run46374.pdf` | 2019-20 | Final | 46374 | Feb. 12, 2026 |
| `sources/sof_history/sof_2020-21_final_run46377.pdf` | 2020-21 | Final | 46377 | Feb. 12, 2026 |
| `sources/sof_history/sof_2021-22_final_run46737.pdf` | 2021-22 | Final | 46737 | Apr. 29, 2026 |
| `sources/sof_history/sof_2022-23_final_run47041.pdf` | 2022-23 | Final | 47041 | Jul. 8, 2026 |
| `sources/sof_history/sof_2023-24_final_run46845.pdf` | 2023-24 | Final | 46845 | May 29, 2026 |
| `sources/sof_history/sof_2026-27_preliminary_run47318.pdf` | 2026-27 | Preliminary | 47318 | Oct. 5, 2026 |

The dashboard's list of every run for each year (390 runs, with each run's Foundation School Fund allotment and recapture amount) is in `data/sof_run_history.csv`.

## Audited financial statements (ACFR)

HISD's Annual Comprehensive Financial Reports, FYE June 30, for 2019 through 2025 (2025 is the latest; 2026's is not yet published), downloaded from HISD's Controller's Office page. Auditor: Weaver and Tidwell, L.L.P. for all years examined. The FY2025 report's opinion is dated January 12, 2026. Full catalog: `sources/acfr/SOURCES.md`. The FY2025 PDF is split into three page-range parts for GitHub's 100 MB file limit (see that file for the split method and integrity checks).

## Adopted budgets

HISD's adopted budget books, official adopted budget schedules, board workshop decks and in-year budget amendments for FY2019 through FY2027, from HISD's own Budget & Financial Planning page (the FY2019 book from the Internet Archive's copy of HISD's file). No budget book could be found for FY2020 or FY2024; those years rely on the one-page adopted schedules. Full catalog: `sources/budget/SOURCES.md`.

## TEA / Texas Comptroller data (actual spending, staffing, ratings, property values)

- PEIMS Financial Standard Reports (district and statewide actuals, 2018-19 through 2024-25) and PEIMS actual financial data by campus (HISD's campuses, 2018-19 through 2024-25).
- TAPR (Texas Academic Performance Reports), district and statewide staffing/salary data, 2018-19 through 2024-25.
- School FIRST (Financial Integrity Rating System of Texas) district status detail for HISD and seven peer districts, rating years 2019-20 through 2025-26.
- Texas Comptroller School District Property Value Study worksheets for HISD, 2019 (final) through 2025 (preliminary).
- HISD's own NES (New Education System) campus list, from HISD's ArcGIS schools layer and HISD's own press packet.

Full catalog: `sources/tea_peims/SOURCES.md`.

## Federal funds, debt and bonds

- Federal Audit Clearinghouse: HISD's single-audit records and Schedule of Expenditures of Federal Awards, FY2018-FY2025.
- EMMA (MSRB): official statements for HISD's Series 2026 refunding bonds and Series 2025A variable-rate maintenance tax notes, and HISD's FY2025 annual continuing-disclosure filing.
- HISD's own debt-obligations and ESSER pages, and a Whitley Penn internal audit of ESSER II/III funds (May 2024).
- USAC E-Rate funding data for HISD (BEN 141223).
- Texas Comptroller Chapter 313 agreement list (HISD does not appear on it).

Full catalog: `sources/federal_debt/SOURCES.md`.

## Press and advocacy reporting (cited by URL, not republished)

Full-page copies of the news articles and web pages cited below are held in a private working archive and are not republished here, for copyright reasons. Two advocacy items are included in the evidence folder: the OSOD "Charter Schools: Impact on Houston" fact sheets (PDF) and the TPPF chart transcribing HISD's 2024 Voter Information Document (image), both under `sources/federal_debt/`. The facts drawn from each are in [the notes](notes/) and in the report pages; every article's URL and retrieval date is listed here.

| Outlet | What it covers | URL |
|---|---|---|
| Ballotpedia | HISD's November 2024 bond election, Propositions A and B: certified results and ballot text | <https://ballotpedia.org/Houston_Independent_School_District,_Texas,_Proposition_A,_Schoolhouse_Bond_Measure_(November_2024)>, and the Proposition B equivalent |
| Texas Public Policy Foundation | "The Real Cost of Houston ISD's Bond Package" (Oct. 17, 2024), transcribing HISD's own Voter Information Document cost chart | <https://www.texaspolicy.com/the-real-cost-of-houston-isds-bond-package/> |
| Houston Public Media | Bond rejection (Nov. 5, 2024); NES campus list finalization (Feb. 9, 2024); school closure plan (Feb. 12, 2026) and board vote (Feb. 26, 2026); state takeover sustainability and cost (Sept. 21, 2026); voucher program cost to HISD (Oct. 1, 2026) | houstonpublicmedia.org |
| KPRC Click2Houston | HISD's $2M bond campaign spending (Feb. 2025); 19 additional NES campuses announced (Feb. 2024); October 2025 "disaster pennies" tax rate increase | click2houston.com |
| Houston Chronicle (via Yahoo) | HISD board considering $182.5M in lease-revenue bonds for a CTE center (Nov. 12, 2025) | yahoo.com/news |
| Houston Landing | HISD's ~$870M in vendor spending approved outside normal board process (Jan. 13 and 16, 2025) | houstonlanding.org |
| Texas Tribune | "High costs, dwindling enrollment: Is Houston ISD's playbook under takeover sustainable?" (Sept. 21, 2026); "What to know about the Texas 'Robin Hood' school funding system" (Jul. 24, 2026) | texastribune.org |
| Fox 26 Houston / The Leader News | NES-aligned campus list announcements, 2023 | fox26houston.com, theleadernews.com |
| Our Schools Our Democracy (OSOD) / Every Texan | Advocacy estimates of TEFA voucher program losses to Texas public schools (Oct. 1, 2026) and charter-school enrollment/revenue impact on Houston (Jul. 2026); cites Texas Comptroller PIR data | osod.org |

## Not retrieved

- TEA's Title I-IV and IDEA-B grant entitlement/planning-amount pages (tea.texas.gov) and the U.S. Department of Education's Title I LEA allocation tables both returned 403 (login required).
- HISD's own 2024 bond election Voter Information Document was not located directly; its cost figures are known only through the TPPF chart above.
- Separate Single Audit reports after FY2017 are not posted separately by HISD; from FY2018 on, the Single Audit is inside each ACFR's compliance section, which is what was used.
- 2025-26 and 2026-27 PEIMS actuals are not yet published (the school years are not complete / not yet audited by TEA).
