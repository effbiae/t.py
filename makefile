SHELL=/bin/bash
o=-fno-builtin -funsigned-char -fno-unwind-tables -Wno-psabi -Wfatal-errors -Wno-multichar -Wno-parentheses -Wno-pointer-type-mismatch -Wno-incompatible-pointer-types
c=clang-13
m=-mavx512f -mavx512dq -mavx512vbmi -mavx512vnni
O=-O3
all:P Y liba.so
liba.so:k.edu makefile a.c
	$c -oliba.so $o -g -shared -fPIC k.edu/?.c a.c $O -nostdlib $m
k.edu:
	git clone https://github.com/effbiae/k.edu.git
P:k.edu
	a=$$(grep -o 'P="[^"]*"' k.edu/z.c);echo -n $${a:3:29}>P
Y:k.edu
	a=$$(grep -o 'cc\[[^"]*"[^"]*"' k.edu/z.c);echo -n $${a:8:16}>Y
g:g.b g.c liba.so
	$c -og -D_start=_kstart $o -g g.c -L. -la -Wl,-rpath=`pwd`
z:;zip py.zip makefile a.py a.c t.py p.py n.py
test:;python3 p.py
clean:;rm -f P s liba.so t py.zip t log g.b g.c -r k.edu __pycache__
