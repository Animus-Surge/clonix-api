import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from objects import DeviceReprObject

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

