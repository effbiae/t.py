from a import P;k=lambda i,y,z:k1(P[i],z)if y is None else k2(P[i],y,z)
from numpy import *;seterr(divide='ignore', invalid='ignore');Y=(open('Y').read()+' nop').split()#'nyi rnk len typ dom'+' nop'
a=lambda z:z.shape==();mv=lambda n:lambda z:not a(z)and len(z.shape)==n;v=mv(1);m=mv(2)
ar=lambda z:array(z);ti=ar;te=ar;ID=lambda z:z;pk=ID;r_=ID;_r=ID;i,f=int,float;ty=lambda z:[f,i][0+issubclass(z.dtype.type,integer)]
err=lambda z:type(z)is tuple;smp=lambda z,g:a(z)and z>g and not isinf(z)and not isnan(z);ii=lambda z:(i(z),i(z))
ma=lambda y,z:(_:=[ar(_)for _ in(y,z)],0+(_[0].shape==_[1].shape and allclose(*_,rtol=1e-4,equal_nan=1)))[-1]
def k1(c,z):
 if c in'?+-*%#*_':return(5,)if c=='?'else ar(abs(z)if c=='+'else -z if c=='-'else z*z if c=='*'else\
  sqrt(z)if c=='%'else(k1('^',z)if a(z)else len(z))if c=='#'else z*z if c=='*'else floor(z).astype(i))
 if c=='~':return ar(0+logical_not(z))if a(z)else k2('=',z,0)
 if c=='|':return z[::-1]if v(z)else k1('=',z)[::-1]if smp(z,0)else(2,)if a(z)else(1,)
 if c in'<>':return (triu,tril)[c=='>'](ones(ii(z),dtype=i),(1,-1)[c=='>'])if smp(z,0)else(2,)
 if c=='=':return identity(i(z))if smp(z,0)else(2,)
 if c=='!':return arange(i(z))if smp(z,-1)else ar(z.shape)if m(z)else ("dosomthing",z)[-1] if v(z)and ty(z)==i and len(z)<3 else(2,)
 if c==',':return reshape(z,(1,)+z.shape)if a(z)or v(z)else k1(',',ar(len(z)))
 if c=='@':return k1('^',z)if a(z)else tr(lambda z:z[0],(z,),(0,))
 if c=='^':return ar(1)/z*arange(i(z))if smp(z,-1)else(2,)
 if c=='&':return full(ii(z),1)if smp(z,0)else transpose(matrix(z))if m(z)else(1,)if v(z)else(2,)
 if c=='E':return k1('^',z)if a(z)else exp(z)
 if c=='M':return max(z);z=exp(z-max(z));return z/sum(z)
 if c=='R':return(5,)
 return(0,)
def k2(c,y,z):
 if c in'+-*%<>=&|':return tr(lambda y,z:y+z if c=='+'else y-z if c=='-'else y*z if c=='*'else\
   (ar(f(y))if a(y)else y)/z if c=='%'else 0+(y<z)if c=='<'else 0+(y>z)if c=='>'else\
   0+isclose(y,z)if c=='='else minimum(y,z)if c=='&'else maximum(y,z),(y,z),(2,))
 if c=='!':
  if not a(z)and not a(y):return(4,)
  return tr(lambda y,z:z%y,(y,z),(2,))if ty(y)==i and ty(z)==i else k2('*',y,z)if not a(z)else(4,)
 if c=='?':#s? is inverse;v? is inverse;m? is commutem (z@m)
  if not a(y):
   if v(z)and not m(y):return(3,)
   if not a(z):return k2('@',z,y)
   if v(y):n=where([ma(_,z)for _ in y])[0];return ar(n[0]if len(n)else len(y))
   else:return(2,)
  return z/y
 if c=='_':return tr(lambda y,z:z[i(y)if y>=0 else 0:len(z)if y>=0 else len(z)+i(y)],(y,z),(1,))
 if c==',':
  if ty(y)!=ty(z):return(3,)
  if m(y)or m(z):return(1,)
  return tr(lambda y,z:concatenate([k1(',',_)if a(_)else _ for _ in(y,z)]),(y,z),(0,))
 if c=='#':
  n=1 if a(z) else len(z)
  if not a(y)or not n:return(1,)
  if isnan(y)or isinf(y):return(4,)
  ia=i(y);zs=(arange(ia)%n)if ia>0 else n+ia+arange(-y);return tr(lambda z:(k1(',',z)if a(z)else z)[zs],(z,),(2,))
 if c=='@':#s@ is scalar(i.e. multiply);v@ is indez;m@ is matmul
  if a(y):return y*z
  if v(y):
   if v(z):return(3,)
   if a(z):return tr(lambda y,z:y[z],(y,z),(2,))if ty(z)==i and z>=0 else(2,)if z<0 else y*z
   elif m(z):return tr(matmul,(y,z),(2,))
  if m(y):
   if a(z):return tr(lambda y,z:y[z],(y,z),(2,))if z>=0 else(2,)
   return tr(matmul,(y,z),(2,))
  return(3,)
 if c=='~':return k2('=',y,z)
 if c=='^':
  if ty(y)!=i or not a(y) or y<1 or a(z):return(1,)
  if v(z):return(2,)if len(z)%y else reshape(z,(y,len(z)//y))
  return tr(lambda:ar([_[:y]for _ in z]),(),(2,))
 if c=='E':return(2,)if a(z)else y*(z/(1+exp(-z)))
 if c=='R':return(2,)if a(z)or not len(z)else y*(z/sqrt(1/len(z)*sum(z*z)))
 if c=='M':return(5,)
 return(0,)
def tr(f,v,e):
 try:return f(*v)
 except:return e
