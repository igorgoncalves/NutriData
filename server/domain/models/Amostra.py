from mongoengine import *
from marshmallow_mongoengine import ModelSchema

class Amostra(EmbeddedDocument):
    ano    = StringField(required=True, max_length=8)
    valor  = DecimalField(required=True)
    codigo = IntField(required=True)

    def __repr__(self):
        return '<Amostra(ano={self.ano!r}, valor={self.valor!r})>'.format(self=self)

class AmostraSchema(ModelSchema):
    class Meta:
        model = Amostra


