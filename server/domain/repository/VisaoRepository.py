from domain.repository._base import RepositoryBase
from domain.models.Visao import Visao

class VisaoRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(VisaoRepository, self).__init__(model_class=Visao)