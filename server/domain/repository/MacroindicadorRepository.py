from domain.models.Macroindicador import Macroindicador
from domain.repository._base import RepositoryBase


class MacroindicadorRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(MacroindicadorRepository, self).__init__(model_class=Macroindicador)

    def get_by_localidade(self, id_localidade):
        return Macroindicador.objects.filter(localidade__contains=id_localidade)
    
    def get_one_by_localidade(self, codigo_localidade, id_macroindicador):
        return Macroindicador.objects.filter(indicadores__amostras__codigo_localidade=codigo_localidade, id=id_macroindicador)

    def get_by_id(self, pk):
        partial = Macroindicador.objects.with_id(object_id=pk)
        if partial:
            partial = partial.select_related()
        return partial


