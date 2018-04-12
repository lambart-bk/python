#!/usr/bin/env python

#range(start,stop,step)
s="h2eililfos gwvodrjlnd"
for i in range(0,len(s),2):
    print s[i]

#enumerate()
for i,v in enumerate(s):
    print i,v

#zip()
#cluster
la=[1,2,3]
lb=[4,5,6]
lc=['a','b','c']
print zip(la,lb,lc)
for a,b,c in zip(la,lb,lc):
    print type(a),a,b,c

#decompose
zipped=zip(la,lb,lc)
a,b,c=zip(*zipped)
print type(a),a,b,c





