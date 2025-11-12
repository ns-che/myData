import socket
import threading
import json

HOST = '192.168.0.49'  # 공유기 내부 ip이므로 안전
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

MAX_CLIENT = 5

HOST2 = '0.0.0.0'
PORT2 = 8001

# TCP IP ipv4 방식
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(ADDR)


# def send_data(data):
#     client_socket.sendall(data.encode())


def data_process(hw_socket, addr):
    while(True):
        data = hw_socket.recv(BUFSIZ).decode('utf-8')
        print(dict(data))
        # data = json.loads(data)
        if(data == 'exit'):
            break

        if data['type'] == 0:
            print(f"타입 0 {data}")
        elif data['type'] == 1:
            print(f"타입 1 {data}")


def observer(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(MAX_CLIENT)

    while True:
        hw_socket, addr = server_socket.accept()
        threading.Thread(target=data_process, args=(hw_socket, addr), daemon=True).start()




observer_thread = threading.Thread(target=observer, args=(HOST2, PORT2))
observer_thread.start()
observer_thread.join()