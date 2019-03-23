from mongoengine import *
from marshmallow_mongoengine import ModelSchema
from .Indicador import Indicador

class Macroindicador(EmbeddedDocument):
    nome        = StringField(required=True, max_length=200)
    descricao   = StringField(required=True)
    indicadores = ListField(EmbeddedDocumentField(Indicador))

    def __repr__(self):
        return '<User(name={self.nome!r})>'.format(self=self)



class MacroindicadorSchema(ModelSchema):
    class Meta:
        model = Macroindicador


