# base flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension
from domain.Database import Base


app = Flask(__name__)
app.config.from_object('config')

# components
db      = SQLAlchemy(app, model_class=Base)
toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#routes
from app.Routes import *

# models
from domain.models import *
db.create_all()

