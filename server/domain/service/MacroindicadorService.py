from domain.service._base import ServiceBase
from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador, MacroindicadorSchema


class MacroindicadorService(ServiceBase):
    repository = MacroindicadorRepository()
    schema = MacroindicadorSchema()
    def __init__(self):
        super(MacroindicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, nome, objetivo):
        novo_macroindicador = Macroindicador(nome=nome, descricao=descricao)
        return super().create(novo_indicador)

    def dumps(self, macroindicador, many=False):
        macroindicadorJson = self.schema.dumps(macroindicador, many=many)
        return macroindicadorJson

    def serializerMacroindicador(self, indicadores, macroindicador):
        macroindicadorObj = self.schema(macroindicador['nome'], macroindicador['descricao'])
        for indicador in indicadores:
            macroindicadorObj.indicadores.append(indicador)
        macroindicador_result = self.schema.dump(macroindicadorObj)
        return macroindicadorObj