# ====================================================
# 랜덤 난수 발생기 프로그램
# ====================================================
# 2개의 데이터 발생기에서 데이터가 계속 발생한다
import random
import json
from datetime import datetime, date, timedelta
import time
import threading
import socket

HOST = "192.168.0.49"
PORT = 8001

# -----------------------------
# 0. json에서 처리할 수 없는 형식(obj) 처리
# -----------------------------
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return str(obj)
        return super().default(obj)

# -----------------------------
# 1. 데이터1(name(korean string), value1(int32), value2(float64), value3(Bool))
# -----------------------------
def random_value1():
    '''
    :return: json data
    '''
    json_dict = {}

    li_rand_uni_ko = random.sample(range(int('AC00', 16), int('D7A3', 16) + 1), random.randint(3, 7))
    json_dict['name'] = ''.join(chr(rand_uni_ko) for rand_uni_ko in li_rand_uni_ko)
    json_dict['value1'] = random.randint(100, 1000)
    json_dict['value2'] = random.random() * float(json_dict['value1'] / 100)
    json_dict['value3'] = json_dict['value1'] > 500

    return json_dict


# -----------------------------
# 2. 데이터2(name(english string), value2(eng+kor string), value3(date))
# -----------------------------
def random_value2():
    '''
    :return: json data
    '''
    json_dict = {}

    li_rand_uni_ko = random.sample(range(int('AC00', 16), int('D7A3', 16) + 1), random.randint(1, 4))
    li_rand_ascii_alpha = random.sample([*range(ord('a'), ord('z') + 1), *range(ord('A'), ord('Z'), 1)],
                                        random.randint(2, 4))

    li_rand_uni = li_rand_uni_ko + li_rand_ascii_alpha
    random.shuffle(li_rand_uni)

    date_start = datetime(1900, 1, 1, 0, 0, 0)
    date_end = datetime(2100, 12, 31, 0, 0, 0)

    total_time = date_end - date_start
    total_time_sec = int(total_time.total_seconds())

    rand_date = date_start + timedelta(seconds=random.randint(0, total_time_sec))

    json_dict['name'] = ''.join(chr(rand_ascii_alpha) for rand_ascii_alpha in li_rand_ascii_alpha)
    json_dict['value1'] = ''.join(chr(rand_uni) for rand_uni in li_rand_uni)
    json_dict['value2'] = rand_date

    return json_dict

# -----------------------------
# 3. 데이터 발생기(data 함수를 time_sec초당 start~end개의 데이터 발생)
# -----------------------------
def random_machine(data_func, time_sec, start, end, type):
    id = 0

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    success = False

    for i in range(100):
        try:
            client_socket.connect((HOST, PORT))
            print("서버에 연결됨!")
            success = True
            break
        except ConnectionRefusedError:
            print("서버 연결 실패, 1초 후 재시도...")
            time.sleep(1)

    while(True):
        for i in range(random.randint(start, end+1)):
            dict_data = data_func()
            dict_data['type'] = type

            if(success):
                client_socket.sendall(json.dumps(dict_data, ensure_ascii=False, cls=DateTimeEncoder).encode('utf-8'))
        time.sleep(time_sec)
        id += 1
        if(id > 10):
            break

    if (success):
        client_socket.sendall("exit".encode('utf-8'))
    client_socket.close()

def start():
    machine1 = threading.Thread(target=random_machine, args=(random_value1, 1, 1, 3, 1))
    # machine2 = threading.Thread(target=random_machine, args=(random_value2, 2, 1, 3, 2))

    machine1.start()
    # machine2.start()

    machine1.join()
    # machine2.join()

start()