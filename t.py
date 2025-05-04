from a import *;import numpy as np;import subprocess
def ru(s):
 try:subprocess.run(["python3","-c",s],check=True)
 except subprocess.CalledProcessError as err:
     if err.returncode==-11:
         print("probably segfaulted")
     else:
         print(f"crashed for other reasons: {err.returncode}")
for c in P[1:]:
 print(c)
 ru("from a import *;ini();x=m(%s,ti(2));print(pk(x))"%repr(c))
