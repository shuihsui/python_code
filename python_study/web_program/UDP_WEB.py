#!/usr/bin/env python
# -*- coding:utf-8

from socket import *
from time import ctime
import os

HOST = ''
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
addrs = []

while True:
	data,addr = udpSerSock.recvfrom(BUFSIZ)
	if addr not in addrs:
		addrs.append(addr)
	print addrs
	for addr1 in addrs:
		udpSerSock.sendto('[%s] %s' % (addr1,data),addr1)

udpSerSock.close()
