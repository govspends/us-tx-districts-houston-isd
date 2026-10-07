# HISD audited actuals: Annual Comprehensive Financial Reports (ACFR), FY2023–FY2025

District: Houston ISD (TEA 101-912). Fiscal year runs July 1 to June 30.
Prepared 2026-10-06. All files are in `../sources/acfr/` (see `SOURCES.md`).

**Citation key.** `FY25 p.41` means PDF page 41 of `HISD_ACFR_FY2025.pdf`. PDF page numbers equal the page numbers in the `.txt` extraction; printed page numbers differ (FY2025 printed page ≈ PDF − 10). An "(OCR)" tag means the page has no text layer and the figure comes from `ocr_fy2025/pNN.txt`. All dollar figures are copied from the reports unless marked **[calc]**, which means I computed them from cited inputs.

**Auditor:** Weaver and Tidwell, L.L.P. (Houston) for all three years. The FY2025 opinion is dated **January 12, 2026** (FY25 p.25). The FY2025 report came out late: the transmittal letter is dated Jan 15, 2026 and cites a TEA filing-deadline extension to February 2026 (FY25 p.8 OCR).
**FY2026 ACFR:** not yet published (as of 2026-10-06).

---

## 0. Key takeaways

1. **The General Fund (GF) ran an operating deficit in each of the three years, and the deficits grew:** −$20.2M (FY23), −$166.6M (FY24), −$310.6M (FY25). These are revenues minus expenditures, before transfers (FY23 p.40, FY24 p.39, FY25 p.41).
2. **GF fund balance:** $1,127.1M (6/30/2023) → $1,047.2M (6/30/2024) → **$748.1M (6/30/2025)**, a drop of **$379.0M [calc]** over the first two Board-of-Managers fiscal years.
   - Committed + assigned + unassigned fell **$501.2M** ($1,100.8M → $599.6M) **[calc]**.
   - All governmental funds fell **$546.2M** ($1,578.1M → $1,032.0M) **[calc]**.
   - The press figure of "~$450M" falls between these measures. No single audited line equals $450M; FY2026 actuals are not yet audited.
3. **Unassigned GF balance was exactly $590,067,862 at both 6/30/2023 and 6/30/2024.** The "Instructional Reserve" assignment absorbed the FY24 drawdown ($264.2M → $215.6M) and was zeroed in FY25. Unassigned then fell to **$464.8M = 2.48 months of GF expenditures [calc]**. Board policy, as stated in the notes, requires unassigned ≥ **3 months** of operating expenditures (FY25 p.59 OCR). The ACFR does not itself say the policy was breached, but on a total-GF-expenditure basis it was.
4. **The ESSER cliff is the main driver of falling total spending.**
   - Federal revenue, all governmental funds: $816.3M (FY23) → $779.8M (FY24) → $401.4M (FY25).
   - ESSER expenditures in the Schedule of Expenditures of Federal Awards (SEFA): ~$441.4M → ~$316.9M → ~$40.9M.
5. **Recapture (the "contracted instructional services between public schools" expense):** $276.4M (FY23) → **$0** (FY24) → **$56.9M** (FY25). The FY25 figure does not match TEA's SOF figure of $49.1M for SY24-25 (see §11).
6. **Debt fell sharply.** Bonds + notes: $2,123.2M (7/1/2023) → $1,813.6M → **$1,513.6M** (6/30/2025). As of 6/30/2025 HISD has **no authorized-but-unissued bond capacity** (the 2024 bond was defeated).
   - Net pension liability: $709.9M → $985.3M → $767.99M.
   - Net OPEB liability: $355.8M → $382.6M → $502.5M.
7. **Opinions were clean (unmodified) in all three years, with no material weaknesses.**
   - FY2023: one significant deficiency (accounts payable).
   - FY2024: no findings.
   - FY2025: three findings. One financial-reporting significant deficiency (SHARS revenue). Two ARP ESSER III compliance significant deficiencies: an equipment inventory failure (20 of 25 sampled assets unaccounted for or not counted) and $54,626 in questioned costs.

---

## 1. Government-wide Statement of Activities (accrual basis, governmental + business-type)

Sources: FY23 p.37; FY24 p.36; FY25 p.38. The 10-year version is in FY25 pp.126–127.

### 1a. Expenses by function, governmental activities ($)

| Function | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Instruction | 1,482,445,295 | 1,723,051,662 | 1,538,323,202 |
| Instructional resources & media | 17,405,973 | 14,622,709 | 6,784,883 |
| Instructional staff development (curriculum/PD) | 72,879,396 | 61,866,741 | 39,423,580 |
| Instructional leadership | 45,100,262 | 87,572,450 | 83,216,084 |
| School leadership | 159,095,322 | 212,820,052 | 229,399,368 |
| Guidance, counseling & evaluation | 102,772,324 | 86,549,574 | 80,801,202 |
| Social work services | 36,240,696 | 27,374,499 | 8,809,154 |
| Health services | 42,127,065 | 47,328,843 | 74,481,189 |
| Student transportation | 64,817,413 | 63,081,071 | 56,895,801 |
| Food service | 126,807,464 | 145,114,681 | 134,337,443 |
| Co-curricular / extracurricular | 37,139,862 | 40,057,606 | 40,029,492 |
| General administration | 67,632,844 | 67,212,911 | 66,188,602 |
| Plant maintenance & operations | 239,340,098 | 243,298,331 | 234,071,239 |
| Security & monitoring | 31,271,482 | 32,668,893 | 33,557,784 |
| Data processing | 84,536,654 | 107,334,299 | 52,214,950 |
| Community services | 14,222,218 | 15,795,831 | 11,814,114 |
| Fiscal agent / shared services | 3,612,568 | 4,476,468 | 4,250,433 |
| JJAEP | 579,600 | 583,200 | 583,200 |
| Tax reinvestment zone (TIRZ) payments | 72,368,633 | 75,544,048 | 56,066,884 |
| Tax appraisal & collection | 15,767,806 | 16,453,702 | 14,172,784 |
| **Contracted instructional svcs between public schools (recapture)** | **276,396,220** | **0** | **56,900,029** |
| Interest on long-term debt | 83,457,575 | 67,694,686 | 67,520,043 |
| **Total governmental activities** | **3,076,016,770** | **3,140,502,257** | **2,889,841,460** |
| Business-type (Medicaid, Marketplace) | 7,248,309 | 7,246,659 | 7,151,466 |
| **Total expenses** | **3,083,265,079** | **3,147,748,916** | **2,896,992,926** |

