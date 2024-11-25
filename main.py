from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.app.application import lifespan


app = FastAPI(
    title=settings.app.name,
    lifespan=lifespan
)

# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=settings.app.origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"]
# )
