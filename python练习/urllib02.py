#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

auth_handler=urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
						  uri='http://mahler:8092/site - updates.py',
						  user='18775542644',
						  passwd='18775542644')
opener=urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
s=urllib.request.urlopen('https://pan.baidu.com')
print(s.read().decode('utf-8'))