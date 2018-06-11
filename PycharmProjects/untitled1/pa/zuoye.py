# -*- coding: utf-8 -*-
'''
dict_date = {
"Led Zeppelin":1969, "Led Zeppelin II": 1969,
    "Led Zeppelin III": 1970, "Led Zeppelin IV": 1971,
    "Houses of the Holy":1973, "Physical Graffiti": 1975,
    "Presence":1976, "In Through the Out Door":1979, "Coda":1982
}
a = list(dict_date.values())  #取出value
for k, v in dict_date.items():
    #if v in range(1970, 1976):   #两种方法便利
    if v < 1976 and v > 1970 :
        print(k)




import re

value = ['http://www.weather.com.cn/weather1d/101010100.shtml#search',
    'http://www.weather.com.cn/weather1d/101020100.shtml#search',
    'http://www.weather.com.cn/weather1d/101210101.shtml#search',
    'http://www.weather.com.cn/weather1d/101280101.shtml#search',
    'http://www.weather.com.cn/weather1d/101200101.shtml#search',
    'http://www.weather.com.cn/weather1d/101190101.shtml#search',
    'http://www.weather.com.cn/weather1d/101280601.shtml#search',
    'http://www.weather.com.cn/weather1d/101190401.shtml#search',
    'http://www.weather.com.cn/weather1d/101230201.shtml#search',
    'http://www.weather.com.cn/weather1d/101220101.shtml#search']
key = ['北京', '上海', '杭州', '广州', '武汉', '南京', '深圳', '苏州', '厦门', '合肥']
values =[]
for i in range(0,len(value)):  #遍历url
    v = re.sub("\D","",value[i])  #利用正则去除非数字
    shuju_w = list(v)   #将数据制成列表
    shuju_w.pop(0)     #去除第一个无效数据
    shuju = ''.join(shuju_w)   #将数据恢复成字符串
    values.append(shuju)   #将数据加入值列表

zidian = dict(zip(key,values))  #制成字典
print(zidian)
'''