#!/usr/bin/env python

# subprocess
from subprocess import *
check_call('ls .',shell=True)
a=check_output('ls -l .',shell=True)
print a

#regex
msg="sakskm;lk1234dsvs"
import re
p=re.compile('(\d+)')
m=p.search(msg)
print m.group(1)

a=range(1,10,2)
print a

#iner func
print "name: %s,age: %d" % ('bob',20)
print len('sdfsfsa')
print len(a)
#range([start],stop,[step])
#help(fun)   eg. help(range)

#lambda function
#lambda args:express
def  fuc(f,l):
    ret=[]
    for var in l:
        ret.append(f(var))
    return ret
print fuc(lambda x:x*x ,a)

a=range(10)
#[expr for var in list condition]
l=[x*2 for x in a if x%2==0]
print l

print "fib seq"
def fibs(num):
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2]+result[-1])
	return result
num=input()
while  num :
	print fibs(num)
	num=input()

print "function param"

def func(a=3,b=4,c=5):
	print a,b,c
func(4,5,6)
func(a=50)
func(b=50)
func(c=50,a=60)

print "if test"
a=input()
b=input()
if (a==b):
    print "a==b"
elif a>b:
    print "a>b"
else:
    print "a<b"

print "for test"
ta=(1,2,3)
lb=[4,5,6]
dc={1:7,2:8,3:9}
for a in ta:
    print a
lb+=[10,11,12]
for a in lb[::2]:
    print a
for a in dc:
    print dc[a]
print dc.keys()
print dc.values()




