from a import P;import numpy as np;np.seterr(divide='ignore', invalid='ignore')
ax=lambda x:not isinstance(x,np.ndarray);ID=lambda x:x;ti=ID;te=ID;pk=ID
topy=lambda x:x.item()if not ax(x)and x.shape==()else x
k=lambda i,a,x:topy(m(P[i],x)if a is None else d(P[i],a,x))
def m(c,x):
 if x is None:return x
 if c=='+':return abs(x)
 if c=='-':return -x
 if c=='*':return x*x
 if c=='%':return np.sqrt(x)
 if c=='#':return 1 if ax(x)else len(x)
 if c=='*':return x*x
 if c=='~':return np.vectorize(lambda x:0+(x==0))(x)
 if c=='_':return np.floor(x)
 if c=='|':return x[::-1]if not ax(x) else None
 if c=='!':return np.arange(int(x))if ax(x)else None
 if c==',':return np.reshape(x,1)if ax(x)else np.reshape(x,(1,)+x.shape)if len(x.shape)==1 \
                  else None
 if c=='@':
  try:return x[0]
  except TypeError:return x
 if c=='^':return 1/x*np.arange(x)if type(x)==int else None
 if c=='&':return np.full((x,x),1)if ax(x)else np.transpose(x)
 return None 
def d(c,a,x):
 if a is None or x is None:return None
 if c=='+':return a+x
 if c=='-':return a-x
 if c=='*':return a*x
 if c=='%':return a/x
 if c=='<':return 0+(a<x)
 if c=='>':return 0+(a>x)
 if c=='=':
     a,x=[m(',',_)if ax(_)else _ for _ in(a,x)]
     if any([len(_)==0 for _ in(a,x)]):return None
     p,q=[np.where(np.isnan(_))[0]for _ in(a,x)]
     n=all([_.size==0 for _ in(p,q)])
     return d('|',n or p.size==q.size and p==q,0+(abs(a-x)<1e-6))
 if c=='!':return x%a
 if c=='?':return x/a
 if c=='&':return np.minimum(a,x)
 if c=='|':return np.maximum(a,x)
 if c==',':
     try:return np.concatenate((m(',',a)if ax(a)else a,m(',',x)if ax(x)else x))
     except Exception as e:return e
 if c=='#':n=m('#',x);return np.take(x,np.arange(a)%n)if ax(a)and n else None
 if c=='@':
  if not ax(a)and not ax(x):return np.matmul(a,x)
  if not ax(a)and x<len(a):return a[x]
  return a*x
 if c=='~':r=d('=',a,x);return 0+(r if ax(r)else r.all())
 return None
