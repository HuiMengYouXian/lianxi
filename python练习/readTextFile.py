#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'读取并显示文本文件'

#获取文件名字
fname=input('Enter filename:')
print('\n')

#尝试打开文件读取
try:
	fobj=open(fname,'r')
except IOError as e:
	print("***文件打开错误:",e)
else:
    #向屏幕显示内容
	for eachLine in fobj:
	    print(eachLine,end='')
	fobj.close()