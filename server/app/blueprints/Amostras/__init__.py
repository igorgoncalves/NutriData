from domain.service.IndicadorService import IndicadorService
from domain.service.LocalidadeService import LocalidadeService
from domain.service.MacroindicadorService import MacroindicadorService
from flask import Blueprint, request
from flask_restful import abort, Resource

localidade = Blueprint('localidade', __name__)

_service_indicador = LocalidadeService()

_service_macroindicador = MacroindicadorService()
indicadorService = IndicadorService()


class MacroindicadorApi(Resource):
    def get(self, localidade_codigo):
        local = _service_indicador.get_all(codigo=localidade_codigo)
        if len(local) == 0:
            abort(404)
        local = local[0]
        dump = _service_indicador.serialize(local, False)
        return dump.data['macroindicadores'], 201

    def post(self, localidade_codigo):
        # f = request.files['file']
        # retorno = xslxAdapter.ler_planilha_xlsx(f)
        # obj = localidadeService.serializerMacroindicador(retorno)
        local = _service_indicador.get_all(codigo=localidade_codigo)
        if len(local) == 0:
            abort(404)
        local = local[0]

        json_data = request.get_json(force=True)
        json_data['id'] = str(local['id'])+"midc"+json_data['nome']
        resposta, validated = _service_macroindicador.validate(json_data)

        if validated:
            obj = _service_macroindicador.create(resposta['id'], resposta['nome'], resposta['descricao'], [])
            try: 
                local['macroindicadores'].append(obj)
            except Exception:
                local['macroindicadores'] = []
                local['macroindicadores'].append(obj)            
            resposta, validatedL =  _service_indicador.validate(local)
            if validatedL:
                objLocal = _service_indicador.update(local)
                return objLocal, 201

        return resposta, 400

class MacroindicadorApiDetail(Resource):    
    def get(self, localidade_codigo, mid):
        local = _service_indicador.get_all(codigo=localidade_codigo)
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


    #Object Macroindicador has no attribute delete
    def delete(self, mid):
        localizacoes = _service_indicador.get_all()
        for local in localizacoes:            
            listaMid = local['macroindicadores']
            for midObj in listaMid:
                idObj = midObj.id
                idC = mid
                if idObj == idC:
                    dump = _service_macroindicador.delete(midObj)
                    return {"object": "deleted"}, 201
            abort(404)

    # def put(self, localidade_codigo, mid):
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