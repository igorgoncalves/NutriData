from flask import Blueprint, request,  Response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.LocalidadeService import LocalidadeService
from domain.service.IndicadorService import IndicadorService
from domain.service.VisaoService import VisaoService
from app.adapters import xslxAdapter
import json

localidade = Blueprint('localidade', __name__)

_service_localidade = LocalidadeService()
_service_macroindicador = MacroindicadorService()
_service_indicador = IndicadorService()
_service_visao = VisaoService()


class MacroindicadorApi(Resource):
    def get(self):
        list_all = _service_macroindicador.get_all()
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
        data, err = _service_macroindicador.serialize(macroindicador_obj, False)
        return  Response(data, mimetype="application/json", status=200)

class MacroindicadorApiDetail(Resource):
    
    def get(self, id_macroindicador):
        local = _service_macroindicador.get_by_id(id_macroindicador)
        print(local.visao.tipo_do_grafico)
        dump, err = _service_macroindicador.serialize(local, False)
        aux = json.loads(dump)
        visao = _service_visao.get_by_id(aux['visao'])
        aux['visao'] = json.loads(_service_visao.serialize(visao).data)        
        return Response(json.dumps(aux), mimetype="application/json", status=200)

    def delete(self, id):
        local = _service_macroindicador.get_all(id=id)
        if len(local) == 0:
            abort(404)
        dump = _service_macroindicador.delete(local[0])
        return Response(json.dumps({'obejct deleted':id}), mimetype="application/json", status=200)

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

class IndicadoresMacroApi(Resource):
    def get(self, mid):
        macroindicador = _service_macroindicador.get_by_id(mid)
        dump, err = _service_indicador.serialize(macroindicador.indicadores, True)
        return Response(dump, mimetype="application/json", status=200)