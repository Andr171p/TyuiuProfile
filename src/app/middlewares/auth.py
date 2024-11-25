from fastapi import FastAPI
from fastapi import Request, Response
from fastapi import HTTPException, status

from typing import Callable


class AuthMiddleware:
    def __init__(self, app: FastAPI) -> None:
        self._app = app

    async def __call__(
            self,
            request: Request,
            call_next: Callable
    ) -> Response:
        token = request.cookies.get("access")
        if not token or not self.validate_token(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        response = await call_next(request)
        return response

    def validate_token(self, token: str) -> bool:
        # Здесь будет валидация токена ...
        ...
