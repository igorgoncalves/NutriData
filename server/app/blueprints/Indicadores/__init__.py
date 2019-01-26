import json
from flask import Blueprint, render_template, jsonify
from domain.service.IndicadorService import IndicadorService


indicadores = Blueprint('indicadores', __name__)

_service_indicador = IndicadorService()

@indicadores.route("/indicadores")
def hello():            
    indicadores = _service_indicador.get_all()
    
    return jsonify(json.dumps(indicadores))