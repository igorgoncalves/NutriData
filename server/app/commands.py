import os
from flask_script import Command
from app import manager
from domain.service.LocalidadeService import LocalidadeService
from domain.service.IndicadorService import IndicadorService
from domain.service.VisaoService import VisaoService
from domain.models.Amostra import Amostra, AmostraSchema
from domain.models.Indicador import Indicador


class Initdb(Command):
    def run(self):
        cwd = os.getcwd()
        service_localidade = LocalidadeService()
        arquivo = open(os.getcwd()+"/app/carga_localidades.json").read()
        localidades = json.loads(arquivo)
        for localidade in localidades:
            localidade = service_localidade.deserialize(localidade)
            service_localidade.create(item=localidade)
            print("{nome} foi adicionado".format(nome=localidade.nome))

manager.add_command('initdb', Initdb())

class test(Command):
    def run(self):
        service_visao = VisaoService()
        service_indicador = IndicadorService()
        indicadores = service_visao.get_all()[0].indicadores
        amostras = [x for x in indicadores if x.codigo_localidade == 23]
        

        jsonv = service_indicador.serialize(amostras,many=True)

        print(jsonv)

manager.add_command('test', test())
