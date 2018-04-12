#!/usr/bin/env python
import time
print time.time()  #wall clock time  unit:second
print time.clock() #processor clock time unit:second
#struct_time:tm_year,tm_mon,tm_mday...
print time.gmtime() #return UTC time
print time.localtime()  #return local time
print time.mktime(time.localtime()) #transform to walltime

import datetime
t=datetime.datetime(2016,12,20,14,29)
print t
dt=datetime.timedelta(minutes=35)
print t-dt

#datetime str format parse
format="%Y-%m-%d %H:%M:%S"
str="2016-12-20 14:35:26"
d=datetime.datetime.strptime(str,format)
print d
print d.strftime("%H:%M:%S %Y-%m-%d")



