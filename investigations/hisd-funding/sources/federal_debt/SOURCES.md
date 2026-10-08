# Sources: federal funds, debt/bonds, policy money flows (HISD, TEA 101912)

Retrieved 2026-10-06 unless noted. PRIMARY means an official document from HISD, a regulator, an auditor, or an issuer (single audit/ACFR, official statement, government dataset). SECONDARY means press, advocacy, or an aggregator.
Text extractions (`*.txt`, `*.paged.txt`) were made with `pdftotext` (`-layout`, or `-raw` for the FAC ACFRs). Each line of a `*.paged.txt` file starts with its **PDF page number** (`NN: `). Printed page numbers differ: in the FY2025 ACFR, printed page = PDF page - 10.

## Federal Audit Clearinghouse (single audits, SEFA)

| File | Title | URL | Type |
|---|---|---|---|
| fac_general_hisd.json | FAC "general" records for HISD (EIN 746001255, UEI NC2GGLMFYC66), FY2016-FY2025 | https://api.fac.gov/general?auditee_ein=eq.746001255 | PRIMARY |
| fac_awards_<report_id>.json (FY2020-FY2025, 6 files) | FAC federal_awards (SEFA line items) per audit year | https://api.fac.gov/federal_awards?report_id=eq.<report_id> | PRIMARY |
| fac_findings_text_2025-06-GSAFAC-0000402495.json, fac_findings_text_2024-06-GSAFAC-0000068366.json | Single-audit finding text, FY2025 (2 findings) and FY2024 (none) | https://api.fac.gov/findings_text?report_id=eq.<report_id> | PRIMARY |
| fac_report_2025-06-GSAFAC-0000402495.pdf (+ .raw.paged.txt) | HISD ACFR FY ended 6/30/2025 incl. single-audit/SEFA section (Weaver and Tidwell), 200 pp. | https://app.fac.gov/dissemination/report/pdf/2025-06-GSAFAC-0000402495 | PRIMARY |
| fac_report_2024-06-GSAFAC-0000068366.pdf (+ .raw.paged.txt) | HISD ACFR FY ended 6/30/2024 incl. single audit, 186 pp. | https://app.fac.gov/dissemination/report/pdf/2024-06-GSAFAC-0000068366 | PRIMARY |
| fac_sefa_summary_FY2020-2025.txt | Derived table of SEFA expenditures by Assistance Listing, FY2020-25 (made by /git/Texas/HISD/scripts/fac_summary.py from the JSON above) | (derived) | PRIMARY-derived |

## EMMA (MSRB) official statements and disclosures

| File | Title | URL | Type |
|---|---|---|---|
| emma_HISD_LTRB_Series2026_OS.pdf (+ .paged.txt) | Official Statement, $342,790,000 Limited Tax Refunding Bonds, Series 2026, dated May 4, 2026 (276 pp.; Appendix A = FY2025 ACFR) | https://emma.msrb.org/P11950457-P11489325-P11941293.pdf (issue page https://emma.msrb.org/IssueView/Details/P2444428) | PRIMARY |
| emma_HISD_VR_MTN_Series2025A_OS.pdf (+ .txt) | Official Statement, $114,390,000 Variable Rate Maintenance Tax Notes, Series 2025A, dated July 10, 2025 | https://emma.msrb.org/P21940546-P21482449-P21933429.pdf (issue P1433646) | PRIMARY |
| emma_HISD_annual_continuing_disclosure_FY2025.pdf (+ .txt) | HISD Annual Financial Operating Data, FY ended 6/30/2025 (Rule 15c2-12 filing) | https://emma.msrb.org/P22012772-P21521952-P21989951.pdf | PRIMARY |

## HISD website and documents

