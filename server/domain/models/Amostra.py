from mongoengine import *
from marshmallow_mongoengine import ModelSchema, fields

class Amostra(EmbeddedDocument):
    ano    = StringField(required=True, max_length=8)
    valor  = FloatField(required=True)
    codigo_localidade = IntField(required=True)

    def __repr__(self):
        return '<Amostra(ano={self.ano!r}, valor={self.valor!r}, codigo_localidade={self.codigo_localidade!r}) >'.format(self=self)

class AmostraSchema(ModelSchema):
    class Meta:
        model = Amostra