Curriculum development (function 13) has had no separate line since FY2016.

### 1b. Revenues, government-wide ($)

| Source | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Charges for services (governmental) | 13,207,059 | 13,419,655 | 11,831,109 |
| Operating grants & contributions (governmental) | 866,332,992 | 905,882,287 | 561,463,911 |
| M&O property taxes | 1,817,671,688 | 1,509,641,654 | 1,524,874,951 |
| Debt-service (I&S) property taxes | 349,664,760 | 357,639,974 | 363,098,260 |
| State aid not restricted to programs | 129,781,577 | 201,534,211 | 151,341,271 |
| Tax increment reinvestment zone | 36,725,241 | 33,387,318 | 54,530,380 |
| Unrestricted investment earnings | 71,527,732 | 93,375,084 | 67,964,633 |
| Miscellaneous | 74,785,789 | 4,340,986 | 4,021,073 |
| Transfers from business-type | 30,000,000 | 14,000,000 | 9,000,000 |
| **Change in net position, governmental** | **+313,680,068** | **−7,281,088** | **−141,715,872** |
| Change in net position, total | +295,725,945 | −21,762,590 | −155,942,432 |
| Total net position, end of year | 2,371,990,164 | 2,350,227,574 | 2,206,566,831 |
| Unrestricted net position (total) | 93,532,916 | (172,546,266) | **(484,539,292)** |

- FY2025 beginning net position was restated **+$12,281,689** for GASB 101 (FY25 p.38).
- The FY2025 MD&A attributes the revenue decline mainly to "decreases in grants and contributions": total revenues fell $385M (FY25 p.31 OCR).

---

## 2. Governmental funds: revenues, expenditures, changes in fund balance (modified accrual)

Sources: FY23 p.40; FY24 p.39; FY25 p.41.

### 2a. Totals by fund ($)

| Fund | Item | FY2023 | FY2024 | FY2025 |
|---|---|---:|---:|---:|
| General | Revenues | 2,154,751,784 | 1,982,608,752 | 1,940,386,056 |
| General | Expenditures | 2,175,000,800 | 2,149,214,679 | 2,250,964,487 |
| General | Rev − Exp | (20,249,016) | (166,605,927) | **(310,578,431)** |
| General | Other financing sources (net) | 20,409,368 | 86,733,707 | 11,470,045 |
| General | Net change in fund balance | 160,352 | (79,872,220) | **(299,108,386)** |
| Special Revenue | Revenues | 808,992,030 | 780,370,238 | 459,963,705 |
| Special Revenue | Expenditures | 803,273,145 | 778,582,836 | 477,224,076 |
| Debt Service | Revenues | 358,967,942 | 384,184,837 | 386,184,508 |
| Debt Service | Expenditures | 452,707,628 | 409,281,911 | 383,955,271 |
| Capital Projects | Revenues | 45,914,598 | 38,015,600 | 6,194,187 |
| Capital Projects | Expenditures | 41,238,985 | 103,860,432 | 38,736,820 |
| **All governmental** | **Revenues** | **3,368,626,354** | **3,185,179,427** | **2,792,728,456** |
| **All governmental** | **Expenditures** | **3,472,220,558** | **3,440,939,858** | **3,150,880,654** |
| All governmental | Net change in fund balance | 15,895,139 | (221,301,731) | (324,881,876) |
| All governmental | Ending fund balance | 1,578,140,427 | 1,356,838,696 | 1,031,956,820 |

HISD has no nonmajor governmental funds in FY2023–FY2025. The Public Facility Corporation was nonmajor only through FY2022 (FY25 p.129 note).

Large transfers drove the GF "other financing sources" line:
- **FY24:** $84.0M transferred into the GF, including **$70M of TIRZ funds moved from the Capital Projects Fund**, plus $18.2M of insurance recoveries (FY24 p.39; MD&A FY24 p.31).
- **FY25:** the original budget assumed **$80M from property sales**. The final budget cut this to $14M, and actual sales were **$30,000** (FY25 p.95).

### 2b. Revenues by source, all governmental funds ($)

Source: FY25 p.129, 10-year table; FY25 values tie to p.41.

