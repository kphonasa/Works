from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.bind(('127.0.0.1', 6000))
print("Please write the message you would like to send:")
message=input()

clientSocket.sendto(message.encode(),(('127.0.0.1', 5000)))
                    
rMessage, address = clientSocket.recvfrom(1000)
print("Message received:")
print(rMessage.decode())
clientSocket.close()

