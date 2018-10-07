#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'creat text file'

import os
ls=os.linesep

#获取文件名字-
while True:
	fname=input('输入你要创建的文件\n')
	if os.path.exists(fname):    #path存在返true exists存在
		print("ERROR: '%s' already exists(已经存在)" % fname)
	else:
		break

#获取每行的文本内容
all=[]
print("\n输入每行内容(通过'.'退出).\n")

#循坏直到用户终止输入
while True:
	entry=input('>')
	if entry == '.':
	    break
	else:
	    all.append(entry)
	
#用适当的行结束将文件写入文件
fobj=open(fname,'w')
fobj.writelines(['%s%s'%(x,ls) for x in all])
fobj.close()
print('完成!')