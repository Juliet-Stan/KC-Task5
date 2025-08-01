from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone: str
    email: str

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
