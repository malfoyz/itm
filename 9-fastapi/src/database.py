from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base


from src.config import settings


engine = create_async_engine(url=settings.DATABASE_URL_asyncpg)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

Base: DeclarativeBase = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session