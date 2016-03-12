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

number = 0

def getImg(m, url):
    print('In getImg')

    #print(url)

    #if str(url[-1]) == '/':
    #    #print('In if')
    #    pass
    #else:
    #    url = str(url) + '/'
    #    #print('In else')

    #print(url)
    #return

    imglist = re.findall(r'[\w\.\/]+jpg', str(m))  
    imglist = list(set(imglist))

    temp = imglist
    for x in temp:
        if str(url[-1]) != '/' and str(x[0]) != '/':
            url = str(url) + '/'
        elif str(url[-1]) == '/' and str(x[0]) == '/':
            url = url[:-1]
        else:
            pass


        #if str(url[-1]) == '/' and str(x[0]) == '/':
        #    pass
        #elif str(url[-1]) == '/' and str(x[0]) != '/':
        #    pass
        #elif str(url[-1]) != '/' and str(x[0]) == '/':
        #    pass
        #else:
        #    #print('Before ' + str(url) + str(x))
        #    url = str(url) + '/'
        #    #print('After ' + str(url) + str(x))
        #    #input()

    try:
        global number
        for x in imglist:
            templist = str(url) + str(x)
            print(templist)
            try:
                #创建文件
                f = open("/home/acer/python/webapp/JPG/" + str(number) + ".jpg", "w")
                f.flush()
                f.close()
                #下载图片 
                image = urllib.request.urlretrieve(templist, "/home/acer/python/webapp/JPG/" + str(number) +".jpg")
            except BaseException:
                print('下载错误')
            finally:
                number += 1
                print('number = %d' % (number - 1))
    except IndexError:
        print('Done.')

    return imglist

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
        imglist = getImg(m, url)
        #list去重，先将list转为set再转为list即可
        check = list(set(check))

        for x in check:
            if x in has_q:
                break
            else:
                wait_q.append(x)

        try:
            url = wait_q.pop()
            #pass
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


