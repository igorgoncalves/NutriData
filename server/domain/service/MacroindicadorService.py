from domain.service._base import ServiceBase
from domain.service.IndicadorService import IndicadorService
from domain.service.LocalidadeService import LocalidadeService
from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador, MacroindicadorSchema


import json

from marshmallow import ValidationError


class MacroindicadorService(ServiceBase):
    
    schema = MacroindicadorSchema()
    _service_localidade = LocalidadeService()
    _service_indicador = IndicadorService()
    _errors = []

    def __init__(self, repository=MacroindicadorRepository()):
        self.repository = repository
        super(MacroindicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, macroindicador):

        indicadores_dict = macroindicador['indicadores']
        self._errors = []
        indicadores = []
        for indicador in indicadores_dict:
            indicador_obj, err = self._service_indicador.create(indicador)
            indicadores.append(indicador_obj)
            
            self._errors = self._errors + err['validacao_amostra']
        
        if len(self._errors) > 0:
            return {}, self._errors

        novo_macroindicador = Macroindicador(
                                             nome=macroindicador['nome'],
                                             descricao=macroindicador['descricao'],
                                             fonte=macroindicador['fonte'],
                                             unidade=macroindicador['unidade'],
                                             localidade=[self._service_localidade.get_all(posicao=x)[0]
                                                         for x in macroindicador['locais_id']],
                                             indicadores=indicadores)
        
        return super().create(novo_macroindicador), self._errors

    # validate entrada
    def validate(self, macroindicador_dict):
        
        try:
            macroindicador = self.deserialize(macroindicador_dict)
            return macroindicador_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False

    def get_by_localidade(self, codigo_localidade, service_localidade=LocalidadeService()):
        # service_localidade = LocalidadeService()
        localidade = service_localidade.get_all(codigo=codigo_localidade)
        if len(localidade) > 0:
            return self.repository.get_by_localidade(localidade[0].id)
        return []

    def get_one_by_localidade(self, codigo_localidade, id_macroindicador):                        
        return self.repository.get_one_by_localidade(codigo_localidade, id_macroindicador)
        