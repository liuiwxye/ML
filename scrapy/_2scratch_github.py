import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 新建一个文件用以存放图片
os.makedirs("./img",exist_ok=True)


home="https://github.com"

# 图片来源
url='https://github.com/liuiwxye/SQL/tree/master/src'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
imgsrc = soup.find_all("a",{"href":re.compile('/liuiwxye/SQL/blob/master/src/.*\.png')})
l=[l['href'] for l in imgsrc]


# github上的图片，路径一般都有blob，所有我们需要再进入blob目录寻找真正的图片路径
'''
形如 https://github.com/liuiwxye/SQL/blob/master/src/RIGHTJOIN.png
我们需要在这个页面找到图片的真实路径
'''
for i in range(len(l)):
    sub_url=home+l[i]
    sub_html = urlopen(sub_url).read().decode('utf-8')
    soup = BeautifulSoup(sub_html,features='lxml')
    imgsrc1 = soup.find_all("img",{"src":re.compile('/liuiwxye.*')})
    l1=[l['src'] for l in imgsrc1]
    urlretrieve(home+l1[0],'./img/image%d.jpg'%i)
    
