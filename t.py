import a;import n;from p import p;import numpy as np;import subprocess
def e(x,m):
 if type(x)==float:return m.te(x)
 elif type(x)==int:return m.ti(x)
 elif len(x)==2:return m.m(x[0],e(x[1],m))
 elif len(x)==3:return m.d(x[0],*[e(x,m)for x in x[1:]])
 return 0
def ru(s):
 try:r=subprocess.run([f"python3","-c","from t import *;a.pk(e(p('{s}'),a))"],check=True)
 except subprocess.CalledProcessError as err:
  return err.returncode
 return r.returncode
def cmp(x,y):return x==y
if __name__=='__main__':
 s=[]
 for c in a.P[1:a.P.find('S')+1]:#first scan for SEGV
  print(c);d=repr(c)
  for t in [c+"(2)",c+"^2"]:
   if x:=ru(t):print('SIGSEGV'if x==-11 else str(x),t)
   else:s+=[t]
 for x in s:
  if x[0] in n.Q:
   print(cmp(*[m.pk(e(x,m))for m in (a,n)]))
