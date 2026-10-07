"""Minimal stdlib-only .xlsx reader (no openpyxl available on this host).

read_xlsx(path) -> {sheet_name: [[cell, ...], ...]}
Cells are str or float (numbers) or None. Handles shared strings and inline strings.
"""
import re
import zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
RELNS = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def _col_index(ref):
    letters = re.match(r"([A-Z]+)", ref).group(1)
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def read_xlsx(path, sheets=None):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    relmap = {r.get("Id"): r.get("Target") for r in rels.iter(RELNS + "Relationship")}
    out = {}
    for s in wb.find("m:sheets", NS):
        name = s.get("name")
        if sheets and name not in sheets:
            continue
        target = relmap[s.get("{%s}id" % NS["r"])]
        target = target.lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target
        root = ET.fromstring(z.read(target))
        rows = []
        for row in root.iter("{%s}row" % NS["m"]):
            cells = {}
            for c in row.findall("m:c", NS):
                idx = _col_index(c.get("r"))
                t = c.get("t")
                v = c.find("m:v", NS)
                if t == "s" and v is not None:
                    val = shared[int(v.text)]
                elif t == "inlineStr":
                    val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
                elif v is not None:
                    try:
                        val = float(v.text)
                    except ValueError:
                        val = v.text
                else:
                    val = None
                cells[idx] = val
            if cells:
                rows.append([cells.get(i) for i in range(max(cells) + 1)])
            else:
                rows.append([])
        out[name] = rows
    return out


if __name__ == "__main__":
    import sys
    d = read_xlsx(sys.argv[1])
    for k, v in d.items():
        print(k, len(v), "rows")
        for r in v[:int(sys.argv[2]) if len(sys.argv) > 2 else 5]:
            print("  ", r[:30])
