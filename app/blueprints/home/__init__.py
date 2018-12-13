from flask import Blueprint
from app.domain.service.IndicadorService import IndicadorService


# class HomeController():
#     @inject
#     def __init__(self, indicadorRepository: IndicadorRepository):
#         self.indicadorRepository = indicadorRepository
#         print(self.indicadorRepository.create())

home = Blueprint('home', __name__)

indicadorService = IndicadorService()

@home.route("/")
def hello():
    return indicadorService.get_by_id(20)
