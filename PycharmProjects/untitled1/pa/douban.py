# -*- coding:utf-8 -*-

import requests
import os
import csv
from bs4 import BeautifulSoup
from pa.doload import request
class Topdouban(object):

    ur = 'https://movie.douban.com/top250'
    def URL(self, name):
        field = ['排名', '电影', '导演','评分', '影评']
        self.init_csv(name, field)
        urls = [self.ur + '?start={}&filter='.format(i) for i in range(0, 226, 25)]
        ye = 0
        for url in urls:
            ye = ye + 1
            print('....................正在获取', ye, '页....................')
            self.getInfo(url, name)

    def getInfo(self, url, name):
        item = {}
        re = request.get(url, 3)
        bs = BeautifulSoup(re.text, 'lxml')
        body = bs.body
        div = body.find('div', {'id': 'content'})
        li = div.find('ol').find_all('li')
        for i in li:
            item[1] = i.find('em').string
            div_hd = i.find('div', {'class': 'hd'})
            movie_name = div_hd.find('a').find('span').string  # 电影名
            item[2] = div_hd.find('a').find('span').string
            div_bd = i.find('div', {'class': 'bd'})
            spans = div_bd.find('div').find_all('span')
            href = div_hd.find('a')['href']

            try:
                can_play = div_hd.find('span', {'class': 'playable'}).text
                print(movie_name , can_play)
                re1 = request.get(href, 3)
                bs1 = BeautifulSoup(re1.text, 'lxml')
                div = bs1.body.find('div', {'class': 'article'})
                div1 = div.find('div', {'id': 'info'})
                item[3] = div1.find('span', {'class': 'attrs'}).find('a').string
            except:
                item[3] = u'未知'

            item[4] = spans[1].string
            item[5] = div_bd.find_all('p')[1].find('span').string
            row = [item[a] for a in range(1, 6)]
            self.write(name, row)

    def init_csv(self,csv_name, fist =[]):
        self.name = csv_name
        if os.path.exists(csv_name):
            print('文件已存在')
            os._exit(1)
        with open(self.name, 'a+') as files:
            write = csv.writer(files)
            write.writerow(fist)
    def write(self, csv_name, row = []):
        with open(csv_name, 'a+') as files:
            write = csv.writer(files)
            write.writerow(row)

if __name__ == '__main__':
    top = Topdouban()
    top.URL('movie.csv')
    print('获取完毕')




