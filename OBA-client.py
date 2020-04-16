import socket
import sys
import time
import datetime
# from server import time



def saveL(msg):
    now = datetime.datetime.now()
    timeN = str(now.hour) + ":" + str(now.minute)
    with open("messagelog.txt", "a") as log:
        log.writelines(["[",timeN,"]","You", ": ", msg, "\n"])



kisiler = {}


phonebook = open(r"phonebook.txt","r")
for x in range(50):
        tempo = (phonebook.readline()).strip('\n')
        tempo2 = (phonebook.readline()).strip('\n')
        kisiler[tempo] =  tempo2
        x = x + 1

#
while 1:
        for k in kisiler.keys():
            print(k)

        endC = input("Who do you want to message? ")
        cip = kisiler[endC]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 5001
        s.connect((cip, port))


        while 1:


                message = input()
                saveL(message)
                if message == "zürück":

                    break
                message = message.encode()
                s.send(message)
