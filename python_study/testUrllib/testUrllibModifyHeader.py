# -*- coding:utf8
#在python编程中注意编码问题~~真的是爆炸
#尤其是在写入文件的时候，一定要选择转换为utf-8

__author__ = 'shuihsui'

import urllib.request
import userAgents
import gzip

class UrllibModifyHeader(object):
	"""docstring for UrllibModifyHeader"""
	def __init__(self):
		'''pc + IE 9.0 的UserAgent'''
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		'''Mobile + safari  的UserAgent'''
		MUUA = userAgents.mobileUserAgent.get('safari iOS 4.33 – iPad')

		self.url = 'http://fanyi.youdao.com'

		self.useUserAgent(PIUA,1)
		self.useUserAgent(MUUA,2)

	def useUserAgent(self,userAgent,name):
		req = urllib.request.Request(self.url,headers={userAgent.split(':')[0]:userAgent.split(':')[1],'Accept-Encoding': 'gzip'})
		page = urllib.request.urlopen(req)
		data = gzip.decompress(page.read()).decode('utf-8')

		# print(page.info().get('Content-Encoding'))

		filename = str(name) + '.html'
		with open(filename,'wb+') as fp:
			fp.write(userAgent.encode('utf-8'))
			fp.write('\n\n'.encode('utf-8'))
			fp.write(data.encode('utf-8'))

if __name__ == '__main__':
	umh = UrllibModifyHeader()

		