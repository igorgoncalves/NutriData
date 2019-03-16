from mongoengine import *
from marshmallow import Schema, fields
from . import Indicador as indicador

class Macroindicador(Document):

    nome          = StringField(required=True, max_length=200)
    descricao      = StringField(required=True)   
    #indicadores 

    def __init__(self, nome, objetivo, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return '<User(name={self.nome!r})>'.format(self=self)



class MacroindicadorSchema(Schema):
    nome     = fields.String()
    descricao = fields.String()
    indicadores = fields.Nested('indicador.IndicadorSchema',many=True )


