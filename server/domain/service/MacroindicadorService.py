from domain.service._base import ServiceBase
from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador, MacroindicadorSchema
from marshmallow import ValidationError
import json


class MacroindicadorService(ServiceBase):
    repository = MacroindicadorRepository()
    schema = MacroindicadorSchema()
    def __init__(self):
        super(MacroindicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self,id, nome, descricao, indicadores):
        novo_macroindicador = Macroindicador(id=id, nome=nome, descricao=descricao, indicadores=indicadores)
        return novo_macroindicador

        #validate entrada
    def validate(self, macroindicador_dict):
        try:
            result = self.schema.load(macroindicador_dict)
            return macroindicador_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False
