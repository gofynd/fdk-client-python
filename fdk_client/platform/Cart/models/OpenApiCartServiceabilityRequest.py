"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShippingAddress import ShippingAddress



from .CartItem import CartItem



class OpenApiCartServiceabilityRequest(BaseSchema):
    #  swagger.json

    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    cart_items = fields.Nested(CartItem, required=False)
    
