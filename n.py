from a import P;from numpy import *;seterr(divide='ignore', invalid='ignore');from functools import reduce
ax=lambda x:not isinstance(x,ndarray)or not len(x.shape);ID=lambda x:x;ti=ID;te=ID;pk=ID;r_=ID;_r=ID;rr=lambda x:1
ty=lambda x:2 if type(x)is int else 5 if type(x)is float else [5,2][0+(x.dtype=='int64')]
topy=lambda x:x.item()if not ax(x)and x.shape==()else x;k=lambda i,a,x:topy(k1(P[i],x)if a is None else k2(P[i],a,x))
mv=lambda n:lambda x:not ax(x)and len(x.shape)==n;v=mv(1);m=mv(2);Y='nyi rnk len typ wontdo other'.split()
err=lambda x:type(x)is tuple;aix=lambda x:ax(x)and ty(x)==2;smp=lambda x,g:ax(x)and x>g and not isinf(x)and not isnan(x)
ii=lambda x:(int(x),int(x))
def k1(c,x):
 if c in'?+-*%#*~_':return(4,)if c=='?'else abs(x)if c=='+'else -x if c=='-'else x*x if c=='*'else \
  sqrt(x)if c=='%'else(1 if ax(x)else len(x))if c=='#'else x*x if c=='*'else k2('=',x,0)if c=='~'else floor(x).astype(int)
 if c=='|':return x[::-1]if v(x)else k1('=',x)[::-1]if smp(x,0)else(2,)if ax(x)else(1,)
 if c in'<>':return (triu,tril)[c=='>'](ones(ii(x),dtype=int),(1,-1)[c=='>'])if smp(x,0)else(2,)
 if c=='=':return identity(int(x))if smp(x,0)else(2,)
 if c=='!':return arange(int(x))if smp(x,-1)else array(x.shape)if m(x)else\
               reshape(arange(int(prod(x))),x)if v(x)and ty(x)==2 and len(x)<3 else(2,)
 if c==',':return reshape(x,1)if ax(x)else reshape(x,(1,)+x.shape)if v(x)else reshape(x,(1,prod(x.shape)))
 if c=='@':return tr(lambda x:x[0],(x,),(0,))
 if c=='^':return array(1)/x*arange(int(x))if smp(x,-1)else(0,)
 if c=='&':return full(ii(x),1)if smp(x,0)else transpose(matrix(x))if m(x)else(1,)if v(x)else(2,)
 return(0,)
def k2(c,a,x):
 if c in'+-*%<>=&|':return tr(lambda a,x:a+x if c=='+'else a-x if c=='-'else a*x if c=='*'else\
   (array(float(a))if ax(a)else a)/x if c=='%' else 0+(a<x)if c=='<'else 0+(a>x)if c=='>'else 0+(abs(a-x)<1e-5)if c=='='\
   else minimum(a,x)if c=='&'else maximum(a,x),(a,x),(2,))
 if c=='!':return tr(lambda a,x:x%a,(a,x),(2,)) if ty(a)==2 and ty(x)==2 else(0,)
 if c=='?':#s? is inverse;v? is inverse;m? is commutem (x@m)
  if not ax(a):
   if v(x) and not m(a):return(3,)
   if not ax(x):return k2('@',x,a)
   if v(a):i=nonzero([k2('~',a[i],x)for i in arange(len(a))])[0];return i[0] if len(i)else len(a)
   else:return(2,)
  q=array(x)/a;return q if any([ty(_)==5 for _ in(a,x)])else floor(q).astype(int)
 if c=='_':return tr(lambda a,x:x[int(a):],(a,x),(1,))
 if c==',':
  if ax(a):return(1,)
  if m(a)or m(x)or ty(a)!=ty(x):return(3,)
  return tr(lambda a,x:concatenate([k1(',',_)if ax(_)else _ for _ in(a,x)]),(a,x),(0,))
 if c=='#':n=k1('#',x);return(k1(',',x)if ax(x)else x)[arange(int(a))%n]if ax(a)and n else(1,)
 if c=='@':#s@ is scalar(i.e. multiply);v@ is index;m@ is matmul
  if ax(a):return a*x
  if ax(x):return(2,)
  if v(a):
   if ty(x)==2 and v(x):return tr(lambda a,x:a[x],(a,x),(2,))
   elif m(x):return tr(matmul,(a,x),(2,))
  if m(a):return tr(matmul,(a,x),(2,))
  return(3,)
 if c=='~':
  if ax(a)!=ax(x):return 0
  p=[k1(',',_)if ax(_)else _ for _ in(a,x)]
  if not equal(*[_.shape for _ in p]).all():return 0
  fs=(isnan,isposinf,isneginf);ms=[logical_and(*[f(_)for _ in p])for f in fs]
  return 0+k2('|',reduce(logical_or,ms),k2('=',*p)).all()
 if c=='^':
  if ty(a)!=2:return(1,)
  if ax(x):return k2('#',a,x)
  f=lambda a,x:k1('&',k2('#',a,x)if ax(a)else a);x=k1('!',x)if ax(x)else x
  return tr(f,(a,x),(5,))if ax(a)else(1,)
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
