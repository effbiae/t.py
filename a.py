from ctypes import *;U=c_ulonglong;i2=c_uint;e2=c_float
import os;P=os.popen('grep -o \'P="[^"]*"\' k.edu/z.c').read()[3:-2]
import numpy as np
a=CDLL('./liba.so')
def d(f,s):f.restype=s[0];f.argtypes=s[1:];return f
k_=d(a.k_,[U,i2,U]);ti=d(a.kti,[U,i2]);te=d(a.kte,[U,e2]);ix=d(a.kix,[i2,U]);k=d(a.k,[U,i2,U,U]);ax=d(a.kax,[i2,U]);tx=d(a.ktx,[i2,U]);mx=d(a.kmx,[i2,U]);nx=d(a.knx,[i2,U]);sx=lambda x:k_(3,x);ux=lambda x:k_(2,x)
m=lambda c,x:k(P.find(c),0,x)
d=lambda c,a,x:k(P.find(c),a,x)
sh=lambda x:(round(nx(x)/ux(x)),ux(x))if mx(x) else (nx(x),)if not ax(x)else (1,)
k2p=lambda x:ix(x) if ax(x) else np.ctypeslib.as_array(cast(sx(x),POINTER(e2)),shape=sh(x))

a.m_(0,0);k_(0,0)
x=m('&',ti(2))
x=d('+',te(0.0),x)
print(k2p(x))
x=m('^',ti(9))
print(k2p(x))
