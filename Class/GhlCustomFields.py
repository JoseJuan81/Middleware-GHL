import requests

from fastapi import Request

class GhlCustomFields:
    def __init__(self, url) -> None:
        self.url = url

    def check(self, request: Request, custom_fields: dict) -> dict:
        """Funcion para obtener los custom fields de ghl y crea los requeridos"""

        ghl_custom_fields = self.get_ghl_custom_fields(request)
        custom_fields_to_create = difference_between_list(custom_fields, ghl_custom_fields)
        created_custom_fields = self.create(custom_fields_to_create)
        ghl_custom_fields = ghl_custom_fields + created_custom_fields
        custom_fields_to_send = self.build_custom_fields(ghl_custom_fields, custom_fields)
        
        return custom_fields_to_send
    
    def get_ghl_custom_fields(self, request: Request) -> list[dict]:
        """Funcion que obtiene los custom fields de GHL"""

        try:
            response = requests.get(self.url, headers=request.headers)
            return response["customFields"] if response.status_code == 200 else []
        except Exception as e:
            print("Error consultado los custom fields de GHL")
            print(e)
            print("Error consultado los custom fields de GHL")
            return []
