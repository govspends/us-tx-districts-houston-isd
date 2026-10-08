# HISD audited financial statements (ACFR) — sources

Retrieved 2026-10-06. All files downloaded from the HISD Controller's Office page
(<https://www.houstonisd.org/our-district/budget-financial-planning/controllers-office>,
tab "Annual Comprehensive Financial Report"). Saved copy of that page: `controller.html`.

| File | Title | URL | Retrieved | Type |
|---|---|---|---|---|
| `HISD_ACFR_FY2025.pdf` (200 pp, 113 MB) | HISD Annual Comprehensive Financial Report, FYE June 30, 2025. Auditor Weaver and Tidwell, L.L.P., opinion dated Jan 12, 2026; transmittal letter dated Jan 15, 2026. Server filename `Houston_ISD_2025_ACFR.pdf` | https://www.houstonisd.org/fs/resource-manager/view/6d01b7e7-86bd-4d0c-a29f-27fddf1f509a | 2026-10-06 | PRIMARY |
| `HISD_ACFR_FY2024.pdf` (186 pp) | HISD ACFR, FYE June 30, 2024 (transmittal dated Nov 14, 2024). Server filename `Houston_ISD_2024_ACFR.pdf` | https://www.houstonisd.org/fs/resource-manager/view/ed60c22c-a22a-4c4c-adf6-e533139df61e | 2026-10-06 | PRIMARY |
| `HISD_ACFR_FY2023.pdf` (199 pp) | HISD ACFR, FYE June 30, 2023 (PDF created Nov 28, 2023). The server filename is `Houston_ISD_FY24_ACFR.pdf`, but the link is labeled "2022–2023 Financial Report" and the cover says FYE June 30, 2023. The filename is wrong. | https://www.houstonisd.org/fs/resource-manager/view/52ff298e-cc6b-45ec-99f4-26104c1f1113 | 2026-10-06 | PRIMARY |
| `HISD_ACFR_FY2022.pdf` | HISD ACFR, FYE June 30, 2022 (used only for the FY2022 General Fund baseline). Server filename `HISD_FY22_ACFR.pdf` | https://www.houstonisd.org/fs/resource-manager/view/870213bc-e06f-4d71-82f7-9eb39444915c | 2026-10-06 | PRIMARY |
| `controller.html` | Snapshot of the HISD Controller's Office web page, listing ACFRs FY2008–FY2025 and Single Audits FY2013–FY2017 | https://www.houstonisd.org/our-district/budget-financial-planning/controllers-office | 2026-10-06 | PRIMARY (index page) |

SHA-256:
```
7bd8010f8ecf3c8e4cacc91adcc81f5618719c57e3fb9f02245739bfa61d011f  HISD_ACFR_FY2025.pdf
d8fcfcfaa317eab6a7b48adab6147ed720a5b4d135aa15a5f99bae9de0660520  HISD_ACFR_FY2024.pdf
09fc8c46cdf50241c6f53c881d8c6da4411c1381b4fb0e384038d5cc583e8e2e  HISD_ACFR_FY2023.pdf
86bbcefc9cb242a7b88740b3b89e13a60227ff1e78360b32298121b62fdc124d  HISD_ACFR_FY2022.pdf
```

### FY2025 split into parts (GitHub's per-file limit is 100 MB)

The FY2025 original is 109 MB (113 MB in decimal units), over GitHub's per-file limit. It was split with poppler (`pdfseparate` + `pdfunite`, run on 2026-10-07) into three parts, each under GitHub's 50 MB warning size. File names carry the **original PDF page ranges**, so a citation of "FY25 p.N" is page N − (start − 1) of the matching part.

| Part | Original pages | Pages |
|---|---|---|
| `HISD_ACFR_FY2025_p001-055.pdf` | 1–55 | 55 |
| `HISD_ACFR_FY2025_p056-086.pdf` | 56–86 | 31 |
| `HISD_ACFR_FY2025_p087-200.pdf` | 87–200 | 114 |

Checks against the original:
- Page counts sum to 200.
- Embedded images sum to 1,452 (584 + 0 + 868).
- `pdftotext -layout` output of the three parts, concatenated, is byte-identical to the original's.
- Rendered pages 3, 60, 72 and 150 are pixel-identical (PNG md5 at 60 dpi).

Bookmarks and document metadata are not carried over. To reassemble: `pdfunite HISD_ACFR_FY2025_p001-055.pdf HISD_ACFR_FY2025_p056-086.pdf HISD_ACFR_FY2025_p087-200.pdf HISD_ACFR_FY2025.pdf`.

```
e9dce676f692e8c47ccf3108182be40e3f417e362bd97b4bc316da59af0e4aa7  HISD_ACFR_FY2025_p001-055.pdf
0ddc11a4e827916fc578abd10e90a2f9b026d5c87c1d0bafed9c325f168d4868  HISD_ACFR_FY2025_p056-086.pdf
c6b736785c46d83ff901ceeaffb659cf5c226f395f412ae574e510d07073a6ee  HISD_ACFR_FY2025_p087-200.pdf
```

