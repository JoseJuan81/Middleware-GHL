from Class.GhlContact import GhlContact
from Class.GhlCustomFields import GhlCustomFields

GHL_CONTACT_URL = "https://rest.gohighlevel.com/v1/contacts/"
GHL_CUSTOM_FIELD_URL = "https://rest.gohighlevel.com/v1/custom-fields/"

class GHL:
    CustomFields = GhlCustomFields(GHL_CUSTOM_FIELD_URL)
    Contact = GhlContact(GHL_CONTACT_URL, CustomFields)