| Source | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Property taxes | 2,157,325,323 | 1,864,110,487 | 1,884,862,928 |
| Investment earnings | 68,180,320 | 89,137,503 | 65,179,766 |
| Misc. local | 93,924,762 | 67,849,162 | 96,310,926 |
| **Total local** | 2,319,430,405 | 2,021,097,152 | 2,046,353,620 |
| State: per capita (ASF) | 109,660,859 | 70,931,424 | 101,406,956 |
| State: Foundation School Program | 23,366,522 | 139,019,349 | 56,544,571 |
| State: TRS on-behalf (non-cash) | 81,866,878 | 109,490,737 | 113,672,854 |
| State: other | 17,953,916 | 64,805,758 | 73,398,745 |
| **Total state** | 232,848,175 | 384,247,268 | 345,023,126 |
| **Federal** | 816,347,774 | 779,835,007 | 401,351,710 |
| **Total** | 3,368,626,354 | 3,185,179,427 | 2,792,728,456 |
| Share local / state / federal **[calc]** | 68.9 / 6.9 / 24.2 % | 63.5 / 12.1 / 24.5 % | 73.3 / 12.4 / 14.4 % |
| Total revenue per enrolled student **[calc]** | $17,736 | $17,301 | $15,803 |

### 2c. General Fund revenue by source ($)

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Property taxes | 1,809,366,483 | 1,506,848,009 | 1,523,111,132 |
| Investment earnings | 50,872,795 | 72,775,580 | 52,185,094 |
| Misc. local | 9,603,175 | 5,347,301 | 67,369,842 |
| State | 214,953,566 | 319,532,249 | 272,139,946 |
| Federal | 69,955,765 | 78,105,613 | 25,580,042 |
| Property tax share of GF revenue **[calc]** | 84.0% | 76.0% | 78.5% |

FY24 property tax revenue fell ~$300M. The cause was the 88th Legislature's compression of the maximum compression rate (MCR) by $0.1070 and the rise in the homestead exemption from $40k to $100k. The M&O rate went from $0.8705 to $0.7016. The FY24 MD&A shows the budget was cut by "$342.0 million due to the increase in exemptions and refunds" (FY24 p.33).

### 2d. General Fund expenditures by function ($)

| Function | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Instruction | 1,037,292,731 | 1,150,954,093 | 1,261,908,377 |
| Instr. resources & media | 18,410,029 | 13,830,385 | 6,952,956 |
| Instr. staff development | 29,076,351 | 25,815,707 | 14,265,492 |
| Instructional leadership | 22,530,676 | 63,063,461 | 68,430,832 |
| School leadership | 162,215,725 | 215,392,395 | 234,320,097 |
| Guidance & counseling | 65,086,596 | 64,717,439 | 67,564,581 |
| Social work | 8,351,000 | 4,712,785 | 8,418,802 |
| Health | 26,671,528 | 24,201,089 | 26,031,897 |
| Transportation | 52,317,948 | 57,023,753 | 52,179,127 |
| Food services | 86,050 | 71,239 | 118,309 |
| Extracurricular | 21,005,560 | 25,280,790 | 25,759,045 |
| General administration | 41,114,014 | 53,050,919 | 51,233,688 |
| Plant maintenance & ops | 227,609,507 | 235,307,348 | 215,104,150 |
| Security | 31,396,069 | 32,091,167 | 30,520,778 |
| Data processing | 51,198,314 | 58,440,335 | 44,249,043 |
| Community services | 1,909,451 | 7,050,496 | 5,148,816 |
| JJAEP | 579,600 | 583,200 | 583,200 |
| TIRZ payments | 72,368,633 | 75,544,048 | 56,066,884 |
| Tax appraisal & collection | 15,767,806 | 16,453,702 | 14,172,784 |
| Recapture | 276,396,220 | 0 | 56,900,029 |
| Debt service (principal + interest; leases/SBITAs) | 12,901,379 | 18,998,183 | 10,163,192 |
| Capital outlay | 715,613 | 6,632,145 | 872,408 |
| **Total GF expenditures** | **2,175,000,800** | **2,149,214,679** | **2,250,964,487** |
| GF exp. excluding recapture & TIRZ **[calc]** | 1,826,235,947 | 2,073,670,631 | 2,137,997,574 |
| ...per enrolled student **[calc]** | $9,615 | $11,263 | $12,098 |

**The shift to the General Fund under NES.** GF instruction rose $224.6M (+21.7%) from FY23 to FY25 while enrollment fell 7%. School leadership rose $72.1M (+44%), and instructional leadership roughly tripled ($22.5M → $68.4M). Meanwhile special-revenue (ESSER) instruction fell from $390.0M (FY23 and FY24) to $170.6M (FY25). The overall pattern is consistent with ESSER-funded costs migrating onto the GF as ESSER expired.

### 2e. GF budget vs actual

Sources: RSI, FY23 p.95; FY24 p.91; FY25 p.95.

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Original budget, net change in FB | (100,769,458) | (168,539,426) | (131,118,382) |
| Final budget, net change in FB | (164,930,325) | (194,381,109) | (247,332,216) |
| Actual net change | +160,352 | (79,872,220) | **(299,108,386)** |
| Actual expenditures vs final budget | $184.1M under | $78.0M under | **$74.7M over** |

FY2025 overspend drivers (MD&A FY25 p.35 OCR): "$59.9 million over budget in instructional salary and Texas Connections expenditures"; "$12.5 million in school leadership"; "$12.4 million in recapture."

FY2024: the original budget carried $326.5M of recapture. The final budget and the actual were $0 (FY24 p.91). The MD&A lists "Increase due to New Education System (NES) implementation of $69.2 million" (FY24 p.33).

---

## 3. General Fund fund balance

