# from domain.service.VisaoService import VisaoService
# from domain.models.Visao import Visao, VisaoSchema
# from domain.models.Indicador import Indicador, Amostra

# # # from domain.infraestructure import DbMongo

# service_visao = VisaoService()

# # # Testes de repositorio
# def test_create():
#     # Cria Objeto de localidade com lista de macroindicadores
#     amostra1 = Amostra(ano="2018", valor=11)
#     amostra2 = Amostra(ano="2015", valor=11)
#     amostra3 = Amostra(ano="2016", valor=11)
#     amostra  = Amostra(ano="2017", valor=11)
#     indicador2 = Indicador(nome="outro", codigo_localidade = 22, amostras=[Amostra(ano="2018", valor=11), Amostra(ano="2015", valor=11), Amostra(ano="2016", valor=11), Amostra(ano="2017", valor=11)])
#     new_visao = Visao(
#             tipo_do_grafico = "barras",
#             indicadores=[Indicador(nome="Producao de batatatop", codigo_localidade = 23, amostras=[amostra1, amostra2, amostra3, amostra]), indicador2])

#     service_visao.create(new_visao)
#     ultimo = service_visao.get_all()[-1]
#     assert  ultimo.tipo_do_grafico == "barras"

# # def test_get_by_id():
# #     ultimo = service_visao.get_all(indidores__amostras__codigo_localidade=0)
# #     assert


# # # def test_delete():
# # #     ultimo = repository_localidade.get_all()[-1]
# # #     repository_localidade.delete(ultimo)
# # #     assert  repository_localidade.get_by_id(ultimo.id) == None
