"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CartItem(BaseSchema):
    #  swagger.json

    
    size = fields.Str(required=False)
    
    product_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
