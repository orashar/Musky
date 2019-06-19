import socket
import select
from _thread import *


tcpip = socket.gethostname()
tcpport = 6966

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

skt.bind((tcpip, tcpport))
print("socket binded to: ", tcpip, ":", tcpport)
skt.listen(1000)

clients = []
data = []
def cthread(conn, addr):

    data.append(conn.recv(1024))
    #print(data.decode())
    for msg in data:
        for client in clients:
            client.send(msg)
        data.remove(msg)


while True:
    conn, addr = skt.accept()
    if conn not in clients:
        conn.send("Wlecome to chatroom".encode())
    clients.append(conn)
    print("connected: ", addr)
    for client in clients:
        start_new_thread(cthread, (client, addr))
