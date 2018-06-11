'''
import threading
import time

def loop():
    print('thread %s is running.....' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>>>%s ' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is running....' % threading.current_thread().name)

print('thread  %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'loopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('run task %s (%s)....' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('parent processing %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('waiting for all subprocesses done....')
    p.close()
    p.join()
    print('all subprocessing done')



from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('process to write: %s.' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('put %s tp queue....' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):0
    print('process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)

if __name__ =='__main__':
    q = Queue()


###                 json的使用
import json
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
r = requests.get('http://seputu.com/', headers = headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding = 'utf-8')
content = []
for mulu in soup.find_all(class_ = 'mulu'):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        list = []
        for a in mulu.find(class_ = 'box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href': href,'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

with open('qiye.json', 'w') as fp:
    json.dump(content, fp = fp, indent =4)


from lxml import etree
import requests
import re
import csv

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
r = requests.get('http://seputu.com/', headers = headers)
html = etree.HTML(r.text)
div_mulus = html.xpath('.//*[@class = "mulu"]')
rows =[]
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('./div[@class = "mulu-title"]/center/h2/text()')
    if len(div_h2)> 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class = "box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                content = (h2_title, real_title, href, date)
                print(content)
                rows.append(content)
head = ['title','real_title', 'href', 'date']
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f,)
    f_csv.writerow(head)
    f_csv.writerows(rows)


import urllib
from lxml import etree
import requests

def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
        print('当前下载进度: %d' % per)
    headers = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    url = 'http://www.ivsky.com/tupian/ziranfengguang/'
    r = requests.get(url, headers = headers)
    html = etree.HTML(r.text)
    img_urls = html.xpath('.//img/@src')
    i = 0
    for img_url in img_urls:
        urllib.urlretrieve(img_url,'img' + str(i) + '.jpg', Schedule)
        i += 1

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = 'libusi1124@163.com'
passw = "javaweb123"
to_addr = '3405901508@qq.com'
smtp_server = 'smtp.163.com'
msg = MIMEText('Python爬虫异常,异常信息为遇到http 403', 'plain', 'utf-8')
msg['From'] = _format_addr('一号爬虫<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('一号爬虫运性状态', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, passw)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''
