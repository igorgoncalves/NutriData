import json
import csv
import io
from io import BytesIO
from flask import Blueprint, render_template, jsonify, request, make_response
from domain.service.IndicadorService import IndicadorService
from flask_restful import reqparse, abort, Api, Resource
from openpyxl import load_workbook
from domain.service.MacroindicadorService import MacroindicadorService
from domain.service.IndicadorService import IndicadorService



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

# def readCsv(f):
#         stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
#         csv_input = csv.reader(stream)
#         #print("file contents: ", file_contents)
#         #print(type(file_contents))
#         print(csv_input)
#         for row in csv_input:
#             print(row)

#         stream.seek(0)
#         result = (stream.read().replace("=", ","))


#         response = make_response(result)
#         response.headers["Content-Disposition"] = "attachment; filename=result.csv"
#         return response

# def leituraArquivo(arquivo):
#         with open(arquivo) as ficheiro:
#             reader = csv.reader(ficheiro)
#             indicadores = []
#             data = [i for i in reader if i.count('') != len(i[1:])]
#         return data

    

# def hierarquiaCabecalho(cabecalho, hierarquia, valores):
#         cab = []
#         for item in hierarquia:
#     #         print(item['raiz'], item['sub'])
#             raiz = item["raiz"]
#             subs = item["sub"]
#             dic = {"indicador": cabecalho[raiz],
#                 "valor" : valores[raiz],
#                 "unidade" : unidades[raiz],
#                 "fonte" : fontes[raiz]
#                 }
#             listSubs = []
#             for sub in subs:
#                 dicSub = {}
#                 dicSub["indicador"] = cabecalho[sub]
#                 dicSub["valor"] = valores[sub]
#                 dicSub["unidade"] = unidades[sub]
#                 dicSub["fonte"] = fontes[sub]
#                 listSubs.append(dicSub)
#             dic["subs"] = listSubs
#             cab.append(dic)
            
#         return cab


# def exibir():
#         indicadores.reverse()
#         cabecalho = indicadores.pop()
#         unidades = indicadores.pop()
#         fontes = indicadores.pop()
#         indicadores.reverse()
#         saida = hierarquiaCabecalho(indicadores_example, hierarquia_example)
#         print(jsonCabecalhoLeitura)
#         print(hierarquiaCabecalho)



class TodoSimple(Resource):
    def get(self):
        list_all = macroindicadorService.get_all()
        return list_all

    def post(self):
        f = request.files['file']
        name = (f.filename.split('.'))[0]
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
            print('a')
            indicadoresValores = sheet[0:3]
            valores = sheet[3:]
            cidades = [cidade[0] for cidade in valores ]
            for i in range (1, len(indicadoresValores[0])-1): # 3 primeira linhas
                print('b')
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

        return resultado, 201

    
