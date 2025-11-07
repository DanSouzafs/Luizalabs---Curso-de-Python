from typing import Annotated
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Monster', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua A, BCD ', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario do centro de treinamento', example='Marquinhos', max_length=30)]