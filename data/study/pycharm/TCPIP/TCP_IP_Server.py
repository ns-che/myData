# =====================
# TCP/IP 서버예제
# =====================
# 클라이언트 접속 기다리고, 보낸 메세지 수신하고
# 간단한 음담을 보내는 서버

import socket # 네트워크 통신을 위한 기본 모듈

# -----------------------
# 1. 서버 기본 설정
# -----------------------
HOST = '0.0.0.0' # 서버 IP 주소(localhost)
PORT = 5000 # 다른 프로그램이나 다른 유저가 사용하지 않는 그런 포트

# -----------------------
# 2. 소켓 객체 생성
# -----------------------
# socket.AF_INET : IPv4 주소 체계 사용
# socket.SOCK_STREAM : TCP 프로토콜 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------
# 3. IP와 포트를 소켓에 바인딩(연결)
# -----------------------
# 서버가 클라이언트 요청을 받을 수 있도록 설정
server_socket.bind((HOST, PORT)) # bind(): 소켓 연결(ip, 포트)

# -----------------------
# 4. 클라이언트 연결 대기 시작
# -----------------------
# 인자 없이 listen() 호출 시 기본적으로 동시 접속 1개만 허용 => 여러 접속 위해서는 멀티 스레드 구축 필요
server_socket.listen() # listen(): 접속 요청 대기

print(f'서버가 {HOST}:{PORT} 에서 연결 대기 중입니다...')

# -----------------------
# 5. 클라이언트 연결 수락
# -----------------------
# 클라이언트가 접속할 때까지 블로킹 상태로 대기
# 연결이 발생하면 튜플 반환
client_socket, addr = server_socket.accept()
print(f'client {addr} connected...')

# -----------------------
# 6. 클라이언트 요청 처리
# -----------------------
while True:
    # 클라이언트로부터 최대 1024바이트 데이터 수신
    data = client_socket.recv(1024).decode() # bytes -> str 변환
    if not data:
        # 클라이언트 연결이 끊기면 루프 종료
        print("데이터 수신 종료(클라이언트 연결 해제됨)")
        break

    # 클라이언트 사용자 종료 명령 감지
    if data.lower() == 'exit':
        print("클라이언트 종료 요청 수신")
        break

    print(f"클라이언트 메세지: {data}")

    reply = f"서버 응답: [{data}] 잘 받았습니다."

    client_socket.sendall(reply.encode())


# -----------------------
# 7. 연결 종료
# -----------------------
client_socket.close()
server_socket.close()
print("서버 종료 완료")





