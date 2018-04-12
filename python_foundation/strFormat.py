#!/usr/bin/env python
#coding=utf8
name='Tom'
age=20
print "my name is %s,I\'m %d" % (name,age) #需要(),不能直接name,age

d={'name':'Tom','age':20}
print "my name is %(name)s,I\'m %(age)d" % d

print "%%%d" % 100

#%[(name)][flag][width].[precision] typecode
#flag:'+','-',' ','0'
print "%+10x" % 256
print "%-5.2f" % 1.667
print "% 4d" % 4
print "%04d" % 4
print "%4d" % -4

#动态代入width precision *
print "%.*f" % (2,1234.56789)

