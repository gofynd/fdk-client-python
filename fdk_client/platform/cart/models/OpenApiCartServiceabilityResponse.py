"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartBreakup import CartBreakup



from .ShipmentPromise import ShipmentPromise



from .CartProductInfo import CartProductInfo







class OpenApiCartServiceabilityResponse(BaseSchema):
    #  swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
