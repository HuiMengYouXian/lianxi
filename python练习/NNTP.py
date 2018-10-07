#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nntplib import NNTP
from datetime import date,timedelta  #获取24小时的新闻源需要datetime模块

server=NNTP('web.aioe.org') #实例化NNTP服务器连接对象
yesterday=date.today()-timedelta(days=1) #当前时间减去时间间隔
group='comp.lang.python' #新闻组名称

def get_id():  #创建新闻id生成器
	ids=server.newnews(group,yesterday)[1] #获取进近4小时新闻内容中的所有新闻id
	for id in ids: #遍历所有新闻id
		yield id  #生成1个新闻id
		
ids=get_id() #创建新闻id生成器对象
id=next(ids) #获取第一个新闻id
head_data = server.head(id)[1][2] #获取新闻头部内容
body_data=server.body(id)[1][2]   #获取新闻的主体内容
title = '' #创建标题
body = '' #创建主体

for line in head_data:  #遍历头部内容
	if line.decode().lower().startswith('subject:'):  #如果发现新闻标题特征（"subject:"开头）  startswithk开始于
		title=line[9:].decode() #去除特征文字保存标题内容
for line in body_data:  #遍历主体内容
	if line.decode().endswith('='):  #如果行内容以'='结尾  endswith结束于
		line=line[:-1] #去除“=”
	if line.decode().endswith('=20'):	#如果行内容以'=20'结尾
		line=line[:-3]+b'\n'	#去除'=20'并添加换行符
	body+=line.decode()  #将每行内容组织为新的主体内容

print(title) #显示输出标题内容
print('-'*len(title)) #显示输出和标题字符数量同等的'-'符号
print(body)  #显示输出主体内容
server.quit()	#退出与服务器的连接