from ninja import NinjaAPI
from django.core import serializers
from ninja.security import HttpBearer
from api.models import Livro
from api.schemas import LivroSchema
import jwt
from datetime import datetime, timedelta


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

api = NinjaAPI(auth=GlobalAuth(), title="RestApi", description="A rest api with django-ninja")

@api.get('auth', auth=None)
def Jwt(request):
    token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=2)
    }, key='1234', algorithm="HS256")
    return {"token": token}

@api.get('livro/')
def livro(request):
    livros = Livro.objects.all()
    json_data = serializers.serialize('json', livros)
    return {"livros": json_data}

@api.post('/livro/create', response=LivroSchema)
def create_livro(request, livro: LivroSchema):
    dict = livro.dict()
    novo_livro = Livro(**dict)
    novo_livro.save()
    return livro