from typing import AsyncGenerator, Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base, sessionmaker

from src.config import settings


# engine = create_engine(url=settings.DATABASE_URL_psycopg)
# session_maker = sessionmaker(engine, expire_on_commit=False)

async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

Base: DeclarativeBase = declarative_base()


# def get_session() -> Generator[Session, None]:
#     with session_maker() as session:
#         yield session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session