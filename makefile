SHELL=/bin/bash
o=-funsigned-char -fno-{builtin,unwind-tables} -w
c=clang-13
m=-mavx512{f,dq,vbmi,vnni,vpopcntdq}
O=-O3
all:P Y liba.so
liba.so:k.edu makefile a.c
	$c -oliba.so $o -g -shared -fPIC k.edu/?.c a.c $O -nostdlib $m
k.edu:
	git clone https://github.com/effbiae/k.edu.git
P:k.edu
	a=$$(grep -o 'R="[^"]*"' k.edu/z.c);echo -n $${a:3:29}>P
Y:k.edu
	a=$$(grep -o 'Q\[[^"]*"[^"]*"' k.edu/z.c);echo -n $${a:5:20}>Y
d:g.b g.c liba.so
	$c -od -D_start=_kstart $o -g g.c -L. -la -Wl,-rpath=`pwd`
t:t.c liba.so
	$c -ot -D_start=_kstart $o -g t.c -L. -la -Wl,-rpath=`pwd`
z:;zip py.zip makefile a.py a.c t.py p.py n.py
test:
	python3 p.py
	python3 a.py
clean:;rm -f P s liba.so t py.zip t log g.b g.c -r k.edu __pycache__
