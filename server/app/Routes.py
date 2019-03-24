from app import app, api
from app.blueprints.home import home
from app.blueprints.Indicadores import indicadores
from app.blueprints.Macroindicadores import MacroindicadorApi
from app.blueprints.Localidade import LocalidadeApi, LocalidadeDetails
from flask_restful import  Api


# Routes
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(indicadores, url_prefix='/api')
api.add_resource(MacroindicadorApi, '/api/macroindicador')
api.add_resource(LocalidadeApi, '/api/localidade')
api.add_resource(LocalidadeDetails, '/api/localidade/<codigo>')


