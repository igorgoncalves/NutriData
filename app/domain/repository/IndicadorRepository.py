# from models import Indicador
from app.domain.repository._base import RepositoryBase
from injector import inject

class IndicadorRepository(RepositoryBase):
    def __init__(self, db, item):
        super(IndicadorRepository, self).__init__(db=db, item=item)
