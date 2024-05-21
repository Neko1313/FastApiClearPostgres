from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

from conf import SQLALCHEMY_ASYNC_DATABASE_URL

engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


@asynccontextmanager
async def get_async_session():
    async with async_session_maker() as session:
        yield session
