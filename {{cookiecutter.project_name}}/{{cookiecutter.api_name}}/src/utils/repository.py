from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def find_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def find_filter(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(query)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_all(self):
        query = select(self.model)
        res = await self.session.execute(query)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(query)
        res = res.scalar_one().to_read_model()
        return res

    async def update_one(self, _id: int, data: dict):
        stmt = (
            update(self.model)
            .where(self.model.id == _id)
            .values(**data)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
