import json

# TEMPORARY - ram-based JSON database. REPLACE WITH RELATIONAL (mysql/mariadb/postgresql/etc...)
DATABASE = {}

# Used when the actual connections are made to the database
db_obj = None 

def init():
    global DATABASE
    # Runs schemas and loads fake data from dbtest.json

    with open ('dbtest.json', 'r') as file:
        DATABASE = json.loads(file.read())


def get_devices(count=25, offsetPage=0):
    global DATABASE

    if 'devices' not in DATABASE:
        return []

    result = []

    if count == 0: return []

    startpoint = count * offsetPage
    endpoint = count * (offsetPage + 1)

    if startpoint >= len(DATABASE.get('devices')):
        return []

    for i in range(startpoint, endpoint):
        if i >= len(DATABASE.get('devices')):
            break

        result.append(DATABASE.get('devices')[i])

    return result

