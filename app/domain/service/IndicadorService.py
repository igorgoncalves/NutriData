from app.domain.service._base import ServiceBase
from app.domain.repository.IndicadorRepository import IndicadorRepository

from app.models.Indicador import Indicador

class IndicadorService(ServiceBase):
    repository = IndicadorRepository()
    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository)
    
    def create(self, nome, objetivo, periodicidade):
        novo_indicador = Indicador(nome=nome, objetivo=objetivo, periodicidade=periodicidade)
        return super().create(novo_indicador)