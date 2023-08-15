from datetime import datetime, timedelta
import jwt
from api.models import Livro
from django.core import serializers

class Controllers:
    def create_token_jwt():
        token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=2)
    }, key='1234', algorithm="HS256")
        return token
    
    def get_all_books():
        livros = Livro.objects.all()
        json_data = serializers.serialize('json', livros)
        return json_data
    
    def create_new_book(livro):
        dict = livro.dict()
        novo_livro = Livro(**dict)
        novo_livro.save()
        return dict