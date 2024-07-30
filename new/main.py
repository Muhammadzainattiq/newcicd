from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def salam():
    return {"message": "assalam o alaikum wa rehmatullah hi wa barakatoho."}

@app.get('/name/')
def zain():
    return "Muhammad Zain Attiq"