import socket
import _thread
import threading
from listSoal import listSoal
import json
import time


def listen():
    counter=0
    while True:
        global listPlayer
        conn, addr = s.accept()
        nama = conn.recv(1024)
        nama = nama.decode()
        global msg
        if msg == "begin":
            break #when begin no user can join
        counter += 1
        print("user ", nama, ": ", addr)
        player = {
            "nama": nama,
            "conn": conn,
            "addr": addr,
            "totalSkor": 0
        }
        listPlayer.append(player)


def recieve_data(indeks, player,jawaban):
    data = player["conn"].recv(1024)
    recieve = json.loads(data.decode())
    if jawaban.casefold() == recieve["jawaban"].casefold() : #wrong answer is thrown away
        result = {
            "indeks": indeks,
            "time": recieve["time"]
        }
        global answer
        answer.append(result)




global listPlayer
global msg
global answer
answer = []
msg=""
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(5)
listPlayer = []
listThread = []
_thread.start_new_thread(listen, ()) #wait for player
msg = input("write 'begin' to start \n")
listSoal = listSoal()
arrOfSoal = listSoal.fetchSoal()

for x in range(0,arrOfSoal.__len__()):
    soal = arrOfSoal[x].getSoal()
    pilihan = arrOfSoal[x].getPilihan()
    concate = soal + "\n".join(pilihan) +"\n"
    listThread=[]
    for y in range(0, listPlayer.__len__()):
        listThread.append(threading.Thread(target=recieve_data, args=(y,listPlayer[y],arrOfSoal[x].getJawaban(),)))
        listThread[y].start() #start thread for recieve answer
    for y in range(0,listPlayer.__len__()):
        listPlayer[y]["conn"].send(bytearray(concate,'utf-8'))#send question
    absolute_time_out = time.time() + 20
    for y in range(0, listPlayer.__len__()):
        timeout = absolute_time_out-time.time()
        if timeout<0:
            break
        listThread[y].join(timeout) #waiting
    answer = sorted(answer, key=lambda k: k["time"])
    if answer != []:
        listPlayer[answer[0]["indeks"]]["totalSkor"]+= 50 #+50 point for the fastest answer
    for y in range(0,listPlayer.__len__()):
        skor = listPlayer[y]["totalSkor"]
        listPlayer[y]["conn"].send(bytearray(str(skor),'utf-8')) #send user current score
        if x == arrOfSoal.__len__()-1:
            listPlayer[y]["conn"].send(bytearray("finish",'utf-8')) #send code the game is finished
    if x == arrOfSoal.__len__() - 1:
        break
    msg2 = input("write 'next' untuk ke soal selanjutnya \n")
    answer=[]
result ="Leaderboard \n"
for x in range(0,listPlayer.__len__()):
    result+= listPlayer[x]["nama"]+" : "+str(listPlayer[x]["totalSkor"]) +"\n" #print all leaderboards
print(result)
for x in range(0,listPlayer.__len__()):
    listPlayer[x]["conn"].send(bytearray(result,'utf-8')) #send all result