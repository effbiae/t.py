o=-fno-builtin -funsigned-char -fno-unwind-tables -Wno-psabi -Wfatal-errors -Wno-multichar -Wno-parentheses -Wno-pointer-type-mismatch -Wno-incompatible-pointer-types
liba.so:k.edu makefile k.edu/*.[abc] a.c
	clang-13 -oliba.so $o -g -shared -fPIC k.edu/[az].c a.c -Ofast -nostdlib -mavx512f -mavx512dq -mavx512vbmi -mavx512vnni
k.edu:
	git clone https://github.com/effbiae/k.edu.git
	cd k.edu && git checkout 30eaa9e3 2>/dev/null
t:t.c makefile k.edu
	clang-13 -ot -D_start=_kstart $o -g t.c -L. -la -Wl,-rpath=`pwd`
