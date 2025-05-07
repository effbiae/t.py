from a import P;import numpy as np;np.seterr(divide='ignore', invalid='ignore')
ax=lambda x:not isinstance(x,np.ndarray);ID=lambda x:x;ti=ID;te=ID;pk=ID
k=lambda i,a,x:m(P[i],x)if a is None else d(P[i],a,x)
def m(c,x):
 if x is None:return x
 if c=='+':return abs(x)
 if c=='-':return -(x)
 if c=='*':return x*x
 if c=='%':return np.sqrt(x)
 if c=='#':return 1 if ax(x)else len(x)
 if c=='*':return x*x
 if c=='~':return np.vectorize(lambda x:0+(x==0))(x)
 if c=='_':return np.floor(x)
 if c=='|':return x[::-1]if not ax(x) else None
 if c=='!':return np.arange(int(x))if ax(x)else None
 if c=='@':
  try:return x[0]
  except TypeError:return x
 if c=='^':
  if type(x)==int:return 1/x*np.arange(x)
 if c=='&':return np.full((x,x),1,np.dtype('b'))if ax(x)else np.transpose(x)
 return None 
def d(c,a,x):
 if a is None or x is None:return None
 if c=='+':return a+x
 if c=='-':return a-x
 if c=='*':return a*x
 if c=='%':return a/x
 if c=='<':return 0+(a<x)
 if c=='>':return 0+(a>x)
 if c=='=':return 0+(a==x)
 if c=='&':return np.minimum(a,x)
 if c=='|':return np.maximum(a,x)
 if c=='#':n=m('#',x);return np.take(x,np.arange(a)%n)if ax(a)and n else None
 if c=='@':
  if not ax(a)and not ax(x):return np.matmul(a,x)
  if not ax(a)and x<len(a):return a[x]
  return a*x
 if c=='~':c=(a-x)<1e-6;return 0+(c if ax(c)else c.all())
 return None
