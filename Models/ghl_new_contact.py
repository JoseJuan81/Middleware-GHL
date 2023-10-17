from pydantic import BaseModel
from typing import Union

class GHLNewContactModel(BaseModel):
    address1: Union[str, None] = ""
    city: Union[str, None] = ""
    companyName: Union[str, None] = "Digital Disruptor"
    country: Union[str, None] = "peru"
    customField: Union[dict, None] = {}
    dni: Union[str, None] = ""
    email: str
    firstName: str
    lastName: str
    name: Union[str, None] = ""
    phone: str
    source: str 
    state: Union[str, None] = "active"
    tags: Union[list[str], None] = []
