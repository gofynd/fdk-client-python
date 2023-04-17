"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ProductStockUnitPriceV3(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    

