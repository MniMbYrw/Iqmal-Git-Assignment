import socket

HOST = "10.1.10.138"
PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("I say hello".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
