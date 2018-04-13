#!/usr/bin/env python
# -*- coding:utf8

from poplib import *

#连接邮件服务器
p = POP3('pop.163.com')
#使用用户名以及帐号登录
p.user('17607140510@163.com')
try:
	p.pass_("zhangyao123")
	#得到邮件状态,为一个2元组,(消息数量,消息总大小)
	zt = p.stat()
	#获取邮件信息
	rsp,msg,siz = p.retr(zt[0])
	#打印邮件
	for eachLine in msg:
		print(eachLine)
except poplib.error_proto as e:
	print("Password is wrong!")
	p.quit()

p.quit()
print("Done")


