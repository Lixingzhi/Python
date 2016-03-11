#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

import string, urllib2
import re

urlbase = 'http://www.snut.edu.cn/'

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
} 

def spider(url):
    for i in range(1):  
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名   
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'w+')
        
        req = urllib2.Request(url, str(header))
        socket = urllib2.urlopen(req)
        m = socket.read()
        #m = urllib2.urlopen(url + str(i)).read()  
        check = re.findall(r'http://[\w.]+', m)
        for x in check:
            print(x)
        f.write(m)  
        f.close() 

spider(urlbase)


