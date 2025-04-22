from enum import Enum
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.core import Base


class RoleEnum(str, Enum):
    NOT_VERIFIED = "not_verified"
    VERIFIED = "verified"
    MANAGER = "manager"
    ADMIN = "admin"


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128))

    role: Mapped[RoleEnum] = RoleEnum.NOT_VERIFIED

    email_otp: Mapped[str | None] = mapped_column(String(6), nullable=True)
    otp_created_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
