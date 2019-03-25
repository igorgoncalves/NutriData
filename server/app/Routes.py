from app import app, api
from app.blueprints.home import home
from app.blueprints.Indicadores import indicadores
from app.blueprints.Macroindicadores import *
from app.blueprints.Localidade import *
from app.blueprints.Indicadores import *
from flask_restful import  Api


# Rotas
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(indicadores, url_prefix='/api')
api.add_resource(LocalidadeApi, '/api/localidade')
api.add_resource(LocalidadeDetails, '/api/localidade/<codigo>')
api.add_resource(MacroindicadorApi, '/api/macroindicador/<localidadeCodigo>')
api.add_resource(MacroindicadorApiDetail, '/api/macroindicador/<localidadeCodigo>/<mid>')
api.add_resource(IndicadorApi, '/api/macroindicador/<localidadeCodigo>/<mid>/indicadores')
api.add_resource(IndicadorApiDetail, '/api/macroindicador/<localidadeCodigo>/<mid>/indicador/<ind>')


