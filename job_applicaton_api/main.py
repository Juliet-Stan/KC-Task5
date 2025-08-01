from fastapi import FastAPI, HTTPException
from job_application import JobApplication
from file_handler import save_to_json, load_from_json

app = FastAPI()

applications = load_from_json('applications.json')

@app.post("/applications/")
def create_application(application: JobApplication):
    try:
        applications.append(application.dict())
        save_to_json(applications, 'applications.json')
        return application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/")
def read_applications():
    return applications

@app.get("/applications/search/")
def search_applications(status: str):
    try:
        return [app for app in applications if app['status'] == status]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
