import json
from flask import Blueprint, render_template, jsonify
from domain.service.IndicadorService import IndicadorService

indicadores = Blueprint('indicadores', __name__)

_service_indicador = IndicadorService()

@indicadores.route("/indicadores")
def hello():           
    indicadores = _service_indicador.get_all()

    dump = _service_indicador.dumps(indicadores, many=True)
    indicadoresJson =  { 'data' : dump[0], 
                         'erros': dump[1] }

    return jsonify(indicadoresJson)
