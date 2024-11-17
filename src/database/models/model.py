from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from typing import List
from datetime import datetime

from src.database.models.abstract import Abstract


class User(Abstract):
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    snils: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)

    profile: Mapped['Profile'] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    @mapped_column
    def full_name(cls) -> str:
        return f"{cls.first_name} {cls.last_name} {cls.surname}"

    def __repr__(self) -> str:
        return f"<User(name={self.full_name()}, email={self.email})>"



class Profile(Abstract):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    gender: Mapped[str]
    bdate: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    sport: Mapped[str]
    foreign: Mapped[str]
    gpa: Mapped[float]
    exams_points: Mapped[int] = mapped_column(Integer, nullable=True)
    bonus_points: Mapped[int] = mapped_column(Integer, nullable=True)
    exams: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    education: Mapped[str] = mapped_column(nullable=True)
    study_form: Mapped[str] = mapped_column(nullable=True)

    user: Mapped['User'] = relationship(
        back_populates='profile',
        uselist=False,
        cascade="all, delete-orphan"
    )

    @mapped_column
    def full_name(cls) -> str:
        return cls.user.full_name()
    
    def __repr__(self) -> str:
        return f"<Profile(user_id={self.user_id}, gender={self.gender}, bdate={self.bdate}, exam_points={self.exams_points})>"
