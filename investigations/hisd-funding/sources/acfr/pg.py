import sys
f=sys.argv[1]; pages=open(f,errors='ignore').read().split('\f')
for a in sys.argv[2:]:
    if '-' in a: lo,hi=map(int,a.split('-'))
    else: lo=hi=int(a)
    for i in range(lo,hi+1):
        print(f'########## PDF page {i}'); print(pages[i-1])
