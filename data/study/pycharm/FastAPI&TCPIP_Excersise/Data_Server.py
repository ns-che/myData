import socket
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
app = FastAPI(title="FastAPI Server")
client = MongoClient("mongodb://localhost:27017")
db = client["dataset"]

class JsonValue1(BaseModel):
    name: str
    value1: int
    value2: float
    value3: bool

class JsonValue2(BaseModel):
    name: str
    value1: str
    value2: str

def dblogic(data, collection_name):
    collection = db[collection_name]
    collection.insert_one(data)
    # 서버에 데이터가 쌓이면 그때 DB에 한번에올리면(insert_many) 좀더 개선이 가능해보임

# @app.get을 하나로 합치고 flag값을 두면 더 좋아보임
@app.post("/type1")
def value1(request: JsonValue1):
    dblogic(dict(request), "type1")

@app.post("/type2")
def value2(request: JsonValue2):
    dblogic(dict(request), "type2")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9999)
