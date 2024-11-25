from contextlib import AbstractAsyncContextManager
from fastapi import FastAPI

from src.config import settings
from src.app.middlewares.globals import g
from src.database.services.service import UserService


async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    user_service = UserService()
    g.set_default("user_service", user_service)
    yield
    del user_service


# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=settings.app.origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"]
# )
