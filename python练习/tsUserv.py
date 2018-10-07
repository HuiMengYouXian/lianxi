#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''此服务器能够接受客户端的信息，返回时在信息前加一个时间戳'''
from socket import *
from time import ctime

host='localhost'#本地主机名
port=8888		#端口号
bufsiz=1024     #设置最大缓冲数
addr=(host,port)
udpSerSock=socket(AF_INET,SOCK_DGRAM) #创建服务器套接字
udpSerSock.bind(addr) #绑定端口

while True:
	print('等待消息...')
	data,addr=udpSerSock.recvfrom(bufsiz)
	udpSerSock.sendto(('[%s] %s' % (ctime(),data.decode('utf-8'))).encode('utf-8'),addr)
	print('...收到并返回:',addr)
udpSerSock.close()