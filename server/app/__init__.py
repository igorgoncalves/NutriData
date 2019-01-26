# base flask
from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension

# from domain.infraestructure import DbMongo

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# components
toolbar = DebugToolbarExtension(app)
manager = Manager(app)

# routes
from app.Routes import *

# models
# from domain.models import *

