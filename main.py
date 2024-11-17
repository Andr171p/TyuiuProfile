from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import contextlib

from src.config import settings


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    ...


app = FastAPI(
    title=settings.app.name
)

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=settings.app.origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"]
#)
