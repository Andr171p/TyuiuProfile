from src.database.services.crud import CRUD
from src.database.models.user import UserModel


class UserService(CRUD):
    def __init__(self) -> None:
        super().__init__(model=UserModel)

    async def get_user(self, id: int) -> UserModel:
        return await self.get(id)

    async def create_user(self, user: UserModel) -> UserModel:
        return await self.create(user)

    async def update_user(self, user: UserModel) -> UserModel:
        return await self.update(user)

    async def delete_user(self, id: int) -> bool:
        return await self.delete(id)
