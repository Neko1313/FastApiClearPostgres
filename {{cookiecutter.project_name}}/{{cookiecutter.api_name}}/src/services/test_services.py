from typing import List
from pydantic import BaseModel

from src.utils.unitofwork import IUnitOfWork


class TestService:
    async def add(self, uow: IUnitOfWork, test_schama: BaseModel) -> BaseModel:
        test_dict = test_schama.model_dump()

        async with uow:
            test = await uow.clients.add_one(test_dict)
            await uow.commit()

        return test

    async def update(
        self, uow: IUnitOfWork, test_id: int, test: BaseModel
    ) -> BaseModel:
        async with uow:
            test_dict = {
                key: value
                for key, value in test.model_dump().items()
                if value is not None
            }

            test_info: BaseModel = await uow.clients.update_one(
                _id=test_id,
                data=test_dict,
            )

            await uow.commit()

        return test_info

    async def get_all(self, uow: IUnitOfWork) -> List[BaseModel]:
        async with uow:
            return await uow.clients.find_all()
