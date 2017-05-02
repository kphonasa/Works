#Networking and Security assignment 2 port scanner
from socket import *
from utils import *
import time


IPS=['31.13.74.36','53.163.225.50','40.97.142.194','132.163.4.107'] 
for IP in IPS:
    counter=0
    closed=0
    openports=[]
    for port in range(0,1001):
        try:
            sock=socket(AF_INET, SOCK_STREAM)
            sock.settimeout(2)
            x=sock.connect_ex((IP,port))
            if x==0:
                counter+=1
                openports.append(port)
                print ("IP: "+str(IP)+" Port {"+str(port)+"}: OPEN")
        except OSError:
            closed+=1
        finally:
            sock.close

    print("There were "+str(counter)+" open ports in IP: "+str(IP))
    print("There were "+str(closed)+" closed ports in IP: "+str(IP))
    print(str(IP)+" open ports: ")
    print(openports)
