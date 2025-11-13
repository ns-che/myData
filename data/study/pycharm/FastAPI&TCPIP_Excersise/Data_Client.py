import socket
import threading
import json
import re
import requests

SERVER_URL = "http://localhost:9999/"

MAX_CLIENT = 5
HOST2 = '0.0.0.0'
PORT2 = 8001
BUFSIZE = 1024

# def send_data(data):
#     client_socket.sendall(data.encode())


def data_process(hw_socket, addr):
    while(True):
        data = hw_socket.recv(BUFSIZE) # 1024 이상의 데이터가 올경우 해당 데이터는 버린다(데이터는 수없이 쌓이고, 빠른 속도 처리 위함)

        if (str(data) == 'exit'):
            print("종료 문자 수신")
            break
        data = data.decode('utf-8').strip()
        rdata_find = re.findall(r'\{.*?\}', data)

        for rdata in rdata_find:
            try:
                data = json.loads(rdata)

                try:
                    print(data)
                    if data['type'] == 1:
                        requests.post(SERVER_URL + "type1", json=data)
                    elif data['type'] == 2:
                        requests.post(SERVER_URL + "type2", json=data)
                except requests.exceptions.RequestException as e:
                    print(f" 서버 연결 오류: {e}\n")
                    continue
            except:
                print("오류" + rdata + str(addr))

    hw_socket.close()

def observer(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(MAX_CLIENT)

    while True:
        hw_socket, addr = server_socket.accept()
        threading.Thread(target=data_process, args=(hw_socket, addr), daemon=True).start()




observer_thread = threading.Thread(target=observer, args=(HOST2, PORT2))
observer_thread.start()
