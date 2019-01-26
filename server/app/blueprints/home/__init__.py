from flask import Blueprint, render_template
from domain.service.IndicadorService import IndicadorService


home = Blueprint('home', __name__)

_service_indicador = IndicadorService()

@home.route("/hello")
def hello():    
    
    indicador = _service_indicador.create(nome="Indicador boladão", objetivo="mostrar quem é boladão")
    indicadores = _service_indicador.get_all()
    
    for indicador in indicadores:
        print (str(indicador))

    return str(indicador.nome)


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
