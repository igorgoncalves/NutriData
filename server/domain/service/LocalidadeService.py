from domain.service._base import ServiceBase
from domain.repository.LocalidadeRepository import LocalidadeRepository
from domain.models.Localidade import Localidade, LocalidadeSchema

class LocalidadeService(ServiceBase):

    repository = LocalidadeRepository()
    schema = LocalidadeSchema()

    def __init__(self):
        super(LocalidadeService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, codigo, nome, macroindicadores=[]):
        new_localidade = Localidade(codigo=nome, nome=objetivo, macroindicadores=macroindicadores)
        return self.create(item=new_localidade)