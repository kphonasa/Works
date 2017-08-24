from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

#bind socket
clientSocket.bind(('127.0.0.1', 40000))

#connect
try:
    clientSocket.connect(('127.0.0.1',5000))
except:
    print('Cannot connect to the server:')
    print(clientSocket)
    clientSocket.close()
    exit()
    
print("Please write the message you would like to send:")
message="hello"

#send 
clientSocket.send(message.encode())

#receive
rMessage= clientSocket.recvfrom(1000)
print("Message received:")
print(rMessage.decode())

#close
clientSocket.close()

