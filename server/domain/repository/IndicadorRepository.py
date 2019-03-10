from domain.repository._base import RepositoryBase
from domain.models.Indicador import Indicador

class IndicadorRepository(RepositoryBase):    
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(IndicadorRepository, self).__init__(model_class=Indicador)