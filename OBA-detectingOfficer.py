# get everyones username and IP
import socket
import sys
import time
import select
import json



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 5000))




# s.setblocking(0)
while 1:
        incomingi = s.recv(1024)
        incomingi = incomingi.decode()
        incomingi = json.loads(incomingi)

        phonebook = open(r"phonebook.txt","a+")
        phonebook.writelines([incomingi["username"], '\n', incomingi["ip_address"], '\n'])
        phonebook.close()
        print(" Server: ", incomingi)
        print("")
