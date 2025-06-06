import a;from numpy import *;seterr(divide='ignore', invalid='ignore')
ax=lambda x:x.shape==();ID=lambda x:x;ar=lambda x:array(x);ti=ar;te=ar;pk=ID;r_=ID;_r=ID
i,f=int,float;ty=lambda x:[f,i][0+issubclass(x.dtype.type,integer)];k=lambda i,y,z:k1(a.P[i],z)if y is None else k2(a.P[i],y,z)
mv=lambda n:lambda x:not ax(x)and len(x.shape)==n;v=mv(1);m=mv(2);Y=(open('Y').read()+' nop').split()#'nyi rnk len typ dom'+' nop'
err=lambda x:type(x)is tuple;smp=lambda x,g:ax(x)and x>g and not isinf(x)and not isnan(x);ii=lambda x:(i(x),i(x))
match=lambda a,x:(_:=[ar(_)for _ in (a,x)],0+(_[0].shape==_[1].shape and allclose(*_,rtol=1e-4,equal_nan=1)))[-1]
def k1(c,x):
 if c in'?+-*%#*_':return(5,)if c=='?'else ar(abs(x)if c=='+'else -x if c=='-'else x*x if c=='*'else \
  sqrt(x)if c=='%'else(k1('^',x)if ax(x)else len(x))if c=='#'else x*x if c=='*'else floor(x).astype(i))
 if c=='~':return ar(0+logical_not(x))if ax(x)else k2('=',x,0)
 if c=='|':return x[::-1]if v(x)else k1('=',x)[::-1]if smp(x,0)else(2,)if ax(x)else(1,)
 if c in'<>':return (triu,tril)[c=='>'](ones(ii(x),dtype=i),(1,-1)[c=='>'])if smp(x,0)else(2,)
 if c=='=':return identity(i(x))if smp(x,0)else(2,)
 if c=='!':return arange(i(x))if smp(x,-1)else ar(x.shape)if m(x)else\
               reshape(arange(i(prod(x))),x)if v(x)and ty(x)==i and len(x)<3 else(2,)
 if c==',':return reshape(x,(1,)+x.shape)if ax(x)or v(x)else reshape(x,(1,prod(x.shape)))
 if c=='@':return k1('^',x)if ax(x)else tr(lambda x:x[0],(x,),(0,))
 if c=='^':return ar(1)/x*arange(i(x))if smp(x,-1)else(2,)
 if c=='&':return full(ii(x),1)if smp(x,0)else transpose(matrix(x))if m(x)else(1,)if v(x)else(2,)
 if c=='E':return exp(x)
 return(0,)
def k2(c,a,x):
 if c in'+-*%<>=&|':return tr(lambda a,x:a+x if c=='+'else a-x if c=='-'else a*x if c=='*'else\
   (ar(f(a))if ax(a)else a)/x if c=='%'else 0+(a<x)if c=='<'else 0+(a>x)if c=='>'else\
   0+isclose(a,x)if c=='='else minimum(a,x)if c=='&'else maximum(a,x),(a,x),(2,))
 if c=='!':return tr(lambda a,x:x%a,(a,x),(2,))if ty(a)==i and ty(x)==i else k2('*',a,x)if not ax(x)else(4,)
 if c=='?':#s? is inverse;v? is inverse;m? is commutem (x@m)
  if not ax(a):
   if v(x)and not m(a):return(3,)
   if not ax(x):return k2('@',x,a)
   if v(a):n=where([match(_,x)for _ in a])[0];return ar(n[0]if len(n)else len(a))
   else:return(2,)
  return ar(x)/a if not ax(x)else(4,)
 if c=='_':return tr(lambda a,x:x[i(a)if a>=0 else 0:len(x)if a>=0 else len(x)+i(a)],(a,x),(1,))
 if c==',':
  if ty(a)!=ty(x):return(3,)
  if m(a)or m(x)or ax(a):return(1,)
  return tr(lambda a,x:concatenate([k1(',',_)if ax(_)else _ for _ in(a,x)]),(a,x),(0,))
 if c=='#':
  n=1 if ax(x) else len(x)
  if not ax(a)or not n:return(1,)
  ia=i(a);xs=(arange(ia)%n)if ia>0 else n+ia+arange(-a);return tr(lambda x:(k1(',',x)if ax(x)else x)[xs],(x,),(2,))
 if c=='@':#s@ is scalar(i.e. multiply);v@ is index;m@ is matmul
  if ax(a):return a*x
  if v(a):
   if v(x) or ax(x):return tr(lambda a,x:a[x],(a,x),(2,))if ty(x)==i else a*x
   elif m(x):return tr(matmul,(a,x),(2,))
  if m(a):return a*x if ax(x)else tr(matmul,(a,x),(2,))
  return(3,)
 if c=='~':return k2('=',a,x)
 if c=='^':
  if ty(a)!=i or not ax(a) or a<1 or ax(x):return(1,)
  if v(x):return(2,)if len(x)%a else reshape(x,(a,len(x)//a))
  return tr(lambda:ar([_[:a]for _ in x]),(),(2,))
 if c=='E':return a*(x/(1+exp(-x)))
 return(0,)
def tr(f,v,e):
 try:return f(*v)
 except:return e

'''m?x is x@m (i.e. commute of @. useful for our ai machinations)
btw in general  a@x is at/application/composition/..
i.e. 'a' is a function. e.g. scalar s is scalar i.e. it scales. that is why it is called scalar.
2@3 is 6

a?x is the inverse operation, e.g

2?6 is 3

except m?x is not least squares. instead we are using it for something else.

m@x is linear transform(m is function)
v@x is indexing (vectors are functions)
v?x is find(i.e. inverse of index)
  '''
