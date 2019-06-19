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
from _thread import start_new_thread



data = []

def send():
    sdata = smsg.get()
    print(sdata)

    data.append("you > " + sdata)
    display(data)

def display(data):
    for message in data:
        l = Label(root, text=message, bg="#aeee8c").grid(row=0, column=0, columnspan=2, sticky="NSEW")
        data.remove(message)


root = Tk()

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6966

skt.connect((host, port))

start_new_thread(receive, (host, port))

smsg = StringVar()
entry = Entry(root, textvariable=smsg).grid(row=1, column=0, sticky="NSEW")

sendb = Button(root, text='     send     ', command=send, bg="#93ff5b").grid(row=1, column=1, sticky="NSEW")

mainloop()
