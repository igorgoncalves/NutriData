from domain.repository._base import RepositoryBase
from domain.models.Macroindicador import Macroindicador

class MacroindicadorRepository(RepositoryBase):    
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(MacroindicadorRepository, self).__init__(model_class=Macroindicador)