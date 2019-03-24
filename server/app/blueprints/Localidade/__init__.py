import json
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask import Blueprint, render_template, jsonify
from domain.service.LocalidadeService import LocalidadeService


localidade = Blueprint('localidade', __name__)

_service_indicador = LocalidadeService()

# @indicadores.route("/localidade")
# def hello():           
#     indicadores =  _service_indicador.get_all(nome="Sergipe")

#     dump, err = _service_indicador.serialize(indicadores, many=True)

#     return dump


#A partir do codigo do local
class LocalidadeDetails(Resource):
    
    def get(self, codigo):
        list_all = _service_indicador.get_all(codigo=codigo)
        if len(list_all) == 0:
            abort(404)
        dump = _service_indicador.serialize(list_all[0], False)
        return dump.data, 201

    def delete(self, codigo):
        locais = _service_indicador.get_all(codigo=codigo)
        if len(locais) == 0:
            abort(404)
        local = locais[0]
        obj = _service_indicador.delete(local)
        return {"object": "deleted"}, 204

    def put(self, codigo):
        locais = _service_indicador.get_all(codigo=codigo)
        if len(locais) == 0:
            abort(404)
        local = locais[0]
        json_data = request.get_json(force=True)
        for k in json_data:
            local[k] = json_data[k]
        resposta, validated =  _service_indicador.validate(local)
        if validated:
            obj = _service_indicador.update(local)
            return obj, 201
        return resposta, 401


class LocalidadeApi(Resource):
    def get(self):
        list_all = _service_indicador.get_all()
        dump = _service_indicador.serialize(list_all, True)
        return dump.data, 201

    def post(self):
        json_data = request.get_json(force=True)
        resposta, validated =  _service_indicador.validate(json_data)
        if validated:
            obj = _service_indicador.create(resposta['codigo'], resposta['nome'], resposta['macroindicadores'])
            return obj, 201
        return resposta, 401
