import json

from server.domain.models.Localidade import Localidade, LocalidadeSchema
from server.domain.repository.LocalidadeRepository import LocalidadeRepository
from server.domain.service._base import ServiceBase
from marshmallow import ValidationError


class LocalidadeService(ServiceBase):

    repository = LocalidadeRepository()
    schema = LocalidadeSchema()

    def __init__(self):
        super(LocalidadeService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, item):
        return super().create(item)

    # def create(self, codigo, nome, posicao):
    #     new_localidade = Localidade(codigo=codigo, nome=nome, posicao=posicao)
    #     return super().create(new_localidade)

    # validate entrada
    def validate(self, item):
        try:
            result = self.schema.load(item)
            return item, True
        except ValidationError as err:
            error = err.messages
            valid_data = err.valid_data
            return json.dumps(error, indent=2), False