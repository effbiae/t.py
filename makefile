SHELL=/bin/bash
o=-fno-builtin -funsigned-char -fno-unwind-tables -Wno-psabi -Wfatal-errors -Wno-multichar -Wno-parentheses -Wno-pointer-type-mismatch -Wno-incompatible-pointer-types
all:P liba.so
liba.so:k.edu makefile a.c
	clang-13 -oliba.so $o -g -shared -fPIC k.edu/[az].c a.c -Ofast -nostdlib -mavx512f -mavx512dq -mavx512vbmi -mavx512vnni
k.edu:
	git clone https://github.com/effbiae/k.edu.git
	cd k.edu && git checkout 96437adcb81f 2>/dev/null #30eaa9e3 
P:k.edu
	a=$$(grep -o 'P="[^"]*"' k.edu/z.c);b=$${a:3:29};echo -n $$b>P
t:t.c makefile k.edu
	clang-13 -ot -D_start=_kstart $o -g t.c -L. -la -Wl,-rpath=`pwd`
g:c.b g.c liba.so
	clang-13 -og -D_start=_kstart $o -g g.c -L. -la -Wl,-rpath=`pwd`
z:;zip py.zip makefile a.py a.c t.py p.py n.py
test:;python3 p.py
clean:;rm -f P s liba.so t py.zip t log -r k.edu __pycache__
