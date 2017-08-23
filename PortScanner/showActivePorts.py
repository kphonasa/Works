from socket import *
from utils import *
from ipaddress import *

ips = ip_network("129.255.0.0/24", strict=False)
active=[]
inactive=[]
log=[]
subs=[]
logb=[]
activeb=[]
inactiveb=[]
for ip in ips:
    if check_host(str(ip)):
        print(str(ip) + ": Active")
        active.append(ip)
        log.append(1)
        subs.append(str(ip))
    else:
        print(str(ip) + ": Inactive")
        inactive.append(ip)
        log.append(0)
        subs.append(str(ip))
for ip in ips:
    if check_host(str(ip)):
        print(str(ip) + ": Active")
        activeb.append(ip)
        logb.append(1)
    else:
        print(str(ip) + ": Inactive")
        inactiveb.append(ip)
        logb.append(0)

print("IPS: ")
print(subs)
print("Log1: ")
print(log)
print("Active IPs first round: ")
print (active)
print ("Log2: ")
print(log2)
print("Active IPs second round: ")
print (active)
