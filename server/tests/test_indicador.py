from domain.service.IndicadorService import IndicadorService
from domain.repository.IndicadorRepository import IndicadorRepository
from domain.models.Indicador import Indicador
from domain.infraestructure import DbMongo

repository_indicador =  IndicadorRepository()
service_indicador =  IndicadorService()

# Testes de repositorio
def test_create():    
    repository_indicador.create(Indicador(nome="test", objetivo="test"))
    ultimo = repository_indicador.get_all()[-1]
    assert  ultimo.nome == "test"


def test_get_by_id():
    ultimo = repository_indicador.get_all()[-1]
    print(str(ultimo.id))
    assert  repository_indicador.get_by_id(ultimo.id) == repository_indicador.get_all()[-1]

def test_delete():        
    ultimo = repository_indicador.get_all()[-1]    
    repository_indicador.delete(ultimo)
    assert  repository_indicador.get_by_id(ultimo.id) == None


# # Testes de serviço
# def test_s_get_by_id():
#     assert  isinstance(service_indicador.get_by_id(1), Indicador)
