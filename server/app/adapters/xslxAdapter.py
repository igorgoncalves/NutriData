import io
from io import BytesIO
from openpyxl import load_workbook
from domain.service.LocalidadeService import LocalidadeService
from domain.models.Localidade import Localidade, LocalidadeSchema
from domain.models.Macroindicador import Macroindicador
from domain.models.Indicador import Indicador
from domain.models.Amostra import Amostra

service_localidade =  LocalidadeService()

# Essa classe é responsável por ler uma planilha e transformar em um dicionario (e seu inverso)

# ver methodos no diagrama de classe

def LerPlanilhaXlsx(arquivo):
    wb = load_workbook(filename=BytesIO(arquivo.read()))
    macroindicador = arquivo.filename

    #leitura do arquivo xlsx
    anos = wb.sheetnames
    leitura = []
    valores = {}
    for ws in wb:
        sheet = []
        for row in ws.values:
            sheet.append(row)
        leitura.append(sheet)

    
    objeto_transformado = OrganizerSheet(leitura, "Macroindicador", "Descricao", anos)
    return objeto_transformado


def OrganizerSheet(planilha2, nome_macroindicador, descricao_macroindicador, anos):
    nome_macroindicador = nome_macroindicador
    descricao_macroindicador= descricao_macroindicador
    output = []

    fonte, indicadores, unidade = planilha2[0][0][1:],planilha2[0][1][1:], planilha2[0][2][1:]
    valores = []
    for pagina in planilha2:
        valores.append(pagina[3:])
        
    macroindicador = {}
    localidades_com_valores = []
    macroindicador['nome'] = nome_macroindicador
    macroindicador['descricao_macroindicador'] = descricao_macroindicador
    macroindicador['fonte'] = fonte[0]
    macroindicador['unidade'] = unidade[0]
    indicadores_list = []
    amostras_ano = len(valores)

    for header in indicadores:
        indicador = {}
        coluna = indicadores.index(header)+1
        indicador['nome'] = header
        indicador['indicadores_filho'] = []
        amostras = []     
        for ano in range (0, amostras_ano):
            for territorio in valores[ano]:
                    amostra_obj = {}
                    local_id = valores[ano].index(territorio)+3
                    valor_obtido = territorio[1:]
                    valor_amostral = valor_obtido[coluna-1]
                    amostra_obj['local_id'] = local_id
                    amostra_obj['ano'] = anos[ano]
                    amostra_obj['valor'] = valor_amostral
                    if valor_amostral != '-' and valor_amostral != None and valor_amostral != 0 and valor_amostral != "...":
                        amostras.append(amostra_obj)
                        localidades_com_valores.append(local_id+3)
        print(amostras)
        indicador['amostras'] = amostras
    
            
        indicadores_list.append(indicador)
    aux = set(localidades_com_valores)
    localidades_com_valores = list(aux)
    macroindicador['locais_id'] = localidades_com_valores
    macroindicador['indicadores'] = indicadores_list
        

    return macroindicador
        

