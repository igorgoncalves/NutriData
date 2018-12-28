from flask import Blueprint
from domain.service.IndicadorService import IndicadorService

home = Blueprint('home', __name__)

_service_indicador = IndicadorService()

@home.route("/")
def hello():    
    indicadores = _service_indicador.get_all()
    
    for indicador in indicadores:
        print (str(indicador))

    return str("Indicador 'Produção de frutas'")