Sources: balance sheets FY23 p.38, FY24 p.37, FY25 p.39; detail notes FY23 p.59, FY24 p.57, FY25 p.59 (OCR); FY2022 from FY25 p.128.

| Component ($) | 6/30/2022 | 6/30/2023 | 6/30/2024 | 6/30/2025 |
|---|---:|---:|---:|---:|
| Nonspendable (inventory, prepaids) | 16,488,097 | 26,255,559 | 24,549,497 | 21,090,776 |
| Restricted (capital projects, i.e. TIRZ money) | 0 | 0 | 70,000,000 | 127,389,365 |
| Committed: contingency operating reserve | 97,481,219 | 98,991,251 | 99,874,040 | 101,134,650 |
| Assigned: total | 348,770,724 | 411,754,248 | 262,705,301 | 33,713,134 |
| … Instructional Reserve | n/a | 264,213,080 | 215,634,981 | **0** |
| … Encumbrances | n/a | 117,774,619 | 17,303,771 | 3,487,287 |
| … Insurance programs | n/a | 25,000,000 | 25,000,000 | 25,000,000 |
| … Auto/general liability | n/a | 4,766,549 | 4,766,549 | 5,225,847 |
| Unassigned | 664,168,528 | **590,067,862** | **590,067,862** | **464,760,389** |
| **Total GF fund balance** | **1,126,908,568** | **1,127,068,920** | **1,047,196,700** | **748,088,314** |
| Year-over-year change | +130,282,856 | +160,352 | −79,872,220 | −299,108,386 |

Coverage, computed as fund balance divided by that year's GF expenditures **[calc]**:

| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|
| GF expenditures | 1,992,857,365 | 2,175,000,800 | 2,149,214,679 | 2,250,964,487 |
| Total GF FB, months | 6.79 | 6.22 | 5.85 | **3.99** |
| Total GF FB, days | 206 | 189 | 178 | **121** |
| Unassigned, months | 4.00 | 3.26 | 3.29 | **2.48** |
| Unassigned, days | 122 | 99 | 100 | **75** |
| Unassigned as % of GF exp. | 33.3% | 27.1% (ACFR: "27 percent") | 27.5% (ACFR: "28 percent") | 20.6% (ACFR: "21 percent") |

- ACFR percentages are from FY23 p.32, FY24 p.31 and FY25 p.34 (OCR).
- Board policy as stated in the ACFR: "the District's unassigned fund balance at year end shall equal at least three months of operating expenditures" (FY25 p.59 OCR).

**Checking the "reserves fell ~$450M under the Board of Managers" claim.** The Board was appointed June 1, 2023, so the baseline is 6/30/2023. Through 6/30/2025:

| Measure | Change |
|---|---:|
| Total GF fund balance | −$379.0M |
| GF committed + assigned + unassigned ($1,100.8M → $599.6M) | −$501.2M |
| GF unassigned only | −$125.3M |
| All governmental funds | −$546.2M |
| Total net position (government-wide) | −$165.4M |
| Unrestricted net position | −$578.1M |

None of these equals $450M. The claim is directionally supported, but the number depends on the measure, and any FY2026 drawdown is not yet audited.

### 3b. Other governmental fund balances (FY25 p.128, 10-yr; tie to the balance sheets)

| $ | 6/30/2023 | 6/30/2024 | 6/30/2025 |
|---|---:|---:|---:|
| Special Revenue (restricted) | 111,111,759 | 114,228,504 | 101,940,294 |
| Debt Service (restricted) | 126,657,122 | 123,816,823 | 156,388,194 |
| Capital Projects: restricted | 176,767,699 | 67,606,370 | 40,692,826 |
| Capital Projects: assigned | 36,534,927 | 3,990,299 | 1,219,845 |
| Capital Projects: **unassigned (deficit)** | 0 | 0 | **(16,372,653)** |

---

## 4. Long-term liabilities (governmental activities)

Sources: FY24 p.70 roll-forward (gives the 7/1/2023 opening balances); FY25 p.72 (OCR) roll-forward; FY25 p.37 statement of net position.

| $ | 7/1/2023 | 6/30/2024 | 6/30/2025 |
|---|---:|---:|---:|
| Bonds payable (GO + PFC lease revenue) | 1,973,100,000 | 1,670,345,000 | 1,378,515,000 |
| Maintenance tax notes | 150,130,000 | 143,210,000 | 135,120,000 |
| **Debt principal subtotal** | **2,123,230,000** | **1,813,555,000** | **1,513,635,000** |
| Unamortized premium | 80,997,645 | 51,546,688 | 45,003,038 |
| Leases | 22,375,833 | 12,170,118 | 41,434,668 |
| Subscriptions (SBITA) | 16,977,708 | 5,857,595 | 11,201,847 |
| Compensated absences | 70,774,868 | 72,828,931 (restated to 60,593,093 by GASB 101) | 58,506,201 |
| Claims payable | 16,889,078 | 17,684,494 | 23,292,650 |
| **Net pension liability (TRS)** | **709,879,768** | **985,320,732** | **767,987,153** |
| **Net OPEB liability (TRS-Care)** | **355,822,534** | **382,621,558** | **502,451,392** |
| **Total governmental LT liabilities** | **3,396,947,434** | **3,341,585,116** | **2,963,511,949** |

Per enrolled student **[calc]**, using the enrollment in §5c:

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Debt principal per student | $11,179 | $9,850 | $8,565 |
| All governmental LT liabilities per student | $17,885 | $18,150 | $16,769 |

