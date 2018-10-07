#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''新闻采集'''

from datetime import date,timedelta
from nntplib import NNTP
from email import message_from_string
from urllib.request import urlopen
import re,textwrap

def wrap(string, width=50):  # 定义处理字符串宽度的方法
    return '\n'.join(textwrap.wrap(string, width)) + '\n'  # 返回处理之后的结果
	
class NewsItem: #新闻内容类
	def __init__(self,title,body,byteNumber=1):
		self.title=title
		self.body=body
		self.byteNumber=byteNumber  #每个字符的字节数量
class NNTPSource:  # NNTP新闻源类
    def __init__(self, server_name, group, window):
        self.server_name = server_name  # 服务器地址
        self.group = group  # 新闻组名称
        self.window = window  # 时间窗口

    def getItems(self):  # 新闻生成器
        yesterday = date.today() - timedelta(days=self.window)  # 计算新闻获取的起始时间
        server = NNTP(self.server_name)  # 创建服务器连接对象
        ids = server.newnews(self.group, yesterday)[1]  # 获取新闻id列表
        count = 0  # 创建计数变量
        for id in ids:  # 循环获取新闻id
            count += 1  # 计数递增
            if count <= 10:  # 如果计数小于10
                article = server.article(id)[1][2]  # 获取指定id的新闻文章
                lines = []  # 创建每行新闻内容的列表
                for line in article:  # 从新闻文章中读取每一行内容
                    lines.append(line.decode())  # 将每行新闻内容解码，添加到新闻内容列表。
                message = message_from_string('\n'.join(lines))  # 合并新闻列表内容为字符串并转为消息对象
                title = message['subject'].replace('\n', '')  # 从消息对象中获取标题
                body = message.get_payload()  # 从消息对象中获取到新闻主体内容
                if message.is_multipart():  # 如果消息对象包含多个部分
                    body = body[0]  # 获取到的内容中第1个部分获取新闻主体内容
                yield NewsItem(title, body)  # 生成1个新闻内容对象
            else:  # 如果超出10条内容
                break  # 跳出循环
        server.quit()  # 关闭连接
class SimpleWebSource: #网页新闻源类
	def __init__(self,url,titlePattern,bodyPattern):
		self.url=url  #网页地址
		self.titlePattern=re.compile(titlePattern)	#提取新闻标题的正则表达式
		self.bodyPattern=re.compile(bodyPattern)	#提前新闻主体内容的正则表达式
	def getItems(self):	#新闻生成器
		text=urlopen(self.url).read().decode()	#读取目标网页内容并解码
		titles=self.titlePattern.findall(text)	#通过正则表达式读取所有新闻标题
		bodies=self.bodyPattern.findall(text)	#通过正则表达式读取所有新闻主体内容
		for title,body in zip(titles,bodies):	#将新闻标题和内容混合到一起并获取每一条新闻的标题和主体内容
			yield NewsItem(title,wrap(body),2)	#生成一个每行新闻具体指定宽度并且每个字符宽度为2个字节的新闻内容对象
		
class PlainDestination: #普通输出目标类
	def receiveItems(self,items):	#定义接收到新闻对象时的处理方法
		for item in items:	#遍历新闻对象列表
			print(item.title)	#显示输出新闻标题
			print('-'*item.byteNumber*len(item.title))	#显示输出分隔线
			print(item.body)	#显示输出新闻主体内容
			
class HTMLDestination:  # HTML文件目标类
    def __init__(self, filename):
        self.filename = filename  # 创建的HTML文件名称

    def receiveItems(self, items):  # 定义接收到新闻对象时的处理方法
        with open(self.filename, 'w', encoding='UTF-8') as file:  # 打开或创建HTML文件
            file.write('<html>\n'  # 写入HTML文件头部内容、网页主体中的标题以及新闻列表的开始标签
                       '<head>\n'
                       '<meta charset="UTF-8">\n'  # 注意：需要声明网页文件的编码类型
                       '<title>24小时快讯</title>\n'
                       '</head>\n'
                       '<body>\n'
                       '<h1>24小时快讯</h1>\n'
                       '<ul>\n')
            id = 0  # 初始化HTML文件中的新闻id
            for item in items:  # 遍历新闻对象集合
                id += 1  # 递增新闻id
                file.write('<li><a href="#%i">%s</a></li>\n' % (id, item.title))  # 写入1条新闻的列表项并指定id
            file.write('</ul>')  # 写入新闻列表的结束标签
            id = 0  # 初始化HTML文件中的新闻id
            for item in items:  # 遍历新闻对象集合
                id += 1  # 递增新闻id
                file.write('<h2><a name="%i">%s</a></h2>\n' % (id, item.title))  # 写入1条新闻的标题并指定id
                file.write('<p>' + item.body + '</p>\n')  # 写入1条新闻的主体内容
            file.write('</body>\n'  # 写入HMTL文件主体的结束标签和HTML文件结束标签
                       '</html>')

class NewsAgent: #新闻代理类 负责处理新闻源和输出目标，进行最终的分发
	def __init__(self):
		self.sources=[]	#新闻源列表
		self.destinations=[]	#输出目标列表
	def add_source(self,source):	#添加新闻源的方法
		self.sources.append(source)
	def add_destinations(self,dest):	#添加输出目标的方法
		self.destinations.append(dest)
	def	distribute(self):	#进行分发的方法
		items=[] #新闻对象列表
		for source in self.sources:	#遍历每一个新闻源
			items.extend(source.getItems())	#从新闻源的生成器将所有新闻对象添加到新闻对象列表
		for dest in self.destinations:	#遍历每一个输出目标
			dest.receiveItems(items)	#调用处理新闻对象的方法处理新闻对象集合
def runDefaultSetup(): #主程序  负责指定新闻来源和输出目标，将来源和目标添加到代理类对象中进行处理，完成最终的分发	
	agent=NewsAgent() #创建代理类对象
	server_name='web.aioe.org'
	group='comp.lang.python'
	window=1 #指定时间窗口
	clpa = NNTPSource(server_name, group, window)  # 创建新闻源对象
	
	url=r'http://36kr.com/newsflashes'	#指定目标网页地址
	titlePattern=r'"pin":"0","title":"(.{10,60})","cover"'	#组织提取新闻标题的正则表达式
	bodyPattern=r'"description":"(.{100,400})","conver"'	#组织提取新闻主体的正则表达式
	web=SimpleWebSource(url,titlePattern,bodyPattern)	#创建新闻源对象
	agent.add_source(web)	#添加网页新闻源
	agent.add_source(clpa)  # 添加NNTP新闻源对象
	agent.add_destinations(PlainDestination()) #添加普通输出目标对象
	agent.add_destinations(HTMLDestination('news.html', ))  # 添加输出HTML文件目标对象
	agent.distribute()	#调用分发方法

if __name__=='__main__':
	runDefaultSetup()	#执行主程序