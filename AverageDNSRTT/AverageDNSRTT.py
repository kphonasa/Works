from socket import *
from utils import *
import time 

hostname=['www.facebook.com','www.google.com','www.uiowa.edu'] 
DNS=['168.1.79.229','156.154.70.1','138.197.25.214','94.206.181.22','122.176.20.6','217.73.226.120','27.34.140.46','110.165.44.152','187.86.59.3','128.255.1.3']
#//	create a UDP socket
#//  	send the packet to the DNS server 
#//	receive the response from the DNS server in <message>
for i in hostname:
    packet = create_DNS_query(i)
    for x in DNS:       
        UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        UDPsocket.sendto(packet,((x, 53)))
        #//	conduct multiple RTT measurements to <ip>
        #//	report mean and standard deviation of the RTT measurements
    
        #	To measure RTT, you can simply measure the time it takes to establish a TCP connection with the server.
        #Example: (To measure RTT between your machine and a server <ip>)
            
        #import socket
    
        message, address = UDPsocket.recvfrom(1000)
        print("Message received:")
        ip = decode_dns_message(message)
        print (ip)
        UDPsocket.close()
    

        RTTlist=[]
        while len(RTTlist)!=10:
            #// 	create a TCP socket
            TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            #connect
            t1=time.time()
            TCPsocket.connect((ip,80))            
            t2=time.time()
            RTT=t2-t1
            RTTlist.append(RTT)
    
            #close
            TCPsocket.close()
        RTTsum=sum(RTTlist)
        RTTavg=(RTTsum/10)
        print("The average RTT for "+str(i)+" using DNS "+str(x)+" is "+str(RTTavg)) 
        
