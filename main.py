# main.py

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data": {"name": "venky"}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": request.dict()}
