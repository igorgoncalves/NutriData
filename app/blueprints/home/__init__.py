from flask import Blueprint
from app.domain.service.IndicadorService import IndicadorService

home = Blueprint('home', __name__)

indicadorService = IndicadorService()

@home.route("/")
def hello():
    return indicadorService.get_all()
