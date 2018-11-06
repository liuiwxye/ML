import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

# 新建一个文件用以存放图片
os.makedirs("./img",exist_ok=True)

url = "http://www.nationalgeographic.com.cn/animals/"
'''
html = requests.get(url).content.decode('utf-8')
等价于 html = urlopen(url).read().decode('utf-8')
'''
html = requests.get(url).text
soup = BeautifulSoup(html,features='lxml')
img_ul = soup.find_all('ul',{'class':'img_list'})

# 网页中有两个ul满足 soup.find_all('ul',{'class':'img_list'})
for ul in img_ul:
    imgs = ul.find_all('img')
    # 每个ul有三个图片地址
    for img in imgs:
        final_url = img['src']
        r = requests.get(final_url,stream=True)
        image_name = final_url.split('/')[-1]
        with open('./img/%s'%image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
            print('Saved %s' % image_name)
            
