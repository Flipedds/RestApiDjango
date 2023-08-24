from ninja import ModelSchema
from api.models import Livro

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = ['titulo', 'autor', 'editora']


class AllBooks(ModelSchema):
    class Config:
        model = Livro
        model_fields = ['id','titulo', 'autor', 'editora']