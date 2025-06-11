#!/home/jack/goal/goal
v1:?[1<#ARGS;ARGS 1;"log"]
e:{e:x run"sh""-c""./e|expect - k.edu/a";"e"~@e}
c:{,/'x@&~a=`a:!#x}
f:{a:*x;t:x@-1;h:1_-1_x;b:y$h;?[~"S"~@b[0];:error @b[0];:];:/[{?["i"~@x;x;~e@x]};1;(a,'(c@b),'t),0]}
t:{n:-2+#x;?[~n;:x;::];p:"i"$2 exp 1+!_2 log n;?[~#p;:x;:];?[n>p@-1;p,:n;:]; \p;?[s:{f[x;z]}[x]/[{~"S"~@x};1;p];s;x]}
l:=-read v1
?[e@az:l[0 -1];az;t/l]shell"./e>x"
