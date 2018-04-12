#!/usr/bin/env python
#coding=utf8
import signal
# define signal handler
def myHandler(signum,frame):
    print "I received: ",signum
#register signal handler
signal.signal(signal.SIGALRM,myHandler)
signal.alarm(2)
signal.pause()