| File | Title | URL | Type |
|---|---|---|---|
| hisd_debt_obligations_page.html | "Debt Obligations": FY2025 debt summary and issue-by-issue listing | https://www.houstonisd.org/our-district/financial-transparency/debt-obligations | PRIMARY |
| hisd_esser_page.html | "ESSER I, II, & III": allocations and dates | https://www.houstonisd.org/our-district/budget-financial-planning/external-funding/esser-i-ii-iii | PRIMARY |
| hisd_internal_audit_esser_2024.pdf (+ .txt) | Whitley Penn internal audit of ESSER II and III funds, May 7, 2024 | https://resources.finalsite.net/images/v1759263310/houstonisdorg/oniavakyafnvb7qidpiq/HoustonISDESSERAuditGrant572024.pdf | PRIMARY |
| hisd_FY2024-25_board_workshop_2024-05-23.pdf (+ .paged.txt) | FY2024-25 Budget Board Workshop deck, May 23, 2024 (NES budgets, ESSER cliff) | https://resources.finalsite.net/images/v1749058503/houstonisdorg/dzrjhxfrpazgtp8fdnim/FY_2024-2025_Board_Workshop_May232024.pdf | PRIMARY |
| hisd_tax_information_page.html | "Tax Information": adopted 2025 tax rate | https://www.houstonisd.org/our-district/budget-financial-planning/tax-information | PRIMARY |

## Other government data

| File | Title | URL | Type |
|---|---|---|---|
| usac_erate_hisd_ben141223_by_year.json | USAC E-Rate FRN status, HISD BEN 141223, committed and disbursed by funding year (form_version=Current) | https://opendata.usac.org/resource/qdmp-ygft.json (SoQL query, see notes) | PRIMARY |
| comptroller_ch313_agreements.html | Texas Comptroller, Chapter 313 School Value Limitation Agreement Documents (district list; Houston ISD absent) | https://comptroller.texas.gov/economy/development/prop-tax/ch313/agreement-docs.php | PRIMARY |

## Press, advocacy, aggregators

The saved web pages (`.html`) in this section are kept in the private working archive only and are not republished in the public govspends repository (copyright); they are cited there by URL. The OSOD fact-sheet PDF and the TPPF chart image are included in the public repository.

| File | Title | URL | Type |
|---|---|---|---|
| ballotpedia_hisd_2024_propA.html | Ballotpedia, HISD Proposition A (Nov 2024), certified results and ballot text | https://ballotpedia.org/Houston_Independent_School_District,_Texas,_Proposition_A,_Schoolhouse_Bond_Measure_(November_2024) | SECONDARY (reproduces certified canvass) |
| ballotpedia_hisd_2024_propB.html | Ballotpedia, HISD Proposition B (Nov 2024) | https://ballotpedia.org/Houston_Independent_School_District,_Texas,_Proposition_B,_Schoolhouse_Bond_Measure_(November_2024) | SECONDARY |
| tppf_hisd_bond_cost.html, tppf_hisd_vid_chart_2024.jpg | TPPF, "The Real Cost of Houston ISD's Bond Package" (Oct 17, 2024), with a chart transcribed from HISD's Voter Information Document | https://www.texaspolicy.com/the-real-cost-of-houston-isds-bond-package/ | SECONDARY (VID figures) |
| hpm_hisd_bond_rejected_2024.html | Houston Public Media, "Houston ISD bond rejected in large margin...", Nov 5, 2024 | https://www.houstonpublicmedia.org/articles/news/education-news/hisd/2024/11/05/504770/... | SECONDARY |
| click2houston_hisd_bond_campaign_spending_2025-02-04.html | KPRC, "Houston ISD approved $2M to campaign for the massive failed bond", Feb 3-4, 2025 | https://www.click2houston.com/news/local/2025/02/04/hisds-bond-spending-exposed/ | SECONDARY |
| yahoo_hisd_cte_lease_bonds.html | Houston Chronicle (via Yahoo), "Houston ISD board may OK borrowing $182.5 million for a new CTE center", Nov 12, 2025 | https://www.yahoo.com/news/articles/houston-isd-board-may-ok-220016528.html | SECONDARY |
| click2houston_hisd_disaster_pennies_2025-10-15.html | KPRC, "Houston ISD votes for property tax hike to cover storm repairs", Oct 15, 2025 | https://www.click2houston.com/news/local/2025/10/15/houston-isd-considers-property-tax-hike-to-cover-15m-in-storm-repairs/ | SECONDARY |
| hpm_hisd_closures_plan_2026-02-12.html | HPM, "Houston ISD unveils plan to shutter 12 schools in 2026-27", Feb 12, 2026 | https://www.houstonpublicmedia.org/articles/education/2026/02/12/543326/hisd-school-closures-houston/ | SECONDARY |
| hpm_hisd_closures_vote_2026-02-26.html | HPM, "Houston ISD board votes to close 12 schools", Feb 26, 2026 | https://www.houstonpublicmedia.org/articles/education/2026/02/26/544580/houston-school-closures-hisd-board/ | SECONDARY |
| txtrib_hisd_takeover_cost_2026-09-21.html | Texas Tribune, "High costs, dwindling enrollment: Is Houston ISD's playbook under takeover sustainable?", Sept 21, 2026 | https://www.texastribune.org/2026/09/21/houston-isd-state-takeover-sustainability/ | SECONDARY |
| houstonlanding_hisd_870M_skipped_approval.html | Houston Landing, "HISD leaders failed to get board approval for up to $870 million in spending", Jan 13, 2025 | https://www.houstonlanding.org/hisd-leaders-failed-to-get-board-approval-for-up-to-870-million-in-spending-records-show/ | SECONDARY |
| houstonlanding_hisd_870M_vendor_approval.html | Houston Landing, "HISD board approves up to $870 million in vendor contracts after policy breach", Jan 16, 2025 | https://www.houstonlanding.org/hisd-board-approves-up-to-870-million-in-vendor-contracts-after-policy-breach/ | SECONDARY |
| osod_voucher_loss_report.html | Our Schools Our Democracy / Every Texan press release on TEFA voucher losses, Oct 1, 2026 | https://osod.org/texas-public-schools-will-lose-at-least-227-million-this-school-year-alone-to-texas-new-voucher-program/ | SECONDARY (advocacy; cites Comptroller PIR data) |
| hpm_voucher_cost_2026-10-01.html | HPM, "Voucher program could cost Texas schools close to $300 million...", Oct 1, 2026 | https://www.houstonpublicmedia.org/articles/news/2026/10/01/563388/... | SECONDARY |
| osod_houston_charter_fact_sheets_2026-07.pdf (+ .txt) | OSOD, "Charter Schools: Impact on Houston" fact sheets, July 2026 | http://osod.org/wp-content/uploads/2026/07/Houston-Fact-Sheets.pdf | SECONDARY (advocacy estimate) |

