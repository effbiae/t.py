#!/usr/bin/python3
import sys;from p import p,P;lg=lambda x,f,e:(print(x,file=f,end=e),f.flush());
def e(x,s):
 if x[0]=='[':return '\n'.join([e(_,s)for _ in x[1:]])+'// '+s
 if x[0]=='0':return f't{"ei"[type(x[1])==int]}({x[1]})'
 if type(x)==str and x.isalpha():return f'r_({x})'
 if (p:=P.find(x[0]))>0:return f'ke({P.find(x[0])},{e(x[1],s)if x[1] else "0"},{e(x[2],s)})'
 if p==0:return f'!x({x[1]},px)&&_r({x[1]});{x[1]}={e(x[2],s)}; //{s}'
def main():
 gf=open('g.b','w')
 while 1:
  x=sys.stdin.readline().strip()
  if not x:break
  if any(_ in x for _ in':;'):lg(e(p(x),x),gf)
  else:lg(f'_r({e(p(x),x)}); //{x}',gf)
 gf.close()
if __name__=='__main__':
 main()
