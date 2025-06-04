# C:\Users\venka\Downloads\fastapi\main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data": {"name": "venky"}}

@app.get("/about")
def about():
    return {"data": {"info": "about page1"}}
