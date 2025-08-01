# Simple Contact API (Using Path & Query Parameters)

A FastAPI-based API to manage contacts using path and query parameters.

## Features
* Create, read, and manage contacts
* Use path and query parameters to filter contacts
* Store data in a dictionary
* Version control using Git

## Endpoints
* `POST /contacts/`: Create a new contact
* `GET /contacts/{name}`: Get a contact by name
* `GET /contacts/`: Get all contacts
* `GET /contacts/?name={name}`: Get a contact by name using query parameter
* `GET /contacts/?email={email}`: Get a contact by email using query parameter

## Usage
1. Clone the repository: `git clone https://github.com/your-username/simple-contact-api.git`
2. Navigate to the project directory: `cd simple-contact-api`
3. Install dependencies: `pip install fastapi uvicorn`
4. Run the application: `uvicorn main:app --reload`
5. Use a tool like curl or Postman to test the API

## Example Requests
* Create a new contact: `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"}' http://localhost:8000/contacts/`
* Get a contact by name: `curl -X GET http://localhost:8000/contacts/John%20Doe`
* Get all contacts: `curl -X GET http://localhost:8000/contacts/`
* Get a contact by name using query parameter: `curl -X GET 'http://localhost:8000/contacts/?name=John%20Doe'`
* Get a contact by email using query parameter: `curl -X GET 'http://localhost:8000/contacts/?email=john@example.com'`

