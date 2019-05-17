from domain.service._base import ServiceBase
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.IndicadorService import IndicadorService

from domain.repository.VisaoRepository import VisaoRepository
from domain.models.Visao import Visao, VisaoSchema
from domain.models.Indicador import Indicador

class VisaoService(ServiceBase):

    repository = VisaoRepository()
    schema = VisaoSchema()

    def __init__(self):
        super(VisaoService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, id_macroindicador, tipo_de_grafico, indicadores):
        service_indicador = IndicadorService()
        service_macroindicaor = MacroindicadorService()
        new_visao = Visao()
        new_visao.tipo_do_grafico = tipo_de_grafico
        new_visao.indicadores = [service_indicador.deserialize(indicador) for indicador in indicadores]
        visao_salva = super().create(new_visao)
        # atualizar macroindicador
        macroindicador = service_macroindicaor.get_by_id(id_macroindicador)
        macroindicador.update(visao=visao_salva)
        return visao_salva

