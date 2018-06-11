# -*- encoding:utf-8 -*-
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


