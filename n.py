from a import P;import numpy as np;np.seterr(divide='ignore', invalid='ignore')
from functools import reduce
ax=lambda x:not isinstance(x,np.ndarray);ID=lambda x:x;ti=ID;te=ID;pk=ID
ty=lambda x:2 if type(x)is int else 5 if type(x)is float else [5,2][0+(x.dtype=='int64')]
topy=lambda x:x.item()if not ax(x)and x.shape==()else x
k=lambda i,a,x:topy(m(P[i],x)if a is None else d(P[i],a,x))
def tr(f,v,e):
 try:return f(*v)
 except:return e
Y='nyi rnk 2 typ 4 5 6 7 wontdo err'.split()
def m(c,x):
 if c=='?':return (8,)
 if c=='+':return abs(x)
 if c=='-':return -x
 if c=='*':return x*x
 if c=='%':return np.sqrt(x)
 if c=='#':return 1 if ax(x)else len(x)
 if c=='*':return x*x
 if c=='~':return d('=',x,0)
 if c=='_':return np.floor(x)
 if c=='|':return x[::-1]if not ax(x) else m('|',np.identity(x))
 if c=='<':return np.triu(np.ones((x,x)),+1)if ax(x) else (9,)
 if c=='>':return np.tril(np.ones((x,x)),-1)if ax(x) else (9,)
 if c=='=':return np.identity(x)if ax(x) else (9,)
 if c=='!':return np.arange(int(x))if ax(x)else np.array(x.shape)
 if c==',':return np.reshape(x,1)if ax(x)else np.reshape(x,(1,)+x.shape)if len(x.shape)==1 else (9,)
 if c=='@':return tr(lambda x:x[0],(x,),x)
 if c=='^':return 1/x*np.arange(x)if type(x)==int else(9,)
 if c=='&':return np.full((x,x),1)if ax(x)else np.transpose(np.matrix(x))
 return (0,) 
def d(c,a,x):
 if c=='+':return a+x
 if c=='-':return a-x
 if c=='*':return a*x
 if c=='%':return (np.array(float(a))if ax(a)else a)/x
 if c=='<':return 0+(a<x)
 if c=='>':return 0+(a>x)
 if c=='=':return 0+(abs(a-x)<1e-6)
 if c=='!':return x%a if ty(x)==2 else a*x
 if c=='?':#s? is inverse;v? is inverse;m? is commute
  q=x/a;return q if any([ty(_)==5 for _ in (a,x)]) else np.floor(q)
 if c=='&':return np.minimum(a,x)
 if c=='|':return np.maximum(a,x)
 if c=='_':return tr(lambda a,x:x[a:],(a,x),(1,))
 if c==',':
  if ty(a)!=ty(x):return (3,)
  return tr(lambda a,x:np.concatenate([m(',',_)if ax(_)else _ for _ in(a,x)]),(a,x),(0,))
 if c=='#':n=m('#',x);return (m(',',x)if ax(x) else x)[np.arange(a)%n]if ax(a)and n else (1,)
 if c=='@':#s@ is scalar(i.e. multiply);v@ is index;m@ is matmul
  if ax(a):return a*x
  if len(a.shape)==1:return tr(lambda a,x:a[x],(a,x),(9,))if ty(x)==2 else(3,)
  if len(a.shape)==2:return tr(np.matmul,(a,x),(9,))
 if c=='~':
     if ax(a)!=ax(x):return 0
     p=[m(',',_)if ax(_)else _ for _ in(a,x)]
     if not np.equal(*[_.shape for _ in p]).all():return 0
     fs=(np.isnan,np.isposinf,np.isneginf)
     ms=[np.logical_and(*[f(_)for _ in p])for f in fs]
     return 0+d('|',reduce(np.logical_or,ms),d('=',*p)).all()
 if c=='^':
     if ty(a)!=2:return (1,)
     if ax(x):return d('#',a,x)
     f=lambda a,x:m('&',d('#',a,x)if ax(a)else a);x=m('!',x)if ax(x)else x
     return tr(f,(a,x),(9,))if ax(a)else(1,)
 return (0,)
