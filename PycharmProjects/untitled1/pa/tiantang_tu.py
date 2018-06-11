# -*- encoding:utf-8 -*-
import urllib
from lxml import etree
import requests

def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize /totalsize
    if per > 100:
        per = 100
        print('当前下载进度: %d ' % per)
    headers = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                       ' (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }