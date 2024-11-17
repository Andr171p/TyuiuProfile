from pydantic import BaseModel, ConfigDict
from typing import List, Literal


class RecsSchema(BaseModel):
    recommendations: List[str]


class RecSysResponseSchema(BaseModel):
    status: Literal['ok'] = 'ok'
    data: RecsSchema

    model_config = ConfigDict(from_attributes=True)
