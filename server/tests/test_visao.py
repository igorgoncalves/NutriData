# from domain.service.VisaoService import VisaoService
# from domain.models.Visao import Visao, VisaoSchema
# from domain.models.Indicador import Indicador
# from domain.service.IndicadorService import IndicadorService
# from domain.repository.IndicadorRepository import IndicadorRepository
# from domain.models.Amostra import Amostra
# from domain.repository.MacroindicadorRepository import MacroindicadorRepository
# from domain.models.Macroindicador import Macroindicador


# repository_macroindicador = MacroindicadorRepository()
# service_visao = VisaoService()

# # # Testes de repositorio
# def test_create():
#     repository_macroindicador.create(
#         Macroindicador(nome="Producao de frutas", descricao="producao de frutas e rutas", fonte="IBGE",
#                        unidade="quilos"))
#     ultimo = repository_macroindicador.get_all()[-1]
    
#     # Cria Objeto de localidade com lista de macroindicadores
#     amostra1 = Amostra(ano="2018", valor=11, codigo_localidade="2800308")
#     amostra2 = Amostra(ano="2015", valor=11, codigo_localidade="2800308")
#     amostra3 = Amostra(ano="2016", valor=11, codigo_localidade="2800308")
#     amostra  = Amostra(ano="2017", valor=11, codigo_localidade="2800308")

#     indicador2 = Indicador(nome="outro", amostras=[Amostra(ano="2018", valor=11, codigo_localidade="2800308"), Amostra(ano="2015", valor=11, codigo_localidade="2800308"), Amostra(ano="2016", valor=11, codigo_localidade="2800308"), Amostra(ano="2017", valor=11, codigo_localidade="2800308")])
    
#     IndicadorRepository.create(
#         Indicador(nome="blabla")
#         )
    
#     IndicadorRepository.create(
#         Indicador(nome="Producao de batatatop", 
#                     amostras=[
#                         amostra1, 
#                         amostra2, 
#                         amostra3, 
#                         amostra
#                     ]
#                 )
#         )

#     # new_visao = Visao(
#     #         tipo_do_grafico = "barras",
#     #         indicadores=[Indicador(nome="Producao de batatatop", amostras=[amostra1, amostra2, amostra3, amostra]), indicador2])

#     service_visao.create(ultimo.id, "barras", IndicadorRepository.get_all())
#     ultimo = service_visao.get_all()[-1]
#     assert  ultimo.tipo_do_grafico == "barras"

# # def test_get_by_id():
# #     ultimo = service_visao.get_all(indidores__amostras__codigo_localidade=0)
# #     assert


# # # def test_delete():
# # #     ultimo = repository_localidade.get_all()[-1]
# # #     repository_localidade.delete(ultimo)
# # #     assert  repository_localidade.get_by_id(ultimo.id) == None
