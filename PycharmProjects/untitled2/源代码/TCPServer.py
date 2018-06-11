
from socket import *
import socket

ip_port = ('127.0.0.1',9000)

sk = socket.socket()

sk.bind(ip_port)

sk.listen(5)

print ('server waiting...')


conn,addr = sk.accept()
print('hhhhhhhhhhhhhhhhhhhhhhh')
print(addr)
while True:

    client_data = conn.recv(1024)

    print ("receive Clinet Data-> ",client_data.decode('utf-8').encode('utf-8'))

    if client_data=='q': break
    conn.sendall(('client,server').encode('utf-8'))

conn.close()
sk.close()
