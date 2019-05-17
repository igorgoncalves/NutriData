# base flask
from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import  Api

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

app.config.from_object('config.ProductionConfig')

api = Api(app)

# components
# toolbar = DebugToolbarExtension(app)
manager = Manager(app)

# routes
from app.Routes import *

from app.commands import *


