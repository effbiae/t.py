import a;import n;from p import p;import numpy as np;import subprocess as sp;import sys;import pickle;import os;P=a.P
ax=lambda x:not isinstance(x,np.ndarray);np.set_printoptions(precision=3);v='-v'in sys.argv;log=open('log','w');cf=open('c.b','w')
def kb(f):
 try:f()
 except KeyboardInterrupt:pass
e=lambda x,m:(m.te(x[1])if type(x[1])==float else m.ti(x[1]))if x[0]=='0'else m.k(P.find(x[0]),*[e(x,m)if x else x for x in x[1:]])
ce=lambda x:f't{"e"if type(x[1])==float else "i"}({x[1]})'if x[0]=='0' else f'k({P.find(x[0])},{",".join([ce(x)if x else "0"for x in x[1:]])})'
lg=lambda x,f:(print(x,file=f),f.flush());cb=lambda x:lg(f'_r({ce(p(x))});',cf);ev=lambda s,m:m.pk(e(p(s),m))
def ru(s):
 try:r=sp.run(["python3","-c",f"from t import *;kb(lambda:ev('{s}',a))"],check=True)
 except sp.CalledProcessError as err:
  return err.returncode
 return r.returncode
def safe():#returns exprs that don't segv
 s=[]
 print('testing for crash\n this is slow because it runs a new k.edu process many times for each prim\n'+
       '  be patient -- this is only done once and then cached')
 for c in a.P[1:a.P.find('S')+1]:#first scan for SEGV
  print(c,end="");sys.stdout.flush()
  g=('(2)','!2','^2','&2');n=lambda x,e:print('\na','SIGSEGV'if x==-11 else 'FAIL',e)
  for t in g:
   if x:=ru(e:=c+t):n(x,e)
   else:
    s+=[e]
    for u in g:
     if x:=ru(f:=f'({u}){c}{t}'):n(x,f)
     else:s+=[f]
 print(' done');pickle.dump(s,open('s','wb'));return s
chk=lambda x:lg(x,log)and 0
def mis(x,s,t):
 def sm(an,x):n=(not ax(x))and len(x.shape)>1;l='\n'if n else'';return l+an+':'+l+str(x)
 print('>>>>>> mismatch:',x,sm('a',s),sm('n',t),'\n<<<<<<')
def match(x,y):c=(x-y)<1e-6;return c.all()if not ax(c)else c
def main():
 for x in pickle.load(open('s','rb'))if os.path.exists('s')else safe():
  if chk(x):continue
  cb(x);s,t=[ev(x,m)for m in(a,n)]
  if s is None:print('a','nyi',x);continue
  elif t is None:v and print('n nyi',x);continue
  if not match(s,t):mis(x,s,t)
if __name__=='__main__':
 kb(main)
