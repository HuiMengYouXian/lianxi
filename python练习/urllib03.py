#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''获取网站的cookie并保存成文件'''

import http.cookiejar,urllib.request

filename='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)