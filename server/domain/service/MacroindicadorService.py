from domain.service._base import ServiceBase
from domain.service.IndicadorService import IndicadorService
from domain.service.LocalidadeService import LocalidadeService
from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador, MacroindicadorSchema
from domain.models.Indicador import Indicador
from domain.models.Amostra import Amostra, AmostraSchema



import json

from marshmallow import ValidationError, fields, missing
from mongoengine import ValidationError as MongoValidationError, NotRegistered

class MacroindicadorService(ServiceBase):
    repository = MacroindicadorRepository()    
    schema = MacroindicadorSchema()
    _service_indicador = IndicadorService()
    _errors = []
    def __init__(self):
        super(MacroindicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, macroindicador):
        service_localidade = LocalidadeService()
        indicadores_dict = macroindicador['indicadores']
        self._errors = []
        indicadores = []
        for indicador in indicadores_dict:
            indicador_obj, err = self._service_indicador.create(indicador)
            indicadores.append(indicador_obj)
            
            self._errors = self._errors + err['validacao_amostra']
        
        if (len(self._errors)> 0):
            return ({}, self._errors)

        novo_macroindicador = Macroindicador(
                                             nome=macroindicador['nome'],
                                             descricao=macroindicador['descricao'],
                                             fonte=macroindicador['fonte'],
                                             unidade=macroindicador['unidade'],
                                             localidade= [service_localidade.get_all(posicao=x)[0] for x in macroindicador['locais_id']],
                                             indicadores=indicadores)
        
        return super().create(novo_macroindicador), self._errors

    #validate entrada
    def validate(self, macroindicador_dict):
        
        try:
            macroindicador = self.deserialize(macroindicador_dict)
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