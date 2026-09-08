# security.py - Authentication handling

import jwt

from fastapi import Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, SecurityScopes

from onelogin.saml2.auth import OneLogin_Saml2_Auth

from sqlalchemy.orm import Session

import database

async def saml_prep(req: Request) -> dict:
    form_data = await req.form()

    return {
            "https": "on" if req.url.scheme == "https" else "off",
            "http_host": req.url.netloc,
            "script_name": req.url.path,
            "server_port": req.url.port or (443 if req.url.scheme == "https" else 80),
            "get_data": dict(req.query_params),
            "post_data": {k: v for k, v in form_data.items()}
    }

def create_jwt(saml_id: str) -> str:
    return jwt.encode({"sub": saml_id}, "lalalalala", algorithm="HS256") # TODO: asymmetric encryption of this
