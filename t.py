import a;import n;from p import p;import numpy as np;import sys
P=a.P;Y=open('Y').read().split()
ax=lambda x:not isinstance(x,np.ndarray);np.set_printoptions(precision=3)
v='-v'in sys.argv;lf,gf,ef=[open(x,'w')for x in['log','g.b','e']]
e=lambda x,m:([m.te,m.ti][type(x[1])==int](x[1]))if x[0]=='0'else \
        m.k(P.find(x[0]),e(x[1],m)if x[1] else None,e(x[2],m))
ce=lambda x:f't{"ei"[type(x[1])==int]}({x[1]})'if x[0]=='0'else \
        f'k({P.find(x[0])},{ce(x[1])if x[1] else "0"},{ce(x[2])})'
lg=lambda x,f:(print(x,file=f),f.flush());gb=lambda x:[lg(f'_r({ce(p(a))});',gf)for a in x]
le=lambda x:[lg(e,ef)for e in x];log=lambda x:lg(x,lf);ev=lambda s,m:m.pk(e(p(s),m))
def exprs():
 g=('(2)','!2','^2','&2');x=[(c,t)for t in g for c in a.P[1:a.P.find('S')+1]]
 return [f'{c}{t}'for (c,t) in x]+[f'({u}){c}{t}'for u in g for (c,t) in x]
def mis(x,s,t):
 sm=lambda an,x:[l:='\n'if (not ax(x))and len(x.shape)>1 else'',l+an+':'+l+str(x)][1]
 print('>>> mismatch:',x,sm('a',s),sm('n',t),'\n<<<')
def match(x,y):c=(x-y)<1e-6;return c.all()if not ax(c)else c
def main():
 es=exprs();gb(es);le(es)
 for x in es:
  log(x);v and print('try',x);s,t=[ev(x,m)for m in(a,n)]
  if type(s)is tuple:print('a','err',s[1],Y[s[1]],'for',x);continue
  elif t is None:v and print('n nyi',x);continue
  if not match(s,t):mis(x,s,t)
if __name__=='__main__':main()