def SheetToDict():
    anos = ['2017', '2018'] # os anos vem das folhas do excel
    planilha2 = [[('INDICADORES', '1. Cereais e leguminosas', '1.1. Cereais', '1.2. Leguminosas', '2. Hortaliças', '2.1. Hortaliças folhosas e florais', '2.2. Hortaliças frutais', '2.3. Hortaliças tuberosas e outras', '3. Frutas', '3.1. Frutas de clima tropical', '3.2. Frutas de clima temperado', '4. Cocos, castanhas e nozes', '4.1 Coco', '4.2. Castanhas e nozes', '5. Farinhas, féculas e massas', '5.1. Farinhas', '5.2. Féculas', '5.3. Massas', '6. Panificados', '6.1. Pães', '6.2. Bolos', '6.3. Biscoitos, roscas, etc.', '7. Carnes', '7.1. Carnes bovinas de primeira', '7.2. Carnes bovinas de segunda', '7.3. Carnes bovinas outras', '7.4. Carnes suínas com e sem osso', '7.5. Carnes suínas outras', '7.6. Carnes de outros animais', '8. Vísceras', '8.1. Vísceras bovinas', '8.2. Vísceras suínas', '8.3. Outras vísceras', '9. Pescados', '9.1. Pescados de água salgada', '9.2. Pescados de água doce', '9.3. Pescados não especificados', '10. Aves e ovos', '10.1. Aves', '10.2. Ovos', '11. Laticínios', '11.1. Leite e creme de leite', '11.2. Queijos e requeijão', '11.3. Outros laticínios', '12. Açúcares, doces e produtos de confeitaria', '12.1. Açúcares', '12.2. Doces e produtos de confeitaria', '12.3. Outros açúcares, doces e produtos de confeitaria', '13. Sais e condimentos', '13.1. Sais', '13.2. Condimentos', '14. Óleos e gorduras', '14.1. Óleos', '14.2. Gorduras', '15. Bebidas e infusões', '15.1. Bebidas alcoólicas', '15.2. Bebidas não alcoólicas', '15.3. Cafés', '15.4. Chás', '16. Alimentos preparados e misturas industriais', '16.1. Alimentos preparados', '16.2. Misturas industriais', '17. Outros produtos'), 
                ('UNIDADE', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita'), 
                ('Fonte', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE'), 
                ('SERGIPE', 27.36, 15.811, 11.549, 29.841, 2.052, 15.268, 12.521, 29.46, 26.004, 3.456, 0.513, 0.48, 0.033, 31.713, 14.891, 13.004, 3.817, 22.817, 17.873, 0.514, 4.429, 28.272, 5.06, 10.482, 7.561, 1.009, 2.475, 1.686, 1.369, 1.264, 0.064, 0.041, 5.973, 3.312, 1.347, 1.315, 21.213, 17.166, 4.047, 26.129, 21.773, 1.515, 2.841, 18.381, 16.054, 1.897, 0.429, 5.062, 2.594, 2.468, 6.428, 4.84, 1.588, 34.206, 4.491, 27.998, 1.702, 0.016, 1.834, 1.718, 0.116, 0.07),
                ], 
                [('INDICADORES', '1. Cereais e leguminosas', '1.1. Cereais', '1.2. Leguminosas', '2. Hortaliças', '2.1. Hortaliças folhosas e florais', '2.2. Hortaliças frutais', '2.3. Hortaliças tuberosas e outras', '3. Frutas', '3.1. Frutas de clima tropical', '3.2. Frutas de clima temperado', '4. Cocos, castanhas e nozes', '4.1 Coco', '4.2. Castanhas e nozes', '5. Farinhas, féculas e massas', '5.1. Farinhas', '5.2. Féculas', '5.3. Massas', '6. Panificados', '6.1. Pães', '6.2. Bolos', '6.3. Biscoitos, roscas, etc.', '7. Carnes', '7.1. Carnes bovinas de primeira', '7.2. Carnes bovinas de segunda', '7.3. Carnes bovinas outras', '7.4. Carnes suínas com e sem osso', '7.5. Carnes suínas outras', '7.6. Carnes de outros animais', '8. Vísceras', '8.1. Vísceras bovinas', '8.2. Vísceras suínas', '8.3. Outras vísceras', '9. Pescados', '9.1. Pescados de água salgada', '9.2. Pescados de água doce', '9.3. Pescados não especificados', '10. Aves e ovos', '10.1. Aves', '10.2. Ovos', '11. Laticínios', '11.1. Leite e creme de leite', '11.2. Queijos e requeijão', '11.3. Outros laticínios', '12. Açúcares, doces e produtos de confeitaria', '12.1. Açúcares', '12.2. Doces e produtos de confeitaria', '12.3. Outros açúcares, doces e produtos de confeitaria', '13. Sais e condimentos', '13.1. Sais', '13.2. Condimentos', '14. Óleos e gorduras', '14.1. Óleos', '14.2. Gorduras', '15. Bebidas e infusões', '15.1. Bebidas alcoólicas', '15.2. Bebidas não alcoólicas', '15.3. Cafés', '15.4. Chás', '16. Alimentos preparados e misturas industriais', '16.1. Alimentos preparados', '16.2. Misturas industriais', '17. Outros produtos'), 
                ('UNIDADE', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita', 'Kg/ano per capita'), 
                ('Fonte', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE', 'IBGE'), 
                ('SERGIPE', 27.36, 15.811, 11.549, 29.841, 2.052, 15.268, 12.521, 29.46, 26.004, 3.456, 0.513, 0.48, 0.033, 31.713, 14.891, 13.004, 3.817, 22.817, 17.873, 0.514, 4.429, 28.272, 5.06, 10.482, 7.561, 1.009, 2.475, 1.686, 1.369, 1.264, 0.064, 0.041, 5.973, 3.312, 1.347, 1.315, 21.213, 17.166, 4.047, 26.129, 21.773, 1.515, 2.841, 18.381, 16.054, 1.897, 0.429, 5.062, 2.594, 2.468, 6.428, 4.84, 1.588, 34.206, 4.491, 27.998, 1.702, 0.016, 1.834, 1.718, 0.116, 0.07),
                ]
                ]
    out = [
            {'nome': 'arquivo',
            'descricao': 'descricao',
            'fonte':'fonte',
            'unidade':'unidade',
            'indicadores': [
                {
                    'nome' : 'indicador1',
                    'indicadores_filho':'indicadores_filho',
                    'amostras' : [
                        {
                            'ano': 'sheets-name1',
                            'valor':' valor',
                            'local_posicao': '1',
                        },
                        {
                            'ano': 'sheets-name2',
                            'valor':' valor',
                            'local_posicao': '1',

                        }
                    ]
                },
                {
                    'nome' : 'indicador2',
                    'indicadores_filho':'indicadores_filho',
                    'amostras' : [
                        {
                            'ano': 'sheets-name1',
                            'valor':' valor',
                            'local_posicao': '1',
                        },
                        {
                            'ano': 'sheets-name2',
                            'valor':' valor',
                            'local_posicao': '1',

                        }
                    ]
                },
            ]}
    ]
    return out     
    

                    
        