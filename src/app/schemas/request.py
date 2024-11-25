from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime

from src.app.schemas.user import UserSchema


class CreateUserRequestSchema(UserSchema, BaseModel):
    pass
