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

#region Repository

#region localidade
def test_localidadeRepository_GetAll():
    localidades = LocalidadeRepository().get_all()
    assert len(localidades) == 84

def test_localidadeRepository_Get():
    localidade = LocalidadeRepository().get_by_id("5d5d363a7dca2c4410e947f4")
    assert  localidade.nome == 'Brasil' 

def test_localidadeRepository_GetError():
    localidade = LocalidadeRepository().get_by_id("5d5d363a7dca2d5510e947f4")
    assert  localidade is None  

def test_localidadeRepository_GetTypeError():
    with pytest.raises(Exception):
        assert   LocalidadeRepository().get_by_id("0")
# endregion

#region macroindicador

def test_macroindicadorRepository_GetAll():
    macroindicador = MacroindicadorRepository().get_all()
    assert len(macroindicador) == 9

def test_macroindicadorRepository_Get():
    macroindicador = MacroindicadorRepository().get_by_id("5d5d49ff7dca2c6353c92cd1")
    assert  macroindicador.nome == 'Adubação' 

def test_macroindicadorRepository_GetError():
    macroindicador = MacroindicadorRepository().get_by_id("5d5d363a7dca2d5510e947f4")
    assert  macroindicador is None  

def test_macroindicadorRepository_GetTypeError():
    with pytest.raises(Exception):
        assert   MacroindicadorRepository().get_by_id("0")

# endregion

#region indicador

# def test_indicadorRepository_GetAll():
#     indicador = IndicadorRepository().get_all()
#     assert len(indicador) == 8

# def test_indicadorRepository_Get():
#     indicador = IndicadorRepository().get_by_id("5d5d49ff7dca2c6353c92cd1")
#     assert  indicador.nome == 'Adubação' 

# def test_indicadorRepository_GetError():
#     indicador = IndicadorRepository().get_by_id("5d5d363a7dca2d5510e947f4")
#     assert  indicador is None  

# def test_indicadorRepository_GetTypeError():
#     with pytest.raises(Exception):
#         assert   IndicadorRepository().get_by_id("0")

# endregion

#region visao

def test_visaoRepository_GetAll():
    visao = VisaoRepository().get_all()
    assert len(visao) == 2

def test_visaoRepository_Get():
    visao = VisaoRepository().get_by_id("5d5d4a1a7dca2c6353c92cd2")
    assert  visao.tipo_do_grafico == 'bar' 

def test_visaoRepository_GetError():
    visao = VisaoRepository().get_by_id("5d5d363a7dca2d5510e947f4")
    assert  visao is None  

def test_visaoRepository_GetTypeError():
    with pytest.raises(Exception):
        assert   VisaoRepository().get_by_id("0")
# endregion

# region Service

def test_macroindicadorService_get_localidade():
    service = MacroindicadorService()
    localidade = service.get_by_localidade(0)
    assert len(localidade) == 2

def test_macroindicadorService_get_localidade_vazio():
    service = MacroindicadorService()
    localidade = service.get_by_localidade(300)
    assert localidade == []

def test_macroindicadorService_getAll():
    service = MacroindicadorService()
    macroindicador = service.get_all()
    assert len(macroindicador) == 9

def test_macroindicadorService_get():
    service = MacroindicadorService()
    macroindicador = service.get_by_id("5d5d3bf47dca2c51a33b5fe0")
    assert macroindicador.nome == 'Producao de frutas' 

def test_macroindicadorService_GetError():
    macroindicador = MacroindicadorService().get_by_id("5d5d363a7dca2d5510e947f4")
    assert  macroindicador is None  

def test_macroindicadorService_GetTypeError():
    with pytest.raises(Exception):
        assert   LocalidadeRepository().get_by_id("0")

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
