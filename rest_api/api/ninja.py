from api.schemas import LivroSchema
from api.controllers import Controllers
from api.api_settings import api
from typing import List

@api.get('auth/', auth=None, tags=["Get"])
def Jwt(request):
    token = Controllers.create_token_jwt()
    return {"token": token}

@api.get('livros/', response=List[LivroSchema], tags=["Get"])
def livros(request):
    json_data = Controllers.get_all_books()
    return json_data

@api.post('/livro/create/', response=LivroSchema, tags=['Post'])
def create_livro(request, livro: LivroSchema):
    dict = Controllers.create_new_book(livro=livro)
    return dict

@api.delete('/livro/delete/{id}/', tags=["Delete"])
def delete_livro(request, id: int):
    result = Controllers.delete_book(id=id)

    return result
