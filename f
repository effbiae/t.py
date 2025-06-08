#!/usr/bin/python3
from sys import *;import os;from functools import reduce;from itertools import *;v1=argv[1]if len(argv)>1 else 'log'
def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch
n='/tmp/n'
e='/tmp/e'
t='/tmp/t'
os.system(f'cp {v1} {t}')
def u(b):f=open(n,'w');f.writelines(b);f.close();os.system(f'./e<{n}>{e}');return os.system(f'expect {e} k.edu/a 1')
def tt():
 l=open(t).readlines()
 def tc(l,d):
  t=l[-1];h=l[1:-1];a=l[0];b=list(batched(h,len(h)//d));xs=[(a,)+_[0]+(t,)for _ in combinations(b,len(b)-1)]
  for x in xs:
   if u(x):return x
  return 0
 r=0
 for x in (2,3):
  if y:=tc(l,x):
   print('found smaller')
   r=1
   os.system(f'less {n}')
   os.system(f'cp {n} {t}')
   break
 return r
while tt():pass
