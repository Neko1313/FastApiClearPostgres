from __future__ import annotations


from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres import Base
from src.dtos.test_dto import DtoTest


class Test(Base):
    __tablename__ = "tests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_1: Mapped[str] = mapped_column(String)
    name_2: Mapped[str] = mapped_column(String, nullable=True)
    list_name: Mapped[list[str]] = mapped_column(
        ARRAY(String), nullable=True, default=None
    )

    def to_read_model(self) -> DtoTest:
        return DtoTest(
            id=self.id,
            name_1=self.name_1,
            name_2=self.name_2,
            list_name=self.list_name,
        )
