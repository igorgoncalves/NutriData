from mongoengine import *
from marshmallow import Schema, fields


class Indicador(Document):

    nome          = StringField(required=True, max_length=200)
    objetivo      = StringField(required=True)   

    def __init__(self, nome, objetivo, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.nome = nome
        self.objetivo = objetivo

    def __repr__(self):
        return '<User(name={self.nome!r})>'.format(self=self)



class IndicadorSchema(Schema):
    nome     = fields.String()
    objetivo = fields.Email()


