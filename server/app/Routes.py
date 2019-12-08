from app import app, api
from app.blueprints.Indicadores import IndicadorApi, IndicadorApiDetail
from app.blueprints.Localidade import LocalidadeApi, LocalidadeDetails, MacroindicadoresLocalidadesApi, MacroindicadoresLocalidadesDetailsApi
from app.blueprints.Macroindicadores import MacroindicadorApi, MacroindicadorApiDetail, IndicadoresMacroApi
from app.blueprints.Visaoes import VisaoApi, VisaoPreview
from app.blueprints.home import home

# Rotas
app.register_blueprint(home, url_prefix='/')
api.add_resource(LocalidadeApi, '/api/localidade')
api.add_resource(LocalidadeDetails, '/api/localidade/<codigo>')
api.add_resource(MacroindicadoresLocalidadesApi, '/api/localidade/<codigo_localidade>/macroindicadores')
api.add_resource(MacroindicadoresLocalidadesDetailsApi, '/api/localidade/<codigo_localidade>/macroindicadores/<id_macroindicador>')

api.add_resource(MacroindicadorApi, '/api/macroindicadores')
api.add_resource(MacroindicadorApiDetail, '/api/macroindicadores/<id_macroindicador>')
api.add_resource(IndicadoresMacroApi, '/api/macroindicador/<mid>/indicadores')

api.add_resource(IndicadorApi, '/api/macroindicador/<localidade_codigo>/<mid>/indicadores')
api.add_resource(IndicadorApiDetail, '/api/macroindicador/<localidade_codigo>/<mid>/indicador/<ind>')

api.add_resource(VisaoApi, '/api/macroindicador/<id_macroindicador>/visao')
api.add_resource(VisaoPreview, '/api/visao/<id_macroindicador>/<codigo_localidade>/preview')



