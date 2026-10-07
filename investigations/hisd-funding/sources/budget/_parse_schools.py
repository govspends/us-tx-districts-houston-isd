import re,sys,csv
txt=open(sys.argv[1]).read().split('\f')
pages=[int(x) for x in sys.argv[2].split('-')]
out=csv.writer(open(sys.argv[3],'w',newline=''))
rows=[]
money=r'\$?\s*\(?-?[\d,]+(?:\.\d+)?\)?|\$\s*-'
for p in range(pages[0],pages[1]+1):
    for line in txt[p-1].split('\n'):
        m=re.match(r'\s*(.+?)\s{2,}(\d{3})\s{2,}(NES-A|NES|Non-NES|NES-Aligned|NESA|[A-Za-z-]+)\s{2,}(.+?)\s{2,}(\S.+?)\s{2,}([\d,]+)\s+(\$.*)$',line)
        if not m: continue
        name,org,typ,lvl_div,feeder,enr,rest=m.groups()
        vals=re.findall(r'\$\s*([\d,]+\.\d{2}|-)',rest)
        vals=[0.0 if v=='-' else float(v.replace(',','')) for v in vals]
        if len(vals)==6: vals=vals[:4]+[0.0]+vals[4:]
        rows.append([p,name.strip(),org,typ,lvl_div.strip(),feeder.strip(),int(enr.replace(',',''))]+vals)
out.writerow(['pdf_page','campus','org','type','level_division','feeder','proj_enrollment','6100_payroll','6200_contracted','6300_supplies','6400_other_op','6600_capital','gf_total','title_i_alloc'])
for r in rows: out.writerow(r)
from collections import defaultdict
agg=defaultdict(lambda:[0,0,0.0,0.0])
for r in rows:
    if len(r)<14: print('SHORT',r); continue
    a=agg[r[3]]; a[0]+=1; a[1]+=r[6]; a[2]+=r[12]; a[3]+=r[13]
tot=[0,0,0,0]
for k,a in agg.items():
    print(f"{k:10s} n={a[0]:4d} enr={a[1]:8d} GF=${a[2]:,.0f} perstu=${a[2]/a[1]:,.0f} TitleI=${a[3]:,.0f}")
    for i in range(4): tot[i]+=a[i]
print(f"TOTAL n={tot[0]} enr={tot[1]} GF=${tot[2]:,.0f} perstu=${tot[2]/tot[1]:,.0f} TitleI=${tot[3]:,.0f}")
