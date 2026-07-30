from loguru import logger

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/")
def index():
    logger.info("GET: / Root index get")
    return "Hello!"

@app.get("/api/v1/devices/")
def devices():
    pass
