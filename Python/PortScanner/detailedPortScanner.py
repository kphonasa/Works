#Detailed Port scanner
import socket
from socket import *
from socket import AF_INET, SOCK_STREAM
import sys
import time

#PortScan-KatrinaPhonasa
hostName="www.uiowa.edu"
hostIP="128.255.166.65"
counter=0

starttime=time.time()

try:
   for port in range (0,1024):
      sock=socket(AF_INET, SOCK_STREAM)
      x=sock.connect_ex(("128.255.166.65",port))
        
   if x==0:
      counter+=1
   print ("Port {}: OPEN")
   sock.close

except socket.error:
   print("Error occurred. System exiting")
   sys.exit()
   
t=(time.time()-starttime)
closed=(1024-counter)
rate=(1024/t)

print("Probe time lasted "+str(t)+" seconds")
print("There were "+str(counter)+" open ports")
print("There were "+str(closed)+" closed ports")
print("The scan rate was "+str(rate)+" ports per second")