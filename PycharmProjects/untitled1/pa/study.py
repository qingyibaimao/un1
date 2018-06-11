# -*- coding: utf-8 -*-
'''
import requests
#下载图片
def download_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.93 Safari/537.36'}
    url = "http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg"
    response = requests.get(url, headers = headers, stream = True)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_improved():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/45.0.2454.93 Safari/537.36'}
    url = "http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg"
    response = requests.get(url, headers = headers, stream = True)
    from contextlib import closing
    with closing(requests.get(url, headers = headers, stream = True)) as response:
        with open('demo1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

download_image_improved()
download_image()

#流式请求
import json
import requests
r = requests.get('http://httpbin.org/stream/20', stream = True)
if r.encoding is None:
    r.encoding = 'utf-8'

lines = r.iter_lines(decode_unicode = True)
first_line = next(lines)
for line in lines:
    print(json.loads(line))
'''
import requests
r =requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
if (r.status_code == requests.codes.ok):
    print(r.headers['content-type'])
commit_data = r.json()
print(commit_data.keys())
print(commit_data[u'committer'])
print(commit_data[u'message'])
verbs = requests.options('http://a-good-website.com/api/cats')
print (verbs.headers['allow'])