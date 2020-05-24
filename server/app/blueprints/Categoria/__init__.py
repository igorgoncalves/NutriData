from flask import Blueprint, request, Response
from flask_restful import abort, Resource
from domain.service.CategoriaService import CategoriaService
from domain.service.MacroindicadorService import MacroindicadorService

Blueprint('categoria', __name__)
_service_categoria = CategoriaService()


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
        macroindicador = _service_categoria.get_by_id(categoria_id)
        json_data = request.get_json(force=True)
        for k in json_data:
            macroindicador[k] = json_data[k]
        resposta, validated = _service_categoria.validate(macroindicador)
        if validated:
            obj = _service_categoria.update(macroindicador)
            dump, err = _service_categoria.serialize(obj, False)
            return Response(dump, mimetype="application/json", status=201)
        return resposta, 401


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
