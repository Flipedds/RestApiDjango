from ninja import NinjaAPI
from django.core import serializers
from ninja.security import HttpBearer
from api.models import Livro
from api.schemas import LivroSchema
import jwt
from datetime import datetime, timedelta, timezone

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, '1234', algorithms=['HS256'])
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
    return api.create_response(request, {"detail": "Token inválido"}, status=401)


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