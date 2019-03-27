from mongoengine import *
from marshmallow_mongoengine import ModelSchema

class Visao(Document):
    pass
class VisaoSchema(ModelSchema):
    class Meta:
        model = Visao


