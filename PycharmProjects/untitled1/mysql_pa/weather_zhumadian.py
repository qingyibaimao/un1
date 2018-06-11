# -*- encoding:utf-8 -*-
import requests
import json
import pymysql
import pymongo

class Weather(object):
    def __init__(self):
        self.headers = {
            "urer-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "referer" : "http://www.weather.com.cn/weather40d/101181601.shtml"
             }
    def create_url(self):
        year = '2017'
        for i in range(6, 13):
            month = str(i) if i > 9 else "0" + str(i)
            url = "http://d1.weather.com.cn/calendar_new/" + year + "/101181601_" +year + month + ".html"
            self.get_data(url)


    def get_data(self, url):
        response  = requests.get(url, headers = self.headers).content[11:]
        weathers = json.loads(response)
        results =[]
        for weather in weathers:
            result = {}
            result['date'] = weather.get('date')
            result['wk'] = weather.get('wk')
            result['hmax'] = weather.get('hmax')
            result['hmin'] = weather.get('hmin')
            result['hgl'] = weather.get('hgl')
            result['alins'] = weather.get('alins')
            result['als'] = weather.get('als')
            results.append(result)
           #print(weather.get('alins'), weather.get('als'), weather.get('date'))
        self.mysql(results)
        self.mongo(results)
    def mysql(self, results):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd="qingyi", db="pa", charset="utf8")
        cur = conn.cursor()
        for result in results:
            cur.execute(
                'insert into weather(date, wk, hmax, hmin, hgl, alins, als) values(%s, %s, %s, %s, %s, %s, %s)',
                (result['date'], result['wk'], result['hmax'], result['hmin'], result['hgl'], result['alins'], result['als']))
        conn.commit()
        conn.close()
        print('数据库储存完毕....................')

    def mongo(self, results):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['pythonSpider']
        weather_find = db['weather_find']
        for result in results:
            data = {
                '日期' : result['date'],
                '星期' : result['wk'],
                '最高温度' : result['hmax'],
                '最低温度' : result['hmin'],
                '降水概率' : result['hgl'],
                '宜' : result['alins'],
                '忌' : result['als']
            }
            weather_find.insert(data)

        print('mongo数据:%s',weather_find.find_one())
if __name__ == "__main__":
    we = Weather()
    we.create_url()



