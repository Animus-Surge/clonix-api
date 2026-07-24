from loguru import logger

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello!"
