# -*- encoding: utf-8 -*-
#html下载器
import requests

class htmldownloader(object):

    def download(self, url):
        if url is None:
            return None
        headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
