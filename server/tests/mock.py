from unittest.mock import Mock
from services import Service
​
​
class TestRepository:
​
    def __init__(self):
        self.lista = []
​
        obj = {'id': 4, 'nome': "DDD", 'valor': 20}
        obj2 = {'id': 5, 'nome': "EEE", 'valor': 10}
        obj3 = {'id': 6, 'nome': "FFF", 'valor': 500}
​
        self.lista.append(obj)
        self.lista.append(obj2)
        self.lista.append(obj3)
​
    def listagemTest(self):
        repository = Mock()
​
        repository.listagem.return_value = self.lista
​
        service = Service(repository)
​
        return service.listagem()
​
    def obterTest(self):
        repository = Mock()
​
        repository.obter.return_value = self.lista[0]
​
        service = Service(repository)
​
        return service.obter(1)
​
    def obterErroTest(self):
        repository = Mock()
​
        repository.obter.return_value = self.lista[4]
​
        service = Service(repository)
​
        return service.obter(1)