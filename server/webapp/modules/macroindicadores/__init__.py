
from .models import Amostra, Categoria, Macroindicador, Indicador
from .services import CategoriaService, MacroindicadorService, IndicadorService, ServiceBase
from .views.macroindicador_view import (
    IndicadoresMacroApi, MacroindicadorApi, MacroindicadorApiDetail)

from .views.category_view import (CategoriaApi, CategoriaDetails)
