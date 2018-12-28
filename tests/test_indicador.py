from app.domain.service.IndicadorService import IndicadorService
from app.domain.repository.IndicadorRepository import IndicadorRepository
from app.models.Indicador import Indicador

repository_indicador =  IndicadorRepository()
service_indicador =  IndicadorService()

# Testes de repositorio
def test_r_get_by_id():
    assert  isinstance(repository_indicador.get_by_id(1), Indicador)

def test_s_create():    
    repository_indicador.create(Indicador(nome="test", objetivo="test", periodicidade=0))
    ultimo = repository_indicador.get_all()[-1]    
    assert  ultimo.nome == "test"

def test_s_delete():        
    ultimo = repository_indicador.get_all()[-1]    
    repository_indicador.delete(ultimo)
    assert  repository_indicador.get_by_id(ultimo.id) == None

# Testes de serviço
def test_s_get_by_id():
    assert  isinstance(service_indicador.get_by_id(1), Indicador)
