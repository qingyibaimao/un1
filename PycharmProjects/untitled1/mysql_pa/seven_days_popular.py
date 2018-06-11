# -*- encoding:utf-8 -*-

from lxml import etree
import requests
import pymongo
import re
import json
import time

#mongodb
client =pymongo.MongoClient('localhost', 27017)
test = client['test']
sevenday = test['sevenday']
embody = test['embody']

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

urls = ['https://www.jianshu.com/trending/weekly?page={}'.format(str(i)) for i in range(0,11)]

def get_url(url):
    html = requests.get(url, headers = headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class = "note-list"]/li')

    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)

def get_info(url):
    article_url = 'http://www.jianshu.com/' + url
    html = requests.get(article_url, headers = headers)
    selector = etree.HTML(html.text)
    author = selector.xpath('//span[@class = "name"]/a/text()')[0]
    article = selector.xpath('//h1[@class = "title"]/text()')[0]
    date = selector.xpath('//span[@class = "publish-time"]/text()')[0]
    word = selector.xpath('//span[@class = "wordage"]/text()')[0]
    view = re.findall('"views_count":(.*?),', html.text, re.S)[0]
    comment = re.findall('"comments_count":(.*?)}', html.text, re.S)[0]
    like = re.findall('"likes_count":(.*?),', html.text, re.S)[0]
    #寻找异步请求url中id
    id = re.findall('{"id":(.*?),', html.text, re.S)[0]
    #发送异步请求
    gain_url = 'http://www.jianshu.com/notes/{}/rewards?count=20'.format(id)
    wb_data = requests.get(gain_url, headers = headers)
    json_data = json.loads(wb_data.text)
    gain = json_data['rewards_count']
    info = {
        'author' : author,
        'article' : article,
        'date' : date,
        'word' : word,
        'view' : view,
        'comment' : comment,
        'like' : like,
        'gain' : gain
    }
    print(info)
    sevenday.insert_one(info)

    include_urls = ['http://www.jianshu.com/notes/{}/included_collections?page={}'.format (id, str(i)) for i in range(1,4)]
    for include_url in include_urls:
        include_data = requests.get(include_url, headers = headers)
        json_data2 = json.loads(include_data.text)
        includes = json_data2['collections']
        for include in includes:
            include_title = include['title']
            print(include_title)
            embody.insert_one({'include_title' : include_title})

    time.sleep(2)

for url in urls:
    get_url(url)
















