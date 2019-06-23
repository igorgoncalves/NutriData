# fromserver.domain.repository.LocalidadeRepository import LocalidadeRepository
# fromserver.domain.models.Localidade import Localidade, LocalidadeSchema
# fromserver.domain.models.Macroindicador import Macroindicador

# # fromserver.domain.infraestructure import DbMongo

# repository_localidade =  LocalidadeRepository()

# # Testes de repositorio
# def test_create():
#     # Cria Objeto de localidade com lista de macroindicadores
#     new_localidade = Localidade(
#             codigo="22",
#             nome="Sergipe",
#             macroindicadores=[Macroindicador(nome="Producao de frutas", descricao="batatas"),
#                               Macroindicador(nome="Producao de Carros", descricao="batatas de ferro")])

#     repository_localidade.create(new_localidade)
#     ultimo = repository_localidade.get_all()[-1]
#     assert  ultimo.nome == "Brasil"

# def test_get_by_id():
#     ultimo = repository_localidade.get_all()[-1]
#     assert  repository_localidade.get_by_id(ultimo.id) == repository_localidade.get_all()[-1]


# # def test_delete():
# #     ultimo = repository_localidade.get_all()[-1]
# #     repository_localidade.delete(ultimo)
# #     assert  repository_localidade.get_by_id(ultimo.id) == None
