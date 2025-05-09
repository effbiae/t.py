from a import P;import numpy as np;np.seterr(divide='ignore', invalid='ignore')
ax=lambda x:not isinstance(x,np.ndarray);ID=lambda x:x;ti=ID;te=ID;pk=ID
ty=lambda x:2 if type(x)is int else 5 if type(x)is float else [5,2][0+(x.dtype=='int64')]
topy=lambda x:x.item()if not ax(x)and x.shape==()else x
k=lambda i,a,x:topy(m(P[i],x)if a is None else d(P[i],a,x))
def tr(f,v,e):
 try:return f(*v)
 except:return e
Y='nyi 1 2 3 4 5 6 7 wontdo err'.split()
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
 if c=='|':return x[::-1]if not ax(x) else (9,)
 if c=='!':return np.arange(int(x))if ax(x)else (9,)
 if c==',':return np.reshape(x,1)if ax(x)else np.reshape(x,(1,)+x.shape)if len(x.shape)==1 else (9,)
 if c=='@':return tr(lambda x:x[0],(x,),x)
 if c=='^':return 1/x*np.arange(x)if type(x)==int else (9,)
 if c=='&':return np.full((x,x),1)if ax(x)else np.transpose(np.matrix(x))
 return (0,) 
def d(c,a,x):
 if c=='+':return a+x
 if c=='-':return a-x
 if c=='*':return a*x
 if c=='%':return a/x
 if c=='<':return 0+(a<x)
 if c=='>':return 0+(a>x)
 if c=='=':return 0+(abs(a-x)<1e-6)
 if c=='!':return x%a
 if c=='?':return x/a
 if c=='&':return np.minimum(a,x)
 if c=='|':return np.maximum(a,x)
 if c=='_':return tr(lambda a,x:x[a:],(a,x),(0,))
 if c==',':return tr(lambda a,x:np.concatenate([m(',',_)if ax(_)else _ for _ in(a,x)]),(a,x),(0,))
 if c=='#':n=m('#',x);return np.take(x,np.arange(a)%n)if ax(a)and n else (9,)
 if c=='@':
  if not ax(a):
   if ty(x)==2:return tr(lambda a,x:a[x],(a,x),(9,))
   if not ax(x):return np.matmul(a,x)
  return a*x
 if c=='~':
     if (ax(a)+ax(x))%2:return 0
     p=[m(',',_)if ax(_)else _ for _ in(a,x)]
     if not np.equal(*[_.shape for _ in p]).all():return 0
     return 0+d('|',np.logical_and(*[np.isnan(_)for _ in p]),d('=',*p)).all()
 return (0,)
