# TEA / State of Texas sources — HISD (101912) funding & spending

Retrieval date for everything below: **2026-10-06**. All TEA/Comptroller files are PRIMARY (official state data) unless marked.
Broker URLs below are `https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&_debug=0&single=N&batch=N&app=PUBLIC&search=dist&ptype=P&...` ("BROKER" below); `who_box` = county-district number.

## PEIMS Financial Standard Reports — statewide data dumps (all districts + charters, one row per LEA)
Index page: https://tea.texas.gov/finance-and-grants/state-funding/state-funding-reports-and-data/peims-financial-standard-reports (saved as `raw/peims-financial-standard-reports.html`)

| File | Title | URL | Status |
|---|---|---|---|
| actual2025-info-gen-all.xlsx | 2024-25 Actual PWR data dump (Enroll, GF, AF, Equity tabs) | https://tea.texas.gov/about-tea/state-funding/state-funding-reports-and-data/actual2025-info-gen-all.xlsx | PRIMARY |
| actual2024-info-gen-all-w-fb.xlsx | 2023-24 Actual PWR data dump (with fund balance) | https://tea.texas.gov/data-reports/financial-reports/school-finance-reports-and-data/actual2024-info-gen-all-w-fb.xlsx | PRIMARY |
| 2023-actual-pwr.xlsx | 2022-23 Actual PWR data dump | https://tea.texas.gov/data-reports/financial-reports/school-finance-reports-and-data/2023-actual-pwr.xlsx | PRIMARY |
| 2022-actual-pwr-0.xlsx | 2021-22 Actual PWR data dump | https://tea.texas.gov/data-reports/financial-reports/school-finance-reports-and-data/2022-actual-pwr-0.xlsx | PRIMARY |
| 2021-actual-pwr.xlsx | 2020-21 Actual PWR data dump | https://tea.texas.gov/data-reports/financial-reports/school-finance-reports-and-data/2021-actual-pwr.xlsx | PRIMARY |

Not downloaded (available, account-code detail, 26–28 MB zips each): District Financial Actual Data single-file CSV, e.g. https://tea.texas.gov/data-reports/financial-reports/school-finance-reports-and-data/actget2024.zip (2023-24; no 2024-25 file posted yet). Listed in `raw/peims-single-file-financial-data-downloads.html`.

## PEIMS Financial Standard Reports — district/state report PDFs (SAS broker; works with plain GET)
| File | Title | URL | Status |
|---|---|---|---|
| pwr/pwr_actual_2025_101912.pdf (+ .txt) | 2024-25 Actual Financial Data, Totals for HOUSTON ISD (101912) | BROKER&_program=sfadhoc.actual_report_2025.sas&who_box=101912 | PRIMARY |
| pwr/pwr_actual_2024_101912.pdf (+ .txt) | 2023-24 Actual Financial Data, HISD | BROKER&_program=sfadhoc.actual_report_2024.sas&who_box=101912 | PRIMARY |
| pwr/pwr_actual_2023_101912.pdf (+ .txt) | 2022-23 Actual Financial Data, HISD | BROKER&_program=sfadhoc.actual_report_2023.sas&who_box=101912 | PRIMARY |
| pwr/pwr_actual_{2025,2024,2023}__STATE.pdf (+ .txt) | Same reports, State Total (All Districts) | BROKER&_program=sfadhoc.actual_report_YYYY.sas&who_box=_STATE | PRIMARY |
| pwr/longitudinal_10yr_101912.html (+ .txt) | Longitudinal Data: 10 Year History for Houston ISD (2015-16..2024-25) | BROKER&_program=sfadhoc.longitudinal_10_years_report.sas&who_box=101912 (returns HTML) | PRIMARY |
| raw/pwr_101912_2425.html, raw/pwr_hisd_2425.html | HTML versions of the 2024-25 HISD and state reports (first probes) | BROKER (ptype omitted) | PRIMARY |
| raw/2425_FinActRep.html, 2324_FinActRep.html, 2223_FinActRep.html, 2122_FinActRep.html, 2425_allcamp_ActRep.html, 2324_allcamp_ActRep.html, 2425_new_camp_actual.html, 2324_new_camp_actual.html, 2425_stacked_bar_charts.html, 2324_longitudinal.html | Report-selector pages (used to discover `_program` names) | https://rptsvr1.tea.texas.gov/school.finance/forecasting/financial_reports/<name>.html | PRIMARY (index) |

## PEIMS actual financial data organized by campus (HISD, all campuses)
| File | Title | URL | Status |
|---|---|---|---|
| campus/allcamp_actual_2025_101912.pdf (+ .txt) | 2024-2025 PEIMS Actual Financial Data, Organized by Campus — HISD (272 campuses, 544 pp) | BROKER&_program=sfadhoc.allcamp_actual_report_2025.sas&who_box=101912 | PRIMARY |
| campus/allcamp_actual_2024_101912.pdf (+ .txt) | 2023-2024 ... by Campus — HISD | BROKER&_program=sfadhoc.allcamp_actual_report_2024.sas&who_box=101912 | PRIMARY |
| campus/allcamp_actual_2023_101912.pdf (+ .txt) | 2022-2023 ... by Campus — HISD | BROKER&_program=sfadhoc.allcamp_actual_report_2023.sas&who_box=101912 | PRIMARY |

