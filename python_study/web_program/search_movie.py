#!/usr/bin/env python
# -*- coding:utf-8

import urllib
import urllib2
import os

url = 'http://www.baidu.com/s?wd='

wd = '微微一笑很轻成'

wdcode = urllib.quote(wd)

url_all = url + wdcode
print url_all
print '发起请求'
req = urllib2.Request(url_all)
print '收到反馈信息'
res = urllib2.urlopen(req)
print '反馈信息处理'
data = res.read()
print '保存反馈信息'
f = open('search_movie.html','w+')

f.write(data)

f.close()

print 'Done!'

