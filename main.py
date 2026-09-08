import datetime
from typing import Annotated
import uuid

import pydantic
from fastapi import FastAPI, Header, Request, Depends, Response, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, delete
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

import database
import objects
import schema

app = FastAPI()
schema.ClonixTableBase.metadata.create_all(database.engine)

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
    return {"message": "Hello World!"}


# Provisioning endpoints
# These come from the provisioning software

@app.post("/api/v1/provision/{device_serial}/data")
async def device_data_in(authorization: Annotated[str | None, Header()]):
    pass

@app.post("/api/v1/provision/{device_serial}")
async def provision_device(device_serial: str, db: Session = Depends(database.get_db)):
    # Retrieves a configuration object from the database
    
    
    pass

@app.post("/api/v1/provision")
async def create_autoprovision_entry(db: Session = Depends(database.get_db)):
    # Creates a new entry

    pass


# Devices
@app.get("/api/v1/devices/")
async def list_devices(request: Request, db: Connection = Depends(database.get_db)):
    pass

@app.post("/api/v1/devices/", status_code=status.HTTP_201_CREATED)
async def create_device(device_info: objects.DeviceCreateRequestObject, authorization: Annotated[str | None, Header()], response: Response, db: Session = Depends(database.get_db)):
    # Request takes in: hostname, serial number, unit.

    # User scope checking


    stamp = datetime.datetime.now()
    device_uuid = str(uuid.uuid4())

    device = schema.Device(device_id=device_uuid, provision_timestamp=stamp,
        device_hostname=device_info.hostname,
        device_sn=device_info.serial_number,
        device_unit=device_info.unit)

    db.add(device)
    db.commit()
    db.refresh(device)

    return device

@app.get("/api/v1/devices/{device}")
async def get_device_info(request: Request, device: str):
    pass

@app.put("/api/v1/devices/{device}")
async def update_device(request: Request, device: str):
    pass


@app.delete("/api/v1/devices/{device}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(device, response: Response, user_id: int, db: Session = Depends(database.get_db)):
    device_obj = db.get(schema.Device, device)
    if device_obj:
        db.delete(device_obj)
        db.commit()
        return None
    
    response.status_code = 404
    return None


# Keys
@app.get("/api/v1/devices/{device}/keys")
async def get_device_keys(request: Request, device, key):
    pass

@app.post("/api/v1/devices/{device}/keys/{key}")
async def create_device_key(request: Request, device, key):
    # This should be called by a cloner device
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

