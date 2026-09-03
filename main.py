from fastapi import FastAPI
from pydantic import BaseModel
from prompts import generate_report, detect_lead

app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    phone: str
    education: str
    skills: str
    interests: str
    career_goal: str
    preferred_degree_mode: str
    counseling_interest: str

@app.get("/")
def home():
    return {"message": "AI Career Guidance System Running"}

@app.post("/analyze")
def analyze(student: Student):
    report = generate_report(student)
    lead = detect_lead(student)

    return {
        "report": report,
        "lead_generated": lead
    }