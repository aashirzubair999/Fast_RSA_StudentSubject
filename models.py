from pydantic import BaseModel

class Student(BaseModel):
    studentname: str
    subjectid: int

class Subject(BaseModel):
    subjectname: str
    subjectinfo: str