import datetime

from loguru import logger

from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.engine import Connection

import database

from objects import DeviceListResponseObject
from schema import device

app = FastAPI()


# Authentication endpoints
@app.get("/api/v1/auth/login")
async def login(request: Request):
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
    return {"message": "Hello World!"}


# Devices
@app.get("/api/v1/devices/")
async def list_devices(request: Request, db: Connection = Depends(database.get_db)):
    # TODO: filters in the request body
    statement = select(device)

    result = db.execute(statement).all()
    
    device_list = []
    num_devices = len(result)
    device_dict = [dict(device) for device in result]
    for device in device_dict:
        device_list.append(

    response_obj = DeviceListResponseObject(total_count=num_devices, devices=device_dict)

    return dict(response_obj)



@app.post("/api/v1/devices/")
async def create_device(request: Request):
    # Request takes in: hostname, serial number, unit.

    stamp = datetime.datetime.now()
    pass

@app.get("/api/v1/devices/{device}")
async def get_device_info(request: Request, device):
    pass

@app.put("/api/v1/devices/{device}")
async def update_device(request: Request, device):
    pass


@app.delete("/api/v1/devices/{device}")
async def delete_device(request: Request, device):
    pass


# Keys
@app.get("/api/v1/devices/{device}/keys")
async def get_device_keys(request: Request, device, key):
    pass

@app.post("/api/v1/devices/{device}/keys/{key}")
async def create_device_key(request: Request, device, key):
    pass

@app.delete("/api/v1/devices/{device}/keys/{key}")
async def delete_device_key(request: Request, device, key):
    pass


# Units
@app.get("/api/v1/units")
async def list_units(request: Request):
    pass

@app.get("/api/v1/units/{unit}")
async def get_unit_info(request: Request, unit):
    pass

@app.post("/api/v1/units/create")
async def create_unit(request: Request):
    pass


# Users
@app.get("/api/v1/users")
async def list_users(request: Request):
    pass

@app.post("/api/v1/users/add")
async def create_user(request: Request):
    pass

@app.get("/api/v1/users/{user}")
async def get_user_info(request: Request, user):
    pass

@app.put("/api/v1/users/{user}")
async def update_user(request: Request, user):
    pass

@app.delete("/api/v1/users/{user}")
async def remove_user(request: Request, user):
    pass

@app.put("/api/v1/users/{user}/contact")
async def update_user_contact(request: Request, user):
    pass


# Units
@app.get("/api/v1/units")
async def list_units
