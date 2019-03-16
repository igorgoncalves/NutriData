from mongoengine import *
from marshmallow import Schema, fields


class Indicador(Document):

    nome          = StringField(required=True, max_length=200)
    fonte      = StringField(required=True)   #alterar
    anoValor = StringField(required=True)   #alterar

    def __init__(self, nome, objetivo, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.nome = nome
        self.objetivo = objetivo

    def __repr__(self):
        return '<User(name={self.nome!r})>'.format(self=self)


class ValoresIndicadoresSchema(Schema):
    cidade = fields.String()
    valor = fields.Decimal()


class IndicadorSchema(Schema):
    indicador     = fields.String()
    fonte = fields.String()
    unidade = fields.String()
    valores = fields.Nested('ValoresIndicadoresSchema', many = True)
    # subindicadores = fields.Nested('self', exclude=('subIndicadores',), default=None)




