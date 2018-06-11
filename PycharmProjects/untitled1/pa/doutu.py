# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

class doutu(object):
    headers = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/62.0.3202.94 Safari/537.36'
    }
    def get_url(self, url):
        data = requests.get(url, headers = self.headers)
        soup = BeautifulSoup(data.content,'lxml')
        totals= soup.find_all('a', {'class' : 'list-group-item'})
        for one in totals:
            sub_url = one.get('href')
            global path
            div = one.find('div', {'class' : 'random_title'}).text
            path =div[:-10]
            if not self.mkdir(path):  ##跳过已存在的文件夹
                print(u'已经跳过：', path)
                continue
            try:
                self.get_img_url(sub_url)
                os.chdir(os.path.pardir)
            except:
                pass
    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip() #去除空格
        isExists = os.path.exists(os.path.join( path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join(path))
            os.chdir(os.path.join( path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False
    def get_img_url(self, url):
        data = requests.get(url, headers = self.headers)
        soup = BeautifulSoup(data.content, 'lxml')
        totals = soup.find_all('div', {'class': 'artile_des'})
        for one in totals:
            img = one.find('img')
            try:
                sub_url = img.get('src')
                alt = img.get('alt')
            except:
                pass
            try:
                self.get_img(sub_url, alt)
            except:
                pass
    def get_img(self, url, alt):
        global path
        img_path = path + '\\' + alt
        img = requests.get(url, headers = self.headers)
        try:
            with open(img_path, 'wb') as f:
                f.write(img.content)
        except:
            pass
    def create(self):
        os.chdir(os.path.pardir) 
        self.mkdir('doutu')
        for count in range(1, 31):
            url = 'https://www.doutula.com/article/list/?page={}'.format(count)
            print('开始下载第{}页'.format(count))
            self.get_url(url)

if __name__ == '__main__':
    dou = doutu()
    dou.create()
