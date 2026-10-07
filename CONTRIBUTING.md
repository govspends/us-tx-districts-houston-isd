# Contributing to the Houston Independent School District repository

This repository holds everything govspends has published about Houston ISD: the report pages under `docs/` and the evidence under `investigations/`. Changes to the website's Houston ISD pages are pull requests here; the [hub repository](https://github.com/govspends/govspends) holds the site itself, the tools and the [full contributing guide](https://github.com/govspends/govspends/blob/main/CONTRIBUTING.md), which applies here too.

**The one rule: show the source.** Every changed or added figure cites a document and page. New official documents go under `investigations/<investigation>/sources/` with a row in that investigation's `REFERENCES.md`. Do not add full copies of news articles or other copyrighted pages; cite them by URL and put the facts in the notes.

| You want to change | Edit |
|---|---|
| Report text, a hand-typed table, a caption | `docs/<investigation>/*.md` (or click the pencil on the website) |
| A table marked `generated:` in a page | the data file or script under `investigations/<investigation>/`, then `./tools.sh build_tables` |
| References, audit summary, notes | the files under `investigations/<investigation>/`, then `./tools.sh sync_docs` |
| This government's profile (`docs/index.md`) | the prose below the generated block; facts in `jurisdiction.toml`, then `./tools.sh build_site` |
| A new investigation of Houston ISD | add `[[investigation]]` to `jurisdiction.toml`, create `docs/<name>/` and `investigations/<name>/` |

`./tools.sh <tool>` fetches the hub's tools on first use (see the comments in the script). Continuous integration runs the same checks on every pull request and, after a merge to `main`, asks the hub to rebuild the website.

By contributing you agree that text and data are licensed under CC BY 4.0 and code under MIT, like the rest of the repository.
