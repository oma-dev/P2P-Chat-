# advertise my IP and username to everyone in the network
import socket
import sys
import time
import json


def callmyparent():
        temps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temps.connect(("8.8.8.8", 80))
        myp = temps.getsockname()[0]
        myp1 = myp
        # print(myp)
        temps.close()
        a = len(myp)
        b = 0
        for x in myp[::-1]:
                if x != '.':
                        b = b + 1
                else:
                        break
        myp = myp[:-b]
        new = myp + '255'
        print(new)
        return new, myp1

brIP, my = callmyparent()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((brIP, 5000))
print(brIP, ' ', my)

s.setblocking(0)
user = input("Type a username: ")
info = {
    "username": user,
    "ip_address": my
}

y = json.dumps(info)
y = y.encode()

while 1:
        s.send(y)
        time.sleep(60)
