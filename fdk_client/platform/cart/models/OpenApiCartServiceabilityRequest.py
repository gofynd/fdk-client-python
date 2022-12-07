"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartItem import CartItem



from .ShippingAddress import ShippingAddress



class OpenApiCartServiceabilityRequest(BaseSchema):
    #  swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
