# -*- coding:utf8
#!/usr/bin/env python3.6
#
#python 3.x 以后的版本range代替了xrange

from urllib import request
import sys
import re

def testArg():
	'''测试输入参数，只需要一个参数'''
	if len(sys.argv) != 2:
		print('只需要一个参数就够了')
		tipUse()
		exit()
	else:
		TP = TestProxy(sys.argv[1])

def tipUse():
	'''显示提示信息'''
	print('该程序只能输入一个参数，这个参数必须是一个可用的proxy')
	print('usage:python testUrllibWithProxy.py http://1.2.3.4:5')
	print('usage:python testUrllibWithProxy.py https://1.2.3.4:5')

class TestProxy(object):
	"""这个类的作用是测试proxy是否有效"""
	def __init__(self,proxy):
		self.proxy = proxy
		self.checkProxyFormat(self.proxy)
		self.url = 'http://www.baidu.com'
		self.timeout = 5
		self.flagword = '百度'
		self.useProxy(self.proxy)

	def checkProxyFormat(self,proxy):
		try:
			proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\:[\d]{1,5}$')
			re.search(proxyMatch,proxy).group()
		except AttributeError:
			tipUse()
			exit()
		flag = 1
		proxy = proxy.replace('//','')
		try:
			protocol = proxy.split(':')[0]
			ip = proxy.split(':')[1]
			port = proxy.split(':')[2]
		except IndexError:
			print('下标出界')
			tipUse()
			exit()
		flag = ip.split('.')[0] in map(str,range(1,256)) and flag
		flag = ip.split('.')[1] in map(str,range(256)) and flag
		flag = ip.split('.')[2] in map(str,range(256)) and flag
		flag = ip.split('.')[3] in map(str,range(1,255)) and flag
		flag = protocol in ['http','https'] and flag
		flag = port in map(str,range(1,65535)) and flag
		'''这里是在检查proxy的格式'''
		if flag:
			print('输入的代理服务器地址符合标准')
		else:
			tipUse()
			exit()

	def useProxy(self,proxy):
		'''利用代理访问百度，并查找关键词'''
		protocol = proxy.split('//')[0].replace(':','')
		ip = proxy.split('//')[1]
		opener = request.build_opener(request.ProxyHandler({protocol:ip}))
		request.install_opener(opener)
		try:
			req = request.Request(url)
			page = request.urlopen(req)
		except:
			print('连接错误，退出程序')
			exit()
		str = page.read()
		if re.search(self.flagword,str):
			print('已取得特征词，该代理可用')
		else:
			print('该代理不可用')


if __name__ == '__main__':
	testArg()
		
