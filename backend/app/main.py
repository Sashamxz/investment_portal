from fastapi import FastAPI

from app.db.init_db import init_db

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to Investment Portal"}


init_db()
