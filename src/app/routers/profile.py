from fastapi import APIRouter
from fastapi.responses import JSONResponse



profile_router = APIRouter(
    prefix="/profile",
    tags=["Profie"]
)


@profile_router.post(path="/create", response_model=...)
async def create_profile(user: ...) -> JSONResponse:
    ...