# Houston Independent School District — govspends

Public-records investigation of Houston ISD (HISD), Texas, part of [govspends](https://github.com/govspends/govspends). **Read it on the website: https://govspends.github.io/govspends/us/tx/districts/houston-isd/**

| Investigation | Status |
|---|---|
| [Funding and spending, FY2023-FY2027](https://govspends.github.io/govspends/us/tx/districts/houston-isd/hisd-funding/) | First edition (2026-10-07), not independently reviewed |

## What is here

```
jurisdiction.toml               this government's entry in govspends (name, level, fiscal year, websites) and its investigations
docs/index.md                   the profile page (generated facts block + prose)
docs/hisd-funding/               the report, one page per section; references, sources list, audit summary and notes
                                 generated from the evidence folder
investigations/hisd-funding/     the evidence: sources/ (TEA, HISD and Comptroller documents), data/ (parsed tables, metrics,
                                 text extractions), scripts/, notes/ (per-track research findings), REFERENCES.md,
                                 AUDIT_SUMMARY.md, MANIFEST_SHA256.txt
tools.sh                        runs the shared govspends tools against this repository (uses the hub in the parent folder
                                 when cloned inside it as govspends/us-tx-districts-houston-isd/, otherwise fetches the hub
                                 into .hub/)
```

The website is built by the hub repository, which clones this repository and every other government repository, assembles one site and publishes it. A merge to `main` here triggers that rebuild.

## Contributing

Pull requests here change the Houston ISD pages and evidence; see [CONTRIBUTING.md](CONTRIBUTING.md). Full-page copies of the news articles used in the research are held in a private archive and are not republished; they are cited by URL.

## Provenance and license

This investigation was prepared on 2026-10-06 to 2026-10-07 with an AI assistant (Claude) working from public records under a person's direction. It has not yet had an independent review; see [AUDIT_SUMMARY.md](investigations/hisd-funding/AUDIT_SUMMARY.md) for the method, corrections made during the work, and known unreconciled figures. Text, data and images: [CC BY 4.0](LICENSE-CONTENT.md). Code: [MIT](LICENSE). Not affiliated with Houston ISD or the Texas Education Agency.
