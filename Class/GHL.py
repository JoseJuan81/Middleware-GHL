from Class.GhlContact import GhlContact

GHL_CONTACT_URL = "https://rest.gohighlevel.com/v1/contacts/"
GHL_CUSTOM_FIELD_URL = "https://rest.gohighlevel.com/v1/custom-fields/"

class GHL:
    Contact = GhlContact(GHL_CONTACT_URL, GHL_CUSTOM_FIELD_URL)
