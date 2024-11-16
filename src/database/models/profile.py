from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from typing import List
from datetime import datetime

from src.database.models.base import Base


class AbstractModel(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class ProfileModel(AbstractModel):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    gender: Mapped[str]
    bdate: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    sport: Mapped[str]
    foreign: Mapped[str]
    gpa: Mapped[float]
    exams_points: Mapped[int] = mapped_column(Integer, nullable=True)
    bonus_points: Mapped[int] = mapped_column(Integer, nullable=True)
    exams: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    education: Mapped[str] = mapped_column(String)
    study_form: Mapped[str] = mapped_column(String)
