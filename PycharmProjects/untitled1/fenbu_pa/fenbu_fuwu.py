# -*- coding:utf-8 -*-
import random,  time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()   #存放任务
result_queue = queue.Queue()  #存放结果

class Queuemanager(BaseManager):
    pass

#将两个队列通过register方法注册到网络上
Queuemanager.register('get_task_queue', callable = lambda:task_queue)
Queuemanager.register('get_result_queue', callable = lambda:result_queue)

manager = Queuemanager(address = ('', 8111), authkey ='qiye'.encode('utf-8'))
manager.start()   #开启管理,监听通道

task = manager.get_task_queue()  #通过管理实例的方式获取网络访问对象
result = manager.get_result_queue()
#添加任务
for url in ["ImageUrl_" + str(i) for i in range(10)]:
    print('put task %s.....' % url)
    task.put(url)
#获取返回结果
print('try get result......')
for i in range(10):
    print('result is %s' % result.get(timeout = 10))
#关闭管理
manager.shutdown()