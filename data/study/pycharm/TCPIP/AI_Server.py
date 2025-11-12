# =======================
# AI TCP/IP 서버 예제
# =======================
# 분석 요청(Json)을 받고 분석(길이/감정/키워드) 후 분석 결과를 보여주는 예제

import socket # 네트워크 통신용
import json # JSON 직렬화/역직렬화용

# -----------------------
# 1. 서버 기본 설정
# -----------------------
HOST = '0.0.0.0' # 서버 IP 주소(localhost)
PORT = 5000 # 다른 프로그램이나 다른 유저가 사용하지 않는 그런 포트

# -----------------------
# 2. 분석 함수 정의
# -----------------------
def analyze_text(request):
    """
    클라이언트의 요청(Json)을 받아 분석 결과를 반환하는 함수
    :param request: dict(ex) {"mode":"sentiment", "text":"문장"})
    :return:
    """
    mode = request.get('mode') # 분석모드 분류
    text = request.get('text')
    # 1) 문자열 길이 분석
    if mode == 'length':
        return {
            "result": len(text),
            "desc": f"문자 길이는 {len(text)} 입니다"
        }
    # 2) 감성 분석(규칙 기반)
    elif mode == 'sentiment':
        if any(word in text for word in ["좋아", "행복", "멋져", "훌륭"]):
            sentiment = "positive"
        elif any(word in text for word in ["싫어", "불만", "짜증", "나빠"]):
            sentiment = "negative"
        else:
            sentiment = "neutral"
        return {
            "result": sentiment,
            "desc": f"감정 분석 결과: {sentiment}"
        }
    # 3) 키워드 분석
    elif mode == 'keyword':
        keywords = ["AI", "서비스", "생산", "불량", "데이터"]
        found = [k for k in keywords if k in text]
        return {
            "result": found,
            "desc": f"키워드 발견: {', '.join(found) if found else '없음'}"
        }
    # 4) 지원하지 않는 모드 처리
    else:
        return {"error": f"지원하지 않는 분석 모드입니다.: {mode}"}

# -----------------------
# 3. TCP 서버 생성 및 설정
# -----------------------
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) # bind(): 소켓 연결(ip, 포트)
server_socket.listen() # listen(): 접속 요청 대기
print(f'서버가 {HOST}:{PORT} 에서 연결 대기 중입니다...')

# -----------------------
# 4. 연결 수락
# -----------------------
client_socket, addr = server_socket.accept()
print(f'client {addr} connected...')

# -----------------------
# 5. 메세지 수신/응답 루프
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

    try:
        request = json.loads(data)
        result = analyze_text(request)
    except json.JSONDecodeError:
        result = {"error": "잘못된 Json 형식입니다."}

    response = json.dumps(result, ensure_ascii=False)
    client_socket.sendall(response.encode())


# -----------------------
# 6. 연결 종료
# -----------------------
client_socket.close()
server_socket.close()
print("서버 종료 완료")
