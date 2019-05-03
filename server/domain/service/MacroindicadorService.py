from domain.service._base import ServiceBase
from domain.service.IndicadorService import IndicadorService
from domain.service.LocalidadeService import LocalidadeService
from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador, MacroindicadorSchema
from domain.models.Indicador import Indicador

from marshmallow import ValidationError

import json


class MacroindicadorService(ServiceBase):
    repository = MacroindicadorRepository()
    schema = MacroindicadorSchema()
    def __init__(self):
        super(MacroindicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, macroindicador):
        service_localidade = LocalidadeService()
        indicadores_dict = macroindicador['indicadores']
        indicadores = []
        for indicador in indicadores_dict:
            indicador_obj = IndicadorService.create(indicador)            
            indicadores.append(indicador_obj)

        novo_macroindicador = Macroindicador(
                                             nome=macroindicador['nome'],
                                             descricao=macroindicador['descricao'],
                                             fonte=macroindicador['fonte'],
                                             unidade=macroindicador['unidade'],
                                             localidade= [service_localidade.get_all(posicao = x)[0] for x in macroindicador['locais_id']],
                                             indicadores=indicadores)
        return super().create(novo_macroindicador)

        #validate entrada
    def validate(self, macroindicador_dict):
        try:
            result = self.schema.load(macroindicador_dict)
            return macroindicador_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False
    def get_by_localidade(self, codigo_localidade):
        service_localidade = LocalidadeService()
        localidade = service_localidade.get_all(codigo=codigo_localidade)
        if len(localidade) > 0:
            return self.repository.get_by_localidade(localidade[0].id)
        return []