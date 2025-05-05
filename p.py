P=open('P').read();m=["v;",P,";)]\n "];c=dict([(chr(x),' ')for x in range(128)])
def f(x,s):
 for a in s:c[a]=x
for i in range(len(m[0])):f(m[0][i],m[i+1])
def cs(i):
 if(i<len(s)):return c[s[i][0]]
 return ';'
def n():
 global i
 if len(s)!=i:i+=1;return s[i-1]
 return ' ';
def q():return ';'==cs(i)
def E(x):
 while n() in ";[(":
  if type(x)!=tuple:x=(x,)
  x=x+(e(t()),)
 return x
def t():
 if q():return()
 x=n()if not s[i][0]in'(['else x[1]if 3>len(x:=E(s[i]))else x
 while i<len(s)and'['==s[i][0]:x=E(x)
 return x
def v():return';'<cs(i-1)
def e(x):
 if q():return x
 v_=v();f=t();return (f,x,e(t()))if v()>v_ else (x,e(f))
def pn(x,i):#try to parse a num
 j=i;t=int;f=float('nan')
 if not x[i] in '0123456789':return f,0
 while j<len(x):
  if x[j]=='e':j+=1;continue
  if x[j]=='.':t=float
  try:f=float(x[i:j+1])
  except:break
  j+=1
 return t(f),j-i
def lex(x):
 r=[];i=0
 while i<len(x):
  a,n=pn(x,i)
  if n:i+=n;r.append(('0',a));
  else:r.append(x[i]);i+=1
 return r
def p(x):global s,i;s=lex('['+x);i=0;return t()
def test():
    import sys
    if len(sys.argv)>1: #generate test cases
        for x in ["","x;y","x+y","^8e3","x+*y","(+x)%y","%[1;3]"]:
            print("        [%12s,%s ],"%(x.__repr__(),p(x)))
        print(']')
    for x,y in [
        [          '',() ],
        [       'x;y',('[', 'x', 'y') ],
        [       'x+y',('+', 'x', 'y') ],
        [      '^8e3',('^', ('0', 8000)) ],
        [      'x+*y',('+', 'x', ('*', 'y')) ],
        [    '(+x)%y',('%', ('+', 'x'), 'y') ],
        [    '%[1;3]',('%', ('0', 1), ('0', 3)) ],
        ]:
        if (r:=p(x))!=y:print('!',repr(x),repr(r),'!=',y);sys.exit(1)
if __name__=='__main__':
 test()
