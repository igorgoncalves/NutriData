from mongoengine import *
from marshmallow_mongoengine import ModelSchema, fields
from .Indicador import Indicador
from .Localidade import Localidade
from .Visao import Visao

class Macroindicador(Document):
    # id          = StringField(required=True, max_length=200)
    nome        = StringField(required=True, max_length=200)
    descricao   = StringField(required=True)
    localidade  = ListField(ReferenceField(Localidade))
    visao       = ReferenceField(Visao)
    indicadores = ListField(EmbeddedDocumentField(Indicador))

    def __repr__(self):
        return '<Macroindicador(name={self.nome!r})>'.format(self=self)



class MacroindicadorSchema(ModelSchema):
    class Meta:
        model = Macroindicador

