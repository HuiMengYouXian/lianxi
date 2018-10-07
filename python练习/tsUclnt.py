#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

host='localhost' #本地主机名
port=8888        #端口要一致
bufsiz=1024		 #设置最大缓冲数
addr=(host,port)

udpCliSock=socket(AF_INET,SOCK_DGRAM)

while True:
	data=input('-->')
	if not data:
		break
	udpCliSock.sendto(data.encode('utf-8'),addr)
	data,addr=udpCliSock.recvfrom(bufsiz)
	if not data:
		break
	print(data.decode('utf-8'))
udpCliSock.close()