import requests
import random
import time

class down:

    def __init__(self):
        self.iplist = [
            '61.135.169.75',
            '61.135.169.55',
            '61.135.169.22',
            '220.181.51.40',
            '220.181.51.39',
            '111.13.13.74',
            '111.13.13.73',
            '111.13.13.72',
            '111.13.13.71',
            '111.13.13.6',
            '111.13.13.5',
            '111.13.13.4',
            '111.13.13.3',
            '101.254.184.206',
            '1.95.9.244',
            '59.50.71.83',
            '211.89.227.50',
            '211.89.227.16',
            '211.89.227.15',
            '183.224.87.36',
            '59.49.46.165',
            '58.222.20.226',
            '58.218.204.136',
            '45.113.253.53',
            '27.151.30.176',
        ]
        self.user_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        ]
        self.cookie = 'user_trace_token=20171222210437-aa1b5b84-e718-11e7-a56e-525400f775ce; LGUID=20171222210437-aa1b6170-e718-11e7-a56e-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; ' \
                      'TG-TRACK-CODE=index_navigation; _gid=GA1.2.1855774556.1515237219; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515237219,1515291652,1515291952,1515321319; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515326358;' \
                      ' JSESSIONID=ABAAABAAAFCAAEG0558E7CC056E43F9234E11BDA2019E1E; _ga=GA1.2.1427662125.1513947878; LGSID=20180107195918-309e4aa3-f3a2-11e7-a01c-5254005c3644; PRE_UTM=; PRE_HOST=;' \
                      ' PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F%3FlabelWords%3Dlabel; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Ddefault%26city%3D%25E6%259D%25AD%25E5%25B7%259E; ' \
                      'LGRID=20180107195918-309e4c98-f3a2-11e7-a01c-5254005c3644; SEARCH_ID=caa811870d074dc2805fdefcffef3b41'
    def get(self, url, para,timeout, proxy = None, num_retries = 6):
        print(u'开始获取.........', url,para)
        ua = random.choice(self.user_list)
        headers = {'User-Agent' : ua ,
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Content-Length': '25',
                   'Content-Type': 'pplication/x-www-form-urlencoded; charset=UTF-8',
                   'Cookie': self.cookie,
                   'Host': 'www.lagou.com',
                   'Referer': "h'https://www.zhihu.com/search?type=content&q=%E7%88%AC%E5%8F%96%E6%8B%89%E5%8B%BE%E7%BD%91",
                   'X-Anit-Forge-Code': '0',
                   'X-Anit-Forge-Token': 'None',
                   'X-Requested-With': 'XMLHttpRequest'
                   }

        if proxy == None:
            try:
                return requests.get(url, headers = headers,data = para, timeout = timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    print(u'获取网页失败, 10s后开始获取第:' , num_retries, u'次')
                    return self.get(url, para, timeout, num_retries-1)  #调用自身
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http' : IP}
                    return self.get(url, para,timeout, proxy, )
        else:
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http' : IP}
                return requests.get(url, data = para, headers = headers, proxies = proxy, timeout = timeout)
            except:

                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    print(u'正在更换代理,10s后将重新获取倒数第:', num_retries, u'次')
                    print(u'当前代理是:', proxy)
                    return self.get(url, para, timeout, proxy, num_retries - 1)

                else:
                    print(u'取消代理使用')
                    return self.get(url, 3)
request = down()

