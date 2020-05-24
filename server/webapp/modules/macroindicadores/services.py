import json

from marshmallow import ValidationError

from webapp.modules.core.service_base import ServiceBase
from webapp.modules.localidade.services import LocalidadeService
from .schemas import (CategoriaSchema, IndicadorSchema,
                      MacroindicadorSchema, AmostraSchema)
from .models import (Categoria, Indicador, Macroindicador)


class CategoriaService(ServiceBase):

    schema = CategoriaSchema()

    def __init__(self):
        super(CategoriaService, self).__init__(
            model_class=Categoria, schema=self.schema)

    def create(self, item):
        return super().create(item)

    def validate(self, item):
        try:
            categoria = self.deserialize(item)
            return categoria, True
        except ValidationError as err:
            error = err.messages
            return json.dumps(error, indent=2), False


class IndicadorService(ServiceBase):

    schema = IndicadorSchema()
    schema_amostras = AmostraSchema()
    _serviceLocalidade = LocalidadeService()

    _errors = {'validacao_amostra': []}

    def __init__(self):
        super(IndicadorService, self).__init__(
            model_class=Indicador, schema=self.schema)

    def create(self, indicador):
        amostras = []
        self._errors = {'validacao_amostra': []}
        for amostra in indicador['amostras']:
            localidade = self._serviceLocalidade.get_all(
                posicao=amostra['posicao_localidade_arquivo'])
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


class MacroindicadorService(ServiceBase):

    schema = MacroindicadorSchema()
    _service_localidade = LocalidadeService()
    _service_indicador = IndicadorService()
    _errors = []

    def __init__(self):
        super(MacroindicadorService, self).__init__(
            model_class=Macroindicador, schema=self.schema)

    def create(self, macroindicador):

        indicadores_dict = macroindicador['indicadores']
        self._errors = []
        indicadores = []
        for indicador in indicadores_dict:
            indicador_obj, err = self._service_indicador.create(indicador)
            indicadores.append(indicador_obj)

            self._errors = self._errors + err['validacao_amostra']

        if len(self._errors) > 0:
            return {}, self._errors

        novo_macroindicador = Macroindicador(
            nome=macroindicador['nome'],
            descricao=macroindicador['descricao'],
            fonte=macroindicador['fonte'],
            categoria=macroindicador['categoria'],
            unidade=macroindicador['unidade'],
            localidade=[self._service_localidade.get_all(posicao=x)[0]
                        for x in macroindicador['locais_id']],
            indicadores=indicadores)

        return super().create(novo_macroindicador), self._errors

    # validate entrada
    def validate(self, macroindicador_dict):
        try:
            self.deserialize(macroindicador_dict)
            return macroindicador_dict, True
        except ValidationError as err:
            error = err.messages            
            return json.dumps(error, indent=2), False

    def get_by_localidade(self, codigo_localidade):
        return self.get_all(indicadores__amostras__codigo_localidade=codigo_localidade)

    def get_one_by_localidade(self, codigo_localidade, macroindicador_id):
        return self.get_all(indicadores__amostras__codigo_localidade=codigo_localidade, id=macroindicador_id)

    def get_by_id(self, pk):
        partial = super().get_by_id(pk)
        if partial:
            partial = partial.select_related()
        return partial
