import re
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup

# 爬取网站所有的链接
base_url = "https://morvanzhou.github.io/"


def crawl(url):
    response = urlopen(url).read().decode('utf-8')
    return response


def parse(html):
    soup = BeautifulSoup(html, features='lxml')
    urls = soup.find_all('a', {'href':re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    # og:url 开放内容协议
    url = soup.find('meta', {'property': 'og:url'})['content']
    return title, page_urls, url


count, t1 = 1, time.time()

unseen = set([base_url, ])
seen = set()

if base_url != "https://morvanzhou.github.io/":
    restricted_crawl = True
else:
    restricted_crawl = False
    
while len(unseen) != 0:
    if restricted_crawl and len(seen) >= 20:
        break
    
    print('\nCrawling...')
    htmls = [crawl(url) for url in unseen]
    
    print('\nParsing...')
    results = [parse(html) for html in htmls]
    
    print('\nAnalysing...')
    seen.update(unseen)
    unseen.clear()
    
    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        # 过滤掉已经crawl的页面seen，如果不过滤，页面相互引用容易死循环
        unseen.update(page_urls - seen)
    print('time:',time.time()-t1)
print('Total time: %.1f s' % (time.time()-t1, ))
