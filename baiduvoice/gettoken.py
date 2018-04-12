#! /usr/bin/env python

import urllib
import urllib2
url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=R8Gq7LOkbIj3drndyw2rhaXV&client_secret=682791ef9213c867fae0ab5d0b298b05&'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page


