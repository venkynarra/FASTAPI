# main.py (in the project root, next to blog/)
from fastapi import FastAPI
from blog import models
from blog.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/blog")
def create_blog(title: str, body: str):
    return {"title": title, "body": body}
