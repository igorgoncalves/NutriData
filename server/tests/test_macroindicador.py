# from domain.repository.MacroindicadorRepository import MacroindicadorRepository
# from domain.models.Macroindicador import Macroindicador

# # from domain.infraestructure import DbMongo

# repository_macroindicador = MacroindicadorRepository()

# # Testes de repositorio
# def test_create():
#     repository_macroindicador.create(Macroindicador(codigo="1", nome="Producao de alimentos"))
#     ultimo = repository_macroindicador.get_all()[-1]
#     assert  ultimo.nome == "Brasil"

# def test_get_by_id():
#     ultimo = repository_macroindicador.get_all()[-1]
#     assert  repository_macroindicador.get_by_id(ultimo.id) == repository_macroindicador.get_all()[-1]

# def test_delete():
#     ultimo = repository_localidade.get_all()[-1]
#     repository_localidade.delete(ultimo)
#     assert  repository_localidade.get_by_id(ultimo.id) == None
