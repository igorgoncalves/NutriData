import json
import os

from flask_script import Command, Option, commands

from webapp import manager
from webapp.modules.localidade.services import LocalidadeService

from .modules.macroindicadores.services import IndicadorService
from .modules.user.services import UserService


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

    def run(self, username="", password="", email=""):
        UserService.create_user(
            username=username, password=password, email=email)


manager.add_command('createuser', CreateUser())
