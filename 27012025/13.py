from ipaddress import *

ip1 = ip_network('98.162.77.94')
ip2 = ip_network('98.162.64.0')

print(str(bin(int(ip1[0])))[2:].zfill(32))
print(str(bin(int(ip2[0])))[2:].zfill(32))

print('1'*20, 'или')
print('1'*19, 'или')
print('1'*18)