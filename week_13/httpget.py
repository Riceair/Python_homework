import socket
import time

HOST = 'csie.nuk.edu.tw'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET https://www.csie.nuk.edu.tw/ HTTP/1.0\r\n\r\n')
html = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    html = html+data

mysock.close()
print(html.decode())
