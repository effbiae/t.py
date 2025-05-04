from a import P;import numpy as np
ID=lambda x:x;ti=ID;te=ID;pk=ID
Q="+-*%~^&"
def m(c,x):
  if c=='+':return abs(x)
  if c=='-':return -(x)
  if c=='*':return x*x
  if c=='%':return np.sqrt(x)
  if c=='~':return np.vectorize(lambda x:0+(x!=0))(x)
  if c=='^':
   if type(x)==int:return 1/x*np.fromiter(range(x),np.float32)
  if c=='&':
   if type(x)==int:return np.full((x,x),1,np.dtype('b'))
  print(c,'nyi');return None 
def d(c,a,x):
  if c=='*':return a*x
  print(c,'nyi');return None 
