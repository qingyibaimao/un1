# -*- coding: utf-8 -*-
'''
import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text = 'hello lei')
label.pack()
tkinter.mainloop()


top = tkinter.Tk()
quit = tkinter.Button(top, text = "hello word",
                      command = top.quit)
quit.pack()
tkinter.mainloop()

top = tkinter.Tk()
hello = tkinter.Label(top, text = 'hello word')
hello.pack()

quit = tkinter.Button(top, text = "quit", command = top.quit, bg = "red", fg = 'white')
quit.pack(fill = tkinter.X, expand = 1 )

tkinter.mainloop()

from tkinter import *

def resize(ev = None):
    label.config(font = 'helvetica - %d bold' % scale.get())

top = Tk()
top.geometry('250 * 150')
label = Label(top, text = 'hello word', font = 'helvetica - 12 bold')
label.pack(filll = Y, expand =1)

scale = Scale(top, from_ = 10, to = 40, orient = HORIZONTAL, command = resize)
scale.set(12)
scale.pack(fill = X, expand = 1)
quit = Button(top, text = 'quit', command = top.quit, activeforeground = 'white',
              activeback)
#画圆
if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width = 800, height = 600, bg = 'red')
    canvas.pack(expand = YES, fill = BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width = 1)
        k += j
        j += 0.6
    mainloop()

if __name__ =="__main__":
    from tkinter import *
    root = Tk()
    root.title('leixiang')
    canvas = Canvas(root, width = 400,height = 400, bg = 'yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        y1 += 5
        x1 += 5
    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()

#发邮件
from email.mime.text import MIMEText
msg = MIMEText('晚安雷哥', 'plain', 'utf-8')
from_addr = input('3405901508@QQ.com')
password = input('javaweb123')
to_addr = input('2602476344@QQ.com')
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

from tkinter import *

def resize(ev = None):
    label.config(font = 'Helvetica -%d bold' %\
                        scale.get())
top = Tk()
#top.geometry('250 * 150')
label = Label(top, text = 'hello word', font = 'Helvetica -12 bold')
label.pack(fill = Y, expand = 1)
scale = Scale(top, from_ = 10, to = 40, orient = HORIZONTAL, command = resize )
scale.set(12)
scale.pack(fill = X, expand = 1)
quit = Button(top, text = 'quit',
              command = top.quit)
quit.pack()
mainloop()

#偏函数
from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'
SIGNS = {
    'do not enter' : CRIT,
    'railroad crossing ': WARN,
    '55\nspeed limit': REGU,
    'merging traffic' : WARN,
    'one way': REGU,
}
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showWarning('warning', 'warning button pressed')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')
top = Tk()
top.title('Rold Signs')
Button(top, text = 'quit', command = top.quit, bg = 'red', fg = 'white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command = critCB, bg = 'white', fg = 'red')
WarnButton = pto(MyButton, command = critCB, bg = 'goldenrod1')
ReguButton = pto(MyButton, command = infoCB, bg = 'white')
for eachSign in SIGNS:
    signType= SIGNS[eachSign]
    cmd = '%sButton(text = %r%s).pack(fill = X, expand = True)' % (
    signType.title(), eachSign,
    '.upper()' if signType == CRIT else '.title()')
    eval(cmd)pu

top.mainloop()


import os
from time import sleep
from tkinter import *
class DirList(object):

    def __init__(self, initdir = None):#定义构造函数
        self.top = Tk()
        self.label = Label(self.top, text = 'Directory Lister v1.1') #创建一个label控偶给你剪
        self.label.pack()

        self.cwd = StringVar(self.top)   #显示当前目录
        self.dirl = Label(self.top, fg = 'blue', font = ('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)#可移动
        self.dirsb.pack(side = RIGHT, fill = Y)
        self.dirs = Listbox(self.dirfm, height = 15, width = 50, yscrollcommand = self.dirsb.set)
        self.dirs.bind('<Double-1>',self.setDirAndGo)  #bind函数和回调函数链接到一块
        self.dirsb.config(command = self.dirs.yview)#scrollbar与listbox链接到一块
        self.dirs.pack(side = LEFT, fill = BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width = 50, textvariable = self.cwd)  #文本框
        self.dirn.bind('<Return>', self.doLS)#绑定回车键可以刷新
        self.dirn.pack()

        self.bfm = Frame(self.top)#按钮框架
        self.clr = Button(self.bfm, text = 'Clear',
                          command = self.clrDir,
                          activeforeground = 'white')
        self.ls = Button(self.bfm, text = 'list directory',
                         command = self.doLS,
                         activeforeground = 'white')
        self.quit = Button(self.bfm, text = 'Quit',
                           command = self.top.quit,
                           activeforeground = 'white')
        self.clr.pack(side = LEFT)
        self.ls.pack(side = LEFT)
        self.quit.pack(side = LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)  #初始化构造函数,以当前目录为起点
            self.doLS()

    def clrDir(self, ev = None):
        self.cwd.set('')

    def setDirAndGo(self, ev = None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground = 'red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir#获取实际文件列表
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev =None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
             et(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground = 'LightSkyBlue')
            self.top.update()
            return
        self.cwd.set( 'FETCHING DIRECTRORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text = os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        #self.dirs.config(selectbackground = 'LightSkyBule')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()

import requests
import json

r = requests.get('https://api.github.com/requests/kennethreitz/requests/issues/482')
print(r.status_code)
issue = json.loads(r.text)
print(issue[u'comments'])

from requests.auth import HTTPBasicAuth
import requests
import json

auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
url = u"https://api.github.com/repos/requests/requests/issues/482/comments"
body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})

r = requests.post(url = url, data = body, auth = auth)
print(r.status_code)
content = r.json()

import ssl
import requests
import urllib3
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class Ssl3HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block = False):
        self.poolmanager = PoolManager(num_pools = connections,
                                       maxsize = maxsize,
                                       block = block,
                                       ssl_version = ssl.PROTOCOL_SSLv23)

import requests
from bs4 import BeautifulSoup
import re

ip = []
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
all_url = 'https://wenku.baidu.com/view/008f795b04a1b0717ed5dd0c.html'
start_html = requests.get(all_url, headers = headers)
soup = BeautifulSoup(start_html.text, 'lxml')
all_p =soup.find('div', class_ = 'bd`').find_all('p')
#print(all_p.text)
'''
import requests
from lxml import etree
import csv
import os
import sys

