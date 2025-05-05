import a;import n;from p import p;import numpy as np;import subprocess as sp;import sys;import pickle;import os
nda=lambda x:isinstance(x,np.ndarray);np.set_printoptions(precision=3);v=0
if 'v'in sys.argv:v=1
lf=open('log', 'w')
def kb(f):
 try:f()
 except KeyboardInterrupt:pass
def e(x,m):
 if x[0]=='0':return m.te(x[1])if type(x[1])==float else m.ti(x[1])
 if len(x)==2:return m.m(x[0],e(x[1],m))
 elif len(x)==3:return m.d(x[0],*[e(x,m)for x in x[1:]])
 return 0
def up(x):#unparse for k.edu
 if x[0]=='0':return str(x[1])
 return x[0]+up(x[1])if len(x)==2 else f'({up(x[1])}){x[0]}{up(x[2])}'
ev=lambda s,m:m.pk(e(p(s),m))
def ru(s):
 try:r=sp.run(["python3","-c",f"from t import *;kb(lambda:ev('{s}',a))"],check=True)
 except sp.CalledProcessError as err:
  return err.returncode
 return r.returncode
def safe():#returns exprs that don't segv
 s=[]
 print('testing for crash\n this is slow because it runs a new k.edu process many times for each prim')
 for c in a.P[1:a.P.find('S')+1]:#first scan for SEGV
  print(c,end="");sys.stdout.flush()
  g=('(2)','!2','^2','&2');n=lambda x,e:print('\na','SIGSEGV'if x==-11 else x,e)
  for t in g:
   if x:=ru(e:=c+t):n(x,e)
   else:
    s+=[e]
    for u in g:
     if x:=ru(f:=f'{c}[{u};{t}]'):n(x,f)
     else:s+=[f]
 print(' done');pickle.dump(s,open('s','wb'));return s
def log(s):print(up(p(s)),file=lf);lf.flush()
def mis(x,s,t):
 def sm(an,x):n=nda(x)and len(x.shape)>1;l='\n'if n else'';return l+an+':'+l+str(x)
 print('>>>>>> mismatch:',x,sm('a',s),sm('n',t),'\n<<<<<<')
def match(x,y):c=(x-y)<1e-6;return c.all()if nda(c)else c
def main():
 if os.path.exists('s'):sa=pickle.load(open('s','rb'))
 else:sa=safe()
 for x in sa:
  log(x);s,t=[ev(x,m)for m in(a,n)]
  if s is None:print('a','NYI',x);continue
  elif t is None:v and print('n NYI',x);continue
  if not match(s,t):mis(x,s,t)
if __name__=='__main__':
 kb(main)
