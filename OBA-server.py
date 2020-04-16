import socket
import sys
import time
import datetime


def saveL(msg):
    now = datetime.datetime.now()
    timeN = str(now.hour) + ":" + str(now.minute)
    with open("messagelog.txt", "a") as log:
        log.writelines(["[",timeN,"]",client, ": ", msg, "\n"])



chatlog = {}

while 1:

    kisiler = {}
    phonebook = open(r"phonebook.txt","r")
    for x in range(50):
            tempo = (phonebook.readline()).strip('\n')
            tempo2 = (phonebook.readline()).strip('\n')
            kisiler[tempo] =  tempo2
            x = x + 1

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    print("server will start on host: ", host)
    port = 5001
    s.bind((host, port))
    print("")
    print("Server done binding to host and port successfully")
    print("")
    print("Server is looking for a connection...")
    print("")
    s.listen(1)
    conn, addr = s.accept()
    # ^^ s.accept() returns a new socket object usabnle to send and receive data on the connection, and an address of the other enduser (that is connected to this socket)
    client = ""

    for k, v in kisiler.items():
        if v == addr[0]:
            client = k

    # ^^to find out who messages us, we check our phonebook to know which username corresponds to the IP address that is connected to us
    print(addr, "Has connected to the server and is now online ...")
    print("")
    while 1:

            incomingM = conn.recv(1024)
            if not incomingM: break
            incomingM = incomingM.decode()
            saveL(incomingM)
            print(client,":", incomingM)
