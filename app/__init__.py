# base flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('config')

# components
db      = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# import controllers
from app.blueprints.home import home

# blueprints
app.register_blueprint(home, url_prefix='/')

# models
from app.models.FonteDeDados import FonteDeDados
from app.models.Indicador import Indicador
db.create_all()
