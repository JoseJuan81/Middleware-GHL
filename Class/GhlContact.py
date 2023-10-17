import requests

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from Models.ghl_new_contact import GHLNewContactModel
from Class.GhlCustomFields import GhlCustomFields

class GhlContact:
    def __init__(self, URL_CONTACT: str, CustomFields: GhlCustomFields) -> None:
        self.tags: list = []
        self.url_contact = URL_CONTACT
        self.custom_fields = CustomFields
        self.headers: dict = None

    def set_headers(self, headers: dict) -> None:
        """Funcion que establece el valor de Headers en la variable de la clase"""

        self.headers = dict([
            ("Authorization", headers["authorization"]),
            ("Content-Type", headers["content-type"])
        ])

    def create(self, request: Request, new_contact: GHLNewContactModel) -> JSONResponse:
        """Funcion para crear una contacto en GHL"""
        
        self.set_headers(request.headers)

        _custom_fields = self.custom_fields.check(request, new_contact.customField)
        new_contact_updated = { **dict(new_contact), **_custom_fields }

        try:
            response = requests.post(self.url_contact, headers=self.headers, json=new_contact_updated)
            status_code = response.status_code

            if status_code == 200:
                return JSONResponse(content=response.json(), status_code=response.status_code)

            return JSONResponse(content=response.text, status_code=response.status_code)

        except ValueError as e:
            print("/ghl/v1/new-contact: error")
            print(e)
            print("/ghl/v1/new-contact: fin error")
            return JSONResponse(content=e, status_code=500)
    