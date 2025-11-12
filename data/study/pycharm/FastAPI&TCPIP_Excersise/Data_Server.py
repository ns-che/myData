import socket

HOST = '0.0.0.0'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()

print("서버 시작")
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")
    data = client_socket.recv(BUFSIZ).decode()
    print(data)

client_socket.close()