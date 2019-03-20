from mongoengine import *
from marshmallow_mongoengine import ModelSchema
from .Macroindicador import Macroindicador

class Localidade(Document):

    codigo           = IntField(required=True)
    nome             = StringField(required=True, max_length=200)
    macroindicadores = ListField(EmbeddedDocumentField(Macroindicador))

    def __repr__(self):
        return '''<Localidade(
                    codigo={self.codigo!r},
                    nome={self.nome!r})>'''.format(self=self)

class LocalidadeSchema(ModelSchema):
    class Meta:
        model = Localidade