import requests

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from Models.ghl_new_contact import GHLNewContactModel

class GhlContact:
    def __init__(self, URL_CONTACT: str, URL_CUSTOM_FIELDS: str) -> None:
        self.custom_field: list = []
        self.tags: list = []
        self.url_contact = URL_CONTACT
        self.url_custom_field = URL_CUSTOM_FIELDS

    def create(self, request: Request, new_contact: GHLNewContactModel) -> JSONResponse:
        """Funcion para crear una contacto en GHL"""

        headers = dict(request.headers)
        url = self.url_contact 

        try:
            json_data = jsonable_encoder(new_contact)
            response = requests.post(url, headers=headers, json=json_data)
            status_code = response.status_code

            if status_code == 200:
                return JSONResponse(content=response.json(), status_code=response.status_code)

            return JSONResponse(content=response.text, status_code=response.status_code)

        except ValueError as e:
            print("/ghl/v1/new-contact: error")
            print(e)
            print("/ghl/v1/new-contact: fin error")
            return JSONResponse(content=e, status_code=500)