from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime

from src.app.schemas.database import UserSchema


class GetProfileResponse(BaseModel):
    status: Literal["ok"] = "ok"
    user: UserSchema


class CreateProfileResponse(BaseModel):
    status: Literal["ok"] = "ok"
    user: UserSchema
