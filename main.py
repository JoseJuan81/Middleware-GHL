from fastapi import FastAPI, Depends, Response, Request

from Models.ghl_new_contact import GHLNewContactModel
from Class.GHL import GHL

from Middlewares.verify_ghl_token import verify_ghl_token

GHL_AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkNLR1ZRODFyczRSa3F0UGJRdmdPIiwiY29tcGFueV9pZCI6ImttWDhSeEZWYWlSeFI1aGVxUUp5IiwidmVyc2lvbiI6MSwiaWF0IjoxNjk2MzgxNjgyNDcyLCJzdWIiOiJ1c2VyX2lkIn0.UO4IiEUdCncw8SAae3Jx7oPXXsdp0VIUhWh8UN4ILTc"


app = FastAPI()

@app.get("/")
def index():
    return "Hola Mundo"

# Considerar middleware para guardar data de contacto en BD
# Depends(save_contact_data)
@app.post("/ghl/v1/new-contact", dependencies=[Depends(verify_ghl_token)])
async def ghl_create_new_contact(request: Request, new_contact: GHLNewContactModel) -> Response:
    """Funcion para crear nuevo contacto en GHL"""

    return GHL.Contact.create(request, new_contact)
   

@app.get("/ghl/v1/custom-fields", dependencies=[Depends(verify_ghl_token)])
async def ghl_get_custom_fields():
    """Funcion para obtener los custom Fields en GHL"""

    return GHL.contact.custom_fields_handler()

