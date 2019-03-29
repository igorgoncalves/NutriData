from domain.service._base import ServiceBase
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

    def create(self,macroindicador):
        indicadores_dict = macroindicador['indicadores']

        novo_macroindicador = Macroindicador(nome=macroindicador['nome'], 
                                             descricao=macroindicador['descricao'],
                                             fonte=macroindicador['fonte'], 
                                             unidade=macroindicador['unidade'], 
                                             indicadores=indicadores)
        return novo_macroindicador

        #validate entrada
    def validate(self, macroindicador_dict):
        try:
            result = self.schema.load(macroindicador_dict)
            return json.dumps(macroindicador_dict), True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False
