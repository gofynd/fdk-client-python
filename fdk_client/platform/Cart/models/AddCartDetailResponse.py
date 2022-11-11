"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CartDetailResponse import CartDetailResponse





class AddCartDetailResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    partial = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    
