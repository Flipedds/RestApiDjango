from api.schemas import LivroSchema
from api.controllers import Controllers
from api.api_settings import api

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

@api.delete('/livro/delete/{id}')
def delete_livro(request, id: int):
    result = Controllers.delete_book(id=id)

    return {"msg": "deletado com sucesso!"}
