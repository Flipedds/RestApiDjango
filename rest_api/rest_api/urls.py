from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from ninja.security import HttpBearer
from api.models import Livro
from api.schemas import LivroSchema
from django.core import serializers

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

api = NinjaAPI(auth=GlobalAuth())

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
