from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select

from src.models import UserModel
from src.schemas import UserRegisterSchema
from src.api import AsyncSessionDep
from src.core import pwd_context


router = APIRouter(prefix='/v1/auth', tags=['👤Auth'])


@router.post('/register')
async def register(data: UserRegisterSchema, db: AsyncSessionDep):
    result = await db.execute(select(UserModel).filter_by(email=data.email))
    user = result.scalars().first()
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed_password = pwd_context.hash(data.password)
    new_user = UserModel(email=data.email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {'detail': 'User registered successfully'}


