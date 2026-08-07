import json

# TODO: move info to .env
DB_URI='mysql+pymysql://apiconn:supersecurepassword123@localhost:3301/clonixdb'

# Used when the actual connections are made to the database
db_obj = None 

def init():
    global DATABASE
    # Runs schemas and loads fake data from dbtest.json

    with open ('dbtest.json', 'r') as file:
        DATABASE = json.loads(file.read())


def get_devices(count=25, offsetPage=0):
    pass
