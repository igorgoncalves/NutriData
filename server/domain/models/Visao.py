from marshmallow_mongoengine import ModelSchema
from mongoengine import StringField, ListField, Document, EmbeddedDocumentField

from .Indicador import Indicador


class Visao(Document):
    tipo_do_grafico = StringField(required=True)
    indicadores = ListField(EmbeddedDocumentField(Indicador))

class VisaoSchema(ModelSchema):
    class Meta:
        model = Visao


