#UDPClient.py
from socket import *

HOST='59.69.149.166'
PORT=9999
address=(HOST,PORT)
s = socket(AF_INET,SOCK_DGRAM)

while True:
    message = raw_input('send message:>>')
    s.sendto(message,address)
    data = s.recvfrom(1024)
    print (data)
s.close()
