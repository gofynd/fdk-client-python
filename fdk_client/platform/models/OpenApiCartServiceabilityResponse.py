"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CartBreakup import CartBreakup

from .CartProductInfo import CartProductInfo

from .ShipmentPromise import ShipmentPromise


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    

