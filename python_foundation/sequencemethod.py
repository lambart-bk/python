#!/usr/bin/env python
#coding=utf8

#list
a=[1,5,0,7,1]
print a,len(a),min(a),max(a),all(a),any(a)
print sum(a),a.index(5),a.count(1)

b=[6,9]
b.extend(a)
b.append(13)
b.sort()
print b
b.reverse()
print b
print b.pop(),b

print "\n"

#string
str="lksmkfdsgjnass"
print str,str.count('s')
print str.find('s'),str.index('s')  #find 未找到 return -1;index 未找到会报错
print str.rfind('s'),str.rindex('s')
s="goodidealHello123"
print s.isalnum();
s="safaasfds"
print s.isalpha()
s="21312342346"
print s.isdigit()
s="Hello World My Python"
print s.istitle()
s="   "
print s.isspace()
s="sfss"
print s.islower()
s="SADF"
print s.isupper()
s="hello"
print s,s.upper(),s.capitalize()
s="HELLO"
print s,s.lower()
s="HELLO world"
print s,s.swapcase(),s.title()


#str.split(separator[,max])  return a list
s="there are some people play in football "
print s
print s.split(" ",2)
print s.rsplit(" ",2)
print s.split(" ")  #omit is ok
print s.rsplit(" ")

#separator.join(str) return a string
print ','.join(s.split())
s="threedogplayball"
print ' '.join(s)

#str.strip() return a string or unicode
s="#fdsfdgdvsezvdsbsd35131#"
print s,"\n",s.strip('#')

#str.replace(sub,new_sub)  for string
s="hello world"
print s,"\n",s.replace(' ',',')

#alignment 对齐
#str.center(width)  --ljust--rjust
s=["tom","jack"]
print s[0].center(10)
print s[1].center(10)
print s[0].ljust(10)
print s[1].ljust(10)
print s[0].rjust(10)
print s[1].rjust(10)



