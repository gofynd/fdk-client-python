"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ProductStockPriceV2(BaseSchema):
    #  swagger.json

    
    marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    