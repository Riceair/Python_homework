from socket import *
from bs4 import BeautifulSoup

serverPort = 12001

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to recieve')

while True:
    connectionSocket,addr = serverSocket.accept()
    print(connectionSocket.getpeername())

    sentence = connectionSocket.recv(1024)
    
    filepath=sentence.split()[1]
    file = open(filepath,'r')
    Soup = BeautifulSoup(file.read(),'html.parser')
    html = str(Soup)
    
    connectionSocket.send(html.encode()+\
                          b'\r\n\r\nHTTP/1.0 200 OK\r\nServer: NUKA/106.55.06\r\n')

    connectionSocket.close()
