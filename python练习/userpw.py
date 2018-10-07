#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''这个程序用于管理登陆系统的用户信息：用户名和密码。登录用户账号建立后
   已存在用户可以用用户名和密码重返系统，新用户不能用别人的登录名建立用户账号'''
import pickle
def newuser(db):
	prompt='输入要创建的用户名:'
	while True:
		name=input(prompt)
		if name in db.keys():
			print('用户名已存在,请尝试另一个:')
			break
		pwd=input("设置你的密码:") 
		db[name]=pwd
		f=open('userpw.txt','ab')
		pickle.dump(db,f)
		f.close()
		break

def olduser(db):
	name=input("用户名:")
	pwd=input('密码:')
	passwd=db.get(name)
	if passwd==pwd:
		print('欢迎回来',name)
	else:
		print('密码错误')

def deluser(db,name):
	if db.pop(name):
		print('删除成功')
	else:
		print('操作失败')

def showuser(db):
	for name,passwd in db.items():
		print('用户名:%s\t密码:%s' % (name,passwd))
def showmenu(db):
	prompt='''创建新用户请输入N
老用户登录请输入E
退出请输入Q
删除一个用户S
显示所有用户及密码R
输入选择:'''
	done=False
	while not done:
		chosen=False
		while not chosen:
			try:
				choice=input(prompt).strip()[0].lower()
			except (EOFError,KeyboardInterrupt):
				choice='q'
			print('\n你的选择:[%s]' % choice)
			if choice not in 'neqsr':
				print('输入无效,请重试')
			else:
				chosen=True
		if choice=='q':
			done=True
		if choice=='n':newuser(db)
		if choice=='e':olduser(db)
		if choice=='s':
			name=input('输入要删除的用户名:')
			deluser(db,name)
		if choice=='r':showuser(db)

if __name__=='__main__':
	f=open('userpw.txt','rb')
	db=pickle.load(f)
	f.close()
	showmenu(db)