from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import reqparse, abort, Api, Resource
from domain.service.IndicadorService import IndicadorService
from domain.service.MacroindicadorService import MacroindicadorService
import json
import io
from io import BytesIO
from openpyxl import load_workbook

todos = {}
macroindicadorService = MacroindicadorService()
indicadorService = IndicadorService()

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
        list_all = macroindicadorService.get_all()
        return list_all

    def post(self):
        f = request.files['file']
        # name = (f.filename.split('.'))[0]
        wb = load_workbook(filename=BytesIO(f.read()))

        #leitura do arquivo xlsx
        anos = wb.sheetnames
        entrada = []
        valores = {}
        for ws in wb:
            sheet = []
            for row in ws.values:
                sheet.append(row)
            entrada.append(sheet)


        cabecalho = []
        indicadoresPorPagina = []
        valoresPorPagina = []

        resultado = []

        for sheet in entrada: #folha
            indicadoresValores = sheet[0:3]
            valores = sheet[3:]
            cidades = [cidade[0] for cidade in valores ]
            for i in range (1, len(indicadoresValores[0])-1): # 3 primeira linhas
                valor = [{'cidade': cidades[coluna], 'valores':valores[coluna][i]} for coluna in range (0, len(cidades)) if valores[coluna][i] != None]
                indicadoresPorPagina.append(
                    {'indicador': indicadoresValores[0][i],
                    'unidade':indicadoresValores[1][i],
                    'fonte':indicadoresValores[2][i],
                    'valores':valor,
                    'subindicadores':[]
                    })
                indicadorDump = indicadorService.serializerIndicador(indicadoresPorPagina)
                resultado.append(indicadorDump)

        print(resultado[0])

        return resultado, 201
