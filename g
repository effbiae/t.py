#!/usr/bin/python3
import a;import sys;v1=sys.argv[1]if len(sys.argv)>1 else''
g0=('v:^48;m:0.+48^!48*48;s:16;t:-6')
g=[_[0]for _ in g0.split(';')]
print(g0+(';z:0'if'x'in v1 else''))
vs=a.P[1:a.P.find('.')+1].replace('$','').replace('.','')
base=lambda:(x:=[c+t for t in g for c in vs],x:=x+[u+a for u in g for a in x])[-1]
def exprs():
 y=base();x=y+[c+a for c in vs for a in y]
 for a in y:x+=[f'z:{a}'];x+=[f'z{v}{b}'for b in y for v in vs]
 return x
s=exprs()if'x'in v1 else base()
try:
 for _ in s:print(_)
except BrokenPipeError:pass
