from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI(
    title="FastAPI 기본예제",
    description="FastAPI Dex",
    version="1.0.0",
)

class Item(BaseModel):
    name: str
    price: float # 필수: 가격
    description: Optional[str] = None #선택:설명

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
def say_hello(name: str="사용자"):
    return {"message": f"Hello {name}"}

@app.post("/items")
def create_item(item: Item):
    total_price = item.price * 1.1

    return {
        "total_price": total_price,
    }

#if __name__ == "__main__":
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)