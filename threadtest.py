#!/usr/bin/python
#coding=UTF-8
import threading
import time
from  main2nonthreaded import *
from client import *
#print dir(Gest)
mygest = Gest()
t = threading.Thread(name = 'daemon', target=mygest.handler)
tt = threading.Thread(target=mykbdinput.keyboard_input)
t.Daemon = True
t.start
print 'starting the next one'
tt.start
print 'starting the next one'