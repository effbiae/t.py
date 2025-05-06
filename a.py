import ctypes as ct;U=ct.c_ulonglong;i2=ct.c_uint;e2=ct.c_float;i0=ct.c_byte;P=open("P").read();a=ct.CDLL('./liba.so')
def d(f,s):f.restype=s[0];f.argtypes=s[1:];return f
k_=d(a.k_,[U,i2,U]);ti=d(a.kti,[U,i2]);te=d(a.kte,[U,e2]);ix=d(a.kix,[ct.c_int,U]);ex=d(a.kex,[e2,U]);k=d(a.k,[U,i2,U,U])
ax=d(a.kax,[i2,U]);tx=d(a.ktx,[i2,U]);mx=d(a.kmx,[i2,U]);nx=d(a.knx,[i2,U]);gx=d(a.kgx,[i0,U])
_r=lambda x:k_(0,x);r_=lambda x:k_(1,x);ux=lambda x:k_(2,x);sx=lambda x:k_(3,x)
m=lambda c,x:k(P.find(c),0,x);d=lambda c,a,x:k(P.find(c),a,x)
sh=lambda x:0 if ax(x)else(round(nx(x)/ux(x)if ux(x) else nx(x)),ux(x))if mx(x)else(nx(x),)
ty=lambda x:ct.c_int if tx(x)==2 else e2 if tx(x)==5 else i0
pa=lambda x:ix(x) if tx(x)==2 else ex(x) if tx(x)==5 else gx(x)
import numpy as np
def pk(x):return None if x==0 else pa(x)if ax(x) else [np.copy(np.ctypeslib.as_array(ct.cast(sx(x),ct.POINTER(ty(x))),shape=sh(x))),_r(x)][0]
a.m_(0,0);k_(0,0)
