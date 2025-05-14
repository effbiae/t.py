#!/usr/bin/python3
import a,n,sys,os,pickle;from p import p;import numpy as np;P=a.P;Y=open('Y').read().split();Z=n.Y
ax=lambda x:not isinstance(x,np.ndarray);np.set_printoptions(precision=3)
lf,gf,ef=[open(x,'w')for x in['log','g.b','e']]
on,ov,od,oe=[x in sys.argv or 'a' in sys.argv for x in 'nvde'];ow='w'in sys.argv;od=od or all([_ not in sys.argv for _ in'nve'])
def il(c,x):
    if(c):return x()
def e(x,m):
 if x[0]=='0':return([m.te,m.ti][type(x[1])==int](x[1]))
 if type(x)==str and x.isalpha():return m.r_(v[(m,x)])
 if (p:=P.find(x[0]))>0:
  if x[1]:a=e(x[1],m);return a if m.err(a) else m.k(P.find(x[0]),a,e(x[2],m))
  else:return m.k(P.find(x[0]),None,e(x[2],m))
 if p==0:
  k=(m,x[1]);il(k in v,lambda:m._r(v[k]));v[k]=e(x[2],m);return m.r_(v[k])#check for error and don't assign

ce=lambda x:f't{"ei"[type(x[1])==int]}({x[1]})'if x[0]=='0'else f'ke({P.find(x[0])},{ce(x[1])if x[1] else "0"},{ce(x[2])})'
lg=lambda x,f:(print(x,file=f),f.flush());cb=lambda x:[lg(f'i(256,_r({ce(p(a))})); //{a}',gf)for a in x]
le=lambda x:[lg(e,ef)for e in x];log=lambda x:lg(x,lf);ev=lambda s,m:m.pk(e(p(s),m))
#g=('(2)','!2','^2','&2','<2','>2')#,'(1)')
#g=('(2)','0.+!32,32','^256','0.+&256','0.+<256')#,'<2','>2')#,'(1)')
g=('(2)','^256')#,'<2','>2')#,'(1)')
exprs=lambda:(x:=[c+t for t in g for c in a.P[1:a.P.find('.')+1]],x+[f'({u})'+a for u in g for a in x])[-1]
def sm(an,x):
    l='\n'if not ax(x)and len(x.shape)>1 and not ow else''
    s=l+(an+':' if not ow else '\t')+l+(str(x)if not err(x)else 'err '+str(x[0]))
    return s.replace('\n','|').replace('[','').replace(']','')[:100]if ow else s
err=lambda x:type(x)is tuple;errpass=lambda s,e:e==4 or err(s) and (s[0]in[0]or s[0]==e)
def help():p=sys.argv[0];print(f'try {p} for differences, then try {p} n for possible bugs. also {p} a \'2+^2\' for single expr')
def leak(es):
 global gf;gf.close()
 for e in es:
     gf=open('g.b','w');cb([e]);gf.close();
     if os.system('make g 2>&1 >/dev/null&&./g'):
         print(e)
def main(es):
 if 'p'not in sys.argv:
  cb(es);le(es);results=[]
  for x in es:
   if x in [x[1:]for x in sys.argv if x[0]=='-']:continue
   log(x);ov and print('try',x);s,t=[ev(x,m)for m in(a,n)]
   if n.k2('~',s,t):ov and print('agree',x,sm('',s))
   else:ov and print('disagree',x,sm('n',t),sm('a',s))
   results+=[(x,s,t)];sys.stdout.flush()
  with open('p','wb')as f:pickle.dump(results,f)
 else:
  with open('p','rb')as f:results=pickle.load(f)
 for x,s,t in results:
  if not n.k2('~',s,t)and not err(s) and not err(t):od and print('> dif',x,sm('n',t),sm('a',s))#,max(abs(t-s)[1:]))
  elif err(s) and not err(t) and s[0]:oe and print('> a',Y[s[0]],x,sm('n',t))
  elif err(t) and not errpass(s,t[0]):on and print('> n',Z[t[0]],x,sm('a',s))
  sys.stdout.flush()
if __name__=='__main__':
    if'h' in sys.argv:help();sys.exit(0)
    s=[_ for _ in sys.argv[1:] if len(_)>1 and _[0]!='-']
    s=s if len(s) else exprs()
    if'l'in sys.argv:leak(s);sys.exit(0)
    main(s)
