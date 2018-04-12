#!/usr/bin/env python
print "#without context manager"
f=open("file","a+")
print f.closed
f.write("context manager te--\n")
f.close()
print f.closed
print "#with context manager"
with open("file","a++") as f:
    print f.closed
    f.write("context manager --st\n")
print f.closed

print "\n#customized object and special method"
class CMT(object):
    def __init__(self,text):
        print "__init__"
        self.text=text
    def __enter__(self):
        print "__enter__"
        self.text="Enter: "+self.text
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print "__exit__"
        self.text+=" Exit:"
        print exc_type
        print exc_value
        print traceback

print "\n#without context manager"
t=CMT("Hello Context Manager")
print t.text

print "\n#with context manager"
with CMT("Hello Context Manager") as t1:
    print "Block: ",t1.text
print "finally: ",t1.text




