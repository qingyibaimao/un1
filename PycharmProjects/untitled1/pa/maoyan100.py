# -*- coding:utf-8 -*-
'''
import requests
import codecs
import json
from requests.exceptions import RequestException
import re
import multiprocessing

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response = response.text
            print(response)
            return response
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                      +'<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
                      +'(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index': item[0],
            "title": item[2],
            "actor": item[3].strip()[3:],
            "time": item[4].strip()[5:],
            "score": item[5] + item[6],
            "image": item[1]
        }

def write_to_file(content):
    with codecs.open('result.txt', 'a', 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii = False)+ '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' +str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__=='__main__':
    pool=multiprocessing.Pool()
    pool.map(main,[i*10 for i in range(10)])
'''
import requests
from bs4 import BeautifulSoup
import os
'''
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                  "AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
                  "Accept':'Accept=text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
'''
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Connection':'keep-alive',
'Referer':'http://www.mzitu.com/99566'
}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers = headers)
#print(start_html.text)

Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_ = 'all').find_all('a')
for a in all_a:
    title = a.get_text()
    href = a['href']
    html = requests.get(href, headers = headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_ = 'pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span)+1):
        page_url = href + '/' +str(page)
        img_html = requests.get(page_url, headers = headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url= img_Soup.find('div', class_ = 'main-image').find('img')['src']
        name = img_url[-9: -4]
        img = requests.get(img_url, headers = headers)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)