The ACFR's own "net bonded debt per student" is $10,375 / $8,808 / **$6,942** (FY25 p.146). Its "total debt per student" is $11,567 / $9,437 / $9,323 (FY25 p.148). Both use different numerators.

FY2025 debt activity (FY25 pp.72–73 OCR, p.35 OCR):
- $435.2M of refunding debt issued (Series 2025A $149.7M, Series 2025B, and maintenance tax refunding notes $20.555M).
- $452.3M paid to escrow.
- All variable-rate debt eliminated (was $190.435M).
- $115.42M of bonds defeased with debt-service cash on May 28, 2025.
- "As of June 30, 2025, the District had no authorized but unissued debt capacity."
- Debt matures through Feb 15, 2043.
- The transmittal says HISD approved "approximately $120 million in Maintenance Tax Notes" for facilities after the defeat of the 2024 bond (FY25 p.11 OCR). That issuance is not in the FY2025 debt notes.

TRS context (FY25 pp.96–99):
- District share of the TRS net pension liability: 0.012572604 (FY25) vs 0.014344383 (FY24).
- The state's share of the NPL associated with HISD is $938.8M.
- Contributions: $72.2M pension and $13.6M OPEB in FY2025.

---

## 5. Statistical section: 10-year tables (FY2016–FY2025)

All from the FY2025 ACFR (unaudited statistical section). The FY2023 ACFR (p.154) extends some series back to FY2014.

### 5a. Tax rates per $100 (FY25 p.137; p.140; Note 4, FY25 p.65 OCR)

| FY | M&O | I&S | Total |
|---|---:|---:|---:|
| 2016 | 1.0267 | 0.1700 | 1.1967 |
| 2017 | 1.0267 | 0.1800 | 1.2067 |
| 2018 | 1.0400 | 0.1667 | 1.2067 |
| 2019 | 1.0400 | 0.1667 | 1.2067 |
| 2020 | 0.9700 | 0.1667 | 1.1367 |
| 2021 | 0.9664 | 0.1667 | 1.1331 |
| 2022 | 0.9277 | 0.1667 | 1.0944 |
| 2023 | 0.8705 | 0.1667 | 1.0372 |
| 2024 | 0.7016 | 0.1667 | 0.8683 |
| 2025 | **0.7016** (p.140, Note 4); p.137 shows 0.7116 | 0.1667 | **0.8683**; p.137 shows 0.8783 |
| 2026 (TY2025, adopted) | 0.7116 (MCR 0.6322 + 5 golden pennies) | 0.1667 | 0.8783 (MD&A, FY25 p.36 OCR) |

### 5b. Assessed values, levy, collections (FY25 pp.135, 139)

| FY | Net taxable assessed value | Market ("actual") value | Levy | Collected in year | % |
|---|---:|---:|---:|---:|---:|
| 2016 | 152,860,482,797 | 206,223,497,079 | 1,776,902,751 | 1,738,512,893 | 97.84 |
| 2017 | 165,861,644,665 | 218,146,974,374 | 1,938,101,993 | 1,904,734,976 | 98.28 |
| 2018 | 171,610,628,471 | 223,346,451,297 | 2,002,012,192 | 1,963,918,398 | 98.10 |
| 2019 | 173,923,630,109 | 225,614,769,174 | 2,039,948,464 | 1,999,695,187 | 98.03 |
| 2020 | 185,535,534,086 | 241,869,462,270 | 2,048,599,091 | 1,993,877,549 | 97.33 |
| 2021 | 196,631,674,148 | 254,622,445,438 | 2,173,577,655 | 2,116,422,090 | 97.37 |
| 2022 | 200,674,561,625 | 261,122,664,175 | 2,140,410,545 | 2,094,213,784 | 97.84 |
| 2023 | 218,175,138,362 | 289,410,570,643 | 2,224,027,089 | 2,160,912,769 | 97.16 |
| 2024 | 229,523,362,674 | 323,352,954,180 | 1,931,098,418 | 1,865,340,503 | 96.59 |
| 2025 | 233,190,075,832 | 326,864,555,391 | 1,959,305,399 | 1,892,588,797 | 96.59 |

- Exemptions: $65.1B (FY23) → $84.4B (FY24) → $87.1B (FY25). The state homestead exemption grew from $9.16B to $22.76B to $23.18B (FY25 p.136).
- Principal taxpayers, FY2025 (FY25 p.138): CenterPoint Energy $2.295B (0.98%), Chevron Chemical $761M, HG Galleria $747M, Valero $654M, BSREP 1HC-4HC $652M, and others. The top 10 total $7.97B (3.42% of AV), down from 5.25% in FY2016.

### 5c. Enrollment, ADA, teachers, cost per pupil, economically disadvantaged (FY25 p.156)

| FY | Enrollment | Refined ADA | Teachers | Student/teacher | Operating exp. (ACFR) | Cost per pupil (ACFR) | Free/reduced lunch % |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2016 | 215,627 | 195,544.38 | 12,010 | 18.0 | 1,909,369,634 | 8,855 | 75.39 |
| 2017 | 216,106 | 193,735.35 | 12,062 | 18.7 | 1,993,593,224 | 9,225 | 81.20 |
| 2018 | 214,175 | 194,492.28 | 12,368 | 17.3 | 2,354,485,916 | 10,978 | 89.90 |
| 2019 | 209,772 | 190,087.02 | 11,569 | 18.1 | 2,312,607,490 | 11,024 | 97.10 |
| 2020 | 210,061 | 189,736.11 | 11,856 | 18.0 | 2,432,515,360 | 11,580 | 97.71 |
| 2021 | 196,943 | 177,045.49 | 11,866 | 16.6 | 2,508,647,952 | 12,738 | 96.90 |
| 2022 | 194,607 | 170,473.34 | 11,192 | 17.4 | 2,760,175,438 | 14,183 | 98.70 |
| 2023 | 189,934 | 167,780.55 | 11,143 | 17.0 | 3,061,729,773 | 16,120 | 90.00 |
| 2024 | 184,109 | 164,053.20 | 11,907 | 15.5 | 2,865,717,426 | 15,565 | 79.55 |
| 2025 | 176,727 | 157,037.46 | 10,960 | 16.1 | 2,696,768,941 | 15,260 | 77.77 |

