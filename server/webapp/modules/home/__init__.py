from webapp import app
from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


app.register_blueprint(home, url_prefix='/')
