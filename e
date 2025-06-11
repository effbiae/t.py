#!/usr/bin/python3
import sys;re='expect -re "(?n)^ "';ce='eof {puts "crash";exit 1}'
try:
 print('if {[llength $argv] < 1} {puts "usage: expect $argv0 <path-to-a>";exit 1}')
 print('spawn [lindex $argv 0]')
 print('proc s {x} {'+re+' {send -- "$x\\r"} '+ce+'}')
 f=sys.stdin
 while 1:
  x=f.readline()
  if not x:break
  print('s "'+x.strip()+'"')
 print('if {[llength $argv] > 1} {s "\\\\\\\\";expect eof;puts "ok"} else {'+re+' {interact} '+ce+'}')
except (BrokenPipeError, IOError):pass
sys.stderr.close()
