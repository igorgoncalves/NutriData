import io
from io import BytesIO
from openpyxl import load_workbook
from domain.repository.LocalidadeRepository import LocalidadeRepository
from domain.models.Localidade import Localidade, LocalidadeSchema
from domain.models.Macroindicador import Macroindicador
from domain.models.Indicador import Indicador
from domain.models.Amostra import Amostra

repository_localidade =  LocalidadeRepository()

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

    for folha in range (0, len(anos)):
        dic = OrganizerSheet(leitura[folha], anos[folha], macroindicador)

    for localidade in dic:
        new_localidade = Localidade(codigo="1" , nome = localidade, 
            macroindicadores=[Macroindicador(nome=macroindicador, descricao="",
            indicadores=dic[localidade])])
        repository_localidade.create(new_localidade)
    
    return repository_localidade.get_all()[-1]




def OrganizerSheet(sheet, ano, macroindicador):
    cabecalho = sheet[0:2]
    corpo = sheet[3:]

    result = {}

    for val in corpo:
        localidade, valores = val[0], val[1:]
        ind = []
        for it in range (0, len(valores)):
            nomeInd = cabecalho[0][it+1]
            ano = ano
            unidade = cabecalho[1][it+1]
            #fonte = cabecalho[2][it+1]
            valor = valores[it]
            amostra = Amostra(ano = ano, valor = valor)
            indicador = Indicador(nome = nomeInd, amostras = [amostra])
            if localidade in result:
                result[localidade].append(indicador)
            else:
                result[localidade] = []

    return result
        


                    
        