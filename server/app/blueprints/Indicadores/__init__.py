import json
from flask import Blueprint, render_template, jsonify
from domain.service.IndicadorService import IndicadorService, IndicadorSchemaService




indicadores = Blueprint('indicadores', __name__)

_service_indicador = IndicadorService()
_service_schema_indicador = IndicadorSchemaService()

@indicadores.route("/indicadores")
def hello():           
    indicadores = _service_indicador.get_all()

    indicadoresJson = [ _service_schema_indicador.dumps(indicador) for indicador in indicadores]

    return jsonify(indicadoresJson)
