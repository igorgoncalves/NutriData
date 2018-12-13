from app.domain.service import _base
from app.domain.repository.IndicadorRepository import IndicadorRepository
from injector import inject


class IndicadorService(_base.ServiceBase):
    @inject
    def __init__(self, indicadorRepository=IndicadorRepository):
        self.indicadorRepository = indicadorRepository


    def get_by_id(self, id):
        return self.indicadorRepository.get_by_id(id)
