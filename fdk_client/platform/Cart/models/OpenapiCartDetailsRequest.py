"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartItem import CartItem



class OpenapiCartDetailsRequest(BaseSchema):
    #  swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    
