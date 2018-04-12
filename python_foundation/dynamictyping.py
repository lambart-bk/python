#!/usr/bin/env python
print "#immutable object"  #--include tuple
a=3
b=a
print a,b
a=-3
print a,b
def f1(x):
    x=-1
f1(a)
print "pass fuc(a) :",a

print "#mutable object"
la=[1,2,3]
lb=la
print la,lb
la[0]=-1
print la,lb
def f2(x):
    x*=2
f2(la)
print "pass fuc(la) :",la


