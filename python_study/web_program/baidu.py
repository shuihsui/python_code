#!/usr/bin/env python3.5
# -*- coding:utf-8

import urllib.request

url = 'http://www.baidu.com'

req = urllib.request.Request(url)

data = (urllib.request.urlopen(req)).read()

print(data)

f = open('baidu.html','wb')

f.write(data)

f.close()

print('Done!')
