from server.domain.models.Visao import Visao, VisaoSchema
from server.domain.repository.VisaoRepository import VisaoRepository
from server.domain.service.IndicadorService import IndicadorService
from server.domain.service.MacroindicadorService import MacroindicadorService
from server.domain.service._base import ServiceBase


class VisaoService(ServiceBase):

    repository = VisaoRepository()
    schema = VisaoSchema()

    def __init__(self):
        super(VisaoService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, id_macroindicador, tipo_de_grafico, indicadores, service_indicador=IndicadorService(), service_macroindicaor = MacroindicadorService()):
        # service_indicador = IndicadorService()
        # service_macroindicaor = MacroindicadorService()
        # new_visao = Visao()
        new_visao.tipo_do_grafico = tipo_de_grafico
        new_visao.indicadores = [service_indicador.deserialize(indicador) for indicador in indicadores]
        visao_salva = super().create(new_visao)
        # atualizar macroindicador
        macroindicador = service_macroindicaor.get_by_id(id_macroindicador)
        macroindicador.update(visao=visao_salva)
        return visao_salva


