#!/usr/bin/python3
import a,sys;[exec(f"v{i}=sys.argv[{i}]if len(sys.argv)>{i} else''",globals())for i in (1,2,3)]
g0='i:1;j:0;k:-1'
g0='v:^48;m:48^^48*48;s:16;t:-6;i:1;j:0;k:-1'
g0='i:2#1.;v:^2'
g0='v:^48;m:48^^48*48;s:16;t:-6'
g0='v:^2;m:2^^4;s:1'
if v2:g0=v2
g=[_[0]for _ in g0.split(';')]
print(g0+(';z:0'if'x'in v1 else''))
vs=v3 if v3 else a.P[1:a.P.find('.')+1].replace('$','').replace('.','')+'EMR'
if ':'in vs:raise Exception(':')
base=lambda:(x:=[c+t for t in g for c in vs],x:=x+[u+a for u in g for a in x])[-1]
def exprs():
 y=base();x=y+[c+a for c in vs for a in y]
 for a in y:x+=[f'z:{a}'];x+=[f'z{v}{b}'for b in y for v in vs]
 return x
s=exprs()if'x'in v1 else base()
try:
 for _ in s:print(_)
except BrokenPipeError:pass
