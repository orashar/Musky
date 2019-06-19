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
        l = Label(root, text=message).pack(side=TOP)
        data.remove(message)


root = Tk()

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6966

skt.connect((host, port))

start_new_thread(receive, (host, port))

smsg = StringVar()
entry = Entry(root, textvariable=smsg).pack(side=BOTTOM, fill=X)

sendb = Button(root, text='send', command=send).pack(side=BOTTOM)

mainloop()
