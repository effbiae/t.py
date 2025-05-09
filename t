#!/usr/bin/python3
import a,n,sys;from p import p;import numpy as np;P=a.P;Y=open('Y').read().split();Z=n.Y
ax=lambda x:not isinstance(x,np.ndarray);np.set_printoptions(precision=3)
lf,gf,ef=[open(x,'w')for x in['log','g.b','e']]
on,ov,od,oe=[x in sys.argv or 'a' in sys.argv for x in 'nvde'];od=od or all([_ not in sys.argv for _ in'nve'])
e=lambda x,m:([m.te,m.ti][type(x[1])==int](x[1]))if x[0]=='0'else m.k(P.find(x[0]),e(x[1],m)if x[1] else None,e(x[2],m))
ce=lambda x:f't{"ei"[type(x[1])==int]}({x[1]})'  if x[0]=='0'else f'ke({P.find(x[0])},{ce(x[1])if x[1] else "0"},{ce(x[2])})'
lg=lambda x,f:(print(x,file=f),f.flush());cb=lambda x:[lg(f'_r({ce(p(a))}); //{a}',gf)for a in x]
le=lambda x:[lg(e,ef)for e in x];log=lambda x:lg(x,lf);ev=lambda s,m:m.pk(e(p(s),m))
exprs=lambda:(g:=('(2)','!2','^2','&2'),x:=[c+t for t in g for c in a.P[1:a.P.find('.')+1]],x+[f'({u})'+a for u in g for a in x])[-1]
sm=lambda an,x:[l:='\n'if (not ax(x))and len(x.shape)>1 else'',l+an+':'+l+str(x)][1];
err=lambda x:type(x)is tuple;errpass=lambda s,e:e==8 or (err(s) and (e==s[0] or not s[0]))
def help():p=sys.argv[0];print(f'try {p} for differences, then try {p} n for possible bugs. also {p} a \'2+^2\' for single expr')
def main(es):
 cb(es);le(es)
 for x in es:
  log(x);ov and print('try',x);s,t=[ev(x,m)for m in(a,n)]
  if not n.d('~',s,t)and not err(s) and not err(t):od and print('> dif',x,sm('a',s),sm('n',t))
  elif err(s) and not err(t) and s[0]:oe and print('> a',Y[s[0]],x,sm('n',t))
  elif err(t) and not errpass(s,t[0]):on and print('> n',Z[t[0]],x,sm('a',s))
  if n.d('~',s,t):ov and print('agree',x,sm('',s))
  else:ov and print('disagree',x,sm('a',s),sm('n',t))
  sys.stdout.flush()
if __name__=='__main__':
    if'h' in sys.argv:help();sys.exit(0)
    s=[_ for _ in sys.argv[1:] if len(_)>1]
    main(s if len(s) else exprs())
