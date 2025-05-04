import a;import n;from p import p;import numpy as np;import subprocess
def e(x,m):
 if type(x)==float:return m.te(x)
 elif type(x)==int:return m.ti(x)
 elif len(x)==2:return m.m(x[0],e(x[1],m))
 else:return m.d(x[0],*[e(a,m)for a in x[1:]])
 return 0
def ru(s):
 try:r=subprocess.run([f"python3","-c","from t import *;pk(e(p('{s}')),a)"],check=True)
 except subprocess.CalledProcessError as err:
  return err.returncode:
 return r.returncode
def cmp(x,y):return x==y
if __name__=='__main__':
 s=[]
 for c in P[1:P.find('S')+1]:#first scan for SEGV
 print(c);d=repr(c)
 for a in [c+"(2)",c+"^2"]:
  if x:=ru(s):print('SIGSEGV'if x==-11 else str(x),s)
  else:s+=[a]
 for a in s:
  if a[0] in n.Q:
   print(cmp(*[x.pk(e(s,x))for x in (a,n)]))
