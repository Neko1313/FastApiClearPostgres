from typing import Optional, List
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class DtoTestBase(BaseModel):
    name_1: Annotated[str, Field(min_length=3)]
    name_2: Optional[Annotated[str, Field(min_length=3)]]
    list_name: List[str]


class DtoTestAdd(DtoTestBase):
    pass


class DtoTestUpdate(DtoTestBase):
    pass


class DtoTest(DtoTestBase):
    id: int
