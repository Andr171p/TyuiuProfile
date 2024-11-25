from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.middlewares.globals import g
from src.app.schemas.request import CreateUserRequestSchema
from src.app.schemas.response import GetProfileResponse, CreateProfileResponse

from src.database.models.user import UserModel


profile_router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@profile_router.get(path="/get/{id}/", response_model=GetProfileResponse)
async def get_profile(id: int) -> JSONResponse:
    user_service = g.user_service
    db_user = await user_service.get_user(id)
    return JSONResponse(
        content={
            "status": "ok",
            "user": db_user
        }
    )


@profile_router.post(path="/create/", response_model=CreateProfileResponse)
async def create_profile(user: CreateUserRequestSchema) -> JSONResponse:
    user_service = g.user_service
    db_user = await user_service.create_user(
        user=UserModel(**user.__dict__)
    )
    return JSONResponse(
        content={
            "status": "ok",
            "user": db_user
        }
    )
