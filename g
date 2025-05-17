#!/usr/bin/python3
import a;import sys;v1=sys.argv[1]if len(sys.argv)>1 else''
g0=('2','!2','^2','&2','<2','>2','1','0.+&2','^256','0.+&256')#,'<2','>2')#,'(1)')
g0=('^2','0.+&2','0.+<2','1.','^256','0.+&256')#,'<2','>2')#,'(1)')
g0=('1.','0.','-1.')
g='abcdefghijklmnopqrstuvwxyz'[:len(g0)]
ss=[g[i]+':'+g0[i] for i in range(len(g))]+['z:0']
gs=';'.join(ss);print(gs)
vs=a.P[1:a.P.find('.')+1].replace('$','')
base=lambda:(x:=[c+t for t in g for c in vs],x:=x+[u+a for u in g for a in x])[-1]
if'x'in sys.argv:
 def exprs():
  y=base();x=y+[c+a for c in vs for a in y]
  for a in y:
   x+=[f'z:{a}'];x+=[f'z{v}{b}'for b in y for v in vs]
  return x
else:exprs=base
if __name__=='__main__':
    s=[_ for _ in v1 if len(_)>1 and _[0]not in'-/'];s=s if len(s) else exprs()
    for _ in s:print(_)
