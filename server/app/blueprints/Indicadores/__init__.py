import json
from flask import Blueprint, render_template, jsonify, request
from domain.service.IndicadorService import IndicadorService

indicadores = Blueprint('indicadores', __name__)

_service_indicador = IndicadorService()

@indicadores.route("/macroindicador", methods=['GET'])
def get():
    indicadores = _service_indicador.get_all()

    dump = _service_indicador.dumps(indicadores, many=True)
    indicadoresJson =  { 'data' : dump[0],
                         'erros': dump[1] }

    return jsonify(indicadoresJson)


@indicadores.route("/macroindicador", methods=['POST'])
def post():
    print(request)
    return jsonify(request.form)
