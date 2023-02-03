"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ProductPrice(BaseSchema):
    #  swagger.json

    
    add_on = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
