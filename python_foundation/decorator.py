#!/usr/bin/env python
print "#decorator"
def decorator(F):
    def new_F(x,y):
        print "input: ",x,y
        return F(x,y)
    return new_F
@decorator
def square_sum(x,y):
    return x**2+y**2
@decorator
def square_sub(x,y):
    return x**2-y**2
print square_sum(3,4)
print square_sub(5,4)

print "#decorator with param"
def pretext(pre=""):
    def decorator(F):
        def new_F(name):
            print pre+" decorator..."
            return F(name)
        return new_F
    return decorator
@pretext("^_^")
def f1(name=""):
    return "f1: "+name
@pretext("T_T")
def f2(name=""):
    return "f2: "+name
print f1("Tom")
print f2("Jack")

print "#decorator class"
def decorator(C):
    class newClass(object):
        def __init__(self,age):
            self.wrapped=C(age)
        def display(self):
            print "decorator..."
            self.wrapped.display()
    return newClass
@decorator
class people(object):
    def __init__(self,age):
        self.age=age
    def display(self):
        print "age : %d " % self.age
student=people(20)
student.display()


