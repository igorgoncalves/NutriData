import os
from flask_script import Command, Option
from app import manager
from domain.service.LocalidadeService import LocalidadeService
from domain.service.IndicadorService import IndicadorService
from domain.service.VisaoService import VisaoService
from domain.service.UserService import UserService
import json

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


class CreateUser(Command):
    option_list = (
        Option('--username', '-u', dest='username'),
        Option('--password', '-p', dest='password'),
        Option('--email', '-e', dest='email'),
    )
    def run(self, username, password, email):
        UserService.create_user(username=username, password=password, email=email)

manager.add_command('createuser', CreateUser())


class test(Command):
    def run(self):
        service_visao = VisaoService()
        service_indicador = IndicadorService()
        indicadores = service_visao.get_all()[0].indicadores
        amostras = [x for x in indicadores if x.codigo_localidade == 23]


        jsonv = service_indicador.serialize(amostras,many=True)


manager.add_command('test', test())
