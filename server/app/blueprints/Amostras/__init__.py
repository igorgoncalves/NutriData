from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.IndicadorService import IndicadorService
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.LocalidadeService import LocalidadeService
import json
import io
from io import BytesIO
from openpyxl import load_workbook
from app.adapters import xslxAdapter

localidade = Blueprint('localidade', __name__)

_service_indicador = LocalidadeService()

_service_macroindicador = MacroindicadorService()
indicadorService = IndicadorService()



class MacroindicadorApi(Resource):
    def get(self, localidadeCodigo):
        local = _service_indicador.get_all(codigo=localidadeCodigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        dump = _service_indicador.serialize(local, False)
        return dump.data['macroindicadores'], 201

    def post(self, localidadeCodigo):
        # f = request.files['file']
        # retorno = xslxAdapter.LerPlanilhaXlsx(f)
        # obj = localidadeService.serializerMacroindicador(retorno)
        local = _service_indicador.get_all(codigo=localidadeCodigo)
        if len(local) == 0:
            abort(404)
        local = local[0]

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

class MacroindicadorApiDetail(Resource):
    
    def get(self, localidadeCodigo, mid):
        local = _service_indicador.get_all(codigo=localidadeCodigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        listaMid = local['macroindicadores']
        for midObj in listaMid:
            idObj = midObj.id
            idC = mid
            if idObj == idC:
                dump = _service_macroindicador.serialize(midObj, False)
                return dump.data, 201
        abort(404)


    #Obejct Macroindicador has no attribute delete
    def delete(self, localidadeCodigo, mid):
        local = _service_indicador.get_all(codigo=localidadeCodigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        listaMid = local['macroindicadores']
        for midObj in listaMid:
            idObj = midObj.id
            idC = mid
            if idObj == idC:
                dump = _service_macroindicador.delete(midObj)
                return {"object": "deleted"}, 201
        abort(404)

    # def put(self, localidadeCodigo, mid):
    #     locais = _service_indicador.get_all(codigo=codigo)
    #     if len(locais) == 0:
    #         abort(404)
    #     local = locais[0]
    #     json_data = request.get_json(force=True)
    #     for k in json_data:
    #         local[k] = json_data[k]
    #     resposta, validated =  _service_indicador.validate(local)
    #     if validated:
    #         obj = _service_indicador.update(local)
    #         return obj, 201
    #     return resposta, 401