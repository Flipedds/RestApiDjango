from ninja import ModelSchema
from api.models import Livro

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = "__all__"