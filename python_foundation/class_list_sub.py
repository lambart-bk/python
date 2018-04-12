#!/usr/bin/env python
class mylist(list):
    def __sub__(self,b):
        a=self[:]
        b=b[:]
        while len(b)>0:
            e_b=b.pop()
            if(e_b in a):
                a.remove(e_b)
        return a
print mylist([1,2,3,7,4,5,6])-mylist([4,5,6])
