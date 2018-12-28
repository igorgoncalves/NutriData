# from models import Indicador
from app.domain.repository._base import RepositoryBase
from app.models.Indicador import Indicador

class IndicadorRepository(RepositoryBase):    
    def __init__(self):
        super(IndicadorRepository, self).__init__(item=Indicador)