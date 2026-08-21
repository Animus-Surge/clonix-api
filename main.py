import datetime

from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.engine import Connection

import database

import schema
from objects import DeviceListResponseObject, DeviceReprObject, UnitReprObject

app = FastAPI()
schema.metadata_obj.create_all(database.engine)

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


# Devices
@app.get("/api/v1/devices/")
async def list_devices(request: Request, db: Connection = Depends(database.get_db)):
    dev_sel_stmt = select(schema.device)
    dev_sel_res = db.execute(dev_sel_stmt).mappings().all()

    unit_sel_stmt = select(schema.unit)
    unit_sel_res = db.execute(unit_sel_stmt).mappings().all()

    # TODO: filters

    device_list = []
    for device in dev_sel_res:
        device_obj = DeviceReprObject(
            uuid=device.get("device_uuid", ""),
            hostname=device.get("hostname", ""),
            serial_number=device.get("serial_number", ""),
            unit={},
            provision_timestamp=device.get("provision_stamp", "").strftime("%Y/%m/%d %H:%M:%S"),
            checkin_timestamp=device.get("checkin_stamp", "").strftime("%Y/%m/%d %H:%M:%S")
        ) # TODO: facter integration

        for unit in unit_sel_res:
            if unit.get("unit_id") == device.unit:
                unit_obj = UnitReprObject(
                    unit_id=unit.get("unit_id", 0),
                    unit_name=unit.get("unit_name", ""),
                    manifest_id=unit.get("manifest_id", ""),
                )
                device_obj.unit = dict(unit_obj)
        
        device_list.append(dict(device_obj))

    device_list_obj = DeviceListResponseObject(
        count=len(device_list),
        devices=device_list)

    return dict(device_list_obj)

@app.post("/api/v1/devices/")
async def create_device(request: Request):
    # Request takes in: hostname, serial number, unit.

    stamp = datetime.datetime.now()
    pass

@app.get("/api/v1/devices/{device}")
async def get_device_info(request: Request, device: str):
    pass

@app.put("/api/v1/devices/{device}")
async def update_device(request: Request, device: str):
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

