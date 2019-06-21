############################################################################################################
#####                                        Coded By - ORASHAR                                        #####
#####                                           Date - 06/19                                           #####
############################################################################################################

############################################################################################################
#####                               not receiving other clients message                                #####
#####                                                                                                  #####
############################################################################################################

import socket
from tkinter import *
import time
import threading

print_lock = threading.Lock()

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6966

skt.connect((host, port))


data = []

def send():
    sdata = smsg.get()
    print(sdata)
    skt.send(sdata.encode())
    data.insert(0, "you > " + sdata)

def receive():
    rdata = skt.recv(1024)
    print(rdata)
    data.insert(0, rdata)

def display(data):
    print(1)
    with print_lock:
        for message in reversed(data):
            print(2)
            l = Label(root, text=message).pack(side=TOP)
            smsg.set("")
            data.remove(message)
            print(data)
    time.sleep(3)
    display(data)


root = Tk()

trecv = threading.Thread(target=receive)
tdspl = threading.Thread(target=display, args=(data, ))

trecv.daemon = True
tdspl.daemon = True

trecv.start()
tdspl.start()

smsg = StringVar()
entry = Entry(root, textvariable=smsg).pack(side=BOTTOM, fill=X)

sendb = Button(root, text='send', command=send).pack(side=BOTTOM)

mainloop()
