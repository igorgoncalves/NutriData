import json

from domain.models.Categoria import Categoria, CategoriaSchema
from domain.repository.CategoriaRepository import CategoriaRepository
from domain.service._base import ServiceBase
from marshmallow import ValidationError


class CategoriaService(ServiceBase):

    repository = CategoriaRepository()
    schema = CategoriaSchema()

    def __init__(self):
        super(CategoriaService, self).__init__(
            repository=self.repository, schema=self.schema)

    def create(self, item):        
        return super().create(item)

    def validate(self, item):
        try:
            categoria = self.deserialize(item)
            return categoria, True
        except ValidationError as err:
            error = err.messages
            return json.dumps(error, indent=2), False
