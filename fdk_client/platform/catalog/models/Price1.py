"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Price1(BaseSchema):
    #  swagger.json

    
    max = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