## Not retrievable this pass
- TEA grant entitlements and ESSA planning amounts (Title I-IV and IDEA-B by LEA): tea.texas.gov returned 403 "Access denied. Login required" for the entitlements page.
- ED Title I LEA allocation tables (ed.gov budget tables) returned 403.
- KHOU bond-cost article returned 403. HISD's 2019 blog post on the 2012 bond did not download.
- HISD's Voter Information Document (Aug 2024) itself was not located. Its figures come only from the TPPF chart.

## History extension (retrieved 2026-10-07)

| File | Title | URL | Type |
|---|---|---|---|
| fac_awards_2019-06-CENSUS-0000174326.json | FAC federal_awards (SEFA line items), HISD FY ended 6/30/2019 (80 lines, $325,864,703) | https://api.fac.gov/federal_awards?report_id=eq.2019-06-CENSUS-0000174326 | PRIMARY |
| fac_awards_2018-06-CENSUS-0000174326.json | FAC federal_awards, HISD FY ended 6/30/2018 (79 lines, $345,229,820) | https://api.fac.gov/federal_awards?report_id=eq.2018-06-CENSUS-0000174326 | PRIMARY |
| fac_findings_{2019,2018}-06-CENSUS-0000174326.json, fac_findings_text_{2019,2018}-06-CENSUS-0000174326.json | FAC findings / findings_text for FY2019 and FY2018 (both empty: `[]`) | https://api.fac.gov/findings?report_id=eq.<id>, https://api.fac.gov/findings_text?report_id=eq.<id> | PRIMARY |
| fac_sefa_summary_FY2018-2025.txt | Derived SEFA table by Assistance Listing FY2018-FY2025 (`scripts/fac_summary.py`; FY2020-25 columns identical to fac_sefa_summary_FY2020-2025.txt) | (derived) | PRIMARY-derived |
