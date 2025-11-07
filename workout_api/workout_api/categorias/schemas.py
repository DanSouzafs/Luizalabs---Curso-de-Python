from typing import Annotated
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchemas):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]