from server.domain.repository.LocalidadeRepository import LocalidadeRepository
from server.domain.models.Localidade import Localidade
from server.domain.repository.MacroindicadorRepository import MacroindicadorRepository
from server.domain.models.Macroindicador import Macroindicador
from server.domain.repository.IndicadorRepository import IndicadorRepository
from server.domain.models.Indicador import Indicador
from server.domain.repository.VisaoRepository import VisaoRepository
from server.domain.models.Visao import Visao

from server.domain.service.MacroindicadorService import MacroindicadorService

# from server.app.adapters.xslxAdapter import XslxAdapter

import pytest
from unittest.mock import Mock

class Test_RepositoryTeste:
    
    #region repository

    def test_localidadeRepository_GetAll(self):
        localidades = LocalidadeRepository().get_all()
        assert len(localidades) == 84

    def test_localidadeRepository_Get(self):
        localidade = LocalidadeRepository().get_by_id("5d5d363a7dca2c4410e947f4")
        assert  localidade.nome == 'Brasil' 

    def test_localidadeRepository_GetError(self):
        localidade = LocalidadeRepository().get_by_id("5d5d363a7dca2d5510e947f4")
        assert  localidade is None  

    def test_localidadeRepository_GetTypeError(self):
        with pytest.raises(Exception):
            assert   LocalidadeRepository().get_by_id("0")

    def test_macroindicadorRepository_GetAll(self):
        macroindicador = MacroindicadorRepository().get_all()
        assert len(macroindicador) == 9

    def test_macroindicadorRepository_Get(self):
        macroindicador = MacroindicadorRepository().get_by_id("5d5d49ff7dca2c6353c92cd1")
        assert  macroindicador.nome == 'Adubação' 

    def test_macroindicadorRepository_GetError(self):
        macroindicador = MacroindicadorRepository().get_by_id("5d5d363a7dca2d5510e947f4")
        assert  macroindicador is None  

    def test_macroindicadorRepository_GetTypeError(self):
        with pytest.raises(Exception):
            assert   MacroindicadorRepository().get_by_id("0")

    def test_visaoRepository_GetAll(self):
        visao = VisaoRepository().get_all()
        assert len(visao) == 2

    def test_visaoRepository_Get(self):
        visao = VisaoRepository().get_by_id("5d5d4a1a7dca2c6353c92cd2")
        assert  visao.tipo_do_grafico == 'bar' 

    def test_visaoRepository_GetError(self):
        visao = VisaoRepository().get_by_id("5d5d363a7dca2d5510e947f4")
        assert  visao is None  

    def test_visaoRepository_GetTypeError(self):
        with pytest.raises(Exception):
            assert   VisaoRepository().get_by_id("0")

    #endregion

    # region Mock
    def test_macroindicadorService_get_localidade(self):
        localidade = Localidade(
                            codigo="0",
                            nome="Brasil",
                            posicao= "3")
        service = Mock()

        service.get_by_localidade.return_value = localidade
        assert service.get_by_localidade(0).nome == "Brasil"

    def test_macroindicadorService_get_localidade_vazio(self):
        service = Mock()
        service.get_by_localidade.return_value = []
        assert service.get_by_localidade(0) == []

    def test_macroindicadorService_getAll(self):
        macroindicadores = [
            Macroindicador(id ="5d5d3bf47dca2c51a33b5fe0" , nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b6fe0", nome="Producao de frutas 2", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b7fe0", nome="Producao de frutas 3", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos")
        ]

        service = Mock()
        service.get_all.return_value = macroindicadores
        assert len(service.get_all()) == 3

    def test_macroindicadorService_get(self):
        macroindicadores = [
            Macroindicador(id ="5d5d3bf47dca2c51a33b5fe0" , nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b6fe0", nome="Producao de frutas 2", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b7fe0", nome="Producao de frutas 3", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos")
        ]
        service = Mock()
        service.get_by_id.return_value = macroindicadores[0]
        assert service.get_by_id("5d5d3bf47dca2c51a33b5fe0").nome == 'Producao de frutas' 

    def test_macroindicadorService_GetError(self):
        macroindicadores = [
            Macroindicador(id ="5d5d3bf47dca2c51a33b5fe0" , nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b6fe0", nome="Producao de frutas 2", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos"),
            Macroindicador(id ="5d5d3bf47dca2c51a33b7fe0", nome="Producao de frutas 3", descricao="producao de frutas e rutas", fonte="IBGE",
                        unidade="quilos")
        ]
        service = Mock()
        service.get_by_id.return_value = None
        assert  service.get_by_id("5d5d363a7dca2d5510e947f4") is None  

    def test_macroindicadorService_GetTypeError(self):
        with pytest.raises(Exception):
            assert   LocalidadeRepository().get_by_id("0")

    def test_visaoService_create(self):
        indicador_service = Mock()
        macroindicador_service = Mock()
        macroindicador_service.get_by_id.return_value = Macroindicador(id ="5d5d3bf47dca2c51a33b5fe0" , nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",unidade="quilos")

        visao_service = Mock()

        visao_service.create.return_value = Visao(tipo_do_grafico='bar')
        assert visao_service.create("5d5d3bf47dca2c51a33b5fe0", 'bar', [], indicador_service, macroindicador_service)

    #endregion



# region Adapters

# def test_listaVazia():
#     adapter = XslxAdapter()
#     retorno = adapter._organizer_sheet([], [])
#     assert retorno == False

# def test_ListaAnosVazia():
#     adapter = XslxAdapter()
#     retorno = adapter._organizer_sheet([[['', 'fonte', 'fonte', 'fonte', 'fonte', 'fonte'], ['', 'indicador', 'indicador', 'indicador', 'indicador', 'indicador'], ['', 'unidade', 'unidade', 'unidade', 'unidade', 'unidade']]]
#                                         , [])
#     assert retorno == False

# def test_ListaCabecalhoVazia():
#     adapter = XslxAdapter()
#     retorno = adapter._organizer_sheet([['cabecalho', 'fonte', 'indicadores']], [])
#     assert retorno == False

#endregion
