# base flask
from flask import Flask
from flask_restful import Api
from flask_script import Manager
from flask_jwt import JWT, jwt_required, current_identity
from server.domain.service.UserService import UserService
app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

app.config.from_object('config.ProductionConfig')

api = Api(app)

jwt = JWT(app, UserService.authenticate, UserService.identity)

# components
# toolbar = DebugToolbarExtension(app)
manager = Manager(app)

# UserService.create_admin()

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


# routes

from app.Routes import *

from app.commands import *


