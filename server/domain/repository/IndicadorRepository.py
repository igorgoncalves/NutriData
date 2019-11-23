from domain.models.Indicador import Indicador
from domain.repository._base import RepositoryBase


class IndicadorRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(IndicadorRepository, self).__init__(model_class=Indicador)