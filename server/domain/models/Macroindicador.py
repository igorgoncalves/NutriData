import marshmallow_mongoengine as ma
from mongoengine import *

from .Indicador import Indicador, IndicadorSchema
from .Localidade import Localidade
from .Visao import Visao


class Macroindicador(Document):
    # id          = StringField(required=True, max_length=200)
    nome        = StringField(required=True, max_length=200)
    descricao   = StringField(required=True)
    fonte       = StringField(required=True, max_length=200)
    unidade     = StringField(required=True, max_length=200)
    localidade  = ListField(ReferenceField(Localidade))
    visao       = ReferenceField(Visao)
    indicadores = ListField(EmbeddedDocumentField(Indicador))

    def __repr__(self):
        return '<Macroindicador(name={self.nome!r})>'.format(self=self)



class MacroindicadorSchema(ma.ModelSchema):
    indicadores = ma.fields.Nested(IndicadorSchema, many=True)
    class Meta:
        model = Macroindicador
    # visao = ma.fields.Method(serialize="_visao_serializer", deserialize="_visao_deserializer")
    # def _visao_serializer(self, obj):
    #     print(obj)
    #     return Visao.dumps(.objects.with_id(object_id=id))
    # def _visao_serializer(self, obj):
    #     return Visao.load(obj)