- ACFR definitions: "Operating Expenditures are total governmental expenditures less debt service and capital outlay"; cost per pupil = operating expenditures ÷ enrollment.
- These figures include ESSER/grant spending, recapture and TIRZ pass-throughs. For example, FY2025 operating expenditures **excluding recapture and TIRZ** are $2,583.6M, or **$14,619 per pupil [calc]**.
- See §11 for inconsistencies in how HISD computed this series.

### 5d. Teacher salaries (FY25 pp.157–158)

| FY | HISD avg beginning | Region 4 avg beginning | State avg beginning | HISD avg salary | Region 4 avg salary | State avg salary | Pay scale (BA) min–max |
|---|---:|---:|---:|---:|---:|---:|---|
| 2016 | 51,051 | 49,117 | 45,507 | 55,431 | 55,580 | 51,891 | 51,500–71,500 |
| 2020 | 47,742 | 53,229 | 49,868 | 56,340 | 60,292 | 57,091 | 54,369–80,309 |
| 2022 | 50,771 | 53,963 | 51,054 | 59,161 | 62,589 | 58,887 | 56,869–84,309 |
| 2023 | 54,587 | 58,169 | 53,300 | 64,954 | 64,502 | 60,717 | 61,500–87,500 |
| 2024 | 60,583 | 58,202 | 54,272 | 67,073 | 66,411 | 62,474 | 61,500–87,500 |
| 2025 | 56,238 | N/A | N/A | **71,119** | N/A | N/A | 64,000–90,000 |

FY2025 is the first year with a "No Degree" teacher category: 974.9 teachers (p.158).

### 5e. Employees by function (FY25 p.155; FTE + hourly, excluding substitutes)

| | FY2016 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Instruction (11) | 13,763 | 11,226 | 11,656 | 12,603 | 11,063 |
| Instructional leadership (21) | 236 | 324 | 316 | 628 | 641 |
| School leadership (23) | 2,520 | 2,216 | 2,287 | 2,265 | 2,218 |
| Social work (32) | 57 | 361 | 394 | 55 | 53 |
| General administration (41) | 426 | 459 | 561 | 471 | 456 |
| Plant M&O (51) | 1,954 | 2,172 | 2,115 | 1,535 | 1,496 |
| **Total** | **25,001** | **22,081** | **23,098** | **22,156** | **20,532** |

### 5f. Debt ratios (FY25 pp.145–148)

