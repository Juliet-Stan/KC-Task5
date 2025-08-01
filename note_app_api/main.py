from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

# Create a directory to store notes
if not os.path.exists('notes'):
    os.makedirs('notes')

@app.post("/notes/")
def create_note(note: Note):
    try:
        with open(f'notes/{note.title}.txt', 'w') as f:
            f.write(note.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{title}")
def read_note(title: str):
    try:
        with open(f'notes/{title}.txt', 'r') as f:
            return {'title': title, 'content': f.read()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@app.post("/notes/{title}")
def update_note(title: str, note: Note):
    try:
        with open(f'notes/{title}.txt', 'w') as f:
            f.write(note.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        os.remove(f'notes/{title}.txt')
        return {'message': 'Note deleted'}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")