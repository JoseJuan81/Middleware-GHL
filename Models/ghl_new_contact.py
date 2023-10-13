from pydantic import BaseModel
from typing import Union

class GHLNewContactModel(BaseModel):
    address1: Union[str, None] = ""
    age: Union[int, None] = 0
    city: Union[str, None] = ""
    country: Union[str, None] = "peru"
    custom_field: Union[dict, None] = {}
    dni: Union[str, None] = ""
    email: str
    firstName: str
    lastName: str
    name: Union[str, None] = ""
    phone: str
    source: str 
    state: Union[str, None] = "active"
    tags: Union[list[str], None] = []
