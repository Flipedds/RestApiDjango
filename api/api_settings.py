from ninja import NinjaAPI
from ninja.security import HttpBearer
from rest_api.settings import SECRET_KEY
from datetime import datetime, timezone
import jwt

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

api = NinjaAPI(auth=GlobalAuth(), title="The book is on Api", description="A book rest api with django-ninja")

@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(request, {"msg": "Token inválido ou expirado"}, status=401)