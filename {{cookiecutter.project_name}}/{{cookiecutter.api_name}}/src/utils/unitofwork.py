from abc import ABC, abstractmethod
from typing import Type

from src.db.postgres import get_async_session

# from src.repositories.bot import BotRepository


class IUnitOfWork(ABC):
    # тут требуется подключть для типизации свои репозитории bots: Type[BotRepository]

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = get_async_session

    async def __aenter__(self):
        self.session = self.session_factory()

        # тут требуется инициализировать для типизации свои репозитории self.bots = BotRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
