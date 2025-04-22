from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext

from src.models import UserModel
from src.schemas import UserRegisterSchema
from src.api import SessionDep


router = APIRouter(prefix='/v1/auth', tags=['👤Auth'])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/register')
async def register(data: UserRegisterSchema, db: SessionDep):
    user = db.query(UserModel).filter_by(email=data.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed_password = pwd_context.hash(data.password)
    new_user = UserModel(email=data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'detail': 'User registered successfully'}