class Choushi():

        def first(self, url, name):
                data = self.request(url)
                infos = data.xpath('//*[@class = "col1"]/div')
                firstRow =  ['作者', '年龄', '性别', '段子内容', '好笑', '评论']
                with open(name, "a+") as files:
                        write = csv.writer(files)
                        write.writerow(firstRow)
                self.getpa(infos, name)

        def all_url(self, url, name):
                data = self.request(url)
                max = data.xpath('//*[@class = "col1"]/ul/li[last()-1]/a/span/text()')[0]
                for i in range(2, int(max) + 1):
                        print("开始第{}页循环........................................:".format(i))
                        url1 = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
                        data = self.request(url1)
                        infos = data.xpath('//*[@class = "col1"]/div')
                        self.getpa(infos, name)

        def request(self, url):
                headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/62.0.3202.94 Safari/537.36' }
                html = requests.get(url, headers = headers).text
                data = etree.HTML(html)
                return data

        def getpa(self, infos, name):
                item = {}
                self.infos = infos
                self.name = name
                for info in infos:
                        try:
                                item[1] = info.xpath('div[1]/a[2]/h2/text()')[0]
                                try:
                                        item[2] = info.xpath('div[1]/div[@class = "articleGender womenIcon"]/text()')[0]
                                        item[3] = u'女'
                                except:
                                        item[2] = info.xpath('div[1]/div[@class = "articleGender manIcon"]/text()')[0]
                                        item[3] = u'男'
                        except:
                                item[1] = u'匿名用户'
                                item[2] = u'不详'
                                item[3] = u'不详'

                        item[4] = info.xpath('a[1]/div/span/text()')[0]
                        item[5] = info.xpath('div[2]/span[1]/i/text()')[0]
                        item[6] = info.xpath('div[2]/span[2]/a/i/text()')[0]
                        row = [item[i] for i in range(1,7)]
                        with open(self.name, "a+") as files:
                                write = csv.writer(files)
                                write.writerow(row)
if __name__ =='__main__':
        chou = Choushi()
        url = 'https://www.qiushibaike.com/text/'
        csv_name = 'qiushi.csv'
        chou.first(url, csv_name)
        chou.all_url(url, csv_name)


