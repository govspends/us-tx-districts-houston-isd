"""Fetch TEA School FIRST district rating pages (public, needs a session cookie from Main.aspx)
and parse rating/score/indicator scores into data/first_ratings.csv.

FIRST app 'year' param = first calendar year of the RATING year; rating year Y-(Y+1) is based on
school-year (Y-1)-Y data. e.g. year=2024 -> "2025-2026 rating based on SY 2024-2025".
Usage: python3 fetch_first.py   (re-downloads pages into sources/tea_peims/first/)
"""
import csv, html, http.cookiejar, os, re, sys, urllib.request

BASE = "https://tealprod.tea.state.tx.us/First/forms/"
OUT = "/git/Texas/HISD/sources/tea_peims/first"
DATA = "/git/Texas/HISD/data/first_ratings.csv"
DISTRICTS = {"101912": "Houston ISD", "057905": "Dallas ISD", "227901": "Austin ISD",
             "220905": "Fort Worth ISD", "015915": "Northside ISD", "101907": "Cypress-Fairbanks ISD",
             "101914": "Katy ISD", "079907": "Fort Bend ISD"}
YEARS = [2024, 2023, 2022, 2021, 2020]

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", "Mozilla/5.0")]


def get(url):
    return op.open(url, timeout=60).read().decode("utf-8", "replace")


def text(s):
    s = re.sub(r"(?is)<script.*?</script>|<style.*?</style>|<select.*?</select>", "", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?i)</tr>|<br\s*/?>|</p>|</div>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return "\n".join(l for l in (re.sub(r"\s+", " ", x).strip() for x in s.split("\n")) if l.strip("| "))


def parse(t):
    r = {}
    m = re.search(r"Financial Integrity Rating System of Texas\n(\d{4}-\d{4})\nRatings based on School Year (\d{4}-\d{4})", t)
    r["rating_year"], r["data_year"] = (m.group(1), m.group(2)) if m else ("", "")
    m = re.search(r"Rating:\n([^|\n]+)", t); r["rating"] = m.group(1).strip() if m else ""
    m = re.search(r"District Score:\n(\d+)", t); r["score"] = m.group(1) if m else ""
    # indicator rows: "N |\n<desc>\n| <date> | <score> |"
    t = t[t.find("# | Indicator Description"):]
    for m in re.finditer(r"\n(\d{1,2}) \|\n(.*?)\n\|[^|\n]*\| ([^|\n]+?)\s*(?:\||\n)", t, re.S):
        val = m.group(3).strip()
        if "not being evaluated" in m.group(2):
            val = "not evaluated" + ("" if val.endswith("Multiplier Sum") else f" ({val})")
        r[f"ind{int(m.group(1)):02d}"] = val
    return r


def main():
    get(BASE + "Main.aspx")
    rows = []
    for y in YEARS:
        for cdn, name in DISTRICTS.items():
            fn = f"{OUT}/first_District_{y}_{cdn}.html"
            if not os.path.exists(fn) or os.path.getsize(fn) < 120000:
                s = get(f"{BASE}District.aspx?year={y}&district={cdn}")
                open(fn, "w").write(s)
            t = text(open(fn).read())
            if "Internal Server Error" in t:
                print("ERR", y, cdn, file=sys.stderr); continue
            r = {"district": cdn, "name": name, "app_year_param": y}
            r.update(parse(t))
            rows.append(r)
    cols = ["district", "name", "app_year_param", "rating_year", "data_year", "rating", "score"] + [f"ind{i:02d}" for i in range(1, 22)]
    with open(DATA, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    for r in rows:
        print(r["name"], r["rating_year"], r["data_year"], r["rating"], r["score"])


if __name__ == "__main__":
    main()
