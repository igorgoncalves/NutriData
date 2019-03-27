from flask import Blueprint, render_template
from domain.service.IndicadorService import IndicadorService


home = Blueprint('home', __name__)

@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
