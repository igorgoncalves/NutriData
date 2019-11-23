from domain.models.Visao import Visao, VisaoSchema
from domain.repository.VisaoRepository import VisaoRepository
from domain.service.IndicadorService import IndicadorService
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service._base import ServiceBase


class VisaoService(ServiceBase):
    
    schema = VisaoSchema()    

    def __init__(self, service_indicador=IndicadorService(), service_macroindicador = MacroindicadorService(), repository = VisaoRepository()):
        self.repository = repository
        self.service_indicador = service_indicador
        self.service_macroindicador = service_macroindicador

        super(VisaoService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, id_macroindicador, tipo_de_grafico, indicadores):
        
        new_visao = Visao()
        new_visao.tipo_do_grafico = tipo_de_grafico
        new_visao.indicadores = [self.service_indicador.deserialize(indicador) for indicador in indicadores]
        visao_salva = super().create(new_visao)
        # atualizar macroindicador
        macroindicador = self.service_macroindicador.get_by_id(id_macroindicador)
        macroindicador.update(visao=visao_salva)
        return visao_salva


