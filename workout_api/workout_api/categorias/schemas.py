from workout_api.contrib.schemas import BaseSchemas
from typing import Annotated
from pydantic import UUID4, Field

class Categoria(BaseSchemas):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]

class CategoriaIn(Categoria):
    pass

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]