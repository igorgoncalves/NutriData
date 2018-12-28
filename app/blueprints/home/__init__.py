from flask import Blueprint
from app.domain.service.IndicadorService import IndicadorService

home = Blueprint('home', __name__)

_indicadorService = IndicadorService()

@home.route("/")
def hello():
    # indicadorService.create("Produção de frutas", "medir produção de frutas", 1)
    indicadores = _indicadorService.get_all()
    for indicador in indicadores:
        print (str(indicador))
    
    print ("dsadsa" + str(_indicadorService.get_by_id(1)))

    return str("Indicador 'Produção de frutas'")
