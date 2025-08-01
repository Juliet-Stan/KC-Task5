# Job Application Tracker API

A FastAPI-based API to manage job applications.

## Features
* Create, read, and manage job applications
* Store data in a JSON file
* Use try-except blocks for error handling
* Version control using Git

## Endpoints
* `POST /applications/`: Create a new job application
* `GET /applications/{id}`: Get a job application by ID
* `GET /applications/`: Get all job applications
* `PUT /applications/{id}`: Update a job application
* `DELETE /applications/{id}`: Delete a job application

## Usage
1. Clone the repository: `git clone https://github.com/your-username/job-application-tracker-api.git`
2. Navigate to the project directory: `cd job-application-tracker-api`
3. Install dependencies: `pip install fastapi uvicorn`
4. Run the application: `uvicorn main:app --reload`
5. Use a tool like curl or Postman to test the API

## Example Requests
* Create a new job application: `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "company": "ABC Corp", "position": "Software Engineer", "status": "pending"}' http://localhost:8000/applications/`
* Get a job application by ID: `curl -X GET http://localhost:8000/applications/1`
* Get all job applications: `curl -X GET http://localhost:8000/applications/`
* Update a job application: `curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Doe", "company": "ABC Corp", "position": "Software Engineer", "status": "interviewing"}' http://localhost:8000/applications/1`
* Delete a job application: `curl -X DELETE http://localhost:8000/applications/1`