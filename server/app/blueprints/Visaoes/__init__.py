from flask import Blueprint, request,  Response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.VisaoService import VisaoService
from domain.service.MacroindicadorService import MacroindicadorService
from app import api

visao = Blueprint('visao', __name__)

_service_visao = VisaoService()
_service_macroindicador = MacroindicadorService()



class VisaoApi(Resource):
    # @api.representation('application/json')
    def get(self, id):
        visoes = _service_visao.get_all(id=id)
        data, err = _service_visao.serialize(macroindicadores, True)
        return  data, 200

    def post(self, localidade_codigo):
        local = _service_indicador.get_all(codigo=localidade_codigo)
        if len(local) == 0:
            abort(404)
        local = local

        json_data = request.get_json(force=True)
        json_data['id'] = str(local['id'])+"midc"+json_data['nome']
        resposta, validated =  _service_macroindicador.validate(json_data)
        if validated:
            obj = _service_macroindicador.create(resposta['id'], resposta['nome'], resposta['descricao'], [])
            try:
                local['macroindicadores'].append(obj)
            except Exception:
                local['macroindicadores'] = []
                local['macroindicadores'].append(obj)
            print(local['macroindicadores'])
            resposta, validatedL =  _service_indicador.validate(local)
            if validatedL:
                objLocal = _service_indicador.update(local)
                return objLocal, 201

        return resposta, 400

class VisaoPreview(Resource):
    def get(self, id_macroindicador, codigo_localidade):
        print(id_macroindicador)
        macroindicador = _service_macroindicador.get_by_id(id=id_macroindicador)
        indicadores = [x for x in macroindicador.indicadores if x.codigo_localidade == codigo_localidade]
        macroindicador.indicadores = indicadores
        data, err = _service_macroindicador.serialize(macroindicador)
        return data, 200


    #Obejct Macroindicador has no attribute delete

    # def put(self, localidade_codigo, mid):
    #     locais = _service_indicador.get_all(codigo=codigo)
    #     if len(locais) == 0:
    #         abort(404)
    #     local = locai]
    #     json_data = request.get_json(force=True)
    #     for k in json_data:
    #         local[k] = json_data[k]
    #     resposta, validated =  _service_indicador.validate(local)
    #     if validated:
    #         obj = _service_indicador.update(local)
    #         return obj, 201
    #     return resposta, 401