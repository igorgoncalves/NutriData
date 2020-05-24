import json

from marshmallow import ValidationError
from webapp.modules.core.service_base import ServiceBase

from .models import LocalidadeSchema
from .models import Localidade


class LocalidadeService(ServiceBase):

    schema = LocalidadeSchema()

    def __init__(self):
        super(LocalidadeService, self).__init__(
            model_class=Localidade, schema=self.schema)

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
            valid_data = err.data
            return json.dumps(error, indent=2), False
