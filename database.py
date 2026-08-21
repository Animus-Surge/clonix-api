import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker

from objects import DeviceReprObject

# TODO: move info to .env
DB_URI='mysql+pymysql://root:supersecurepassword123@localhost:3301/clonixdb'
# The above line is not representative of the production database

# Used when the actual connections are made to the database
engine = create_engine(DB_URI)

def get_db():
    with engine.connect() as connection:
        yield connection


# TODO: filter
def get_devices(hostname_filter: str = ''):
    pass


def create_device(metadata: DeviceReprObject):
    pass
