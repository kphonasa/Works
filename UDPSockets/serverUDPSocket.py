from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('127.0.0.1', 5000))
print('Waiting to receive something from the client')

message, address = serverSocket.recvfrom(1000)
print("Received message:")
print(message.decode())

serverSocket.sendto(message.upper(), address)
serverSocket.close()

                      