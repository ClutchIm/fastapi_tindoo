from datetime import timedelta
from typing import Optional

from pydantic import EmailStr, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=["../.env", ".env"],
        env_ignore_empty=True,
    )

    # Database
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Email
    SMTP_TLS: Optional[bool] = True
    SMTP_SSL: Optional[bool] = False
    SMTP_HOST: Optional[str]= None
    SMTP_PORT: Optional[int] = 587
    SMTP_USER: Optional[str]= None
    SMTP_PASS: Optional[str]= None
    EMAILS_FROM_EMAIL: Optional[EmailStr]= None

    # Secure
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: Optional[str] = "HS256"
    JWT_TOKEN_LOCATION: Optional[list[str]] = ["headers"]
    JWT_ACCESS_TOKEN_EXPIRES: Optional[timedelta] = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES: Optional[timedelta] = timedelta(days=7)


settings = Settings()
