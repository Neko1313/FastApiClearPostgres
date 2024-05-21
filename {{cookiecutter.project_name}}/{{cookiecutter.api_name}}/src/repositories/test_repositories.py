from src.models.test_model import Test
from src.utils.repository import SQLAlchemyRepository


class TestRepository(SQLAlchemyRepository):
    model = Test