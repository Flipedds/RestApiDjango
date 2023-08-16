from api.schemas import LivroSchema
from api.controllers import Controllers
from api.api_settings import api
from typing import List

@api.get('auth/', auth=None, tags=["Get"], description="Receba um token jwt para acessar as funcionalidades da api")
def Jwt(request):
    token = Controllers.create_token_jwt()
    return {"token": token}

@api.get('livros/', response=List[LivroSchema], tags=["Get"], description="Retorna um json com todos os livros cadastrados")
def livros(request):
    json_data = Controllers.get_all_books()
    return json_data

@api.post('/livro/create/', response=LivroSchema, tags=['Post'], description="Cria um novo livro no banco de dados")
def create_livro(request, livro: LivroSchema):
    dict = Controllers.create_new_book(livro=livro)
    return dict

@api.delete('/livro/delete/{id}/', tags=["Delete"], description="Apaga um livro pré-existente no banco de dados")
def delete_livro(request, id: int):
    result = Controllers.delete_book(id=id)

    return result
