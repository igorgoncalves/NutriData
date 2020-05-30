from flask import Blueprint, Response, request
from flask_restful import Resource, abort

from webapp import api
from webapp.modules.macroindicadores.services import CategoriaService, MacroindicadorService, IndicadorService

Blueprint('categoria', __name__)

_service_categoria = CategoriaService()
_service_macroindicador = MacroindicadorService()
_service_indicador = IndicadorService()


class CategoriaApi(Resource):
    def get(self):
        list_all = _service_categoria.get_all()
        data, err = _service_categoria.serialize(list_all, True)
        return Response(data, mimetype="application/json", status=200)

    def post(self):
        json_data = request.get_json(force=True)
        resposta, validated = _service_categoria.validate(json_data)
        if validated:
            obj = _service_categoria.create(resposta)
            data, err = _service_categoria.serialize(obj, False)
            return Response(data, mimetype="application/json", status=201)
        return resposta, 401

class CategoriaDetails(Resource):
    def get(self, categoria_id):
        categoria = _service_categoria.get_by_id(categoria_id)
        data, err = _service_categoria.serialize(categoria, False)
        return Response(data, mimetype="application/json", status=200)

    def delete(self, categoria_id):
        categoria = _service_categoria.get_by_id(categoria_id)
        obj = _service_categoria.delete(categoria)
        return {"object": "deleted"}, 204

    def patch(self, categoria_id):
        categoria = _service_categoria.get_by_id(categoria_id)
        json_data = request.get_json(force=True)
        for k in json_data:
            categoria[k] = json_data[k]
        resposta, validated = _service_categoria.validate(categoria)
        if validated:
            obj = _service_categoria.update(categoria)
            dump, err = _service_categoria.serialize(obj, False)
            return Response(dump, mimetype="application/json", status=201)
        return resposta, 401


api.add_resource(CategoriaApi, '/api/categorias')
api.add_resource(CategoriaDetails, '/api/categorias/<categoria_id>')
class MacroindicadorByCategory(Resource):
    def get(self, categoria_id, localidade_codigo):
        local = _service_macroindicador.get_by_localidade_and_categoria(localidade_codigo, categoria_id)
        print(local)
        dump, err = _service_macroindicador.serialize(local, True)
        return Response(dump, mimetype="application/json", status=200)

api.add_resource(MacroindicadorByCategory,
                 '/api/categorias/<categoria_id>/<localidade_codigo>')