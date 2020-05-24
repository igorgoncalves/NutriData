from marshmallow_mongoengine import ModelSchema, fields
from .models import Amostra, Indicador, Macroindicador, Categoria


class AmostraSchema(ModelSchema):    
    class Meta:
        model = Amostra


class IndicadorSchema(ModelSchema):
    amostras = fields.Nested(AmostraSchema, many=True)

    class Meta:
        model = Indicador


class MacroindicadorSchema(ModelSchema):
    indicadores = fields.Nested(IndicadorSchema, many=True)

    class Meta:
        model = Macroindicador


class CategoriaSchema(ModelSchema):
    class Meta:
        model = Categoria
