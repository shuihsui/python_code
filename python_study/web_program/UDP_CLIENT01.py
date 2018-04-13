#!/usr/bin/env python
# -*- coding:utf-8

from socket import *

HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST,PORT)

check = True

udpCliSock = socket(AF_INET,SOCK_DGRAM)

print 'Welcome to our chatroom...'

while check:
	data = raw_input('>')
	if not data:
		break
	udpCliSock.sendto(data,ADDR)
	data,ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data

udpCliSock.close()


