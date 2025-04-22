from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from src.core.config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)
new_async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_session() -> AsyncSession:
    async with new_async_session() as session:
        yield session
