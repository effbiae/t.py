import a;import n;from p import p;import numpy as np;import subprocess;import sys
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
eval=lambda s,m:m.pk(e(p(s),m))
def ru(s):
 try:r=subprocess.run(["python3","-c",f"from t import *;kb(lambda:eval('{s}',a))"],check=True)
 except subprocess.CalledProcessError as err:
  return err.returncode
 return r.returncode
def cmp(x,y):return x==y
def main():
  s=[]
  print('testing for crash')
  for c in a.P[1:a.P.find('S')+1]:#first scan for SEGV
   print(c,end="");sys.stdout.flush()
   for t in [c+"(2)",c+"^2"]:
    if x:=ru(t):print('\n','SIGSEGV'if x==-11 else x,t)
    else:s+=[t]
  for x in s:
   if x[0] in n.Q:
    print(cmp(*[m.pk(e(x,m))for m in (a,n)]))
if __name__=='__main__':
 kb(main)
