"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class ProductPrice(BaseSchema):
    #  swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
