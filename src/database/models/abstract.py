from sqlalchemy.orm import Mapped, mapped_column
from typing import TypeVar

from src.database.models.base import Base


class Abstract(Base):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


ModelType = TypeVar("ModelType", bound=Abstract)
