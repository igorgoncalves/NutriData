# base flask
from flask import Flask
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension
from injector import Binder, singleton

# import controllers
from app.blueprints.home import home

app = Flask(__name__)
app.config.from_object('config')

# components
db      = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# blueprints
app.register_blueprint(home, url_prefix='/')

# models
from app.models.Indicador import Indicador
from app.models.FonteDeDados import FonteDeDados

# Injeção de dependencia
from app.domain.repository.IndicadorRepository import IndicadorRepository
from app.domain.service.IndicadorService import IndicadorService

def configure(binder: Binder) -> Binder:
    app = binder.injector.get(Flask)
    binder.bind(IndicadorRepository, IndicadorRepository(db))
    binder.bind(IndicadorService, IndicadorService())
    binder.bind(SQLAlchemy, to=db, scope=singleton)

FlaskInjector(app=app, modules=[configure])
