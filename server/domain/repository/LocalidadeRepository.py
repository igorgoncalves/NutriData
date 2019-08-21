from server.domain.models.Localidade import Localidade
from server.domain.repository._base import RepositoryBase


class LocalidadeRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(LocalidadeRepository, self).__init__(model_class=Localidade)