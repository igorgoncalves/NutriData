from domain.service._base import ServiceBase
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador, IndicadorSchema, ValoresIndicadoresSchema


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

    def serializerIndicador(self, indicador):
        # indicador = self.schema(indicador['indicador'], indicador['fonte'], indicador['unidade'])
        # for valor in valores:
        #     indicador.valores.append(ValoresIndicadoresSchema(valor['cidade'], valor['valor']))
        # for subindicador in subindicadores:
        #     indicador.subindicadores.append(self.schema(indicador['indicador'], indicador['fonte'], indicador['unidade']))
        indicador_result = self.schema.dump(indicador)
        return indicador
    
    def loadPartial(self, indicador):
        return self.schema.load(indicador, partial=('id', 'indicador'))

    