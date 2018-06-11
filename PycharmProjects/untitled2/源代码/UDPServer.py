#UDPServer.py

from socket import *

HOST = '59.69.149.166'
PORT = 9999

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
print( '...waiting for message..')
while True:
    data,address = s.recvfrom(1024)
    print (data,address)
    s.sendto('this is the UDP server',address)
s.close()
