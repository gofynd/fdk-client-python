"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ProductStockUnitPriceV2(BaseSchema):
    #  swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
