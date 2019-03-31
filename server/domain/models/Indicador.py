from mongoengine import *
from marshmallow_mongoengine import ModelSchema
from .Amostra import Amostra

class Indicador(EmbeddedDocument):
    # id                 = StringField(required=True, max_length=200)
    nome               = StringField(required=True, max_length=200)
    # codigo_localidade  = IntField(required=True)
    amostras           = ListField(EmbeddedDocumentField("Amostra"))
    indicadores_filhos = ListField(ReferenceField("Indicador"))

    def __repr__(self):
        return '<Indicador(nome={self.nome!r})>'.format(self=self)

class IndicadorSchema(ModelSchema):
     class Meta:
        model = Indicador




