from flask import Blueprint, request,  Response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.LocalidadeService import LocalidadeService
from app.adapters import xslxAdapter
import json

localidade = Blueprint('localidade', __name__)

_service_localidade = LocalidadeService()

_service_macroindicador = MacroindicadorService()


class MacroindicadorApi(Resource):
    def get(self):
        list_all = _service_macroindicador.get_all()
        if len(list_all) == 0:
            abort(404)
        data, err = _service_macroindicador.serialize(list_all, True)
        return  Response(data, mimetype="application/json", status=200)

    def post(self):
        r = request.files['file']
        resposta = xslxAdapter.LerPlanilhaXlsx(r)
        # dict_dump, error = _service_macroindicador.validate(resposta)
        dict_dump = resposta
        dict_dump['descricao'] = request.form['descricao']
        dict_dump['nome'] = request.form['nome']
        macroindicador_obj = _service_macroindicador.create(dict_dump)
        # data, err = _service_macroindicador.serialize(macroindicador_obj, False)
        return  Response(json.dumps(dict_dump), mimetype="application/json", status=200)

class MacroindicadorApiDetail(Resource):

    pass
    
    # def get(self, localidade_codigo, mid):
    #     local = _service_localidade.get_all(codigo=localidade_codigo)
    #     if len(local) == 0:
    #         abort(404)
    #     local = local[0]
    #     listaMid = local['macroindicadores']
    #     for midObj in listaMid:
    #         idObj = midObj.id
    #         idC = mid
    #         if idObj == idC:
    #             dump = _service_macroindicador.serialize(midObj, False)
    #             return dump.data, 201
    #     abort(404)


    # #Obejct Macroindicador has no attribute delete
    # def delete(self, localidade_codigo, mid):
    #     local = _service_localidade.get_all(codigo=localidade_codigo)
    #     if len(local) == 0:
    #         abort(404)
    #     local = local[0]
    #     listaMid = local['macroindicadores']
    #     for midObj in listaMid:
    #         idObj = midObj.id
    #         idC = mid
    #         if idObj == idC:
    #             dump = _service_macroindicador.delete(midObj)
    #             return {"object": "deleted"}, 201
    #     abort(404)

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