#!/usr/bin/python3
import a,n,sys,os,pickle;from p import p;import numpy as np;P=a.P;Y=open('Y').read().split();Z=n.Y
ax=lambda x:not isinstance(x,np.ndarray);np.set_printoptions(precision=3)
lf,gf,ef=[open(x,'w')for x in['log','g.b','e']]
on,ov,od,oe=[x in sys.argv or 'a' in sys.argv for x in 'nvde'];ow='w'in sys.argv;od=od or all([_ not in sys.argv for _ in'nve'])
v={}
def il(c,x):
    if(c):return x()
def e(x,m):
 if x[0]=='0':return([m.te,m.ti][type(x[1])==int](x[1]))
 if type(x)==str and x.isalpha():o=v[(m,x)];il(not m.ax(o),lambda:m.r_(o));return o
 if (p:=P.find(x[0]))>0:
  if x[1]:a=e(x[1],m);b=e(x[2],m);return a if m.err(a)else b if m.err(b)else m.k(P.find(x[0]),a,b)
  else:a=e(x[2],m);return a if m.err(a) else m.k(P.find(x[0]),None,a)
 if p==0:
  k=(m,x[1]);il(k in v,lambda:m._r(v[k]));v[k]=e(x[2],m);return v[k]#m.r_(v[k])#check for error and don't assign

cd=lambda s:(x:=p(s),f'U {x[1]}={ce(x[2])}; //{s}')[-1]
ce=lambda x:f't{"ei"[type(x[1])==int]}({x[1]})'if x[0]=='0'else f'r_({x})'if type(x)==str and x.isalpha() else\
        f'ke({P.find(x[0])},{ce(x[1])if x[1] else "0"},{ce(x[2])})'
lg=lambda x,f:(print(x,file=f),f.flush());ca=lambda x:[lg(cd(x),gf)];cb=lambda x:[lg(f'_r({ce(p(a))}); //{a}',gf)for a in x]
le=lambda x:[lg(e,ef)for e in x];log=lambda x:lg(x,lf);
if 'i' not in sys.argv:
 #g0=('2','!2','^2','&2','<2','>2','1','0.+&2','^256','0.+&256')#,'<2','>2')#,'(1)')
 #g0=('^2','0.+&2','0.+<2','1.','^256','0.+&256')#,'<2','>2')#,'(1)')
 g0=('1.','0.','-1.')
 g='abcdefghijklmnopqrstuvwxyz'[:len(g0)]
 ss=[g[i]+':'+g0[i] for i in range(len(g))]
 le(ss);[ca(s) for s in ss];gs=';'.join(ss);log(gs);print(gs)
 [e(p(s),m) for s in ss for m in (a,n)]
 vs=a.P[1:a.P.find('.')+1].replace('$','')
 base=lambda:(x:=[c+t for t in g for c in vs],x:=x+[u+a for u in g for a in x])[-1]
 if 'x'in sys.argv:exprs=lambda:base()+[c+a for c in vs for a in base()]
 else:exprs=base
def sm(an,x):
    l='\n'if not ax(x)and len(x.shape)>1 and not ow else''
    s=l+(an+':' if not ow else '')+l+(str(x)if not err(x)else 'err '+str(x[0]))
    return s.replace('\n','|').replace('[','').replace(']','')[:100]if ow else s
err=lambda x:type(x)is tuple;errpass=lambda s,e:e==4 or err(s) and (s[0]in[0]or s[0]==e)
def help():p=sys.argv[0];print(f'try {p} for differences, then try {p} n for possible bugs. also {p} a \'2+^2\' for single expr')
def leak(es):
 return
 global gf;gf.close()
 for e in es:
     gf=open('g.b','w');cb([e]);gf.close();
     if os.system('make g 2>&1 >/dev/null&&./g'):
         print(e)
def main(es):
 if 'p'not in sys.argv:
  le(es)
  for x in es:
   if x in [x[1:]for x in sys.argv if x[0]=='-']:continue
   cb([x]);
   log(x);ov and print('try',x);ks=[e(p(x),m)for m in(a,n)]
   s,t=(9,9)
   if x[1]!=':':#don't get a:1
    s,t=[m.pk(_)for (_,m) in zip(ks,(a,n))]
    if n.k2('~',s,t):ov and print('agree',x,sm('',s))
    else:ov and print('disagree',x,sm('n',t),sm('a',s))
   results=[(x,s,t)];sys.stdout.flush()
  with open('p','wb')as f:pickle.dump(results,f)
 else:
  with open('p','rb')as f:results=pickle.load(f)
 for w in range(3):
  for x,s,t in results:
   if w==0 and not n.k2('~',s,t)and not err(s) and not err(t):od and print(x,'\t',sm('n',t),'\t(',sm('a',s),')')#,max(abs(t-s)[1:]))
   elif w==1 and err(s) and not err(t) and s[0]:oe and print('> a',Y[s[0]],x,sm('n',t))
   elif w==2 and err(t) and not errpass(s,t[0]):on and print('> n',Z[t[0]],x,sm('a',s))
  sys.stdout.flush()
if __name__=='__main__':
    if'h' in sys.argv:help();sys.exit(0)
    if'i' in sys.argv:s=[_.strip() for _ in sys.stdin.readlines()]
    else:s=[_ for _ in sys.argv[1:] if len(_)>1 and _[0]!='-'];s=s if len(s) else exprs()
    if'l'in sys.argv:leak(s);sys.exit(0)
    main(s)
