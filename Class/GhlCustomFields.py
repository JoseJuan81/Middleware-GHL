import requests

from fastapi import Request
from fastapi.encoders import jsonable_encoder

class GhlCustomFields:
    def __init__(self, url) -> None:
        self.url = url
        self.headers: dict = None
        self.ghl_custom_fields: list[dict] = None

    def set_headers(self, headers: dict) -> None:
        """Funcion que establece el valor de Headers en la variable de la clase"""

        self.headers = dict([
            ("Authorization", headers["authorization"]),
            ("Content-Type", headers["content-type"])
        ])

    def check(self, request: Request, custom_fields: dict) -> dict:
        """Funcion para obtener los custom fields de ghl y crea los requeridos"""

        self.set_headers(request.headers)

        self.ghl_custom_fields = self.get_custom_fields()
        exist_in_ghl, no_exist_in_ghl = self.custom_fields_match(custom_fields, self.ghl_custom_fields)
        created_custom_fields = self.create(no_exist_in_ghl)
        custom_fields_to_send = { **exist_in_ghl, **created_custom_fields }
        
        return custom_fields_to_send
    
    def get_custom_fields(self) -> list[dict]:
        """Funcion que decide si solicita los customFields de GHL"""

        return self.ghl_custom_fields if self.ghl_custom_fields else self.get_ghl_custom_fields()
    
    def create(self, custom_fields_to_create: dict) -> list:
        """Funcion para crear custom fields en GHL"""

        response = {}
        for field in custom_fields_to_create.items():
            body = self.build_body(field)
            custom_field_id = self.create_in_ghl(body)
            _, val = field
            response.update({ custom_field_id: val })

        return response

    def create_in_ghl(self, body: dict) -> str:
        """Funcion para crear un custom Field en GHL y retornar su id"""

        try:
            response = requests.post(self.url, headers=self.headers, json=body)
            return response.json()["customField"]["id"] if response.status_code == 200 else ""
        except Exception as e:
            print("Error creando el custom fields en GHL")
            print(e)
            print("Error creando el custom fields en GHL")
            return e
    
    def build_body(self, custom_fields_to_create: tuple = (), data_type: str = "TEXT") -> dict:
        """Funcion para crear dict para enviar en servicio de creacion de customFields"""

        key, _ = custom_fields_to_create
        body = dict([
            ("dataType", data_type),
            ("name", key),
            ("placeholder", key.title())
        ])

        return body
    
    def get_ghl_custom_fields(self) -> list[dict]:
        """Funcion que obtiene los custom fields de GHL"""

        try:
            response = requests.get(self.url, headers=self.headers)
            return response.json()["customFields"] if response.status_code == 200 else []
        except Exception as e:
            print("Error consultado los custom fields de GHL")
            print(e)
            print("Error consultado los custom fields de GHL")
            return []
        
    def custom_fields_match(self, custom_fields: dict = {}, ghl_custom_fields: list = []) -> tuple[dict]:
        """Funcion que retorna los elementos de list1 que no estan en list2"""
        
        exist_in_ghl = {}
        no_exist_in_ghl = {}
        for k, v in custom_fields.items():
            exist = next((item for item in ghl_custom_fields if item["name"] == k), None)
            if exist:
                id = exist["id"]
                exist_in_ghl.update({ id: v })
            else:
                no_exist_in_ghl.update({ k: v })
        
        return (exist_in_ghl, no_exist_in_ghl)
