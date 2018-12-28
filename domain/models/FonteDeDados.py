from app import db

class FonteDeDados(db.Model):
    __tablename__ = "fontesdedados"

    id       = db.Column(db.Integer, primary_key=True)
    nome     = db.Column(db.String)
    endereco = db.Column(db.String)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


    def __repr__(self):
        return "<FonteDeDados %r>" % self.nome
