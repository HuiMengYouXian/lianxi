#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''此服务器能够接受客户端的信息，返回时在信息前加一个时间戳'''
from socket import *
from time import ctime
import os

host='localhost'#本地主机名
port=9999		#端口号
bufsiz=1024     #设置最大缓冲数
addr=(host,port)
tcpSerSock=socket(AF_INET,SOCK_STREAM) #创建服务器套接字
tcpSerSock.bind(addr) #绑定端口
tcpSerSock.listen(5) #指定等待连接最大数

while True:
	print('等待连接...')
	tcpCliSock,addr=tcpSerSock.accept() #接受客户端连接
	print('...连接来自:',addr)
	
	while True:
		data=tcpCliSock.recv(bufsiz) #接受数据
		if not data:
			break
		tcpCliSock.send(('时间:[%s] 信息:%s' % (ctime(),data.decode('utf-8'))).encode('utf-8')) #发送数据
	tcpCliSock.close() #关闭客户端套接字  必须在循坏外否则会 OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。