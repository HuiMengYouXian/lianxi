#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"把一个Unicode字符串写入磁盘文件，然后再把它读出并显示出来"
from io import BytesIO
CODEC="utf-8"
FILE='unicode.txt'

f=open(FILE,"w")
f.write('Hello world!')
f.close()

f=open(FILE,'r')
bytes_in=f.read()
f.close()
hello_in=bytes_in.decode('utf-8')
print(hello_in)