## TAPR (Texas Academic Performance Reports)
| File | Title | URL | Status |
|---|---|---|---|
| tapr/tapr_2025_101912.pdf (+ .txt) | 2024-25 TAPR, HOUSTON ISD (101912), district level (34 pp) | https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&_program=perfrept.perfmast.sas&_debug=0&ccyy=2025&lev=D&id=101912&prgopt=reports/tapr/paper_tapr.sas | PRIMARY |
| tapr/tapr_2024_101912.pdf (+ .txt) | 2023-24 TAPR, HISD | same, ccyy=2024 | PRIMARY |
| tapr/tapr_2023_101912.pdf (+ .txt) | 2022-23 TAPR, HISD | same, ccyy=2023 | PRIMARY |
| tapr/tapr2025_all_d_STAF.csv, tapr2025_all_d_STUD.csv, tapr2025_all_d_REF.csv | TAPR 2025 data download, all districts: staff, student, reference | POST https://rptsvr1.tea.texas.gov/cgi/sas/broker/ with _program=perfrept.perfmast.sas, tapr=all_d, ccyy=2025, dsname=STAF/STUD/REF, prgopt=reports/tapr/dd/dd_tapr_step_7.sas, key=<all variable groups>, datafmt=csv (form at https://rptsvr1.tea.texas.gov/perfreport/tapr/tapr_dd_download.html?year=2025) | PRIMARY |
| tapr/tapr2024_all_d_STAF.csv, tapr2024_all_d_STUD.csv | TAPR 2024 data download, all districts | same, ccyy=2024 | PRIMARY |
| tapr/tapr2025_all_s_STAF.csv, tapr2025_all_s_STUD.csv, tapr2024_all_s_STAF.csv | TAPR state-level data download | same, tapr=all_s | PRIMARY |
| tapr/tapr2025_index.html, tapr_srch.html, tapr_dd_download.html, dd_*.html | TAPR index / search / data-download step pages | https://rptsvr1.tea.texas.gov/perfreport/tapr/2025/index.html etc. | PRIMARY (index) |

## School FIRST (Financial Integrity Rating System of Texas)
| File | Title | URL | Status |
|---|---|---|---|
| first/first_District_{YYYY}_{CDN}.html | FIRST "District Status Detail" for HISD + 7 peers, app years 2020–2024 = rating years 2021-22..2025-26 (data years 2020-21..2024-25) | https://tealprod.tea.state.tx.us/First/forms/District.aspx?year=YYYY&district=CDN (needs a session cookie from Main.aspx first; see scripts/fetch_first.py) | PRIMARY |
| first/first_main.html | FIRST public app main page (district status summary) | https://tealprod.tea.state.tx.us/First/forms/Main.aspx | PRIMARY |
| first/first_page.html | TEA "Financial Integrity Rating System of Texas (FIRST)" info page | https://tea.texas.gov/data-reports/financial-compliance/financial-integrity-rating-system-texas-first | PRIMARY |
| first/news_2425_first.html | TEA news release: Final 2024-2025 Financial Accountability Ratings | https://tea.texas.gov/about-tea/news-and-multimedia/news-releases/news-2025/tea-releases-final-2024-2025-financial-accountability-ratings | PRIMARY |

## Texas Comptroller — School District Property Value Study (PVS)
| File | Title | URL | Status |
|---|---|---|---|
| comptroller/pvs_2024F_1011019121D.html (+ pvs_2024F.txt) | 2024 ISD Summary Worksheet (Final), Houston ISD 101-912 | https://comptroller.texas.gov/auto-data/PT2/PVS/2024F/1011019121D.php | PRIMARY |
| comptroller/pvs_2023F_1011019121D.html (+ .txt) | 2023 ISD Summary Worksheet (Final), HISD | https://comptroller.texas.gov/auto-data/PT2/PVS/2023F/1011019121D.php | PRIMARY |
| comptroller/pvs_2025P_1011019121D.html (+ .txt) | 2025 ISD Summary Worksheet (Preliminary), HISD | https://comptroller.texas.gov/auto-data/PT2/PVS/2025P/1011019121D.php | PRIMARY |

Comptroller FAST (Financial Allocation Study for Texas, fastexas.org): not downloaded — last ratings published for 2014-era data; not current.

