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

    def dumps(self, macroindicador, many=False):
        macroindicadorJson = self.schema.dumps(macroindicador, many=many)
        return macroindicadorJson

    def serializerMacroindicador(self, indicadores, macroindicador):
        macroindicadorObj = self.schema(macroindicador['nome'], macroindicador['descricao'])
        for indicador in indicadores:
            macroindicadorObj.indicadores.append(indicador)
        macroindicador_result = self.schema.dump(macroindicadorObj)
        return macroindicadorObj

    def get_all(self):
        return self.repository.get_all()

    def serialize(self, list, many=False):
        return self.schema.dump(list, many)

        #validate entrada
    def validate(self, macroindicador_dict):
        try:
            result = self.schema.load(macroindicador_dict)
            return macroindicador_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False
