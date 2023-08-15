from ninja import NinjaAPI
from django.core import serializers
from ninja.security import HttpBearer
from api.models import Livro
from api.schemas import LivroSchema
import jwt
from datetime import datetime, timezone
from api.controllers import Controllers
from rest_api.settings import SECRET_KEY

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            expiration = payload['exp']
            current_time = datetime.now(timezone.utc).timestamp()

            if expiration > current_time:
                return token
            else:
                print("Token antigo.")
                return None
            
        except jwt.ExpiredSignatureError:
            raise InvalidToken
        except jwt.DecodeError:
            raise InvalidToken

class InvalidToken(Exception):
    pass

api = NinjaAPI(auth=GlobalAuth(), title="RestApi", description="A rest api with django-ninja")

@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(request, {"msg": "Token inválido ou expirado"}, status=401)


@api.get('auth', auth=None)
def Jwt(request):
    token = Controllers.create_token_jwt()
    return {"token": token}

@api.get('livro/')
def livro(request):
    json_data = Controllers.get_all_books()
    return {"livros": json_data}

@api.post('/livro/create', response=LivroSchema)
def create_livro(request, livro: LivroSchema):
    dict = Controllers.create_new_book(livro=livro)
    return dict