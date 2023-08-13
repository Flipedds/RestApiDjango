# Iniciando com Django e Django-ninja
    
    ativar venv
    pip install django
    pip install django-ninja

# Criando Projeto

    django-admin startproject rest_api

# Rodando servidor

    python manage.py runserver -> http://127.0.0.1:8000/


# Usando django-ninja

    -> urls.py
    from ninja import NinjaAPI

    api = NinjaAPI()
    @api.get('livro/')
    def livro(request):
        return {'msg': 'Livros'}

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
    ]

# Acessando documentação

    api/docs

![Alt text](img/image-1.png)





