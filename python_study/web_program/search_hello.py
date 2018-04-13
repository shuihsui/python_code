#!/usr/bin/env python
# -*- coding:utf-8

import urllib
import urllib2

url = 'http://www.baidu.com/s?wd='
wd = 'hello'

url_all = url + wd
print '发起请求'
req = urllib2.Request(url_all)
print '收到反馈信息'
res = urllib2.urlopen(req)
print '反馈信息处理'
data = res.read()
print '保存反馈信息'
f = open('./html/search_hello.html','w+')

f.write(data)

f.close()

print 'Done!'
