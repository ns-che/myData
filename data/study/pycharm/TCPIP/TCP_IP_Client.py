# =====================
# TCP/IP 서버예제
# =====================
# 클라이언트

import socket # 네트워크 통신을 위한 기본 모듈

# -----------------------
# 1. 접속할 서버 설정
# -----------------------
HOST = '192.168.0.49' # 서버 IP 주소
PORT = 5000 # 다른 프로그램이나 다른 유저가 사용하지 않는 그런 포트(서비스 중복 금지)

# -----------------------
# 2. 소켓 객체 생성
# -----------------------
# socket.AF_INET : IPv4 주소 체계 사용
# socket.SOCK_STREAM : TCP 프로토콜 사용
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------
# 3. 서버에 연결 시도
# -----------------------
client_socket.connect((HOST, PORT))

# -----------------------
# 4. 메세지 송수신 루프
# -----------------------
while True:
    message = input("보낼 메세지: ")
    
    client_socket.sendall(message.encode())
    
    if message.lower() == "exit":
        break
    
    data = client_socket.recv(1024).decode()
    print(f"서버 응답: {data}")

# ----------------------
# 5. 소켓 종료
# ----------------------
client_socket.close()
print('클라이언트 종료 완료')
        
