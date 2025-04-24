from pydantic import BaseModel, EmailStr, Field


class UserRegisterSchema(BaseModel):
    email: EmailStr = Field(max_length=150)
    password: str = Field(min_length=8, max_length=128)
