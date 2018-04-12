#!/usr/bin/env python
print "#lambda"
f=lambda x,y:x+y
print f(4,6)

print "#fuction as param"
def add(x,y):
    return x+y
def test(f,x,y):
    print type(f)
    print f(x,y)
test(add,4,6)
test(lambda x,y:x+y,4,6)

print "#map() "
print "map(lambda x:x**2,[1,2,3,4,5,6]) "
print map(lambda x:x**2,[1,2,3,4,5,6])
print "map(lambda x,y:x+y,[1,2,3],[4,5,6])"
print map(lambda x,y:x+y,[1,2,3],[4,5,6])

print "#filter()"
def f1(x):
    if(x%2==0):
        return True
    else:
        return False
print "#filter(f1,[6,7,8,9,10,11,12,13,14,15])"
print filter(f1,[6,7,8,9,10,11,12,13,14,15])

print "#reduce()"
print "reduce(add,[1,2,3,4,5])"
print reduce(add,[1,2,3,4,5])



