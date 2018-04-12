#!/usr/bin/env python
import re
string1="my id is 1854528"
string2="1213sgfs123s3g132"
pattern="\d+"
replacement="@"
m=re.search(pattern,string1)
print m.group(0)
m=re.match(pattern,string2)
print m.group(0)
print re.sub(pattern,replacement,string2)
print re.split(pattern,string2)
print re.findall(pattern,string2)
#char: . [a-f] [1-6] \s \d \w(0-9a-zA-Z)
#duplicate: * + ? {m} {m,n}
p=re.compile("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
m=p.search("hahaha@163")
if m!=None:
    print m.group()
else:
    print "None"

