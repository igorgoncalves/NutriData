from app import app
from app.blueprints.home import home

# Routes
app.register_blueprint(home, url_prefix='/')