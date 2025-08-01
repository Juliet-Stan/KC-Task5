from pydantic import BaseModel

class Student(BaseModel):
    name: str
    subject_scores: dict
    average: float
    grade: str