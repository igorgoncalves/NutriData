from domain.models.Macroindicador import Macroindicador
from domain.repository.MacroindicadorRepository import MacroindicadorRepository


repository_macroindicador = MacroindicadorRepository()


# # Testes de repositorio


def test_create():
    repository_macroindicador.create(
        Macroindicador(nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                       unidade="quilos"))
    ultimo = repository_macroindicador.get_all()[-1]
    assert ultimo.nome == "Producao de frutas"
    repository_macroindicador.delete(ultimo)


def test_get_by_id():
    repository_macroindicador.create(
        Macroindicador(nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                       unidade="quilos"))
    ultimo = repository_macroindicador.get_all()[-1]
    assert repository_macroindicador.get_by_id(ultimo.id) == repository_macroindicador.get_all()[-1]
    repository_macroindicador.delete(ultimo)


def test_delete():
    repository_macroindicador.create(
        Macroindicador(nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
                       unidade="quilos"))
    ultimo = repository_macroindicador.get_all()[-1]
    repository_macroindicador.delete(ultimo)
    assert repository_macroindicador.get_by_id(ultimo.id) == None
