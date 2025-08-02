from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
import re

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr

    @field_validator('phone')
    def validate_phone_number(cls, v: str) -> str:
        # A simple regex for a 10-15digit phone number
        phone_regex = re.compile(r'^\+?[\d\s()-]{10,15}$')
        
        if not phone_regex.match(v):
            raise ValueError('Invalid phone number format. Please use a valid 10-digit number.')
        return v

contacts = {}

@app.post("/contacts/")
def create_contact(contact: Contact):
    if contact.name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists")
    contacts[contact.name] = contact.dict()
    return contact

@app.get("/contacts/")
def read_contacts(name: str = None):
    if name:
        if name in contacts:
            return contacts[name]
        else:
            raise HTTPException(status_code=404, detail="Contact not found")
    else:
        return list(contacts.values())

@app.post("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    if name in contacts:
        contacts[name] = contact.dict()
        return contact
    else:
        raise HTTPException(status_code=404, detail="Contact not found")

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name in contacts:
        del contacts[name]
        return {"message": "Contact deleted"}
    else:
        raise HTTPException(status_code=404, detail="Contact not found")