import socket
import json
from threading import Timer
import _thread
import random

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
nama = input("masukkan nama:")
s.send(bytearray(nama, 'utf-8'))
while True:
    data = s.recv(BUFFER_SIZE)
    if data.decode() == "finish":
        print("break")
        break
    print(data.decode())
    t = Timer(20, _thread.interrupt_main)
    try:
        t.start()
        jawaban = input("Ketik jawaban A,B,C,D  dalam 10 detik\n")
        time = str(random.sample(range(1,10),1))[1:-1]  # chris ini ntr lo tentuin gimana cara itung timenya cuman kurang lebih gini
        result = {
            "jawaban": jawaban,
            "time": int(time)
        }
        result = json.dumps(result)
        s.send(bytearray(result, 'utf-8'))
    except KeyboardInterrupt:
        print("timeout")
    skor = s.recv(BUFFER_SIZE)
    print("total skor: ", skor.decode(), "\n")
    t.cancel()
skorAkhir = s.recv(BUFFER_SIZE)
skorAkhir = skorAkhir.decode() # ini lo print skor akhir
print("Break")

