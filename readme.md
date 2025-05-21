```
tests for k.edu

there are two modules a and n
. a links to k core via a k.edu shared object
. n implements k core using numpy

sample output:

$make&&echo '&2'|./n
[[1 1]
 [1 1]]

to test a k.zip:

$(cd k.edu&&unzip ../k.zip)
$make&&./g|./n qp;./a
```
