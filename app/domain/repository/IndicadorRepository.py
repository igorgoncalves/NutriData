# from models import Indicador
from app.domain.repository import _base

class IndicadorRepository(_base.RepositoryBase):
    def __init__(self, db):
        _base.RepositoryBase.__init__(self, db);
        self.db = db
