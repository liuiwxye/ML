import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

os.makedirs("./img",exist_ok=True)
# IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

url='https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7\
%E9%BA%A6%E5%85%8B%E6%A0%BC%E9%9B%B7%E8%BF%AA/142344?fr=aladdin'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
imgsrc = soup.find_all('img',{'src':re.compile(".*?\.jpg")})
l = [l['src'] for l in imgsrc]

for i in range(len(l)):
    print(i)
    urlretrieve(l[i],'./img/image%d.jpg' %i)

    
