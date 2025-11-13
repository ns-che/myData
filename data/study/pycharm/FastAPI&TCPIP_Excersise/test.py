import re

data = "1123123 {asdf asdf dasf}"

print(re.search(r'\d+|\{.*\}', data).group())

import json

with open("test.txt", "r", encoding="utf-8") as f:
    while True:
        data = f.readline()
        if not data:
            break
        red = re.findall(r'\{.*?\}', data)
        for x in red:
            print(x)
        # print(data)
        # obj = json.loads(data)
        # print(obj)

data = '{"name": "떐퓒람쁉굁쮙", "value1": 756, "value2": 0.6950718660720081, "value3": true, "type": 1}'
json.loads(data)
print(data)

import json, threading

def worker(data):
    obj = json.loads(data)
    print(obj)

t1 = threading.Thread(target=worker, args=('{"a":1}',))
t2 = threading.Thread(target=worker, args=('{"b":2}',))
t1.start(); t2.start()
t1.join(); t2.join()