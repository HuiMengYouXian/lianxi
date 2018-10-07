#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''用于下载FTP服务器中的文件'''
import ftplib
import os
import socket

host='192.168.43.169'
dirn='/'
file='1.jpg'

def main():
	try:
		f=ftplib.FTP(host)
	except(socket.error,socket.gaierror) as e:
		print('ERROR:不能到达"%s"' % host)
		return
	print('***连接到主机"%s"' % host)
	
	try:
		f.login() #匿名登录
	except ftplib.error_perm:
		print('ERROR:不能匿名登录')
		f.quit()
		return
	print('***匿名登录')
	
	try:
		f.cwd(dirn)#把当前工作目录设置为dirn
	except ftplib.error_perm:
		print('ERROR:不能打开"%s"' % dirn)
		f.quit()
		return
	print('***改为"%s"文件夹' % dirn)
	
	try:
		f.retrbinary('RETR %s' % file,open(file,'wb').write)
	except ftplib.error_perm:
		print('ERROR:不能读取文件"%s"' % file)
		os.unlink(file)
	else:
		print('***从"%s"目录下载' % file)
	f.quit()
	return

if __name__=='__main__':
	main()