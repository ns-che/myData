# ========================
# AI TCP 클라이언트 예제(AI_Client.py)
# ========================

import socket
import json

# -----------------------------
# 1. 서버 접속 정보
# -----------------------------
HOST = '192.168.0.7'
PORT = 5000

# -----------------------------
# 2. 서버 연결
# -----------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('서버연결 성공(종료: exit)')

# -----------------------
# 3. 메세지 송수신 루프
# -----------------------
while True:
    mode = input("(length/ sentiment / keyword: " ).strip()

    if mode == "exit":
        client_socket.sendall(mode.encode())
        break

    text = input("문장 입력: ").strip()

    request = {"mode":mode, "text":text}

    client_socket.sendall(json.dumps(request, ensure_ascii=False).encode())

    data = client_socket.recv(1024).decode()
    try:
        response = json.loads(data)
        print(response)
    except json.JSONDecodeError:
        pass


# ----------------------
# 4. 소켓 종료
# ----------------------
client_socket.close()
print('클라이언트 종료 완료')