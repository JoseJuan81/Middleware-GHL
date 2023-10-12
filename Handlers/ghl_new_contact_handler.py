import requests

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from Models.ghl_new_contact import GHLNewContactModel

GHL_CONTACT_URL = "https://rest.gohighlevel.com/v1/contacts/"

def ghl_new_contact_handler(new_contact: GHLNewContactModel, request: Request) -> JSONResponse:
    """Funcion que maneja la creacion de usuario en GHL"""

    headers = request.headers
    url = GHL_CONTACT_URL 

    try:
        json_data = jsonable_encoder(new_contact)
        response = requests.post(url, headers=headers, json=json_data)
        return JSONResponse(content=response, status_code=200)
    except ValueError:
        print("/ghl/v1/new-contact: error")
        print(ValueError)
        print("/ghl/v1/new-contact: fin error")
        return JSONResponse(content=ValueError, status_code=500)