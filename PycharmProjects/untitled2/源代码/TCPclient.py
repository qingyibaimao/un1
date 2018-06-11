#coding:utf-8
#TCPClient.py

import socket
#链接服务端ip和端口
ip_port = ('127.0.0.1',9000)
#生成一个句柄
sk = socket.socket()
#请求连接服务端
sk.connect(ip_port)

while True:
  msg = input('请输入:\n') #输入数据
 
  #发送数据
  sk.sendall(msg.encode('utf-8'))

  if  msg=='q': break #如果 msg 为空，则跳出循环
  
  #接受数据
  server_reply = sk.recv(1024)
  if not   server_reply: break
  #打印接受的数据
  print (str(server_reply))
 
#关闭连接
sk.close()
