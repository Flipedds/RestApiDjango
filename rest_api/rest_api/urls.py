from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from ninja.security import HttpBearer

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

api = NinjaAPI(auth=GlobalAuth())

@api.get('livro/')
def livro(request):
    return {'msg': 'Livros'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
