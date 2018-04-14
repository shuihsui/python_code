# -*- coding:utf8

from urllib import request
from urllib import parse

def clear():
	'''该函数用于清屏'''
	print(u'内容较多，显示3秒后翻页')
	time.sleep(3)
	OS = platform.system()
	if (OS == u'Windows'):
		os.system('cls')
	else:
		os.system('clear')

def linkBaidu():
	url = 'http://www.baidu.com'
	try:
		req = request.Request(url)
		page = request.urlopen(req)
	except urllib2.URLError:
		print(u'网络地址错误')
		exit()
	with open('./baidu.txt','wb') as fp:
		fp.write(page.read())
	print('获取url信息，response.geturl() \n:%s' % page.geturl())
	print('获取返回代码，response.getcode() \n:%s' % page.getcode())
	print('获取返回信息，response.info() \n:%s' % page.info())
	print('获取的网页内容已经保存在当前目录的baidu.txt中，请自行观察看')

if __name__ == '__main__':
	linkBaidu()