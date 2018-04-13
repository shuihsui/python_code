#!/usr/bin/env python
# -*- coding:utf-8
metro_areas = [('Tokyo','JP',36.933,(1,2))
	,('Beijing','CN',223.23,(2,3))
	,('SP','BR',23.34,(4,5))
	,('xs','ss',23.44,(3,-10))
]

print('{:15} | {:^9} | {:^9}'.format('','lat','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name,cc,pop,(lati,longti) in metro_areas:
	if longti <= 0:
		print(fmt.format(name,lati,longti))
	
