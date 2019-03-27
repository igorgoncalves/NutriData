from mongoengine import *
from marshmallow_mongoengine import ModelSchema

class Visao(Document):


    # def __repr__(self):
    #     return '<Amostra(ano={self.ano!r}, valor={self.valor!r})>'.format(self=self)

class VisaoSchema(ModelSchema):
    class Meta:
        model = Amostra


