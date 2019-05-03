from domain.service._base import ServiceBase
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador, IndicadorSchema
from domain.service.LocalidadeService import LocalidadeService
from domain.models.Amostra import Amostra

class IndicadorService(ServiceBase):
    repository = IndicadorRepository()
    schema = IndicadorSchema()
    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(indicador):
        amostras = []
        for amst in indicador['amostras']:
            codigo_localidade = LocalidadeService().get_all(posicao=amst['codigo_localidade'])
            if len(codigo_localidade) > 0:
                codigo_localidade = int(codigo_localidade[0].codigo)
            else:
                codigo_localidade = None
            amostras.append(Amostra(ano=amst['ano'], valor=amst['valor'], codigo_localidade=codigo_localidade))
        novo_indicador = Indicador(nome=indicador['nome'] , amostras=amostras)
        return novo_indicador

    def loadPartial(self, indicador):
        return self.schema.load(indicador, partial=('id', 'indicador'))

            #validate entrada
    def validate(self, indicador_dict):
        try:
            result = self.schema.load(macroindicador_dict)
            return indicador_dict, True
        except ValidationError as err:
            error = err.messages 
            valid_data = err.valid_data 
            return json.dumps(error, indent=2), False

