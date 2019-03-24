from domain.service._base import ServiceBase
from domain.repository.LocalidadeRepository import LocalidadeRepository
from domain.models.Localidade import Localidade, LocalidadeSchema
from marshmallow import ValidationError
import json


class LocalidadeService(ServiceBase):

    repository = LocalidadeRepository()
    schema = LocalidadeSchema()

    def __init__(self):
        super(LocalidadeService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, codigo, nome, macroindicadores=[]):
        new_localidade = Localidade(codigo=codigo, nome=nome, macroindicadores=macroindicadores)
        return super().create(new_localidade)

    def serializerMacroindicador(self, macroindicador):
        macroindicadorSerialized = self.schema.dump(macroindicador)
        return macroindicadorSerialized

    def get_all(self, **kwargs):
        return super().get_all(**kwargs)

    def validate(self, localidade_dict):
        try:
            result = self.schema.load(localidade_dict)
            return localidade_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False

    def serialize(self, list, many=False):
        return self.schema.dump(list, many)