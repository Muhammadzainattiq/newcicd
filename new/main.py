from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def salam():
    return {"message": "assalam o alaikum"}

@app.get('/name/')
def zain():
    return "Muhammad Zain Attiq"