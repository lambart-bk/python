#!/usr/bin/env python
#coding=utf8
import subprocess
#shell调用
try:
    print "call"
    subprocess.call("ls",shell=True)
    print "check_call"
    subprocess.check_call("cd ..;ls",shell=True)
    print "check_out"
    out=subprocess.check_output("ls",shell=True)
    print out
    print "check_out end"
except subprocess.CalledProcessError:
    print "subprocess.CalledProcessError"
finally:
    print "finally"

#Popen()
child=subprocess.Popen(["ping","-c","2","www.ahut.edu.cn"])
child.wait()
print "pid=",child.pid
print "poll=",child.poll()

#子进程的文本控制流
child1=subprocess.Popen(["ls"],stdout=subprocess.PIPE)
child2=subprocess.Popen(["cat"],stdin=child1.stdout,stdout=subprocess.PIPE)
out=child2.communicate()
print out
child4 = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child4.communicate("hahahaha")
print ""




