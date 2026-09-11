import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from objects import *
from schema import *

# TODO: move info to .env
DB_URI='mysql+pymysql://root:supersecurepassword123@localhost:3301/clonixdb'
# The above line is not representative of the production database

# Used when the actual connections are made to the database
engine = create_engine(DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def q_devices_list(session: Session) -> list[DeviceListViewMinReprObject]:
    """
    Query for the main devices list

    ```sql
    select 
            Devices.device_id as uuid, 
            Devices.device_hostname as hostname, 
            Devices.device_sn as serial_number,
            Units.unit_name as unit,
            Buildings.building_name as building,
            DeviceLocations.room_number as room_number,
            Devices.checkin_timestamp as checkin_date
    from Devices
    join DeviceLocations on DeviceLocations.device_id = Devices.device_id
    join Buildings on DeviceLocations.building_id = Buildings.building_id
    join Units on Devices.device_unit = Units.unit_id;
    ```

    Parameters:
        session (Session): Database session

    Returns:
        list: Complete devices list
    """

    q_st = (select(
                Device.device_id.label("uuid"),
                Device.device_hostname.label("hostname"),
                Device.device_sn.label("serial_number"),
                Unit.unit_name.label("unit"),
                Building.building_name.label("building"),
                DeviceLocation.room_number.label("room_number"),
                Device.checkin_timestamp.label("checkin_date")
            )
            .join(DeviceLocation, DeviceLocation.device_id == Device.device_id)
            .join(Building, DeviceLocation.building_id == Building.building_id)
            .join(Unit, Device.device_unit == Unit.unit_id)
    )

    res = session.execute(q_st).mappings().all()
    return [DeviceListViewMinReprObject.model_validate(row) for row in res]

def q_device_info(session: Session, device_uuid: str) -> DeviceReprObject | ErrorResponseObject | None:
    return None