| FY | Gross bonded debt | Net bonded debt | Net bonded/AV | Net bonded per student | Total debt (primary gov't) | Total debt per student | Total debt per capita |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2016 | 3,154,354,223 | 3,075,365,261 | 2.01% | 14,262 | 3,232,517,797 | 14,991 | 2,184 |
| 2019 | 3,082,881,941 | 3,044,000,722 | 1.75% | 14,511 | 3,314,263,215 | 15,799 | 2,137 |
| 2022 | 2,322,132,646 | 2,262,071,102 | 1.13% | 11,624 | 2,533,965,138 | 13,021 | 1,605 |
| 2023 | 2,042,319,272 | 1,963,860,929 | 0.90% | 10,375 | 2,250,987,159 | 11,567 | 1,425 |
| 2024 | 1,721,891,688 | 1,619,049,503 | 0.71% | 8,808 | 1,836,571,815 | 9,437 | 1,163 |
| 2025 | 1,415,319,284 | 1,276,072,323 | 0.55% | 6,942 | 1,566,271,515 | 9,323 | 992 |

- The FY2025 legal debt margin is $17.10B, so net debt is 6.95% of the limit.
- Direct + overlapping debt is $6.61B, of which HISD's direct share is $1.611B (p.147).
- Debt service is 12.64% of non-capital expenditures in FY2025 (p.130).

### 5g. Recapture history (FY25 p.141, "Local Excess Revenue")

| FY | Amount |
|---|---:|
| 2017 | $91.5M |
| 2018 | $168.3M |
| 2019 | $185.1M |
| 2020 | $74.9M (footnoted) |
| 2021 | $198.1M |
| 2022 | $186.5M |
| 2023 | $275.3M |
| 2024 | $0 (footnoted) |
| 2025 | $56.9M |

The footnote text is not in the text layer. The expense-side table (p.130) shows FY2020 $80.8M and FY2023 $276.4M, which differ from this table.

### 5h. Schools

FY2025 transmittal (p.9 OCR): **274 schools** = 8 early childhood centers + 159 elementary + 39 middle + 37 high + 31 combination/alternative, plus 7 contracted external charter schools. Average building age is 46 years. The building-by-building capacity and enrollment tables are on FY25 pp.159–180.

---

## 6. Federal awards and the ESSER cliff (SEFA)

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Total federal expenditures (SEFA) | 836,623,445 (FY23 p.195) | 736,678,395 (FY24 p.182) | 389,630,012 (FY25 p.197) |
| U.S. Dept. of Education total | 644,274,074 | 594,062,010 | 254,378,186 |
| ESSER (84.425D/U/W) | 441,377,491 (ACFR subtotal, FY23 p.193) | ~316.9M **[calc]**, sum of 84.425 lines | ~40.9M **[calc]** |
| Title I, Part A (+D, 1003) | 127,821,881 | 167,242,527 | 126,638,071 |
| Child Nutrition Cluster | 137,568,498 | 130,387,118 | 124,295,373 |
| Total state awards (SESA) | 930,146 | 1,023,031 | 974,148 |
| Major federal programs audited | Title I, ESSER, FEMA COVID PA | Child Nutrition, SpEd cluster, 21st CCLC, CTE | Title I, Title III-A, Title II-A, Title IV-A, ARP ESSER |
| Low-risk auditee? | **No** | Yes | Yes |

---

## 7. Auditor's opinions and findings

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Opinion on financial statements | Unmodified | Unmodified | Unmodified (with GASB 101 emphasis paragraph) |
| Material weakness, financial reporting | No | No | No |
| Significant deficiency, financial reporting | **Yes**: 2023-001 | None | **Yes**: 2025-001 |
| Major-program compliance opinion | Unmodified | Unmodified | Unmodified |
| Significant deficiency, compliance | None | None | **Yes**: 2025-002, 2025-003 |
| Questioned costs | None | None | **$54,626** |
| Source | FY23 pp.186–190 | FY24 pp.175–178 | FY25 pp.183–193 |

The findings:
- **2023-001 (accounts payable):** about $1.3M of construction goods and services were not recorded, understating Capital Projects Fund expenditures and liabilities. It is marked Complete in FY2024. Two FY2022 findings (capital-asset disposal; incorrect recording of an entry) are also marked Complete.
- **2025-001 (SHARS revenue):** SHARS revenue and the related accrual were misstated because the HHSC 2023 Cost Settlement report "was not provided timely to the Controller's Office."
- **2025-002 (ARP ESSER III equipment):** there was no physical inventory within two years. About 45% of campuses did not take part in the 6/30/2024 inventory, and "20 out of the 25 assets we selected … were either shown as 'unaccounted for' or excluded from the counts." The assets were mainly buses, band instruments and HVAC units.
- **2025-003 (TCLAS ARP ESSER III, allowable costs):** costs were charged after the Nov 30, 2024 liquidation deadline. Questioned costs are $54,626.

---

## 8. MD&A and transmittal narrative on the big changes (quotes)

**Enrollment**
- FY23 (p.9): "Enrollment decreased from the 2021-22 school year by 5,317 students."
- FY24 (p.8): "decreased from the 2022-23 school year by 5,825 students. The 2024-25 budget includes an additional reduction of 4,011 students."
- FY25 (p.9 OCR): "decreased from the 2023-24 school year by 7,382 students. The 2025-26 budget includes an additional reduction of 6,528 students."

**NES**
- FY24 (p.9): Miles introduced "Destination 2035" and the NES, with "increased salaries, incentive payments, and stipends for teachers" and support staff to grade papers and make copies.
- FY24 budget (p.33): "Increase due to New Education System (NES) implementation of $69.2 million."
- FY25 (p.10 OCR): "The district extended the NES model to 45 additional campuses in 2024-25, reallocating central resources."

**ESSER**
- FY25 MD&A (p.31 OCR): "Total revenues decreased by $385 million from the prior year due primarily to decreases in grants and contributions."
- Special Revenue Fund balance "decreased by $12 million … due to a decrease in federal funds" (p.34 OCR).
- FY23 and FY24 budget amendments moved stipends and performance-contract costs onto ESSER: −$13.8M (FY23 p.34) and −$18.2M (FY24 p.33).

**Deficit and fund balance**
- FY25 (p.34 OCR): "The fund balance of the General Fund decreased $299.1 million … unassigned fund balance of $464 million represented 21 percent of the total General Fund expenditures."
- None of the three MD&As discusses the 3-month policy floor or uses the word "deficit."

**Bond and facilities**
- FY25 (p.11 OCR): "Following the defeat of the 2024 bond proposal, HISD approved approximately $120 million in Maintenance Tax Notes."
- TEA "extended its intervention in HISD through June 2027."

**FY2026 outlook**
- FY25 (p.36 OCR): the 2025-26 GF budget projects a "$175.4 million" revenue increase and "$54.3 million" expenditure increase. ADA is estimated at 151,666 and WADA at 223,312. Total FY2026 expenditures are estimated at $2.121B.
- Legislative changes: basic allotment raised to $6,215; homestead exemption raised from $100k to $140k; MCR cut a further $0.0194.

---

## 9. Comparison hooks for the other tracks

**ACFR state FSP vs. TEA SOF.**
- ACFR FY2025 governmental-funds "Foundation school program" $56.5M + "Per capita" $101.4M = **$157.95M [calc]**.
- TEA SOF total FSP/ASF state aid for SY24-25 is $172.0M.
- The two differ in basis: the SOF is an entitlement and settle-up view, while ACFR revenue is modified accrual, includes prior-year settle-ups, and some state aid sits in the Special Revenue and Debt Service funds.
- The government-wide "State aid not restricted" line for FY2025 is $151.3M.

**Recapture.** ACFR FY2025 expense is $56,900,029, versus TEA SOF $49.1M for SY24-25. The ACFR shows $0 for FY2024, although the FY24 original budget carried $326.5M.

**TRS on-behalf.** $113.7M of FY2025 "state revenue" is non-cash TRS on-behalf contributions, offset by equal expenditures. Exclude it when comparing to TEA aid.

---

## 10. Data quality and inconsistencies

1. **Unassigned GF balance is identical in FY23 and FY24: $590,067,862.** It ties in both audited balance sheets (FY23 p.38, FY24 p.37), so it is not a typo. Unassigned was held constant while the "Instructional Reserve" assignment fell from $264.2M to $215.6M. In FY2025 the reserve went to $0 and unassigned fell. Readers should watch assigned plus unassigned, not unassigned alone.
2. **FY2024 committed/assigned differ between the FY25 statistical table and the audited FY24 balance sheet.** The statistical table (FY25 p.128) shows committed 98,991,251 and assigned 263,588,090. The balance sheet (FY24 p.37) shows 99,874,040 and 262,705,301. The totals agree; $882,789 is reclassified.
3. **The FY2025 tax-rate table (p.137) shows 0.7116/0.8783 for FY2025.** Note 4 (p.65 OCR) and the levy table (p.140) give **0.7016/0.8683**. The p.137 row appears to carry the TY2025 (FY2026) rate.
4. **The "cost per pupil" series is not computed consistently.** Recomputing operating expenditures as total governmental expenditures minus principal, interest, fiscal charges, escrow payments and capital outlay:
   - FY2017 matches exactly.
   - FY2020, FY2021 and FY2022 are overstated by exactly the refunding escrow payments ($168.8M, $49.05M, $110.5M). Debt refunding cash was treated as "operating."
   - FY2023 is overstated by $107.1M.
   - FY2024 is understated by $28.7M.
   - FY2025 is within $0.2M.
   - Recomputed per-pupil cost: FY2022 $13,615 (vs $14,183 stated); FY2023 $15,556 (vs $16,120); FY2024 $15,721 (vs $15,565) **[calc]**.
5. **FY2023 real property value looks like a typo.** FY2023 is 227,761,078,835 and FY2022 is 207,761,078,835 (identical except one digit; FY25 p.135).
6. **The "Total collections to date" column equals the in-year collections for FY2023–FY2025** even though subsequent-year collections are non-zero. The column is not maintained (p.139).
7. **The principal-employers table (FY25 p.152) uses FinanceCharts.com worldwide headcounts.** For example, Schlumberger shows 110,000 employees, "3.17%" of Houston MSA employment. These are global, not Houston, figures, and the table is not comparable to FY2016 (Houston Chronicle source).
8. **The GASB 101 restatement has the wrong sign in Note 1.** Note 1 says "($12,281,689)" (FY25 p.49 OCR), but the statements add +$12,281,689 to beginning net position (p.38).
9. **There is a $7,645,000 gap in FY2025 notes payable.** The FY2025 reconciliation (p.40) shows notes payable $(127,475,000), while the statement of net position and Note 8 show $135,120,000 (current portion $7,645,000).
10. **The FY2025 MD&A contains stale or impossible statements.** "Fully funded construction commitments of $8.6 million, $7.7 million … spent and $90 million in remaining commitment" (p.34 OCR) does not add up. "Remaining … maintenance tax notes … $143.210 million as of June 30, 2024" (p.35 OCR) is a prior-year figure. It says "88th Legislature in 2025" (should be 89th). The Note 15 subsequent event repeats the $20.555M tender note, dated 7/31/2025, which conflicts with the March 2025 tender in Note 8.
11. **The FY2025 PDF on houstonisd.org is defective.** About 95 of 200 pages are images with no text layer, including all the Notes and most of the MD&A. The first MD&A text page (normally "Financial Highlights") appears to be missing: PDF p.27 is the section divider and p.28 begins mid-sentence. The certificate of board reads "1 th day of [blank] 2026" (p.7).
12. **The HISD website mislabels the FY2023 file.** The FY2023 ACFR is served as `Houston_ISD_FY24_ACFR.pdf` and labeled "2022–2023."
13. **Recapture figures disagree across schedules and sources.**
    - FY2020: $80.8M (expense, p.130) vs $74.9M (p.141).
    - FY2023: $276.4M vs $275.3M.
    - FY2025: $56.9M (ACFR) vs TEA SOF $49.1M vs secondary "$55.5M."
14. **FY2023 enrollment differs between reports.** The FY2023 ACFR (p.154) shows 189,290; the FY2025 table shows 189,934. 189,290 is the FY2023 "membership" figure in FY25 p.156.

---

## 11. What I could not find or verify

- **FY2026 audited actuals:** the ACFR for FYE 6/30/2026 is not published yet.
- **Footnote text for the recapture table (FY25 p.141)** explaining FY2020 "*" and FY2024 "**": not in the text layer, and not OCR'd because the page has a text layer. It needs a visual check of the PDF.
- **An ACFR-level split of NES vs non-NES campus spending:** the ACFR reports by function only, so the budget documents are needed.
- **FY2025 MD&A "Financial Highlights" page:** apparently missing from the posted PDF (see §10 item 11).
- **Function 13 (curriculum development):** reported as $0 since FY2017 (FY25 p.126). The ACFR does not say where NES curriculum-writing costs are booked. They are probably in instruction or instructional staff development, but this is unverified.
- **TEA's statewide comparison of the FY2024 and FY2025 student/teacher ratio:** "N/A" in the ACFR.
- **FY2025 Region and state teacher-salary comparisons:** "N/A" in the ACFR.
