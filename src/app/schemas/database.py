from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    surname: str
    phone: str
    email: str
    gender: Literal['М', 'Ж']
    bdate: datetime
    sport: str
    foreign: str
    gpa: float
    exams_points: int
    bonus_points: int
    exams: List[str]
    education: str
    study_form: str
    speciality: str