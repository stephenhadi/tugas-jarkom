import socket
import _thread
import threading
from listSoal import listSoal
import json

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


def recieve_data(conn):
    counter=0
    data = conn.recv(1024)
    recieve = json.loads(data.decode())
    print(recieve["jawaban"])




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
arrOfSoal = listSoal.fetchSoal()
thread = threading.Thread(target=recieve_data,args=(playerConn[0],))
thread.start()
for x in range(0,playerConn.__len__()):
    break

for x in range(0,arrOfSoal.__len__()):
    soal = arrOfSoal[x].getSoal()
    pilihan = arrOfSoal[x].getPilihan()
    concate = soal + "\n".join(pilihan) +"\n"
    for y in range(0,playerConn.__len__()):
        playerConn[y].send(bytearray(concate,'utf-8'))
    thread.join()
    msg2 = input("write 'next' untuk ke soal selanjutnya")


