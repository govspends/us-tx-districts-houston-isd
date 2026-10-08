"""Download TEA TAPR "Profile" data-download CSVs (staff + student, one row per district / state) for
older TAPR years (2019..2022), where the newer step-by-step TAPR download tool (dd_tapr_step_7.sas,
used for 2024/2025 files) returns "This request completed with errors".

Old per-year form: https://rptsvr1.tea.texas.gov/perfreport/tapr/<YYYY>/download/DownloadData.html
  POST https://rptsvr1.tea.texas.gov/cgi/sas/broker  _service=marykay, _program=perfrept.perfmast.sas,
       prgopt=<YYYY>/tapr/tapr_download.sas, year4=YYYY, year2=YY, topic=acct, title=Data Download,
       sumlev=D (district) | S (state), setpick=PROF   -> CSV, row 1 = variable codes (DP*/SP*)
Usage: python3 fetch_tapr_dd.py 2019 2020 2021 2022
Writes sources/tea_peims/tapr/tapr{YYYY}_{D,S}PROF.csv (skips files that already exist).
"""
import os, sys, urllib.parse, urllib.request
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))   # the investigation folder

URL = "https://rptsvr1.tea.texas.gov/cgi/sas/broker"
OUT = ROOT + "/sources/tea_peims/tapr"


def main(years):
    for y in years:
        for sumlev in ("D", "S"):
            fn = f"{OUT}/tapr{y}_{sumlev}PROF.csv"
            if os.path.exists(fn) and os.path.getsize(fn) > 1000:
                continue
            fields = {"_service": "marykay", "prgopt": f"{y}/tapr/tapr_download.sas", "year4": y, "year2": y[2:],
                      "topic": "acct", "_debug": "0", "title": "Data Download", "_program": "perfrept.perfmast.sas",
                      "sumlev": sumlev, "setpick": "PROF"}
            req = urllib.request.Request(URL, data=urllib.parse.urlencode(fields).encode(),
                                         headers={"User-Agent": "Mozilla/5.0"})
            body = urllib.request.urlopen(req, timeout=600).read()
            if b"completed with errors" in body[:400]:
                print("ERROR", y, sumlev, file=sys.stderr); continue
            open(fn, "wb").write(body)
            print(y, sumlev, len(body), "bytes", body[:50])


if __name__ == "__main__":
    main(sys.argv[1:] or ["2019", "2020", "2021", "2022"])
