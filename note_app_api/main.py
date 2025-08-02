# main.py (New endpoint added)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from typing import List

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

# Create a directory to store notes
if not os.path.exists('notes'):
    os.makedirs('notes')

# --- NEW ENDPOINT ---
@app.get("/notes/")
def list_notes() -> List[str]:
    """Returns a list of all available note titles."""
    try:
        # Get all filenames from the 'notes' directory
        note_files = os.listdir('notes')
        # Remove the '.txt' extension for a cleaner output
        note_titles = [file.replace('.txt', '') for file in note_files if file.endswith('.txt')]
        return note_titles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# --- END NEW ENDPOINT ---

@app.post("/notes/")
def create_note(note: Note):
    # ... (rest of your code remains the same)
    try:
        with open(f'notes/{note.title}.txt', 'w') as f:
            f.write(note.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{title}")
def read_note(title: str):
    # ... (rest of your code remains the same)
    try:
        with open(f'notes/{title}.txt', 'r') as f:
            return {'title': title, 'content': f.read()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@app.post("/notes/{title}")
def update_note(title: str, note: Note):
    # ... (rest of your code remains the same)
    try:
        with open(f'notes/{title}.txt', 'w') as f:
            f.write(note.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/{title}")
def delete_note(title: str):
    # ... (rest of your code remains the same)
    try:
        os.remove(f'notes/{title}.txt')
        return {'message': 'Note deleted'}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")