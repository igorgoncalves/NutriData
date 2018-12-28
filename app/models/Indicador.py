from app import db

class Indicador(db.Model):
    __tablename__ = "indicadores"

    id            = db.Column(db.Integer, primary_key=True)
    nome          = db.Column(db.String)
    objetivo      = db.Column(db.Text)
    periodicidade = db.Column(db.Integer)

    def __init__(self, nome, objetivo, periodicidade):
        self.nome = nome
        self.objetivo = objetivo
        self.periodicidade = periodicidade

    
    def __repr__(self):
        return "<Indicador %r>" % self.nome
