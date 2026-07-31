from loguru import logger

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Authentication endpoints
@app.get("/api/v1/auth/login/")
def login():
    pass

@app.post("/api/v1/auth/callback")
def saml_Callback():
    pass

# Primary Endpoints
@app.get("/api/v1/")
def index():
    logger.info("GET: / Root index get")
    return "Hello!"

@app.get("/api/v1/devices/")
def devices():
    pass
