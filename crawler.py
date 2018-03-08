# -*- coding: utf-8 -*-
# @Author: cui
# @Date:   2018-03-07 15:57:51
# @Last Modified by:   cui
# @Last Modified time: 2018-03-07 16:42:34

import re, requests, urllib2, json, time

url = "https://api.coinmarketcap.com/v1/ticker/?limit=2000"

#获取json格式的字符串
page = urllib2.urlopen(url)
data = page.read()

#转换成python中的字典格式，用json.loads()方法
ddata = json.loads(data)

#循环获取titile属性的值
len = len(ddata)

for i in range(0,len):
  x = ddata[i].get('id')
  img_src = 'https://files.coinmarketcap.com/static/img/coins_legacy/128x128/' + x + '.png'

  img = requests.get(img_src)

  with open(x + '.png', 'wb') as file:  #以byte形式将图片数据写入  
    file.write(img.content)  
    file.flush()  
    file.close()  #关闭文件  
    print('第%d张图片下载完成' % (i+1))
    time.sleep(1)  #自定义延时

print('抓取完成')