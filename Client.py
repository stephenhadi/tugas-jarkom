import socket
import json
from threading import Timer
import _thread
import random
import time

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
        waktuAwal = time.time()
        jawaban = input("Ketik jawaban A,B,C,D  dalam 20 detik\n")
        waktuAkhir = time.time()
        lamaJawab = waktuAkhir-waktuAwal
        result = {
            "jawaban": jawaban,
            "time": int(lamaJawab)
        }
        result = json.dumps(result)
        s.send(bytearray(result, 'utf-8'))
    except KeyboardInterrupt:
        print("timeout")
    skor = s.recv(BUFFER_SIZE)
    print("total skor: ", skor.decode(), "\n")
    t.cancel()
skorAkhir = s.recv(BUFFER_SIZE)
skorAkhir = skorAkhir.decode()
print(skorAkhir)
print("Break")

