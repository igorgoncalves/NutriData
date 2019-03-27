from domain.service._base import ServiceBase
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador, IndicadorSchema


class IndicadorService(ServiceBase):
    repository = IndicadorRepository()
    schema = IndicadorSchema()
    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, nome, amostras):
        novo_indicador = Indicador(nome=nome, amostras=amostras)
        return super().create(novo_indicador)

    def loadPartial(self, indicador):
        return self.schema.load(indicador, partial=('id', 'indicador'))

    