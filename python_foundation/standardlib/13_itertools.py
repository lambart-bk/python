#!/usr/bin/env python
#coding=utf8
from itertools import *
print "iter:"
for i in iter(range(10)):
    print i
print "\ncount:"
for i in count(5,5):
    if i>30:
        break
    print i
print "\ncycle:"
k=1
for i in cycle("haha"):
    print i
    k+=1
    if k>10:
        break
print "\nrepeat:"
for i in repeat(5,10):
    print i
print "\nimap/starmap:"
for num in imap(pow, [1, 2, 3], [1, 2, 4]):
    print(num)
for num in starmap(pow,[(1,1),(2,2),(3,4)]):
    print num

print "\nifilter/ifilterfalse/takewhile/dropwhile( difference ?? )"
for i in ifilter(lambda x:x>4,[1,5,3,7]):
    print "f:",i
for i in ifilterfalse(lambda x:x>4,[1,5,3,7]):
    print "ff",i
for i in takewhile(lambda x:x>4,[1,5,3,7]):  #***None
    print "tw",i
for i in dropwhile(lambda x:x>4,[1,5,3,7]):  #***All
    print "dw",i

print "\nchain:"
for i in chain([1,3,5],[2,4,6]):
    print i
print "\nproduct:"
for i in product('abc',[1,2]):
    print i
print "\npermutation:"
for i in permutations('asdf',2):
    print i
print "\ncombinations:"
for i in combinations('asdf',2):
    print i
print "\ncombinations_with_replacement:"
for i in combinations_with_replacement('asdf',2):
    print i

print "\ngroupby:"
def classify_fuction(age):
    if age<10:
        return "junior"
    elif age>15:
        return "senior"
    else:
        return "middle"
lists=[1,11,21,22,12,2,23,3,13]
print "without sorted"
for m,n in groupby(lists,key=classify_fuction):
    print m,list(n)
print "with sorted"
lists=sorted(lists,key=classify_fuction)
for m,n in groupby(lists,key=classify_fuction):
    print m,list(n)
print "\ncompress:"
for i in compress([11,22,33,44,55],[1,1,0,0,1]):
    print i
for i in compress("hello",[1,1,0,0,1]):
    print i



