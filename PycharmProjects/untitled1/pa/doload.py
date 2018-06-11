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
    def get(self, url, timeout, proxy = None, num_retries = 6):
        print(u'开始获取.........', url)
        ua = random.choice(self.user_list)
        headers = {'User-Agent' : ua }

        if proxy == None:
            try:
                return requests.get(url, headers = headers, timeout = timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    print(u'获取网页失败, 10s后开始获取第:' , num_retries, u'次')
                    return self.get(url, timeout, num_retries-1)  #调用自身
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http' : IP}
                    return self.get(url, timeout, proxy, )
        else:
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http' : IP}
                return requests.get(url, headers = headers, proxies = proxy, timeout = timeout)
            except:

                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    print(u'正在更换代理,10s后将重新获取倒数第:', num_retries, u'次')
                    print(u'当前代理是:', proxy)
                    return self.get(url, timeout, proxy, num_retries - 1)

                else:
                    print(u'取消代理使用')
                    return self.get(url, 3)
request = down()

