# -*- coding: utf-8 -*-
import time
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass
#注册获取queue的方法
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器
server_addr = '127.0.0.1'
print('connect to server %s......' % server_addr)
m = QueueManager(address = (server_addr, 8111), authkey= 'qiye'.encode('utf-8'))
#从网络连接
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

while(not task.empty()):
    image_url = task.get(True, timeout = 5)
    print('run task download %s......' % image_url)
    time.sleep(1)
    result.put('%s------->success' % image_url)