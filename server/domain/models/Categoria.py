from marshmallow_mongoengine import ModelSchema
from mongoengine import Document, StringField


class Categoria(Document):
    nome = StringField(required=True, max_length=200)
    def __repr__(self):
        return '''<Categoria(nome={self.nome!r})>'''.format(self=self)

class CategoriaSchema(ModelSchema):
    class Meta:
        model = Categoria
    
