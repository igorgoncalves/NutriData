from server.domain.models.Amostra import AmostraSchema
from server.domain.models.Indicador import Indicador, IndicadorSchema
from server.domain.repository.IndicadorRepository import IndicadorRepository
from server.domain.service.LocalidadeService import LocalidadeService
from server.domain.service._base import ServiceBase
from server.domain.service.helpers.NotificationServiceHelper import NotificationServiceHelper


class IndicadorService(ServiceBase):

    repository = IndicadorRepository()
    schema = IndicadorSchema()
    schema_amostras = AmostraSchema()
    notify = NotificationServiceHelper()

    _errors = {'validacao_amostra': []}

    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository, schema=self.schema)

    def create(self, indicador):
        amostras = []                
        self._errors = {'validacao_amostra': []}
        for amostra in indicador['amostras']:
            localidade = LocalidadeService().get_all(posicao=amostra['posicao_localidade_arquivo'])
            codigo_localidade = None

            if len(localidade) > 0:
                codigo_localidade = int(localidade[0].codigo)            
            amostra['codigo_localidade'] = codigo_localidade

            res = self.schema_amostras.load(amostra)
            
            if not res.errors == {}:
                if not str(amostra['valor']).isdigit():
                    res.errors['valor'] = "Ops! Os valores não podem conter letras ou simbolos como '.',  '?'" \
                                          ", \", apenas números"

                elif '=' in str(amostra['valor']):
                    res.errors['valor'] = "Ops! Nada de formulas, apenas números aqui. Você pode usar a ferramenta " \
                                          "de 'colar especial' ou remover a coluna"
                
                else:
                    res.errors['valor'] = "Ops! Algo estranho aconteceu"

                res.errors['indicador'] = indicador['nome']
                res.errors['posicao'] = amostra['coordenada_planilha']

                self._errors['validacao_amostra'].append(res.errors)

            amostras.append(res.data)                            
            
        novo_indicador = Indicador(nome=indicador['nome'], amostras=amostras)
        return novo_indicador, self._errors

    def load_partial(self, indicador):
        return self.schema.load(indicador, partial=('id', 'indicador'))
    