## Derived files (not sources)
- `HISD_ACFR_FY20xx.txt`: `pdftotext -layout` output. Pages are separated by form-feed characters, so "PDF page N" in the notes means the Nth form-feed-delimited page (the same as the PDF viewer page number).
- `ocr_fy2025/pN.txt`: Tesseract 5.5.3 OCR (300 dpi grayscale, `--psm 6`) of the FY2025 pages that have no text layer. That covers the transmittal letter, most of the MD&A, and all Notes to the financial statements (PDF pp. 48–94). The FY2025 PDF was re-assembled with pypdf, and those pages are images only. OCR'd figures were spot-checked against text-layer pages where possible, but read OCR digits with care.
- `pg.py`: helper that prints PDF page N from a `.txt` extraction.

## Not available / not retrieved
- **FY2026 ACFR (FYE June 30, 2026)**: not yet published as of 2026-10-06. The FY2025 report was not issued until January 2026; the transmittal cites a TEA filing-deadline extension to February 2026.
- Separate Single Audit reports after FY2017 are not posted on this page. From FY2018 on, the Single Audit is inside each ACFR's Compliance Section, which is what was used here.
- EMMA (MSRB) continuing-disclosure copies were not needed, because HISD's own site hosts the ACFRs.

## History extension: FY2019-FY2021 (retrieved 2026-10-07)

Downloaded from the same Controller's Office page (links in `controller.html`, tab "Annual Comprehensive Financial Report"). Each `/fs/resource-manager/view/<uuid>` link redirects to the `resources.finalsite.net` file shown. All three have a full text layer (the "Invalid Font Weight" warnings from pdftotext are harmless). The FY2020 auditor's report (PDF pp.23-25) is image-only. All files are under GitHub's 100 MB limit (largest: FY2020, 46.4 MB).

| File | Title | URL | Retrieved | Type |
|---|---|---|---|---|
| `HISD_ACFR_FY2021.pdf` (180 pp, 8.9 MB) | HISD Comprehensive Annual Financial Report, FYE June 30, 2021. Auditor Weaver and Tidwell, L.L.P., report dated Nov 11, 2021. Link label "2020–2021 Financial Report"; server filename `33832_2021_CAFR_ONLINE_12-07.pdf` | https://www.houstonisd.org/fs/resource-manager/view/b1415bb2-d32d-47b3-befa-7616c731e5e7 (→ https://resources.finalsite.net/images/v1749058598/houstonisdorg/rg9ivvr3qstwsohwftiq/33832_2021_CAFR_ONLINE_12-07.pdf) | 2026-10-07 | PRIMARY |
| `HISD_ACFR_FY2020.pdf` (208 pp, 46.4 MB) | HISD CAFR, FYE June 30, 2020. Weaver and Tidwell report dated Nov 13, 2020. Link label "2019–2020 Financial Report"; server filename `Houston_ISD_FY20_CAFR.pdf` | https://www.houstonisd.org/fs/resource-manager/view/14cb9e7e-9242-4567-84d3-8f676355d38b (→ https://resources.finalsite.net/images/v1749058599/houstonisdorg/dyiexj5mljfhd0zvlunb/Houston_ISD_FY20_CAFR.pdf) | 2026-10-07 | PRIMARY |
| `HISD_ACFR_FY2019.pdf` (201 pp, 11.6 MB) | HISD CAFR, FYE June 30, 2019. Weaver and Tidwell report dated Nov 19, 2019. Link label "2018–2019 Financial Report"; server filename `Houston_ISD_CAFR_FYE_2019.pdf` | https://www.houstonisd.org/fs/resource-manager/view/f8d48462-d3c7-46b7-8614-11cfff5f27d0 (→ https://resources.finalsite.net/images/v1749058599/houstonisdorg/vtks09ikkhlbv40rx8jl/Houston_ISD_CAFR_FYE_2019.pdf) | 2026-10-07 | PRIMARY |
| `HISD_ACFR_FY20{19,20,21}.txt` | `pdftotext -layout` output (derived) | – | 2026-10-07 | derived |

SHA-256:
```
6e63a573df0674e2062973c4594bb553a900b808dff7d5b1fff09361557e5064  HISD_ACFR_FY2019.pdf
2fe394e0bf1b64b70595581f9640e4c3c0d508bbf66f06895aee61c227798f04  HISD_ACFR_FY2020.pdf
6495f809e324fadc9352ea69f228d5e107665e354d9532b1ed8f6e9fede6cffe  HISD_ACFR_FY2021.pdf
```

Text-layer caveats:
- FY2019 PDF p.81 (Note 8, long-term liabilities) has two pages' text overlaid in the text layer. The figures used in the notes were verified by roll-forward arithmetic and against the FY2020 opening balances.
- FY2021 PDF p.170 (finding 2021-001 text) has no text layer.
