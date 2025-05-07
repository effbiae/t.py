```
tests for k.edu

there are two modules a and n in respective .py files.
. a links to k core via a k.edu shared object
. n implements k core using numpy

sample output:

$make&&python3 t.py
a err 0 nyi for |(2)              < reporting not yet implemented
>>> mismatch: ~(2) a:1 n:0        < disagreement between a and n for ~2
<<<

to test a k.zip:

$(cd k.edu&&unzip ../k.zip)
$make&&python3 t.py
```
