import ctypes as ct;U=ct.c_ulonglong;i2=ct.c_uint;e2=ct.c_float;i0=ct.c_uint8;P=open("P").read();a=ct.CDLL('./liba.so')
def d(f,s):f.restype=s[0];f.argtypes=s[1:];return f
k_=d(a.k_,[U,i2,U]);ti=d(a.kti,[U,i2]);te=d(a.kte,[U,e2]);ix=d(a.kix,[ct.c_int,U]);ex=d(a.kex,[e2,U])
a_ke=d(a.ke,[U,U,U,U]);k=lambda i,x,y:a_ke(i,0 if x is None else x,y)
ax=d(a.kax,[i2,U]);tx=d(a.ktx,[i2,U]);mx=d(a.kmx,[i2,U]);nx=d(a.knx,[i2,U]);gx=d(a.kgx,[i0,U]);px=d(a.kpx,[i2,U]);ux=d(a.kux,[i2,U])
_r=d(a.k_r,[U,U]);r_=d(a.kr_,[U,U]);sx=d(a.ksx,[U,U])
sh=lambda x:0 if ax(x)else(ux(x),round(nx(x)/ux(x)if ux(x)else nx(x)))if mx(x)else(nx(x),)
ty=lambda x:ct.c_int if tx(x)==4 else e2 if tx(x)==5 else i0;pa=lambda x:ix(x)if tx(x)==4 else ex(x) if tx(x)==5 else gx(x)
import numpy as np;err=lambda x:px(x)
#pk=lambda x:(ix(x),)if px(x) else pa(x)if ax(x)else[np.copy(np.ctypeslib.as_array(ct.cast(sx(x),ct.POINTER(ty(x))),shape=sh(x))),_r(x)][0]
g=lambda x,t,s:[np.copy(np.ctypeslib.as_array(ct.cast(sx(x),ct.POINTER(t)),shape=s)),_r(x)][0]
u=lambda a:np.unpackbits(a,bitorder='little')
def pk(x):
    #import sys;print(sh(x),ty(x),sx(x));sys.stdout.flush()
    return (ix(x),)if px(x)else pa(x)if ax(x)else g(x,ty(x),sh(x))if tx(x)!=1 else u(g(x,ty(x),((nx(x)+7)//8,)))[:nx(x)].reshape(sh(x))

'a.ldmxcsr()';k_(0,0)
