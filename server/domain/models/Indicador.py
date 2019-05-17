from mongoengine import EmbeddedDocument, StringField, ListField, ReferenceField, EmbeddedDocumentField
from marshmallow_mongoengine import ModelSchema, fields
from .Amostra import Amostra, AmostraSchema

class Indicador(EmbeddedDocument):

    nome               = StringField(required=True, max_length=200)
    amostras           = ListField(EmbeddedDocumentField("Amostra"))
    indicadores_filhos = ListField(ReferenceField("Indicador"))

    def __repr__(self):
        return '<Indicador(nome={self.nome!r})>'.format(self=self)

class IndicadorSchema(ModelSchema):
    amostras = fields.Nested(AmostraSchema, many=True)
    class Meta:
        model = Indicador




