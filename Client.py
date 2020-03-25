import socket
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    data = s.recv(BUFFER_SIZE)
    print(data.decode())
    jawaban = input(" ")
    time = 10 #chris ini ntr lo tentuin gimana cara itung timenya cuman kurang lebih gini
    result = {
        "jawaban":jawaban,
        "time":time
    }
    result = json.dumps(result)
    print(result)
    s.send(bytearray(result,'utf-8'))

