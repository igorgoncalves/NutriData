import json
from flask import Blueprint, render_template, jsonify
from domain.service.LocalidadeService import LocalidadeService
from flask_restful import Resource, Api

indicadores = Blueprint('indicadores', __name__)

_service_indicador = LocalidadeService()

@indicadores.route("/indicadores")
def hello():           
    indicadores = _service_indicador.get_all(nome="Sergipe")

    dump, err = _service_indicador.serialize(indicadores, many=True)

    return dump
