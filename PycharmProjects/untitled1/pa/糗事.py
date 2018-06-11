import requests
from lxml import etree
import csv
import os
import sys

class Choushi():

        def first(self, url, name):
                data = self.request(url)
                infos = data.xpath('//*[@class = "col1"]/div')
                firstRow =  ['作者', '年龄', '性别', '段子内容', '好笑', '评论']
                with open(name, "a+") as files:
                        write = csv.writer(files)
                        write.writerow(firstRow)
                self.getpa(infos, name)

        def all_url(self, url, name):
                data = self.request(url)
                max = data.xpath('//*[@class = "col1"]/ul/li[last()-1]/a/span/text()')[0]
                for i in range(2, int(max) + 1):
                        print("开始第{}页循环........................................:".format(i))
                        url1 = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
                        data = self.request(url1)
                        infos = data.xpath('//*[@class = "col1"]/div')
                        self.getpa(infos, name)

        def request(self, url):
                headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/62.0.3202.94 Safari/537.36' }
                html = requests.get(url, headers = headers).text
                data = etree.HTML(html)
                return data

        def getpa(self, infos, name):
                item = {}
                self.infos = infos
                self.name = name
                for info in infos:
                        try:
                                item[1] = info.xpath('div[1]/a[2]/h2/text()')[0]
                                try:
                                        item[2] = info.xpath('div[1]/div[@class = "articleGender womenIcon"]/text()')[0]
                                        item[3] = u'女'
                                except:
                                        item[2] = info.xpath('div[1]/div[@class = "articleGender manIcon"]/text()')[0]
                                        item[3] = u'男'
                        except:
                                item[1] = u'匿名用户'
                                item[2] = u'不详'
                                item[3] = u'不详'

                        item[4] = info.xpath('a[1]/div/span/text()')[0]
                        item[5] = info.xpath('div[2]/span[1]/i/text()')[0]
                        item[6] = info.xpath('div[2]/span[2]/a/i/text()')[0]
                        row = [item[i] for i in range(1,7)]
                        with open(self.name, "a+") as files:
                                write = csv.writer(files)
                                write.writerow(row)
if __name__ =='__main__':
        chou = Choushi()
        url = 'https://www.qiushibaike.com/text/'
        csv_name = 'qiushi.csv'
        chou.first(url, csv_name)
        chou.all_url(url, csv_name)


