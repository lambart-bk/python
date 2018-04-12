#!/usr/bin/env python
a=1
b=1
print id(a),hex(id(a))
print id(b),hex(id(b))
print a,a is b,b

a="haha"
b="haha"
print a,a is b,b

a="good is haha hehe"
b="good is haha hehe"
print a,a is b,b  #true in shell ;false in python terminal

a=[]
b=[]
print a,a is b,b

print "#getrefcount()"
#getrefcount(object) -> integer    
#Return the reference count of object.  The count returned is generally
#one higher than you might expect, because it includes the (temporary)
#reference as an argument to getrefcount().

from sys import getrefcount
a=[1,2,3]
print "a=[1,2,3]: ",getrefcount(a)
b=[1,2,3]
print "b=[1,2,3]: ",getrefcount(a),getrefcount(b)
c=b
print "c=b: ",getrefcount(a),getrefcount(b),getrefcount(c)
d=[b,b]
print "d=[b,b] ",getrefcount(a),getrefcount(b),getrefcount(c),getrefcount(d)
e=[c,c]
print "e=[c,c] ",getrefcount(a),getrefcount(b),getrefcount(c),getrefcount(d),getrefcount(e)
print "#reduce ref count"
print "del: "
a=[1,2]
b=a
print getrefcount(b)
del a
print getrefcount(b)
print "refe another: "
a=[1,2]
b=a
print getrefcount(b)
a=1
print getrefcount(b)




print "#class object reference"
class obj(object):
    def __init__(self,para):
        self.para=para
p=[1,2]
o=obj(p)
print id(p)
print id(o.para)
print p is o.para

#garbage collection --generation 0 1 2
#import gc
#print gc.get_threshold()
#get_threshold() -> (threshold0, threshold1, threshold2)   
#Return the current collection thresholds
#gc.set_threshold(700,10,10)
#gc.collect() #manually collect

#objgraph
#install
#sudo apt-get install python-pip
#sudo pip install xdot
#sudo pip install objgraph
print "objgraph test"
x=[1,2]
y=[x,dict(key1=x,k=1)]
z=[y,(x,y)]
import objgraph
objgraph.show_refs([z],filename='./objgraph_test1.dot')
#reference cycle
x=[]
y=[x]
x.append(y)
objgraph.show_refs([x],filename='./objgraph_RefCycle.dot')






