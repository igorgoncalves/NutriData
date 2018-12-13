from app.domain.service._base import ServiceBase
from app.domain.repository.IndicadorRepository import IndicadorRepository

from injector import inject

class IndicadorService(ServiceBase):
    @inject
    def __init__(self, indicadorRepository=IndicadorRepository):
        # super(IndicadorService, self).__init__(repository=indicadorRepository)
        self.repository = indicadorRepository
        print(self.repository)