## NES campus list sources
See section appended below by the NES-list compilation (folder `nes/`). `nes/hisd_press_2024-01-23_nes.pdf` = HISD press packet "HISD Announces 2023 School Ratings and New NES Schools" (2024-01-23), https://resources.finalsite.net/images/v1749059929/houstonisdorg/jv9khj7dvyeqxtt8qwpw/01-23-24-HISD_Press_Packet_HISD_Announces_2023_School_Ratings_and_New_NES_Schools.pdf — PRIMARY (HISD).


## NES campus list sources (folder `nes/`; compiled into `data/hisd_nes_campuses.csv`; all retrieved 2026-10-06)
| File | Title | URL | Retrieved | Status |
|---|---|---|---|---|
| nes/hisd_arcgis_schools_2025-26.json | HISD ArcGIS layer "HISD Schools 2025–2026" (owner demographics_HoustonISD; web map "HISD New Education System (NES) Schools", snippet "All 130 NES Schools for the 2025–2026 School Year", modified 2025-08-06). Fields NES_Flag + NES_Type (`NES 2023`=28, `NES-A 2023`=57, `NES 2024`=45) + Campus_Nbr + TEA_Campus | https://services7.arcgis.com/YNiGsHEfQPYkIqX5/arcgis/rest/services/HISD_Schools/FeatureServer/6/query?where=1%3D1&outFields=*&returnGeometry=false&f=json (map: https://www.arcgis.com/home/item.html?id=6c764719408f495983165c03d14d0bae) | 2026-10-06 | PRIMARY (HISD) |
| nes/hisd_press_2024-01-23_nes.pdf (+ .txt) | HISD press packet "HISD Announces 2023 School Ratings and New NES Schools" (85 current NES/NES-aligned, 26 mandatory 2024-25 joiners, 24 high-D eligible) | https://resources.finalsite.net/images/v1749059929/houstonisdorg/jv9khj7dvyeqxtt8qwpw/01-23-24-HISD_Press_Packet_HISD_Announces_2023_School_Ratings_and_New_NES_Schools.pdf | 2026-10-06 | PRIMARY (HISD) |
| nes/hisd_news_nine_join_nes_2026-27.html (+ .txt) | HISD Now "Nine Houston ISD Campuses to Join New Education System Next Year" — states no additional campuses became NES for 2025-26; 9 ES join 2026-27; Alcott & Port Houston close after 2025-26 | https://hisdnow.houstonisd.org/p/~board/district-news/post/nine-houston-isd-schools-to-join-new-education-system-next-year | 2026-10-06 | PRIMARY (HISD) |
| nes/houstonlanding_2023-07-11_57aligned.html (+ .txt) | Houston Landing, "Houston ISD announces 57 more schools are joining slimmed-down 'reform' program" (full list of 57 NES-aligned) | https://houstonlanding.org/houston-isd-nes-schools-new-mike-miles/ | 2026-10-06 | SECONDARY |
| nes/leadernews_2023-07_aligned.html (+ .txt) | The Leader News, "HISD announces final list of NES-aligned campuses" (Jul 12, 2023; confirms Highland Heights in original 28) | https://www.theleadernews.com/education/hisd-announces-final-list-of-nes-aligned-campuses/article_b598191e-2132-11ee-a966-eb331d1c2b0e.html | 2026-10-06 | SECONDARY |
| nes/fox26_2024-02_nes_added.html (+ .txt) | FOX 26, "Houston ISD announces schools added to New Education System for 2024-2025" (19 opt-ins + 5 decliners) | https://www.fox26houston.com/news/houston-isd-schools-added-to-new-education-system-2024-2025 | 2026-10-06 | SECONDARY |
| nes/click2houston_2024-02-09_19optin.html (+ .txt) | KPRC Click2Houston, "LIST: Houston ISD announces 19 additional campuses joining the New Education System next year" | https://www.click2houston.com/news/local/2024/02/09/houston-isd-to-announce-14-more-campuses-joining-the-new-education-system-next-year/ | 2026-10-06 | SECONDARY |
| nes/hpm_2024-02-09_19optin.html (+ .txt) | Houston Public Media, "Houston ISD releases final list of NES campuses, including Austin High and 18 elementary and middle schools" (85 + 45 = 130) | https://www.houstonpublicmedia.org/articles/news/education-news/hisd/2024/02/09/477127/houston-isd-releases-final-list-of-nes-campuses-including-austin-high-and-18-elementary-and-middle-schools/ | 2026-10-06 | SECONDARY |

Not retrievable: blogs.houstonisd.org (DNS fails; June 2023 NES principal/school announcements), KHOU (Akamai 403), Good Reason Houston NES overview PDF (served HTML). Campus IDs = `101912` + zero-padded HISD Campus_Nbr, each verified against TEA names in `campus/allcamp_actual_2025_101912.txt`.
Data caveat found: `data/hisd_campus_actuals.csv` mislabels 20 campus names (e.g. 101912310 "Horn El" is Houston MSTC; 101912478 "Anderson El" is Arabic Immersion; 101912081 "Sharpstown H S" is Sharpstown International) — IDs are right, names are wrong.
