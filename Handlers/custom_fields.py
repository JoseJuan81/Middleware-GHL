import requests

from fastapi import Request
from fastapi.responses import JSONResponse

GHL_CUSTOM_FIELDS = "https://rest.gohighlevel.com/v1/custom-fields/"

def custom_fields_handler(request: Request) -> JSONResponse:
    """Funcion que ejecuta consulta para obtener los custom fields en GHL"""

    headers = request.headers
    url = GHL_CUSTOM_FIELDS 

    try:
        response = requests.get(url, headers=headers)
        return JSONResponse(content=response, status_code=200)
    except ValueError:
        print("/ghl/v1/custom-fields: error")
        print(ValueError)
        print("/ghl/v1/custom-fields: fin error")
        return JSONResponse(content=ValueError, status_code=500)
