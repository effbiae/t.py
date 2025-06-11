#!/usr/bin/python3

from sys import *;import os;import math as m;from functools import reduce;from itertools import *;v1=argv[1]if len(argv)>1 else 'log'
def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch
plus=lambda x,y:x+y
n='/tmp/n'
e='/tmp/e'
t='/tmp/t'
sy=lambda x:(x,os.system(x))[-1]
sy(f'cp {v1} {t}')
def u(b):f=open(n,'w');f.writelines(b);f.close();sy(f'./e<{n}>{e}');return sy(f'expect {e} k.edu/a 1 >/dev/null')
def tt():
 l=open(t).readlines()
 def tc(l,d):
  t=l[-1];h=l[1:-1];a=l[0];b=list(batched(h,len(h)//d));xs=[(a,)+reduce(plus,_)+(t,)for _ in combinations(b,len(b)-1)]
  for x in xs:
   if u(x):return x
  return 0
 r=0
 n2=len(l)-2;bs=[2**_ for _ in range(1,m.floor(m.log2(n2))+1)];
 if not(bs):return 0
 bs[-1]=n2
 print('bs',n2,bs)
 for x in bs:
  if tc(l,x):
   r=1;print('split in',x);"sy(f'less {n}')";sy(f'cp {n} {t}');break
 return r
#first, try empty middle
l=open(t).readlines()
em=(l[0],l[-1])
if u(em):sy(f'cp {n} {t}');exit(0)
#then try batches
while tt():pass
