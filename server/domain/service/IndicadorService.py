from domain.service._base import ServiceBase
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador, IndicadorSchema


class IndicadorService(ServiceBase):
    repository = IndicadorRepository()
    schema = IndicadorSchema()
    def __init__(self):    
        super(IndicadorService, self).__init__(repository=self.repository, schema=self.schema)
    
    def create(self, nome, amostras):
        novo_indicador = Indicador(nome=nome, amostras=amostras)
        return super().create(novo_indicador)

    def dumps(self, indicador, many=False):
        indicadorJson = self.schema.dumps(indicador, many=many)
        return indicadorJson

    def serializerIndicador(self, indicador):
        # indicador = self.schema(indicador['indicador'], indicador['fonte'], indicador['unidade'])
        # for valor in valores:
        #     indicador.valores.append(ValoresIndicadoresSchema(valor['cidade'], valor['valor']))
        # for subindicador in subindicadores:
        #     indicador.subindicadores.append(self.schema(indicador['indicador'], indicador['fonte'], indicador['unidade']))
        indicador_result = self.schema.dump(indicador)
        return indicador
    
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

    