from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, String, ForeignKey

from src.database.models.base import Base


class AbstractModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class UserModel:
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    snils: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)

    profile: Mapped['ProfileModel'] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )
