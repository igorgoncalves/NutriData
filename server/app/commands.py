from flask_script import Command
from app import manager
import os
import json
from domain.service.LocalidadeService import LocalidadeService


class Initdb(Command):
    "prints hello world"
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