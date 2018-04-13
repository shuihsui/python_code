#!/usr/bin/env python
# -*- coding:utf-8

html = """
	<html>
	<head>
	<meta charset="utf-8">
	</head>
	<body>
	<p>Hello,New Python!</p>
	<a href="http://www.baidu.com">BaiDu</a>
	<a href="http://www.panda.tv">PandaTv</a>
	</body>
	</html>"""

with open("link.html","w") as f:
	f.write(html)

print "Done!"



