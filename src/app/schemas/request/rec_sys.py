from pydantic import BaseModel, ConfigDict
from typing import List, Literal


class UserSchema(BaseModel):
    gender: str
    age: int
    sport: str
    foreign: str
    gpa: float
    total_points: int
    bonus_points: int
    exams: List[str]
    education: str
    study_form: str


class RecSysRequestSchema(BaseModel):
    top_n: int
    user: UserSchema

    model_config = ConfigDict(from_attributes=True)
