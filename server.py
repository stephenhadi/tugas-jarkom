import socket
import _thread
from listSoal import listSoal

def listen():
    counter=0
    while True:
        global playerConn
        global playerAddr
        conn, addr = s.accept()
        global msg
        if msg == "begin":
            break
        counter += 1
        print("user ", counter, ": ", addr)
        playerConn.append(conn)
        playerAddr.append(addr)


global playerConn
global playerAddr
global msg
msg=""
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(5)
playerConn=[]
playerAddr=[]
_thread.start_new_thread(listen,())
msg = input("write 'begin' to start \n")
listSoal = listSoal()
listSoal.fetchSoal()


