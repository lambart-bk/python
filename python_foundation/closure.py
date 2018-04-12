#!/usr/bin/env python
def line_conf():
    b=10
    def line(x):
        return 2*x+b
    return line
b=1
my_line=line_conf()
print "__closure__: ",my_line.__closure__
print "__closure__[0]: ",my_line.__closure__[0].cell_contents

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line
mline1=line_conf(1,2)
mline2=line_conf(3,4)
print mline1(5),mline2(2)
