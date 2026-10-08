# Houston ISD — TEA Summary of Finances, 3-year trend (PRIMARY SOURCE)

Source documents (TEA Summary of Finances for Houston ISD, district 101912, supplied by the user):
- `sources/2025report.pdf` — SY2024-25, **Final** cycle, Run ID 46849, updated 2026-05-29
- `sources/2026report.pdf` — SY2025-26, **Near-Final** cycle, Run ID 47299, updated 2026-09-30
- `sources/Report_6_47240_2026-10-06T214926.pdf` — SY2026-27, **Preliminary** cycle, Run ID 47240, updated 2026-09-14 (a projection; superseded by run 47318 of 2026-10-05, `sources/sof_history/sof_2026-27_preliminary_run47318.pdf`, which the report pages use: total state aid $281,870,816)

Every figure uses each report's right-hand column (Final / Near-Final / Preliminary). The full line-item table is `data/sof_key_figures.csv`, produced by `scripts/sof_extract.py`, which also checks that the totals reconcile.

| Metric | SY2024-25 (Final) | SY2025-26 (Near-Final) | SY2026-27 (Prelim.) |
|---|---|---|---|
| Basic Allotment | $6,160 | $6,215 | $6,215 |
| Refined ADA | 156,870.772 | 150,014.180 | 148,533.310 |
| WADA | 229,410.254 | 221,658.897 | 217,925.522 |
| PEIMS enrollment | 176,727 | 167,571 | 167,571 |
| M&O tax rate / Tier One (compressed) rate | $0.7016 / $0.6516 | $0.7116 / $0.6322 | $0.7048 / $0.6254 |
| Total Cost of Tier One | $1,420,445,215 | $1,457,965,256 | $1,439,283,060 |
| Tier Two **state aid** | $26,673,074 | $36,803,382 | $31,040,001 |
| Tier Two **entitlement** (Level 1 + 2, state + local) | $131,629,547 | $201,826,100 | $192,781,624 |
| — Tier Two local share (HISD enrichment taxes) | $104,956,473 | $165,022,718 | $161,741,623 |
| Recapture paid | $49,122,872 | $0 | $0 |
| **TOTAL FSP/ASF STATE AID** | **$172,020,062** | **$313,668,063** | **$274,252,534** |
| State aid ÷ ADA | $1,097 | $2,091 | $1,846 |

## Why state aid jumped in SY2025-26 (correction to an earlier explanation)

An earlier version of this file said HISD got more state aid because it "lost so many students that it no longer generates excess local revenue." **That was wrong.** Falling enrollment lowers a district's entitlement, which pushes recapture *up*, not down. The SOF line items show what actually happened.

State aid rose by $141,648,001 from SY2024-25 to SY2025-26. State aid = Tier Two + Other Programs + Available School Fund + facilities homestead aid (ASAHE), so the change splits into:

| Component | Change |
|---|---|
| Other Programs | **+$145,225,541** |
|   of which: aid for the elderly/disabled homestead tax limitation (TEC §48.2542) | +$71,558,328 ($2.8M → $74.4M) |
|   of which: aid for districts hit by tax compression (TEC §48.283, new) | +$41,473,261 |
|   of which: aid for districts no longer subject to recapture (TEC §48.257(b-1), new): computed as the lesser of the local revenue shortfall or the Teacher Retention Allotment (2025-26 SOF p.59), so it funds the TRA | +$29,500,000 |
|   of which: instructional materials (§48.307/§48.308) | +$3,059,640 |
| Tier Two | +$10,130,308 |
| Available School Fund (per-capita rate fell from $619.87 to $470.81) | −$27,550,157 |
| Homestead aid for facilities (ASAHE) | +$13,842,309 |

About $113M of the increase (§48.2542 +$71.6M and §48.283 +$41.5M) is the **state replacing local property-tax revenue that the Legislature cut**: the additional $0.107 rate compression and the $40,000 → $100,000 homestead exemption of SB 2 (88th Legislature, 2nd Called Session, 2023), and the 2025 increase of the exemption to $140,000, with $60,000 more for over-65 and disabled homeowners (SB 4/SB 23, 89th Legislature). Those are hold-harmless payments. The $29.5M under §48.257(b-1) is different: it is how the state pays HISD's new Teacher Retention Allotment (HB 2, 2025) now that HISD no longer pays recapture, so it is new money tied to teacher pay. *(Corrected 2026-10-08 after independent review: an earlier version attributed the compression to the 2025 Legislature and called the whole increase "not new money".)*

**Why recapture disappeared:** the SY2026-27 compression worksheet (TEC §48.283 report, line 13) shows HISD would have owed **$156,310,803 in Tier One recapture** if the extra $0.1070 compression had not happened. The state cut HISD's tax rate and raised exemptions. That pushed local revenue below HISD's entitlement, so recapture went to $0, and the state now backfills the gap. HB2's new allotments also raised the entitlement: teacher retention $29.5M, basic costs $17.8M, school safety +$6.4M.

## What to take from this

1. The Basic Allotment did not fall: $6,160 → $6,215 (HB2 "Guaranteed Yield Increment Adjustment").
2. **Total formula funding per attending student (state + local) rose 11.8% in SY2025-26**: (Total Cost of Tier One + full Tier Two entitlement) ÷ refined ADA = **$9,894 → $11,064 → $10,988** (Final → Near-Final → Preliminary). *(Corrected 2026-10-08: earlier versions showed $9,225 → $9,964 → $9,899, which added Tier One's full entitlement to only Tier Two's state aid.)* Tier One rose $37.5M (new HB2 allotments of about $70M, offset by $38.4M less regular-program allotment as attendance fell); Tier Two rose $70.2M, mostly because the compressed rate fell from $0.6516 to $0.6322 while HISD's M&O rate rose from $0.7016 to $0.7116, so more of HISD's own tax effort counts as enrichment (DTR1 $0.0443 → $0.0703). The SY2026-27 preliminary assumes an M&O rate of $0.7048; HISD's proposed rate is $0.6754, which would lower the Tier Two entitlement.
3. The split between state and local shifted toward the state, mostly because the state cut local taxes and made up the difference, plus new allotments such as the TRA. The entitlement figures are not cash receipts or an adequacy measure.
4. A dollar of "state aid" in these reports is not always spendable on operations. ASAHE for facilities ($16.1M / $29.9M / $12.4M) supports debt service (I&S), and the Instructional Materials & Technology Fund is restricted.

## Caveats

- SY2025-26 is Near-Final and SY2026-27 is Preliminary, so both can be revised. SY2024-25 Final is the settled figure.
- An earlier per-student split ("local share = entitlement − total state aid") is only approximate, because total state aid includes items outside the operating entitlement (facilities homestead aid and instructional materials). Use audited ACFR revenue by source for an exact local/state/federal split.
- TEA's Final SOF shows $49.1M of SY2024-25 recapture. Texas Tribune's $55.5M figure is likely from a different payment cycle. Treat the TEA Final figure as authoritative.
