# 找到正确目录: cd <your path>/CloudToLocalBatchExceptionDetection
# uvicorn main:app --reload
# ngrok http 8000(先下载ngrok配好，uvicorn打开fastapi，再在cmd终端输入这条)
from fastapi import FastAPI,HTTPException,Header
from data_loader import data_loader
from service import detection_service

app = FastAPI()
api_key = "12345"

@app.post("/batchDetection")
def detection(start_time:str=None, end_time:str=None, input_key=Header(None)):
    if input_key != api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    data = data_loader(start_time, end_time)
    result = detection_service(data)
    print("接口被调用了")
    return result

