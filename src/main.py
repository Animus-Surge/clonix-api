from loguru import logger

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# Authentication endpoints
@app.get("/api/v1/auth/login")
async def login(req: Request):
    pass

@app.post("/api/v1/auth/saml/acs")
async def saml_callback():
    pass

@app.get("/api/v1/auth/saml/metadata")
async def saml_metadata():
    pass

# Primary Endpoints
@app.get("/api/v1/")
async def index():
    logger.info("GET: / Root index get")
    return "Hello!"

@app.get("/api/v1/devices/")
async def devices():
    pass
