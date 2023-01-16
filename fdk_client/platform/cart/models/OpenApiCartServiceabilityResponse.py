"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartProductInfo import CartProductInfo





from .ShipmentPromise import ShipmentPromise



from .CartBreakup import CartBreakup





class OpenApiCartServiceabilityResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    message = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
