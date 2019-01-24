from domain.Database import *

class Indicador(Base):
    __tablename__ = "indicadores"

    id            = Column(Integer, primary_key=True)
    nome          = Column(String)
    objetivo      = Column(Text)
    periodicidade = Column(Integer)

    def __init__(self, nome, objetivo, periodicidade):
        self.nome = nome
        self.objetivo = objetivo
        self.periodicidade = periodicidade

    
    def __repr__(self):
        return "<Indicador %r>" % self.nome
