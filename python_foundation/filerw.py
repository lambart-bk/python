#!/usr/bin/env python
dic={'name':'tom','age':20}
f=open("./file","w")
for k in dic.keys():
    f.write(k+'\t')
f.write("\n")
for k in dic.keys():
    f.write(dic[k].__str__()+'\t')
f.close()
