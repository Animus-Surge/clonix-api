# crypthandler.py
# Handles JWTs and asymmetric keys

import pydantic


pk_path = ""

class JWT(pydantic.BaseModel):
    pass

def generate_jwt(ttl_minutes=30):
    pass
