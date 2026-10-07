import struct,sys
def emf_text(path):
    b=open(path,'rb').read(); i=0; out=[]
    while i+8<=len(b):
        t,s=struct.unpack_from('<II',b,i)
        if s<8: break
        if t==84:  # EMR_EXTTEXTOUTW
            x,y,n,off=struct.unpack_from('<iiII',b,i+36)
            txt=b[i+off:i+off+2*n].decode('utf-16le','replace')
            out.append((y,x,txt))
        i+=s
    return out
rows={}
for y,x,t in emf_text(sys.argv[1]):
    key=round(y/ (float(sys.argv[2]) if len(sys.argv)>2 else 8))
    rows.setdefault(key,[]).append((x,t))
for k in sorted(rows):
    print(' | '.join(t for x,t in sorted(rows[k])))
