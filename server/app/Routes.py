from app import app
from app.blueprints.home import home
from app.blueprints.Indicadores import indicadores

# Routes
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(indicadores, url_prefix='/api')