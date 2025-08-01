# Notes App API (With File System Support)

A FastAPI-based API to manage notes with file system support.

## Features
* Create, read, and manage notes
* Store notes in a JSON file
* Use file system to store notes
* Version control using Git

## Endpoints
* `POST /notes/`: Create a new note
* `GET /notes/{title}`: Get a note by title
* `GET /notes/`: Get all notes
* `PUT /notes/{title}`: Update a note
* `DELETE /notes/{title}`: Delete a note

## Usage
1. Clone the repository: `git clone https://github.com/your-username/notes-app-api.git`
2. Navigate to the project directory: `cd notes-app-api`
3. Install dependencies: `pip install fastapi uvicorn`
4. Run the application: `uvicorn main:app --reload`
5. Use a tool like curl or Postman to test the API

## Example Requests
* Create a new note: `curl -X POST -H "Content-Type: application/json" -d '{"title": "My Note", "content": "This is my note"}' http://localhost:8000/notes/`
* Get a note by title: `curl -X GET http://localhost:8000/notes/My%20Note`
* Get all notes: `curl -X GET http://localhost:8000/notes/`
* Update a note: `curl -X PUT -H "Content-Type: application/json" -d '{"title": "My Note", "content": "This is my updated note"}' http://localhost:8000/notes/My%20Note`
* Delete a note: `curl -X DELETE http://localhost:8000/notes/My%20Note`

## File System Support
* Notes are stored in a `notes` directory
* Each note is stored in a separate file with a `.txt` extension

Added basic API endpoints and data storage
* Updated error handling: Added try-except blocks for error handling
* Refactored code: Improved code organization and readability