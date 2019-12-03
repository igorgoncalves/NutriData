from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.LocalidadeService import LocalidadeService
from flask import Blueprint
from flask import request, Response
from flask_restful import abort, Resource

localidade = Blueprint('localidade', __name__)

_service_localidade = LocalidadeService()

_service_macroindicador = MacroindicadorService()

# A partir do codigo do local


class LocalidadeDetails(Resource):
    
    def get(self, codigo):
        list_all = _service_localidade.get_all(codigo=codigo)
        if len(list_all) == 0:
            abort(404)
        data, err = _service_localidade.serialize(list_all[0], False)
        return Response(data, mimetype="application/json", status=200)

    def delete(self, codigo):
        locais = _service_localidade.get_all(codigo=codigo)
        if len(locais) == 0:
            abort(404)
        local = locais[0]
        obj = _service_localidade.delete(local)
        return {"object": "deleted"}, 204

    def put(self, codigo):
        locais = _service_localidade.get_all(codigo=codigo)
        if len(locais) == 0:
            abort(404)
        local = locais[0]
        json_data = request.get_json(force=True)
        for k in json_data:
            local[k] = json_data[k]
        resposta, validated =  _service_localidade.validate(local)
        if validated:
            obj = _service_localidade.update(local)
            return obj, 201
        return resposta, 401


class LocalidadeApi(Resource):
    def get(self):
        list_all = _service_localidade.get_all()
        data, err = _service_localidade.serialize(list_all, True)
        return Response(data, mimetype="application/json", status=200)

    def post(self):
        json_data = request.get_json(force=True)
        resposta, validated =  _service_localidade.validate(json_data)
        if validated:
            obj = _service_localidade.create(resposta['codigo'], resposta['nome'])
            return obj, 201
        return resposta, 401

class MacroindicadoresLocalidadesApi(Resource):
    def get(self, codigo_localidade):

        macroindicadores = _service_macroindicador.get_by_localidade(codigo_localidade)
        data, err = _service_macroindicador.serialize(macroindicadores, True)

        return Response(data, mimetype="application/json", status=200)

class MacroindicadoresLocalidadesDetailsApi(Resource):
    def get(self, codigo_localidade, id_macroindicador):
        macroindicadores = _service_macroindicador.get_one_by_localidade(codigo_localidade, id_macroindicador)
        if len(macroindicadores) == 0:
            abort(404)

        data, err = _service_macroindicador.serialize(macroindicadores[0], False)        

        return Response(data, mimetype="application/json", status=200)