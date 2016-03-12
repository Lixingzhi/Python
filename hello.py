#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import string, urllib.request, urllib.error
import re
import queue

urlbase = 'http://www.snut.edu.cn'

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
} 

def getImg(m):
    print('In getImg')
    imglist = re.findall(r'src="[\w\.\/]+jpg"', str(m))  
    #imglist = re.findall(r'images/tb6.jpg', str(m))  
    #imglist = re.findall(r'_mediafile/snutedu/2015/04/30/34csr9l1ii.jpg', str(m))  
    imglist = list(set(imglist))

    #imgurl = imglist.pop()
    imglist = re.findall('[\w\.\/]+jpg', str(imglist))

    temp = imglist.pop()
    templist = 'http://www.snut.edu.cn/' + str(temp)

    print(templist)

    image = urllib.request.urlretrieve(templist, "/home/acer/python/webapp/test.jpg", None)

    return imglist

    #x = 0  
    #for imgurl in imglist:  
    #    urllib.urlretrieve(imgurl,'%s.jpg' % x)  
    #    x = x + 1 

def spider(url):
    #sName = 'test.html'
    #print('正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......')
    f = open('temp', 'w+')

    wait_q = []
    has_q = []

    while True:
        req = urllib.request.Request(url, None, header)
        try:
            socket = urllib.request.urlopen(req, timeout = 2)
            print('已下载' + str(url))
            f.write('已下载' + url + '\n')
            f.flush()
        except BaseException:
            print('%s 不可达' % url)
        #except urllib.error.HTTPError:
        #    print('%s 不可达' % url)
        #    f.write(url + '不可达' + '\n')
        #    f.flush()
        #except urllib.error.URLError:
        #    print('%s 不可达' % url)
        #    f.write(url + '不可达' + '\n')
        #    f.flush()
        #except socket.timeout:
        #    pass
        #    print('%s 超时' % url)
        #    f.write(url + '超时' + '\n')
        #    f.flush()
            
        try:
            m = socket.read()#.decode('utf-8')
        except BaseException:
            print('%s 不可达' % url)
        has_q.append(url)
        check = re.findall(r'http://[\w.]+snut.edu.cn[\w\/]+', str(m))
        imglist = getImg(m)
        #list去重，先将list转为set再转为list即可
        check = list(set(check))

        for x in check:
            if x in has_q:
                break
            else:
                wait_q.append(x)

        try:
            #url = wait_q.pop()
            break
        except IndexError:
            print('Done.')
            f.close()
            break


            
        #while x:
        #    x = wait_q.get()
        #    print(x)

        #print('Done')

        #f.write(m)  
        #f.close() 

spider(urlbase)


