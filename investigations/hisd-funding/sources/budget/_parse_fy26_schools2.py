import csv,re
from collections import defaultdict
rows=[]
for p in range(145,151):
    W=[x for x in csv.DictReader(open(f'_ocr26s/t{p}.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE) if x['text'].strip()]
    W=[dict(l=int(x['left'])/3,r=(int(x['left'])+int(x['width']))/3,t=int(x['top'])/3,s=x['text']) for x in W]
    pe=sorted(w['l'] for w in W if w['s']=='PEIMS')
    off=pe[1]-216 if len(pe)>1 else 0
    for w in W: w['l']-=off; w['r']-=off
    W.sort(key=lambda w:w['t'])
    lines=[]
    for w in W:
        if lines and abs(w['t']-lines[-1][0])<5: lines[-1][1].append(w)
        else: lines.append([w['t'],[w]])
    # determine x of header 'Enrollment' to bound
    for t,ws in lines:
        ws.sort(key=lambda w:w['l'])
        name=' '.join(w['s'] for w in ws if 95<=w['l']<212)
        org=''.join(w['s'] for w in ws if 212<=w['l']<245)
        typ=' '.join(w['s'] for w in ws if 255<=w['l']<330)
        if not re.match(r'^\d{3}$',org): continue
        toks=[w['s'].replace('$','').replace('S','') for w in ws if w['l']>500]
        toks=[x for x in toks if re.search(r'\d',x)]
        enr=None; money=[]
        for x in toks:
            x2=x.replace(',','')
            if re.fullmatch(r'\d+\.\d\d',x2): money.append(float(x2))
            elif re.fullmatch(r'\d+',x2) and enr is None and not money: enr=int(x2)
        tot=None; t1=None; ok=False
        for j in range(1,len(money)):
            if abs(sum(money[:j])-money[j])<1.5:
                tot=money[j]; t1=money[j+1] if j+1<len(money) else 0.0; ok=True; comps=money[:j]; break
        if not ok and money:
            comps=[]; tot=None
        typ=typ.split()[0] if typ.split() and typ.split()[0] in ('NES','Non-NES','Charter','DAEP') else typ
        FIX={'Clifton MS':(4442577.0,139434.47),'Smith, K. ES':(6179308.0,273473.70),'Whidby ES':(3511807.0,134838.04),
             'White ES':(4100235.0,243171.39),'Windsor Vilage ES':(4106976.0,239798.30),'Worthing HS':(9207074.0,259705.20),
             'Yates HS':(8890553.0,245399.66),'Young ES':(3335239.0,127690.35)}
        if not ok and name in FIX: tot,t1=FIX[name]; ok='manual'
        rows.append(dict(page=p,campus=name,org=org,type=typ,enr=enr,tot=tot,t1=t1,ok=ok,raw=' '.join(toks)))
print('rows',len(rows),'ok',sum(bool(r['ok']) for r in rows))
agg=defaultdict(lambda:[0,0,0.0,0.0])
for r in rows:
    if not r['ok'] or r['enr'] is None: continue
    a=agg[r['type']]; a[0]+=1; a[1]+=r['enr']; a[2]+=r['tot']; a[3]+=r['t1']
for k,a in sorted(agg.items(),key=lambda x:-x[1][0]):
    print(f"{k:22s} n={a[0]:4d} enr={a[1]:9.0f} GF=${a[2]:,.0f} per=${a[2]/a[1] if a[1] else 0:,.0f} T1=${a[3]:,.0f}")
w=csv.writer(open('fy26_campus_allocations_OCR.csv','w',newline=''))
w.writerow(['pdf_page','campus','org','type','proj_enrollment','gf_total','title_i_alloc','gf_total_verified_by_component_sum','raw_ocr_numbers'])
for r in rows: w.writerow([r['page'],r['campus'],r['org'],r['type'],r['enr'],r['tot'],r['t1'],r['ok'],r['raw']])
for r in rows:
    if not r['ok']: print('BAD',r['page'],r['campus'],r['type'],r['raw'])
