# base flask

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from webapp.modules.user.services import UserService
from webapp.modules.core.infraestructure.db_mongo import connect


app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")

app.config.from_object('config.ProductionConfig')

api = Api(app)

jwt = JWT(app, UserService.authenticate, UserService.identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


from webapp.modules.home import *
import webapp.modules.localidade
import webapp.modules.macroindicadores