#!/usr/bin/env python
class bird(object):
    feature=True
class chicken(bird):
    fly=False
    def __init__(self,age):
        self.age=age
    def __getattr__(self,name):
        if name=='adult':
            if(self.age>5):
                return True
            else:
                return False
        else:
            raise AttributeError(name)
c=chicken(7)
#__dict__     --object/bird/chicken/c
print bird.__dict__
print chicken.__dict__
print c.__dict__

c.__dict__['age']=3
print c.__dict__['age']
# or
c.age=4
print c.age

print "#__getattr__"
print c.adult
c.age=7
print c.adult

print "#property"
class num(object):
    def __init__(self,value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self,value):
        self.value = -value
    def delNeg(self):
        print "value also deleted"
        del self.value
    neg = property(getNeg, setNeg,delNeg, "num.neg  negative ")
n = num(1.1)
print n.neg
n.neg=-22
print n.value
print num.neg.__doc__
del n.neg







