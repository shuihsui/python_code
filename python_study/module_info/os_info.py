# -*- coding:utf8

import os
import sys

all = os.__all__

all.sort()

try:
	f = open('os_info.txt','w')
	f.close()
except OSError:
	print('The file has existed.')


for i in all:
	cmd = 'f.write(os.' + i +')'
	cmd_doc = 'f.write(os.' + i + '.__doc__)'
	f = open('os_info.txt','a+')
	f.write('command: 	' + 'os.' + i + '\n')
	try:
		f.write('---------------------info\n')
		try:
			exec(cmd_doc)
		except:
			f.write('None')	
		f.write('\n---------------------output\n')
		exec(cmd)
		f.write('\n---------------------\n')
	except:
		f.write('\n*************Need Args\n\n')

	f.close()
