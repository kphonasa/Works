#Detailed version of getting RTT from a server
def mean(listx):
    m=(sum(listx)/float(len(listx)))
    return m

def standardDevSamp(listx,n):
    global mean
    mean=mean(listx)
    xi=((x-mean) for x in listx)
    squared=(y**2 for y in xi)
    sumx=sum(squared)
    total=(sumx/n)
    return total**.5

import random
import time
import socket
from socket import *
from socket import AF_INET, SOCK_DGRAM

listx=[]
serverName="127.0.0.1"
serverPort=8000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message="Ping"
print ("Client started")

counter=0
limit=100
x=0
while x < limit:
    x+=1
    
    starttime=time.time()
    clientSocket.sendto(message,('127.0.0.1', 8000))
    clientSocket.settimeout(1)
    
    try:
        message, address = clientSocket.recvfrom(1024)
        
        RTT=(time.time()-starttime)
        listx.append(RTT)
        
    except:
        counter+=1
        print ("Request timed out, packet loss")
        
if (x >100):
    clientSocket.close()
    
if counter<=1:
    print("Packet loss percentage was 100%")
    
else:
    print ("Packet loss percentage was "+str(counter)+"%")

if len(listx)==0:
    print ("100% packet loss. No RTT mean or standard deviation")
    
else:
    RTTmean=(sum(listx)/float(len(listx)))
    print ("The mean of the RTT was "+str(RTTmean))

    RTTstd=standardDevSamp(listx,100)
    print ("The standard deviation of the RTT was "+str(RTTstd))