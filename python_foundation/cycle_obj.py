#!/usr/bin/env python
print "#cycle object"
for line in open("file"):
    print line
print "#generator"
def gen():
    a=10
    yield a
    a=100
    yield a
    a=1000
    yield a
for var in gen():
    print var

def gen1():
    for i in range(1,4):
        yield i
for var in gen1():
    print var
print "#Express"
G=(x for x in range(1,4))
for var in G:
    print var

print "#List Comprehension"
l=[]
for i in  range(10):
    l.append(i**2)
print l
print "#Express"
l=[x**2 for x in range(10)]
print l

print "#example"
x1=[1,3,5]
y1=[9,12,13]
L=[x**2 for x,y in zip(x1,y1) if y>10]
print L




