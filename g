#!/usr/bin/python3
import a;import sys;v1=sys.argv[1]if len(sys.argv)>1 else''
g0=('1.','0.','-1.')
g0=('2','!2','^2','&2','<2','>2','1')
g0=('^48','0.+<48','0.+=48','16','-6')
g='abcdefghijlmnopqrstuvwxyz'[:len(g0)]
ss=[g[i]+':'+g0[i] for i in range(len(g))]+['z:0']
gs=';'.join(ss);print(gs)
vs=a.P[1:a.P.find('.')+1].replace('$','').replace('.','')
base=lambda:(x:=[c+t for t in g for c in vs],x:=x+[u+a for u in g for a in x])[-1]
def exprs():
 y=base();x=y+[c+a for c in vs for a in y]
 for a in y:
  x+=[f'z:{a}'];x+=[f'z{v}{b}'for b in y for v in vs]
 return x
if __name__=='__main__':
 try:
    s=[_ for _ in v1 if len(_)>1 and _[0]not in'-/']
    if not len(s):
     if'x'in sys.argv:s=exprs()
     else:s=base()
    for _ in s:print(_)
 except BrokenPipeError:pass
