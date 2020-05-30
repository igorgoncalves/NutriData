import json
from webapp import api

from flask import Blueprint, request, Response
from flask_restful import abort, Resource

from webapp.adapters.xslxAdapter import XslxAdapter
from webapp.modules.macroindicadores.services import (
    MacroindicadorService, IndicadorService)
from webapp.modules.localidade.services import LocalidadeService

localidade = Blueprint('localidade', __name__)

_service_localidade = LocalidadeService()
_service_macroindicador = MacroindicadorService()
_service_indicador = IndicadorService()


class MacroindicadorApi(Resource):

    _xslxAdapter = XslxAdapter()

    def get(self):
        list_all = _service_macroindicador.get_all()

        data, err = _service_macroindicador.serialize(list_all, True)

        return Response(data, mimetype="application/json", status=200)

    def post(self):
        r = request.files['file']
        resposta = self._xslxAdapter.ler_planilha_xlsx(r)

        dict_dump = resposta
        dict_dump['descricao'] = request.form['descricao']
        dict_dump['nome'] = request.form['nome']
        dict_dump['categoria'] = request.form['categoria']
        macroindicador_obj, validacao_erros = _service_macroindicador.create(
            dict_dump)

        url_planilha = ""
        if len(validacao_erros) > 0:
            uri_planilha = self._xslxAdapter.gerar_planilha_para_correcao(
                [(erro['posicao'], erro['valor']) for erro in validacao_erros]
            )

            url_planilha = uri_planilha

        data, err = _service_macroindicador.serialize(
            macroindicador_obj, False)

        return Response(json.dumps({'data': data, 'detail': url_planilha}), mimetype="application/json", status=200)


class MacroindicadorApiDetail(Resource):

    def get(self, macroindicador_id):
        local = _service_macroindicador.get_by_id(macroindicador_id)
        dump, err = _service_macroindicador.serialize(local, False)
        return Response(dump, mimetype="application/json", status=200)

    def delete(self, macroindicador_id):
        local = _service_macroindicador.get_all(id=macroindicador_id)
        if len(local) == 0:
            abort(404)
        dump = _service_macroindicador.delete(local[0])
        return Response(json.dumps({'obejct deleted': macroindicador_id}), mimetype="application/json", status=200)

    def patch(self, macroindicador_id):
        macroindicador = _service_macroindicador.get_by_id(macroindicador_id)

        if macroindicador['categoria']:
            macroindicador['categoria'] = ""

        json_data = request.get_json(force=True)
        for k in json_data:
            macroindicador[k] = json_data[k]
        print(macroindicador)
        resposta, validated = _service_macroindicador.validate(macroindicador)
        if validated:
            obj = _service_macroindicador.update(macroindicador)
            dump, err = _service_macroindicador.serialize(obj, False)
            return Response(dump, mimetype="application/json", status=201)
        return resposta, 401


class IndicadoresMacroApi(Resource):
    def get(self, macroindicador_id):
        macroindicador = _service_macroindicador.get_by_id(macroindicador_id)
        dump, err = _service_indicador.serialize(
            macroindicador.indicadores, True)
        return Response(dump, mimetype="application/json", status=200)



api.add_resource(MacroindicadorApi,
                 '/api/macroindicadores')

api.add_resource(MacroindicadorApiDetail,
                 '/api/macroindicadores/<macroindicador_id>')

api.add_resource(IndicadoresMacroApi,
                 '/api/macroindicador/<macroindicador_id>/indicadores')

