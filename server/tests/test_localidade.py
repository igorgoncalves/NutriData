from server.domain.repository.LocalidadeRepository import LocalidadeRepository
from server.domain.models.Localidade import Localidade, LocalidadeSchema
from server.domain.models.Macroindicador import Macroindicador

# fromserver.domain.infraestructure import DbMongo

repository_localidade =  LocalidadeRepository()

# Testes de repositorio
def test_create():
    # Cria Objeto de localidade com lista de macroindicadores
    new_localidade = Localidade(
            codigo="2800308",
            nome="Aracaju",
            posicao= "15")
            # macroindicadores=[Macroindicador(nome="Producao de frutas", descricao="batatas"),
            #                   Macroindicador(nome="Producao de Carros", descricao="batatas de ferro")])

    repository_localidade.create(new_localidade)
    ultimo = repository_localidade.get_all()[-1]
    assert  ultimo.nome == "Aracaju"

def test_get_by_id():
    ultimo = repository_localidade.get_all()[-1]
    assert  repository_localidade.get_by_id(ultimo.id) == repository_localidade.get_all()[-1]


def test_delete():
    ultimo = repository_localidade.get_all()[-1]
    repository_localidade.delete(ultimo)
    assert  repository_localidade.get_by_id(ultimo.id) == None
