from domain.Database import *

class FonteDeDados(Base):
    __tablename__ = "fontesdedados"

    id       = Column(Integer, primary_key=True)
    nome     = Column(String)
    endereco = Column(String)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


    def __repr__(self):
        return "<FonteDeDados %r>" % self.nome
