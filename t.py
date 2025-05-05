import a;import n;from p import p;import numpy as np;import subprocess as sp;import sys
np.set_printoptions(precision=3);v=0
if 'v'in sys.argv:v=1
def kb(f):
 try:f()
 except KeyboardInterrupt:pass
def e(x,m):
 if x[0]=='0':
  if type(x[1])==float:return m.te(x[1])
  elif type(x[1])==int:return m.ti(x[1])
 if len(x)==2:return m.m(x[0],e(x[1],m))
 elif len(x)==3:return m.d(x[0],*[e(x,m)for x in x[1:]])
 return 0
ev=lambda s,m:m.pk(e(p(s),m))
def ru(s):
 try:r=sp.run(["python3","-c",f"from t import *;kb(lambda:ev('{s}',a))"],check=True)
 except sp.CalledProcessError as err:
  return err.returncode
 return r.returncode
def safe():#returns exprs that don't segv
 s=[]
 print('testing for crash\n this is slow because it runs a new k.edu process 3 times for each prim')
 for c in a.P[1:a.P.find('S')+1]:#first scan for SEGV
  print(c,end="");sys.stdout.flush()
  g=('(2)','!2','^2','&2')
  for t in g:
   #add a 'fast' param to segv that doesn't launch subprocess but will kill test
   if x:=ru(e:=c+t):print('\na','SIGSEGV'if x==-11 else x,e)
   else:
    s+=[e]
    for u in g:
     if x:=ru(f:='('+u+')'+c+t):print('\na','SIGSEGV'if x==-11 else x,f)
     else:s+=[f]
 print(' done')
 return s
def mat(x,y):
 c=(x-y)<1e-6
 if isinstance(c,np.ndarray):return c.all()
 return c
def main():
 for x in safe():
  if x[0] in n.Q:
   s,t=[ev(x,m)for m in (a,n)]
   if s is None:print('a','NYI',x);continue
   elif t is None:v and print('n NYI',x);continue
   if not mat(s,t):print('MISMATCH:',x,'a:',s,'~ n:',t)
   else:
    if v:print('match',x,s)
if __name__=='__main__':
 kb(main)
