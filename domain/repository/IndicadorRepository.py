# from models import Indicador
from domain.repository._base import RepositoryBase
from domain.models.Indicador import Indicador

class IndicadorRepository(RepositoryBase):    
    def __init__(self):
        super(IndicadorRepository, self).__init__(item=Indicador)