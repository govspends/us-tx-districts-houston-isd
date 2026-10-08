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

---

## FY2019-FY2021 (history extension, 2026-10-07)

New sources (see `../sources/acfr/SOURCES.md`): `HISD_ACFR_FY2019.pdf` (201 pp), `HISD_ACFR_FY2020.pdf` (208 pp), `HISD_ACFR_FY2021.pdf` (180 pp), plus the already-held `HISD_ACFR_FY2022.pdf` for the FY2022 column and FY2021 comparatives. Citation key as above: `FY19 p.48` = PDF page 48 of `HISD_ACFR_FY2019.pdf` (= Nth form-feed page of the `.txt`). All three have a full text layer except a few image-only pages (FY2020's auditor's report pp.23-25, which I read visually from a rendered page, marked "(visual)"; FY2021's finding page p.170). No figure in this section is OCR'd. Same auditor all three years: **Weaver and Tidwell, L.L.P.** Consolidated series: `../data/hisd_history_gf_fy2019_2025.csv`.

### H0. Key takeaways

1. **FY2019-FY2022 were four straight General Fund surpluses (revenue − expenditure): +$209.4M, +$118.2M, +$20.9M, +$114.6M** (FY19 p.48, FY20 p.44, FY21 p.36, FY22 p.36). Every one of those years was *adopted* as a deficit (original budget net change −$35.6M, −$23.2M, −$34.0M, −$82.1M; RSI FY19 p.106, FY20 p.101, FY21 p.92, FY22 p.91).
2. **GF fund balance grew $514.2M [calc] from $612.7M (6/30/2018) to $1,126.9M (6/30/2022)**, then was flat through FY2023 and fell to $748.1M by 6/30/2025 (§3 above). The FY2025 level is back between the 6/30/2019 ($819.0M) and 6/30/2018 ($612.7M) levels.
3. **Unassigned GF balance:** $512.3M (FY19) → $655.1M (FY20) → $556.3M (FY21) → $664.2M (FY22) = 3.09 / 4.22 / 3.15 / 4.00 months of that year's GF expenditures [calc]. The FY2025 figure (2.48 months) is the lowest of FY2019-FY2025.
4. **Recapture expense swung with HB3 (86th Legislature, 2019):** $265.2M (FY19) → $80.8M (FY20) → $197.8M (FY21) → $184.5M (FY22). The FY2020 and FY2021 adopted budgets carried $0 and $12.1M; actual came in $80.8M and $197.8M (RSI FY20 p.101, FY21 p.92).
5. **Debt principal fell steadily:** $3,289.0M (7/1/2018) → $3,084.3M → $2,855.7M → $2,616.9M → $2,387.7M (6/30/2022) (FY20 p.75, FY21 p.68, FY22 p.69). Every debt issuance in FY2019-FY2022 was refunding/remarketing debt, not new money (see H7).
6. **Audit opinions were unmodified every year, but FY2019-FY2021 each had a financial-reporting MATERIAL WEAKNESS**, which the FY2023-FY2025 audits did not: FY2019 board governance (TEA investigation) and improper cutoff; FY2020 capital leases and goods receipts (plus two significant deficiencies); FY2021 in-kind revenue/expenditures. HISD was not a "low-risk auditee" in any of the three years.

### H1. Governmental funds: totals by fund ($)

Sources: SRECFB FY19 p.48, FY20 p.44, FY21 p.36, FY22 p.36. In FY2019-FY2022 there was a fifth (nonmajor) fund, the Capital Renovation Fund – PFC.

| Fund | Item | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---|---:|---:|---:|---:|
| General | Revenues | 2,200,600,360 | 1,981,814,081 | 2,139,390,332 | 2,107,492,062 |
| General | Expenditures | 1,991,206,129 | 1,863,604,372 | 2,118,499,494 | 1,992,857,365 |
| General | **Rev − Exp** | **209,394,231** | **118,209,709** | **20,890,838** | **114,634,697** |
| General | Other financing sources (net) | (3,079,097) | 30,696,635 | 7,834,726 | 15,648,159 |
| General | Net change in fund balance | 206,315,134 | 148,906,344 | 28,725,564 | 130,282,856 |
| Special Revenue | Revenues | 383,024,258 | 381,676,122 | 358,803,707 | 694,171,619 |
| Special Revenue | Expenditures | 356,315,031 | 417,471,213 | 348,816,742 | 670,399,489 |
| Debt Service | Revenues | 283,308,996 | 299,501,637 | 316,279,642 | 322,260,136 |
| Debt Service | Expenditures | 515,637,853 | 513,609,020 | 404,855,587 | 460,688,301 |
| Capital Renovation | Revenues | 53,346,518 | 36,911,775 | 31,748,932 | 31,804,643 |
| Capital Renovation | Expenditures | 338,763,269 | 277,285,162 | 74,722,576 | 55,163,371 |
| Cap. Renovation – PFC (nonmajor) | Rev / Exp | 426,090 / 271,879 | 68,193 / 968,193 | 4,160 / 0 | 136 / 0 |
| **All governmental** | **Revenues** | **2,920,706,222** | **2,699,971,808** | **2,846,226,773** | **3,155,728,596** |
| **All governmental** | **Expenditures** | **3,202,194,161** | **3,072,937,960** | **2,946,894,399** | **3,179,108,526** |
| All governmental | Net change in fund balance | (68,516,777) | (131,979,309) | (7,163,774) | 128,865,481 |
| All governmental | Ending fund balance | 1,559,458,068 | 1,427,478,759 | 1,433,379,807 | 1,562,245,288 |

- FY2021 beginning Special Revenue (and total) fund balance was restated **+$13,064,822** for GASB 84 (FY21 p.36).
- Debt Service "payments to escrow agents – current refunding" were $162.1M (FY19), $168.8M (FY20), $49.05M (FY21), $110.5M (FY22). The FY2025 statistical table calls these "remarketing of variable interest debt, not a true debt refunding" (FY25 p.130 note 1).
- The FY2019-FY2020 Capital Renovation spending ($338.8M, $277.3M) is the tail of the 2012 bond program; capital-fund restricted balances fell from $453.4M (FY19) to $205.6M (FY21) (FY25 p.128).

### H2. Revenues by source, all governmental funds ($)

Sources: own SRECFBs (pages as H1) and the FY25 ten-year table (FY25 p.129). FY2019-FY2021 tie exactly. FY2022 differs by $1-2 from FY25 p.129 (see H10).

| Source | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|---:|
| Property taxes | 2,024,206,276 | 2,010,279,432 | 2,115,531,365 | 2,114,671,149 |
| Investment earnings | 41,075,497 | 24,338,742 | 2,781,757 | 4,423,438 |
| Misc. local | 83,112,013 | 64,380,498 | 67,633,938 | 91,436,525 |
| **Total local** | **2,148,393,786** | **2,098,998,672** | **2,185,947,060** | **2,210,531,112** |
| State: per capita (ASF) | 94,244,907 | 60,517,457 | 91,895,823 | 95,775,051 |
| State: Foundation School Program | 227,892,870 | 71,137,762 | 111,670,653 | 50,889,775 |
| State: TRS on-behalf (non-cash) | 76,909,310 | 85,470,235 | 86,923,365 | 81,873,575 |
| State: other | 40,381,995 | 31,203,794 | 28,765,063 | 17,539,418 |
| **Total state** | **439,429,082** | **248,329,248** | **319,254,904** | **246,077,819** |
| **Federal** | **332,883,354** | **352,643,888** | **341,024,809** | **699,119,665** |
| **Total** | **2,920,706,222** | **2,699,971,808** | **2,846,226,773** | **3,155,728,596** |
| Share local / state / federal **[calc]** | 73.6 / 15.0 / 11.4 % | 77.7 / 9.2 / 13.1 % | 76.8 / 11.2 / 12.0 % | 70.0 / 7.8 / 22.2 % |
| Total revenue per enrolled student **[calc]** | $13,923 | $12,853 | $14,452 | $16,216 |

State-source breakdown is from FY25 p.129 (the SRECFBs give only a state total). FY2019's $227.9M FSP is unusually high; the FY2019 MD&A attributes the GF increase "primarily [to] the increase in State sourced funding" (FY19 p.36). Federal revenue roughly doubled in FY2022 as ESSER ramped up (FY22 p.36).

### H3. General Fund revenue by source ($)

| | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|---:|
| Property taxes | 1,747,189,582 | 1,715,002,326 | 1,801,428,452 | 1,794,873,129 |
| Investment earnings | 19,083,204 | 14,027,724 | 2,342,077 | 3,341,346 |
| Misc. local | 15,082,252 | 9,972,928 | 12,241,775 | 19,373,978 |
| State | 399,872,504 | 218,933,263 | 295,665,220 | 228,667,029 |
| Federal | 19,372,818 | 23,877,840 | 27,712,808 | 61,236,580 |
| **Total** | **2,200,600,360** | **1,981,814,081** | **2,139,390,332** | **2,107,492,062** |
| Property tax share of GF revenue **[calc]** | 79.4% | 86.5% | 84.2% | 85.2% |

Sources: FY19 p.48, FY20 p.44, FY21 p.36, FY22 p.36. M&O tax rate: $1.0400 (FY19) → $0.9700 (FY20, HB3 compression) → $0.9664 (FY21) → $0.9277 (FY22) (§5a above).

### H4. General Fund expenditures by function ($)

| Function | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|---:|
| Instruction | 970,793,048 | 996,399,361 | 1,081,410,519 | 980,058,268 |
| Instr. resources & media | 9,822,477 | 7,798,643 | 9,071,254 | 6,732,685 |
| Instr. staff development | 29,267,000 | 29,215,532 | 33,204,034 | 31,637,515 |
| Instructional leadership | 20,820,355 | 20,983,417 | 23,904,023 | 24,155,192 |
| School leadership | 142,326,291 | 149,489,190 | 146,408,036 | 146,733,334 |
| Guidance & counseling | 50,299,761 | 60,053,228 | 63,467,347 | 59,348,406 |
| Social work | 8,429,482 | 12,142,590 | 16,938,834 | 17,955,510 |
| Health | 19,312,797 | 21,317,891 | 48,100,766 | 31,234,756 |
| Transportation | 59,243,844 | 53,629,143 | 46,389,028 | 51,909,647 |
| Food services | 0 | 234,114 | 2,741,097 | 50,603 |
| Extracurricular | 15,549,148 | 16,107,773 | 14,536,297 | 16,464,559 |
| General administration | 41,097,974 | 32,135,554 | 32,663,797 | 37,490,457 |
| Plant maintenance & ops | 195,853,168 | 192,496,074 | 211,943,777 | 218,863,332 |
| Security | 22,606,971 | 24,179,218 | 27,507,090 | 30,024,646 |
| Data processing | 54,951,868 | 62,025,501 | 65,812,348 | 58,213,621 |
| Community services | 2,135,207 | 3,828,274 | 2,631,134 | 1,948,276 |
| JJAEP | 792,000 | 792,000 | 792,000 | 724,500 |
| TIRZ payments | 58,465,450 | 61,321,789 | 61,491,720 | 65,956,709 |
| Tax appraisal & collection | 14,990,752 | 14,980,471 | 15,517,042 | 15,553,451 |
| **Recapture** ("Chapter 41/Purchase of WADA"; FY22 "Contracted instructional services between public schools") | **265,231,840** | **80,843,995** | **197,810,414** | **184,470,759** |
| Debt service (principal + interest, capital leases) | 8,946,862 | 14,995,323 | 14,818,736 | 10,250,591 |
| Capital outlay | 269,834 | 8,635,291 | 1,340,201 | 3,080,548 |
| **Total GF expenditures** | **1,991,206,129** | **1,863,604,372** | **2,118,499,494** | **1,992,857,365** |
| GF exp. excluding recapture & TIRZ **[calc]** | 1,667,508,839 | 1,721,438,588 | 1,859,197,360 | 1,742,429,897 |
| ...per enrolled student **[calc]** | $7,949 | $8,195 | $9,440 | $8,954 |

Sources as H3. The FY2021 health line ($48.1M, vs $21.3M in FY20) and FY2020-21 data processing reflect COVID-19 spending; the FY2021 MD&A says the GF budget variance was "primarily driven by Chapter 41/WADA payments and COVID-19 pandemic related expenditures" (FY21 p.30). For comparison, the same per-student measure is $9,615 (FY23), $11,263 (FY24), $12,098 (FY25) (§2d above). So GF operating spending per student rose about 52% from FY2019 to FY2025 [calc], most of it after FY2022.

### H5. GF budget vs actual (RSI, $)

Sources: FY19 p.106, FY20 p.101, FY21 p.92, FY22 p.91. FY2023-FY2025 are in §2e above.

| | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|---:|
| Original budget: revenues | 1,977,345,003 | 1,903,085,694 | 1,972,054,361 | 2,081,127,566 |
| Original budget: expenditures | 1,996,983,851 | 1,923,742,406 | 1,991,093,833 | 2,186,550,176 |
| Original budget: net change in FB | (35,600,621) | (23,201,689) | (33,988,612) | (82,076,315) |
| Final budget: expenditures | 2,167,653,402 | 2,051,838,084 | 2,330,879,400 | 2,209,721,030 |
| Final budget: net change in FB | (86,736,798) | (89,739,826) | (206,965,474) | (144,400,998) |
| **Actual net change in FB** | **+206,315,134** | **+148,906,344** | **+28,725,564** | **+130,282,856** |
| Actual exp. vs final budget | $176.4M under | $188.2M under | $212.4M under | $216.9M under |
| Actual vs ORIGINAL net change **[calc]** | +$241.9M better | +$172.1M better | +$62.7M better | +$212.4M better |
| Recapture: original / final / actual | 272.4M / 274.8M / 265.2M | 0 / 75.4M / 80.8M | 12.1M / 136.6M / 197.8M | 213.3M / 178.8M / 184.5M |

Across FY2019-FY2024 the actual GF result beat the *original* (adopted) budget every year, by +$62.7M to +$241.9M [calc; FY23 +$100.9M, FY24 +$88.7M from §2e]. **FY2025 is the first year in the series that came in worse than adopted** (−$168.0M [calc]). HISD's own narratives:
- FY19: "Chapter 41/WADA payments were $10 million less than budgeted" (FY19 p.38).
- FY20: the year-end amendment added "$75.4 [million] in recapture payments" and transferred out to offset; GF fund balance rose "$149 million … primarily due to decreased spending during the last quarter … when campuses were closed as a result of the COVID-19 pandemic" (FY20 p.36, p.34).
- FY21: "$61.2 million over budget in recapture due to the ADA hold harmless adjustment" (FY21 p.30).

### H6. General Fund fund balance components ($)

Sources: balance sheets FY19 p.46, FY20 p.42, FY21 p.34, FY22 p.34; 6/30/2018 from FY25 p.128.

| Component | 6/30/2018 | 6/30/2019 | 6/30/2020 | 6/30/2021 | 6/30/2022 |
|---|---:|---:|---:|---:|---:|
| Nonspendable | 11,394,093 | 11,893,235 | 14,510,708 | 20,562,375 | 16,488,097 |
| Restricted | 0 | 0 | 0 | 0 | 0 |
| Committed | 46,364,840 | 46,364,840 | 46,364,840 | 94,146,930 | 97,481,219 |
| Assigned | 165,504,729 | 248,407,583 | 251,970,374 | 325,593,638 | 348,770,724 |
| Unassigned | 389,415,008 | **512,328,146** | **655,054,226** | **556,322,769** | 664,168,528 |
| **Total GF fund balance** | **612,678,670** | **818,993,804** | **967,900,148** | **996,625,712** | **1,126,908,568** |
| Year-over-year change | – | +206,315,134 | +148,906,344 | +28,725,564 | +130,282,856 |

Coverage **[calc]** (as in §3 above; FY2022 repeated for continuity):

| | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---:|---:|---:|---:|
| Total GF FB, months of GF exp. | 4.94 | 6.23 | 5.65 | 6.79 |
| Unassigned, months | 3.09 | 4.22 | 3.15 | 4.00 |
| Unassigned as % of GF exp. | 25.7% (ACFR: "26 percent") | 35.1% ("35 percent") | 26.3% ("26 percent") | 33.3% |

ACFR percentages: FY19 p.36, FY20 p.34, FY21 p.28. The FY2022 6/30 components tie to §3 above. Other governmental fund balances for these years are in FY25 p.128 (e.g., Debt Service restricted $104.6M / $112.9M / $116.3M).

### H7. Long-term liabilities, governmental activities ($)

Sources: FY2019 roll-forward FY19 p.81 (the text layer there overlays two pages; values were confirmed by arithmetic: opening + increases − decreases = closing for each line). FY20 p.75; FY21 p.68; FY22 p.69. The statement-of-net-position cross-check is FY19 p.43.

| | 7/1/2018 | 6/30/2019 | 6/30/2020 | 6/30/2021 | 6/30/2022 |
|---|---:|---:|---:|---:|---:|
| Bonds payable (GO + PFC lease revenue) | 3,081,467,263 | 2,888,242,747 | 2,676,821,528 | 2,453,905,072 | 2,230,990,000 |
| Contractual obligations | 2,800,000 | 1,400,000 | 0 | – | – |
| Notes payable (maintenance tax notes) | 204,750,000 | 194,660,000 | 178,925,000 | 162,970,000 | 156,710,000 |
| **Debt principal subtotal** | **3,289,017,263** | **3,084,302,747** | **2,855,746,528** | **2,616,875,072** | **2,387,700,000** |
| Premium/discount | n/a | 208,960,718 | 184,647,567 | 145,211,365 | 105,530,671 |
| Accretion on capital appreciation bonds | n/a | 7,401,422 | 5,191,168 | 2,726,174 | 0 |
| Capital leases / leases | n/a | 13,598,328 | 52,603,995 | 36,340,506 | 40,734,466 (restated GASB 87 opening 40,366,399) |
| Compensated absences | n/a | 42,283,238 | 50,216,762 | 59,372,181 | 65,649,153 |
| Claims payable | n/a | 21,328,797 | 17,298,186 | 24,688,375 | 17,124,418 |
| **Net pension liability (TRS)** | 464,672,473 | **674,195,407** | **594,268,532** | **556,359,739** | **261,676,905** |
| **Net OPEB liability (TRS-Care)** | 652,967,581 | **792,318,535** | **716,497,750** | **540,884,130** | **531,819,720** |
| **Total governmental LT liabilities** | n/a | **4,844,529,192** | **4,476,470,488** | **3,982,457,542** | **3,410,235,333** |
| Debt principal per enrolled student **[calc]** | – | $14,703 | $13,595 | $13,287 | $12,269 |

- Debt issued: FY2019 "issued variable rate refunding debt with a par value of $159,945,000" on June 21, 2019 (FY19 p.37; p.48); FY2020 $148.9M and FY2021 $45.7M of refunding bonds (FY20 p.44, FY21 p.36); FY2022 issued $109.65M of refunding debt (FY22 p.36), but the FY22 roll-forward shows no bond "increases" (FY22 p.69). This is consistent with HISD's description of these as remarketings of variable-rate debt.
- **Net OPEB liability peaked at $792.3M (6/30/2019)**, more than double the $355.8M of 7/1/2023 (§4 above). Net pension liability bottomed at $261.7M (6/30/2022) before rising to $709.9M (6/30/2023). These swings come from TRS plan-level measurements, not district decisions.
- The FY25 statistical table (§5f) gives FY2019 gross bonded debt as $3,082,881,941, a different definition from the $3,084,302,747 principal subtotal here.

### H8. Government-wide (accrual) summary ($)

| | FY2019 | FY2020 | FY2021 |
|---|---:|---:|---:|
| Total expenses, governmental activities | 2,734,967,901 | 2,699,643,246 | 2,786,605,330 |
| Recapture expense line ("WADA-Chapter 41") | 265,231,840 | 80,843,995 | 197,810,414 |
| Change in net position, total | +272,430,896 | +173,814,549 | +226,266,530 |
| Total net position, end of year | 1,397,490,749 | 1,571,305,298 | 1,810,636,650 |
| Unrestricted net position (total) | (342,967,419) | (329,518,878) | (258,017,731) |

Sources: FY19 pp.43, 45; FY20 pp.40-41; FY21 pp.32-33. Unrestricted net position improved by about $85M from FY2019 to FY2021 [calc], then turned positive (+$93.5M) by FY2023 before falling to −$484.5M in FY2025 (§1b above).

### H9. Auditor's opinions and findings

| | FY2019 | FY2020 | FY2021 |
|---|---|---|---|
| Opinion on financial statements | Unmodified | Unmodified | Unmodified |
| Report date | Nov 19, 2019 (FY19 p.187) | Nov 13, 2020 (FY20 p.25, visual: page is image-only) | Nov 11, 2021 (FY21 p.164) |
| **Material weakness, financial reporting** | **Yes: 2019-001, 2019-002** | **Yes: 2020-001, 2020-002** | **Yes: 2021-001** |
| Significant deficiency, financial reporting | None reported | Yes: 2020-003, 2020-004 | No |
| Major-program compliance opinion | Unmodified | Unmodified | Unmodified |
| Compliance findings / questioned costs | None | None | None |
| Low-risk auditee? | No | No | No |
| Major federal programs | Title I, SpEd cluster, CTE, Magnet Schools, Title III, Title II, TSL/TIF, Title IV | Child Nutrition, CACFP, ESSER (84.425D) | Child Nutrition, CACFP, Coronavirus Relief Fund, Title I, SpEd, 21st CCLC, ESSER |
| Source | FY19 pp.189-192 | FY20 pp.192-200 | FY21 pp.164, 168-171 |

The findings:
- **2019-001 (material weakness: board governance):** TEA's investigation (final report Oct 30, 2019) found the Board of Trustees violated the Open Meetings Act, acted individually beyond its authority, and broke contract-procurement rules. TEA cited a "systemic breakdown of the HISD Board of Trustees' ability to govern" (FY19 p.191). FY2020 status: TEA's Nov 6, 2019 letter announced intent to appoint a board of managers; "A court ruling temporarily halted TEA's plans … The issue is still in litigation" (FY20 p.200). No status line appears in FY2021 (the board of managers was ultimately appointed June 1, 2023; §3 above).
- **2019-002 (material weakness: improper cutoff):** two capital-project invoices, about $7.17M, were not accrued (FY19 p.192). Marked Completed in FY2020 (FY20 p.200).
- **2020-001 (material weakness: capital leases):** unrecorded capital leases of about $19.8M of assets / $18.3M payable in the Internal Service Funds, and about $35.1M in the General Fund (FY20 p.194). Complete per FY21 p.171 status table.
- **2020-002 (material weakness: goods receipts):** goods marked received but not received; FY2020 expenditures understated about $1.7M (FY20 p.195).
- **2020-003 (significant deficiency):** checks held by departments, one for about six months before deposit (FY20 p.196).
- **2020-004 (significant deficiency):** receivables from other governments not evaluated for collectability (FY20 p.197).
- **2021-001 (material weakness: in-kind revenue and expenditures):** the condition text page (FY21 p.170) has no text layer. Only the title and corrective action plan are readable: "Staff will review grant agreements and continue to provide training to ensure that in-kind revenue and expenditures are properly and timely recorded" (FY21 p.171).

Compare FY2023-FY2025 (§7 above): no material weaknesses in any of those years. This is relevant context for claims about financial-control quality before and after the takeover.

### H10. Data quality and inconsistencies (FY2019-FY2022 vs existing FY2022+ figures)

1. **Recapture: the FY25 "Local Excess Revenue" table (FY25 p.141) does not match the audited expense line in any year checked.** Expense (fn 91; FY19 p.48, FY20 p.44, FY21 p.36, FY22 p.36; also FY25 p.130) vs FY25 p.141:
   - FY2017: $93.1M vs $91.5M
   - FY2018: $204.4M vs $168.3M
   - **FY2019: $265.2M vs $185.1M (−$80.1M)**
   - FY2020: $80.8M vs $74.9M
   - FY2021: $197.8M vs $198.1M
   - FY2022: $184.5M vs $186.5M

   The p.141 table is on a different (probably TEA entitlement-year) basis, and its footnotes are unreadable (§11 above). **Use the expense line, which is what the CSV uses.** This extends §10 item 13 above.
2. **FY2020 cost per pupil was misstated in the FY2020 ACFR:** $11,009 (FY20 p.160) vs $11,580 in the FY2021 and FY2025 ACFRs (FY21 p.138, FY25 p.156). 2,432,515,360 ÷ 210,061 = $11,580 [calc], so the FY2020 printing is wrong. The FY2020 operating-expenditure figure itself also includes the $168.8M escrow payment (§10 item 4 above).
3. **FY2022 all-governmental-funds revenue differs by $1-2 between the FY2022 ACFR and the FY2025 ten-year table:** misc. local 91,436,525 vs 91,436,524; federal 699,119,665 vs 699,119,666; total 3,155,728,596 vs 3,155,728,595 (FY22 p.36 vs FY25 p.129). This is rounding; the CSV uses the FY2022 ACFR.
4. **Notes payable in the FY2019 reconciliation is the long-term portion only:** $178,925,000 (FY19 p.47) vs $194,660,000 total in Note 8 (FY19 p.81). The difference is the $15,735,000 current portion. This is the same presentation as the FY2025 gap in §10 item 9 above, so that item is a recurring format, not a one-off error.
5. **FY2019 Note 8 (p.81) text layer is corrupted:** two pages' text is overlaid. Figures used here were verified by roll-forward arithmetic and against the FY2020 opening balances (FY20 p.75).
6. **Debt Service FY2022 refunding:** $109.65M "issuance of refunding debt" (FY22 p.36) does not appear as a bond increase in the FY2022 roll-forward (FY22 p.69). This is consistent with the remarketing explanation (H7), but the ACFR does not reconcile it explicitly.
7. **Image-only pages:** the FY2020 auditor's report (pp.23-25) and the FY2021 finding 2021-001 text (p.170) have no text layer.
8. **No inconsistency was found with the FY2022+ figures already in this file:**
   - The 6/30/2022 GF components (§3) tie to FY22 p.34.
   - FY2021 ending GF fund balance $996,625,712 + FY2022 change $130,282,856 = $1,126,908,568 ✓.
   - FY2019-FY2021 all-funds revenue ties exactly to FY25 p.129.
   - Enrollment (FY25 p.156) ties to FY19 p.157, FY20 p.160 and FY21 p.138.

### H11. Not found / not done

- FY2019-FY2021 SEFA / ESSER totals by year were not extracted (not requested). The CARES ESSER (84.425D) first appears as a major program in FY2020.
- The FY2019-FY2021 detail of the GF "assigned" balance (by purpose) was not extracted; only totals are given.
- The FY2021 finding 2021-001 condition text needs OCR or a visual read of FY21 p.170.
