# base flask
from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__,
            static_folder = "../../dist/static",
            template_folder = "../../dist")

app.config.from_object('config.DevelopmentConfig')

# components
toolbar = DebugToolbarExtension(app)
manager = Manager(app)

# routes
from app.Routes import *


