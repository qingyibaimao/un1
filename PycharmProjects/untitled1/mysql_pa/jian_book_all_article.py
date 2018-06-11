
import requests
from bs4 import BeautifulSoup  # Pycharm可以方便的下载包

# 必须设置headers里的UserAgent,否则拉钩网不返回正确数据
# 因为requests发送请求的默认UA是python-requests/1.2.0，会被检测到是爬虫
# 我们伪装成一个正常的Chrome浏览器，你也可以换成其他的浏览器UA
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

# 请求地址，Java可以换成其他的搜索词
url = 'https://www.lagou.com/zhaopin/Java/'

# 使用get方式发起请求，并且设置headers=我们的header
r = requests.get(url, headers=header)

# 利用BS解析, r.text是返回的网页内容，可以print查看, lxml是解析器，不行就用html.parser
# http://beautifulsoup.readthedocs.io/zh_CN/stable/#id12 各种解析器对比
# print(r.text)
soup = BeautifulSoup(r.text, 'lxml')

# 使用css selector解析，'.' 用来选择class，'#'选择id
# 发布时间
format_time = soup.select(".position .p_top .format-time")  # [0].text.strip()
# 职位
position = soup.select(".position .p_top .position_link h3")
# 地点
location = soup.select(".position .p_top .position_link .add em")
# 薪水
money = soup.select(".position .p_bot .li_b_l span")
# 经验学历
exp = soup.select(".position .p_bot .li_b_l")
# 公司名
company_name = soup.select(".list_item_top .company .company_name a")
# 企业状况
industry = soup.select(".con_list_item .list_item_top .company .industry")
# 公司标签
label1 = soup.select(".list_item_bot .li_b_l")
label2 = soup.select(".list_item_bot .li_b_r")

for i in range(len(format_time)):
    print(format_time[i].text + "\n" + position[i].text + "\n" + location[i].text + "\n" +
          exp[i].text.strip() +"\n"+ "公司名: "+company_name[i].text +"\n"+ industry[i].text.strip() +
          "\n" + label1[i].text.strip() + label2[i].text+"\n")





