from app.domain.service.IndicadorService import IndicadorService
from app.domain.repository.IndicadorRepository import IndicadorRepository
from app.models.Indicador import Indicador

repositoryIndicador =  IndicadorRepository()
serviceIndicador =  IndicadorService()

# Testes de repositorio
def test_r_get_by_id():
    assert  isinstance(repositoryIndicador.get_by_id(1), Indicador)

def test_s_create():    
    repositoryIndicador.create(Indicador(nome="test", objetivo="test", periodicidade=0))
    ultimo = repositoryIndicador.get_all()[-1]    
    assert  ultimo.nome == "test"

def test_s_delete():        
    ultimo = repositoryIndicador.get_all()[-1]    
    repositoryIndicador.delete(ultimo)
    assert  repositoryIndicador.get_by_id(ultimo.id) == None

# Testes de serviço
def test_s_get_by_id():
    assert  isinstance(serviceIndicador.get_by_id(1), Indicador)
