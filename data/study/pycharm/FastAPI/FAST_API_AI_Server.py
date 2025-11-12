import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

app = FastAPI(title="AI Server")

class AnalysisRequest(BaseModel):
    mode: str
    text: str

# -----------------------
# 2. 분석 함수 정의
# -----------------------
@app.post("/analysis")
def analyze_text(request: AnalysisRequest):
    """
    클라이언트의 요청(Json)을 받아 분석 결과를 반환하는 함수
    :param request: dict(ex) {"mode":"sentiment", "text":"문장"})
    :return:
    """
    request = request.__dict__
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
        analysis = sentiment(text)[0]
        label = analysis['label']
        score = analysis['score']

        return {
            "result": label,
            "score": score,
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)