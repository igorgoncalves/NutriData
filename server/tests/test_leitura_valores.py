from domain.repository.LocalidadeRepository import LocalidadeRepository
from domain.models.Localidade import Localidade

from domain.repository.MacroindicadorRepository import MacroindicadorRepository
from domain.models.Macroindicador import Macroindicador
from domain.repository.IndicadorRepository import IndicadorRepository

from domain.models.Indicador import Indicador
from domain.repository.VisaoRepository import VisaoRepository

from domain.models.Visao import Visao


from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.VisaoService import VisaoService

# from app.adapters.xslxAdapter import XslxAdapter

import pytest
from unittest.mock import Mock

class Test_RepositoryTeste:
    
    #region repository

    def test_localidadeRepository_GetAll(self):
        localidades = LocalidadeRepository().get_all()
        assert len(localidades) == 86

    def test_localidadeRepository_Get(self):
        localidade = LocalidadeRepository().get_by_id("5d3015b69dc6d607ef641307")
        assert  localidade.nome == 'Brasil' 

    def test_localidadeRepository_GetNone(self):
        localidade = LocalidadeRepository().get_by_id("5f3015b69dc6d607ef641309")
        assert  localidade is None  

    def test_localidadeRepository_GetTypeError(self):
        with pytest.raises(Exception):
            assert   LocalidadeRepository().get_by_id("0")

    def test_macroindicadorRepository_GetAll(self):
        macroindicador = MacroindicadorRepository().get_all()
        assert len(macroindicador) == 3

    def test_macroindicadorRepository_Get(self):
        macroindicador = MacroindicadorRepository().get_by_id("5d5dbb5a9dc6d626f7dc02c5")
        assert  macroindicador.nome == 'Adubação' 

    def test_macroindicadorRepository_GetError(self):
        macroindicador = MacroindicadorRepository().get_by_id("5d5d363a7dca2d5510e947f4")
        assert  macroindicador is None  

    def test_macroindicadorRepository_GetTypeError(self):
        with pytest.raises(Exception):
            assert   MacroindicadorRepository().get_by_id("0")
  

    def test_visaoRepository_Get(self):
        visao = VisaoRepository().get_by_id("5d5dbb6d9dc6d626f7dc02c6")
        assert  visao.tipo_do_grafico == 'pie' 

    def test_visaoRepository_GetNone(self):
        visao = VisaoRepository().get_by_id("5f5dbb6d9dc6d626f7dc02c6")
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
        repository = Mock()
        repository.get_by_localidade.return_value = localidade        
        service = MacroindicadorService(repository=repository)

        assert service.get_by_localidade(0).nome == "Brasil"

    def test_macroindicadorService_get_localidade_vazio(self):
        repository = Mock()
        repository.get_by_localidade.return_value = []        
        service = MacroindicadorService(repository=repository)

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

        repository = Mock()
        repository.get_all.return_value = macroindicadores        
        service = MacroindicadorService(repository=repository)
        
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
        repository = Mock()
        repository.get_by_id.return_value = macroindicadores[0]        
        service = MacroindicadorService(repository=repository)        

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
        
        repository = Mock()
        repository.get_by_id.return_value = None
        service = MacroindicadorService(repository=repository) 

        assert  service.get_by_id("5d5d363a7dca2d5510e947f4") is None  

    def test_macroindicadorService_GetTypeError(self):
        with pytest.raises(Exception):
            assert   LocalidadeRepository().get_by_id("0")

    def test_visaoService_create(self):                        

        service_macro = Mock()        
        service_macro.get_by_id.return_value = Macroindicador(id ="5d5d3bf47dca2c51a33b5fe0" , nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE", unidade="quilos")
        service = VisaoService(service_macroindicador=service_macro)

        retorno = service.create("5d5d3bf47dca2c51a33b5fe0", 'bar', [])

        assert  retorno.tipo_do_grafico == 'bar'

    #endregionx



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
