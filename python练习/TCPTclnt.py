#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

host='localhost' #本地主机名
port=9999        #端口要一致
bufsiz=1024		 #设置最大缓冲数
addr=(host,port)

tcpCliSock=socket(AF_INET,SOCK_STREAM) #创建客户端套接字
tcpCliSock.connect(addr)               #连接服务器

while True:
	data=input('-->')				   #等待用户输入要发送的消息
	if not data:
		break
	tcpCliSock.send(data.encode('utf-8')) #发送消息给服务器
	data=tcpCliSock.recv(bufsiz)        #接受服务器的消息
	if not data:
		break
	print(data.decode('utf-8'))
tcpCliSock.close()  #关闭客户端套接字  必须在循坏外否则会 OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。