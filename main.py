from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/jeongin")
def read_root():
    return {"Hello": "어서오세요"}


app.mount("/", StaticFiles(directory="public", html = True), name="static")
