from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import get_session

AsyncSessionDep = Annotated[AsyncSession, Depends(get_session)]
