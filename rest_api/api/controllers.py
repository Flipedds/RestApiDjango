from datetime import datetime, timedelta
import jwt
from api.models import Livro
from rest_api.settings import SECRET_KEY

class Controllers:
    def create_token_jwt():
        token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=2)
    }, key=SECRET_KEY, algorithm="HS256")
        return token
    
    def get_all_books():
        livros = Livro.objects.all()
        return livros
    
    def create_new_book(livro):
        dict = livro.dict()
        novo_livro = Livro(**dict)
        novo_livro.save()
        return dict
    
    def delete_book(id):
        try:
            book = Livro.objects.get(pk=id)
        except Exception as err:
            return {"msg": "Livro não encontrado / não foi possível deletar!"}
            
        book.delete()
        return {"msg": "Livro deletado"}
    
    def update_book(id, livro):
        dict = livro.dict()
        print(dict['titulo'])
        try:
            book = Livro.objects.get(pk=id)
        except Exception as err:
            return {"msg": "Livro não encontrado / não foi possível Atualizar!"}
        book.titulo = dict['titulo']
        book.autor = dict['autor']
        book.editora = dict['editora']
        book.save()
        return {"msg": "Livro atualizado com sucesso !"}
    