#!/usr/bin/python3
import sys
print('#use expect <this-filename> <path-to-a>')
print('spawn [lindex $argv 0]')
print('proc s {x} {expect -re {(?n)^ } {send -- "$x\\r" } eof {puts "crash";exit 1} }')
f=sys.stdin
while 1:
 x=f.readline()
 if not x:break
 print('s "'+x.strip()+'"')
print('s "\\\\\\\\"')
print('expect eof')
print('puts "ok"')
