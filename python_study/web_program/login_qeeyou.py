#!/usr/bin/env python
# -*- coding:utf-8

import urllib
import urllib2
print '奇游加速器登录url'
url = 'http://www.qeeyou.cn/api/front/login'
values = {
'username':'1610969069@qq.com',
'pwd':'zhangyao123'
}
data = urllib.urlencode(values)

print 'post请求会报405错误'
print '发起请求'
req = urllib2.Request(url,data)
print '添加浏览器伪装'
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
print '获取反馈信息'
data = urllib2.urlopen(req).read()
print '保存反馈信息'
f = open('login_qeeyou.html','w+')

f.write(data)

f.close()

print 'Done!'

