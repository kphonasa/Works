#Server created for port testing
import random
import time
import socket
from socket import *
#Create a UDP socket

# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket. You CAN change server IP address and port
serverSocket.bind(('127.0.0.1', 8000))
print('Server started')

while True:
 
 # Receive the client packet along with the address it is coming from
 message, address = serverSocket.recvfrom(1024)

 # Generate a random number (for introducing random packet drops)
 rand = random.randint(0, 99)
 
 #If rand is less than 10, we do not respond and consider the packet lost
 if rand < 10:
  continue
 
 # Otherwise, the server responds with a delay
 else:
  time.sleep(float(random.gauss(200,25))/1000.0)
  serverSocket.sendto(message, address)
  
