from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.IndicadorService import IndicadorService
from domain.service.MacroindicadorService import MacroindicadorService
import json
import io
from io import BytesIO
from openpyxl import load_workbook
from app.adapters import xslxAdapter
from domain.service.LocalidadeService import LocalidadeService


todos = {}
macroindicadorService = MacroindicadorService()
indicadorService = IndicadorService()
localidadeService = LocalidadeService()

def jsonCabecalhoLeitura(indicadores):
        listaIndicadoresJson = []
        for i in indicadores:
            dic = {}
            dic["posicao"] = indicadores.index(i)
            dic["indicador"] = i
            listaIndicadoresJson.append(dic)
        return json.dumps(listaIndicadoresJson, indent=2)

class MacroindicadorApi(Resource):
    def get(self):
        list_all = localidadeService.get_all()
        return json.dumps(list_all, indent=2), 201

    def post(self):
        f = request.files['file']
        retorno = xslxAdapter.LerPlanilhaXlsx(f)
        obj = localidadeService.serializerMacroindicador(retorno)

        return obj, 201
