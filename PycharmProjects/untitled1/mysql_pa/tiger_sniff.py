#coding:utf-8
import requests,json,time,sys
import pymysql
from lxml import etree
from bs4 import BeautifulSoup

def get_channel_info(url):
    html = requests.get(url, headers = headers).text
    selector = etree.HTML(html)
    zixun_infos = selector.xpath('//ul[@class="header-column header-column1 header-column-zx menu-box"]/li/a')
    items = []
    for info in zixun_infos:
        item = {}
        channel_name = info.xpath('text()')[0]
        catid = info.xpath('@href')[0].replace('/channel/','').replace('.html','')
        item['channel_name'] = channel_name
        item['catid'] = catid
        items.append(item)
    return items

def get_total_page(item):
    catid = item['catid']
    post_data = {
        'huxiu_hash_code': '18f3ca29452154dfe46055ecb6304b4e',
        'page': '1',
        'catId': catid
    }
    html = requests.post(post_url, data = post_data, headers = headers)
    dict_data = json.loads(html.text)
    parse_data = dict_data['data']
    total_page = int(parse_data['total_page'])
    item2 = {}
    item2['channel_name'] = item['channel_name']
    item2['total_page'] = total_page
    item2['catid'] = catid
    return item2

def get_all_articles(post_data, channel_name):
    html = requests.post(post_url, data = post_data, headers = headers)
    dict_data = json.loads(html.text)
    parse_data = dict_data['data']
    data = parse_data['data']
    #selector = etree.HTML(data)
    mod = BeautifulSoup(data, 'lxml')
    allss = mod.find_all('div', class_ = "mod-b mod-art ")
    #allss = selector.xpath('//div[@class = "mod-b mod-art "]')
    results = []
    for alls in allss:
        result = {}
        title = alls.find('h2').find('a').string
        author = alls.find('span', class_ = "author-name").string
        time = alls.find('span', class_ = "time").string
        mob = alls.find('div', class_ = "mob-author")
        comment = mob.find_all('em')[0].string
        love = mob.find_all('em')[1].string
        #title = alls.xpath('//div[@class = "mob-ctt"]/h2/a/text()')
        #author =alls.xpath('//div[@class = "mob-ctt"]/div[@class = "mob-author"]//span[@class = "author-name"]/text()')
        #time = selector.xpath('//div[@class = "mob-author"]/span[@class = "time"]/text()')
        #comment  = selector.xpath('//div[@class = "mob-author"]/em[1]/text()')
        #love = selector.xpath('//div[@class = "mob-author"]/em[2]/text()')
        result['title'] = title
        result['author'] = author
        result['time'] = time
        result['comment'] = comment
        result['love'] = love
        result['channel_name'] = channel_name
        #print(title,author)
        results.append(result)
    print('完成一页.................休息一下...............')

    return results

def mysql(items):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd="qingyi", db="pa", charset="utf8")
    cur = conn.cursor()
    for it in items:
        cur.execute('insert into tiger_sniff(title, channle_name, author,  comment, love) values(%s, %s, %s, %s, %s )',
                    (it['title'], it['channel_name'], it['author'],  it['comment'], it['love']))
    conn.commit()
    conn.close()
    print('数据库储存完毕....................')
if __name__ == '__main__':
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    root_url='https://www.huxiu.com/channel/103.html'
    url = 'https://www.huxiu.com'
    post_url = 'https://www.huxiu.com/channel/ajaxGetMore'
    items = get_channel_info(url)
    total_pages = []
    for item in items:
       item2 = get_total_page(item)
       total_pages.append(item2)
    for item2 in total_pages:
        channel_name = item2['channel_name']
        catid = item2['catid']
        total_page = item2['total_page']
        for page in range(1, 4):
            post_data = {
                'huxiu_hash_code': '18f3ca29452154dfe46055ecb6304b4e',
                'page': page,
                'catId': catid
          }
        item3 = get_all_articles(post_data,channel_name)
        mysql(item3)

        time.sleep(5)

    #mysql(item3)




