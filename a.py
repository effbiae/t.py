import ctypes as ct;U=ct.c_ulonglong;i2=ct.c_uint;e2=ct.c_float;i0=ct.c_uint8;P=open("P").read();a=ct.CDLL('./liba.so')
def d(f,s):f.restype=s[0];f.argtypes=s[1:];return f
k_=d(a.k_,[U,U]);m_=d(a.m_,[U,i2,U]);ti=d(a.kti,[U,i2]);te=d(a.kte,[U,e2]);iz=d(a.kiz,[ct.c_int,U]);ez=d(a.kez,[e2,U])
a_ke=d(a.ke,[U,U,U,U]);k=lambda i,z,y:a_ke(i-1,0 if z is None else z,y)
az=d(a.kaz,[i2,U]);tz=d(a.ktz,[i2,U]);mz=d(a.kmz,[i2,U]);nz=d(a.knz,[i2,U]);gz=d(a.kgz,[i0,U]);pz=d(a.kpz,[i2,U]);uz=d(a.kuz,[i2,U])
_r=d(a.k_r,[U,U]);r_=d(a.kr_,[U,U]);sz=d(a.ksz,[U,U])
sh=lambda z:0 if az(z)else(uz(z),round(nz(z)/uz(z)if uz(z)else nz(z)))if mz(z)else(nz(z),)
i,f,b,q=tz(ti(1)),tz(te(1.)),1,4;ty=lambda z:ct.c_int if tz(z)==i else e2 if tz(z)==f else i0 if tz(z)==b else i0 if tz(z)==q else i0
import numpy as np;err=lambda z:pz(z);a=lambda z:np.array(iz(z)if tz(z)==i else ez(z) if tz(z)==f else gz(z))
g=lambda z,t,s:[np.copy(np.ctypeslib.as_array(ct.cast(sz(z),ct.POINTER(t)),shape=s)),_r(z)][0];u=lambda a:np.unpackbits(a,bitorder='little')
pk=lambda z:(iz(z),)if pz(z)else a(z)if az(z)else g(z,ty(z),sh(z))if tz(z)!=b else u(g(z,ty(z),((nz(z)+7)//8,)))[:nz(z)].reshape(sh(z))
k_(m_(0,2**36))
if __name__=='__main__':
 import sys;ch=lambda y,z:np.allclose(y,z) or (print(y,'!=',z),sys.exit(1))
 ch(pk(ti(1)),1);ch(abs(pk(te(1.1))-1.1)<0.00001,1);
 ch(1,np.array_equal(pk(k(P.find("!"),0,ti(2))),np.array([0,1])))
 ch(pk(k(P.find("^"),0,ti(2))),np.array([0,0.5]))
 ch(1,pk(k(P.find("<"),te(1.1),te(1.2))))
