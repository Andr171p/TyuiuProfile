from sqlalchemy import Select
from sqlalchemy import select, delete, insert, update
from typing import Generic, List, Optional
from functools import singledispatchmethod

from src.database.services.db import DBSession
from src.database.models.abstract import ModelType


class CRUD(DBSession, Generic[ModelType]):
    def __init__(self, model: type[ModelType]) -> None:
        super().__init__()
        self.init()
        self._model = model

    @singledispatchmethod
    async def get(self, arg) -> Optional[ModelType] | None:
        raise NotImplementedError(f"<CRUD> cannot get value")
    
    @get.register
    async def _(self, id: int) -> Optional[ModelType] | None:
        stmt = select(self._model).where(self._model.id == id)
        async with self.session() as session:
            item = await session.execute(stmt)
            return item.scalar_one_or_none()
        
    @get.register
    async def _(self, stmt: Select) -> Optional[ModelType] | None:
        async with self.session() as session:
            item = await session.execute(stmt)
            return item.scalar_one_or_none()
        
    async def get_multi(
            self,
            offset: int = 0,
            limit: int = 100,
            options: list = None
    ) -> List[ModelType]:
        stmt = select(self._model).offset(offset).limit(limit)
        async with self.session() as session:
            if options:
                stmt = stmt.options(*options)
            items = await session.execute(stmt)
            return items.scalars().unique().all()
        
    async def create(self, item: ModelType) -> ModelType:
        async with self.session() as session:
            stmt = insert(self._model).values(**item.__dict__).returning(self._model)
            db_item = await session.execute(stmt)
            db_item = db_item.fetchone()
            await session.flush()
            return db_item
        
    async def update(self, item: ModelType) -> ModelType:
        async with self.session() as session:
            stmt = (
                update(self._model)
                .where(self._model.id == item.id)
                .values(item.dict(exclude_unset=True))
                .returning(self._model)
            )
            db_item = await session.execute(stmt)
            db_item = db_item.fetchone()
            await session.flush()
            return db_item
        
    async def delete(self, id: int) -> bool:
        stmt = delete(self._model).where(self._model.id == id)
        async with self.session() as session:
            item = await session.execute(stmt)
            return item.rowcount > 0
