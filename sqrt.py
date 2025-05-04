from a import *;import numpy as np
ini()
i=20000  #for c in P[2:]:print(c);x=m(c,ti(i));print(x);print(pk(x))
x=pk(m('%',m('^',ti(i))))
y=np.sqrt(1/i*np.fromiter(range(i),dtype=np.float32))
e=max(abs(x-y))
j=[a for a in range(i)if e==x[a]-y[a]][0]
print(j,x[j]-y[j])
print(x[j])
print(y[j])
