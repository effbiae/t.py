#!/usr/bin/python3
import sys
print('spawn k.edu/a\nproc xx {x} { expect -re {(?n)^ } { send -- "$x\r" } eof { puts "crash";exit 1} }')
f=sys.stdin
while 1:
 x=f.readline()
 if not x:break
 print('xx "'+x.strip()+'"')
print('xx "\\\\\\\\"')
print('expect eof')
print('puts "exit"')

