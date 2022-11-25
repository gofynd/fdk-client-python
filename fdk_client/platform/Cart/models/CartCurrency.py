"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CartCurrency(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
