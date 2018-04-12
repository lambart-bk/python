#!/usr/bin/env python
def subfuc(x,y):
    try:
        c=x/y
    except TypeError:
        print "TypeError"
    except ZeroDivisionError:
        print "y==0"
    else:
        print  "success"
        print c
    finally:
        print "\nsubfuc end"
try:
    a=input()
    subfuc(30,a)
    print "#raise StopIteration"
    raise StopIteration
except StopIteration:
    print "StopIteration"
except :
    print "exception from sub"





