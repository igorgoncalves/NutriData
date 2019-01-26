from mongoengine import *

class Indicador(Document):

    nome          = StringField(required=True, max_length=200)
    objetivo      = StringField(required=True)    

    def __init__(self, nome, objetivo, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.nome = nome
        self.objetivo = objetivo

    
    def asdict(self):
        return { 'id': str(self.id), 'nome': self.nome, 'objetivo': self.objetivo }
