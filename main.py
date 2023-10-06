import requests
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from Models.ghl_new_contact import GHLNewContactModel

GHL_AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkNLR1ZRODFyczRSa3F0UGJRdmdPIiwiY29tcGFueV9pZCI6ImttWDhSeEZWYWlSeFI1aGVxUUp5IiwidmVyc2lvbiI6MSwiaWF0IjoxNjk2MzgxNjgyNDcyLCJzdWIiOiJ1c2VyX2lkIn0.UO4IiEUdCncw8SAae3Jx7oPXXsdp0VIUhWh8UN4ILTc"
GHL_CONTACT_URL = "https://rest.gohighlevel.com/v1/contacts/"

app = FastAPI()

@app.get("/")
def index():
    return "Hola Mundo"

@app.post("/ghl/v1/new-contact")
async def ghl_create_new_contact(new_contact: GHLNewContactModel):
    """Funcion para crear nuevo contacto en GHL"""

    url = GHL_CONTACT_URL 
    headers = {
        "Authorization": GHL_AUTH_TOKEN,
		"Content-Type": "application/json"
    }

    try:
        json_data = jsonable_encoder(new_contact)
        response = requests.post(url, headers=headers, json=json_data)
        return { "data": response.json()}
    except ValueError:
        print("/ghl/v1/new-contact: error")
        print(ValueError)
        print("/ghl/v1/new-contact: fin error")
        return ValueError


@app.post("/ghl/v1/new-contacts")
async def ghl_create_new_contacts(new_contacts: list[GHLNewContactModel]):
    """Funcion para crear varios contactos en GHL"""
    
    responses = []
    for new_contact in new_contacts:
        res = await ghl_create_new_contact(new_contact)
        responses.append(res)

    return responses
