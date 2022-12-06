"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentPromise import ShipmentPromise







from .CartBreakup import CartBreakup



from .CartProductInfo import CartProductInfo



class OpenApiCartServiceabilityResponse(BaseSchema):
    #  swagger.json

    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
