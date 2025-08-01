from fastapi import FastAPI, HTTPException
from student import Student
import json

app = FastAPI()

students = {}

try:
    with open('students.json', 'r') as f:
        students = json.load(f)
except FileNotFoundError:
    pass

@app.post("/students/")
def create_student(student: Student):
    try:
        students[student.name] = student.dict()
        with open('students.json', 'w') as f:
            json.dump(students, f)
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/{name}")
def read_student(name: str):
    if name in students:
        return students[name]
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.get("/students/")
def read_students():
    return list(students.values())

