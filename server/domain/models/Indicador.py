from mongoengine import *
from marshmallow_mongoengine import ModelSchema
from .Amostra import Amostra

class Indicador(EmbeddedDocument):

    nome     = StringField(required=True, max_length=200)
    amostras = ListField(EmbeddedDocumentField(Amostra))

    def __repr__(self):
        return '<Indicador(nome={self.nome!r})>'.format(self=self)

class IndicadorSchema(ModelSchema):
     class Meta:
        model = Indicador




