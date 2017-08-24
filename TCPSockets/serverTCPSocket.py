from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#bind socket
serverSocket.bind(('127.0.0.1', 5000))
serverSocket.listen()

while(1):
    connectionSocket, address = serverSocket.accept()
    print(serverSocket)
    print(connectionSocket)
    message = connectionSocket.recv(1000)
    connectionSocket.sendall(message.upper())
    connectionSocket.close()
    
serverSocket.close()