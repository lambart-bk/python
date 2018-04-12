#!/usr/bin/env python

def add(a=1,b=2,c=3):
    print a,b,c
print "\nadd()" 
add()
print "\nadd(4,5)" 
add(4,5)
print "\nadd(7,c=9,b=8)" 
add(7,c=9,b=8)

#packing---tuple
print "\npacking--tuple"
def fuc(*para):
    print type(para)
    print para[0],para
fuc(1,2,3)

#packing---dictionary
print "\npacking---dic"
def f(**para):
    print type(para)
    print para['name'],para
f(a=3,b=4,name='tom')

#unpacking
def fu(a=1,b=2,c=3):
    print a,b,c

a=(4,5)
print "\nfu(*a) "
fu(*a)

b={'a':'4','c':20}
print "\nfu(**b)"
fu(**b)



