from domain.service._base import ServiceBase
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador, IndicadorSchema


class IndicadorService(ServiceBase):
    repository = IndicadorRepository()
    schema = IndicadorSchema()
    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository)
    
    def create(self, nome, objetivo):
        novo_indicador = Indicador(nome=nome, objetivo=objetivo)
        return super().create(novo_indicador)

    def dumps(self, indicador, many=False):
        indicadorJson = self.schema.dumps(indicador, many=many)
        return indicadorJson