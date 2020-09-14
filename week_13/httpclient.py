import socket

HOST = '127.0.0.1'
PORT = 12001
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))
clientSocket.sendall(b'GET A1065506.htm HTTP/1.0\r\n\r\n')

html = clientSocket.recv(1024)
print(html.decode())
clientSocket.close()
