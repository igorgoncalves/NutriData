from flask import Blueprint, request,  Response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.VisaoService import VisaoService
from domain.service.MacroindicadorService import MacroindicadorService

from app import api
import json

visao = Blueprint('visao', __name__)

_service_visao = VisaoService()
_service_macroindicador = MacroindicadorService()

class VisaoApi(Resource):
    def get(self, id_macroindicador):
        visoes = _service_visao.get_all(id=id_macroindicador)
        data, err = _service_visao.serialize(visoes, True)
        return  data, 200

    def post(self, id_macroindicador):
        print(id_macroindicador)
        dataDict = json.loads(request.data)

        tipo = dataDict['tipo_do_grafico']
        indicadores = dataDict['indicadores']

        resposta = _service_visao.create(id_macroindicador=id_macroindicador, tipo_de_grafico=tipo, indicadores=indicadores)
        data, err = _service_visao.serialize(resposta)
        return Response(data, mimetype="application/json", status=200)

class VisaoPreview(Resource):
    def get(self, id_macroindicador, codigo_localidade):
        macroindicadorObj = _service_macroindicador.get_by_id(id=id_macroindicador)
        indicadores_list = macroindicadorObj['indicadores']
        macroindicador = {}
        macroindicador['nome'] = macroindicadorObj['nome']
        macroindicador['indicadores'] = []
        for i in indicadores_list:
            indicador = {}
            amostras = i['amostras']
            aux = []
            for ams in amostras:
                cd_ams = int(ams.codigo_localidade)
                if cd_ams== int(codigo_localidade):
                    aux.append({
                'valor':ams.valor,
                'ano': ams.ano,
                'codigo_localidade' : ams.codigo_localidade
            })
            indicador['nome_indicador'] = i['nome']
            indicador['amostras'] = aux
            macroindicador['indicadores'].append(indicador)        
        # data, err = _service_macroindicador.serialize(macroindicador)
        return macroindicador, 200


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