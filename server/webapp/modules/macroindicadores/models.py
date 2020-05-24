from mongoengine import (Document, EmbeddedDocument, EmbeddedDocumentField,
                         FloatField, IntField, ListField, ReferenceField,
                         StringField)

from webapp.modules.localidade.models import Localidade


class Amostra(EmbeddedDocument):
    ano = StringField(required=True, max_length=8)
    valor = FloatField(required=True)
    codigo_localidade = IntField(required=True)

    def __repr__(self):
        return '<Amostra(ano={self.ano!r}, valor={self.valor!r}, codigo_localidade={self.codigo_localidade!r}) >'.format(self=self)


class Indicador(EmbeddedDocument):

    nome = StringField(required=True, max_length=200)
    amostras = ListField(EmbeddedDocumentField("Amostra"))
    indicadores_filhos = ListField(ReferenceField("Indicador"))

    def __repr__(self):
        return '<Indicador(nome={self.nome!r})>'.format(self=self)


class Macroindicador(Document):
    # id          = StringField(required=True, max_length=200)
    nome = StringField(required=True, max_length=200)
    descricao = StringField(required=True)
    fonte = StringField(required=True, max_length=200)
    unidade = StringField(required=True, max_length=200)
    categoria = StringField(required=True, max_length=200)
    localidade = ListField(ReferenceField(Localidade))
    indicadores = ListField(EmbeddedDocumentField(Indicador))

    def __repr__(self):
        return '<Macroindicador(name={self.nome!r})>'.format(self=self)


class Categoria(Document):
    nome = StringField(required=True, max_length=200)

    def __repr__(self):
        return '''<Categoria(nome={self.nome!r})>'''.format(self=self)
