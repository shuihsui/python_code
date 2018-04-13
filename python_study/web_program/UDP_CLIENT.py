#!/usr/bin/env python
# -*- coding:utf-8

from socket import *

HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST,PORT)

check = True

def returnData():
	data,ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		return false
	return data

udpCliSock = socket(AF_INET,SOCK_DGRAM)

print 'Welcome to our chatroom...'

while check:
	if returnData():
		print data
	data = raw_input('>')
	if not data:
		break
	udpCliSock.sendto(data,ADDR)

udpCliSock.close()


