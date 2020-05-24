from domain.models.Categoria import Categoria
from domain.repository._base import RepositoryBase


class CategoriaRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(CategoriaRepository, self).__init__(model_class=Categoria)