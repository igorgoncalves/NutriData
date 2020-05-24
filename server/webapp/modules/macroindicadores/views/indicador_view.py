from flask import Blueprint, abort, request
from flask_restful import Resource

from webapp import api
from webapp.modules.macroindicadores.services import (
    MacroindicadorService, IndicadorService)


indicadores = Blueprint('indicadores', __name__)

_service_macroindicador = MacroindicadorService()
_service_indicador = IndicadorService()


class IndicadorApi(Resource):
    def get(self, localidade_codigo, macroindicador_id):
        local = _service_indicador.get_all(codigo=localidade_codigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        dump = _service_indicador.serialize(local, False)
        return dump.data['macroindicadores'], 201

    def post(self, localidade_codigo, macroindicador_id):
        # encontrar aninhamento correto
        local = _service_indicador.get_all(codigo=localidade_codigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        listaMid = local['macroindicadores']
        for midObj in listaMid:
            idObj = midObj.id
            idC = macroindicador_id
            if idObj == idC:
                obj = midObj
                # dump = _service_macroindicador.serialize(midObj, False)

        # validar entrada
        json_data = request.get_json(force=True)
        json_data['id'] = str(local['id'])+"idc"+json_data['nome']
        resposta, validated = _service_indicador.validate(json_data)

        if validated:
            obj = _service_indicador.create(
                resposta['id'], resposta['nome'], [])
            try:
                local['macroindicadores'].append(obj)
            except Exception:
                local['macroindicadores'] = []
                local['macroindicadores'].append(obj)

            resposta, validatedL = _service_indicador.validate(local)
            if validatedL:
                objLocal = _service_indicador.update(local)
                return objLocal, 201

        return resposta, 400


class IndicadorApiDetail(Resource):

    # Object Macroindicador has no attribute delete
    def delete(self, localidade_codigo, macroindicador_id):
        local = _service_macroindicador.get_one_by_localidade(
            localidade_codigo, macroindicador_id)

        listaMid = local['macroindicadores']
        for midObj in listaMid:
            idObj = midObj.id
            idC = macroindicador_id
            if idObj == idC:
                dump = _service_macroindicador.delete(midObj)
                return {"object": "deleted"}, 201
        abort(404)


api.add_resource(
    IndicadorApi, '/api/macroindicador/<localidade_codigo>/<macroindicador_id>/indicadores')
api.add_resource(IndicadorApiDetail,
                 '/api/macroindicador/<localidade_codigo>/<macroindicador_id>/indicador/<ind>')
