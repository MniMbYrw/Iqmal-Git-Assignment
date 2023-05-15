import socket

HOST = "10.1.10.138"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(6)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8)')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Message received. Thank you".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} terminated")
