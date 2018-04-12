#!/usr/bin/env python
#form cPickle as pickle  #cPickle:C,faster
import pickle
class ccc(object):
    name="hahaha"
    age=20
c=ccc()
print c,c.name,c.age
with open('./05_pickle.txt','w') as f:
    picklestr=pickle.dump(c,f)
    print picklestr
with open('./05_pickle_r.txt','r') as f:
    c1=pickle.load(f)
    print c1,c1.name,c1.age




