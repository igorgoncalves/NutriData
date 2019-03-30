from domain.service._base import ServiceBase
from domain.repository.VisaoRepository import VisaoRepository
from domain.models.Visao import Visao, VisaoSchema

class VisaoService(ServiceBase):

    repository = VisaoRepository()
    schema = VisaoSchema()

    def __init__(self):
        super(VisaoService, self).__init__(repository=self.repository, schema=self.schema)