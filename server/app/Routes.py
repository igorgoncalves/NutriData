from app import app, api
from app.blueprints.home import home
from app.blueprints.Indicadores import indicadores
from app.blueprints.Macroindicadores import MacroindicadorApi, MacroindicadorApiDetail
from app.blueprints.Localidade import LocalidadeApi, LocalidadeDetails
from app.blueprints.Indicadores import IndicadorApi, IndicadorApiDetail
from app.blueprints.Visaoes import VisaoPreview
from flask_restful import  Api


# Rotas
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(indicadores, url_prefix='/api')
api.add_resource(LocalidadeApi, '/api/localidade')
api.add_resource(LocalidadeDetails, '/api/localidade/<codigo>')
api.add_resource(MacroindicadorApi, '/api/macroindicadores')
api.add_resource(MacroindicadorApiDetail, '/api/macroindicadores/<id>')
api.add_resource(IndicadorApi, '/api/macroindicador/<localidade_codigo>/<mid>/indicadores')
api.add_resource(IndicadorApiDetail, '/api/macroindicador/<localidade_codigo>/<mid>/indicador/<ind>')

api.add_resource(VisaoPreview, '/api/visao/<id_macroindicador>/<codigo_localidade>/preview')



